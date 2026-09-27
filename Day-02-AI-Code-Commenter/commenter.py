import ast
import os
import sys
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
)

MODEL = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")


def generate_comment(code_snippet: str) -> str:
    """Ask the model for a one-line comment describing the given code."""
    prompt = (
        "You are an expert Python developer. Write a single, clear one-line "
        "comment that explains the purpose of the following code. "
        "Start it with '# ' and return only the comment, nothing else.\n\n"
        f"Code:\n{code_snippet}"
    )
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.2,
    )
    text = response.choices[0].message.content or ""

    # Keep only the first real line, skipping any ``` code fences
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip() and not line.strip().startswith("```")
    ]
    comment = lines[0] if lines else "# (no comment generated)"
    if not comment.startswith("#"):
        comment = "# " + comment.strip("\"'")
    return comment


def comment_file(path: str) -> str:
    """Add an AI comment above every function in a file; save to a new file."""
    with open(path) as f:
        source = f.read()

    tree = ast.parse(source)
    lines = source.splitlines()

    functions = [
        node for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    # Work from the bottom up so inserting lines doesn't shift the ones above
    functions.sort(key=lambda n: n.lineno, reverse=True)

    for node in functions:
        snippet = ast.get_source_segment(source, node)
        comment = generate_comment(snippet)

        # Place the comment above any decorators, matching indentation
        start = min([node.lineno] + [d.lineno for d in node.decorator_list]) - 1
        indent = lines[start][: len(lines[start]) - len(lines[start].lstrip())]
        lines.insert(start, indent + comment)
        print(f"{node.name}: {comment}")

    output_path = os.path.splitext(path)[0] + "_commented.py"
    with open(output_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    return output_path


if __name__ == "__main__":
    if len(sys.argv) > 1:
        out = comment_file(sys.argv[1])
        print(f"\nSaved commented file to: {out}")
    else:
        demo = """def calculate_area(length, width):
    return length * width"""
        print(generate_comment(demo))