#!/usr/bin/env python3
"""Generate API reference pages from a Swagger/OpenAPI JSON file.

Usage:
    python3 scripts/generate_api_reference.py
    python3 scripts/generate_api_reference.py --swagger /path/to/swagger.json --dry-run
"""

import argparse
import json
import re
from pathlib import Path

# Set the default variables for the script
DOCS_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_API_REF_DIR = DOCS_ROOT / "kiichain-pay" / "api-reference"
DEFAULT_SUMMARY_FILE = DOCS_ROOT / "SUMMARY.md"
SPEC_NAME = "kiichain-pay-swagger"
SUMMARY_ANCHOR = "* [API Reference](kiichain-pay/api-reference/README.md)"

# Helper function to load all the paths
def load_paths(swagger_file: Path) -> dict:
    # Load the Swagger
    with swagger_file.open() as f:
        data = json.load(f)
    # Return the paths
    return data["paths"]

# Helper function to group paths by module
def group_by_module(paths: dict) -> dict[str, list[tuple[str, str]]]:
    # Start a hashmap
    modules: dict[str, list[tuple[str, str]]] = {}
    # Iterate all the methods
    for path, methods in paths.items():
        module = path.strip("/").split("/")[0]
        # Add the path and method to the module
        for method in methods:
            modules.setdefault(module, []).append((path, method.lower()))
    # Return the modules list
    return modules


# Helper function to sort endpoints
def sort_endpoints(endpoints: list[tuple[str, str]]) -> list[tuple[str, str]]:
    # Alphabetical by path, then by method
    return sorted(endpoints, key=lambda pm: (pm[0], pm[1]))

# Helper function to clear old pages
# This clean all the generated pages in the api_ref_dir except for README.md
def clear_old_pages(api_ref_dir: Path, dry_run: bool) -> None:
    # Check if we are under the docs root
    try:
        api_ref_dir.relative_to(DOCS_ROOT)
    except ValueError:
        raise SystemExit(f"Refusing to delete markdown files outside docs root: {api_ref_dir}")

    for md_file in api_ref_dir.glob("*.md"):
        if md_file.name == "README.md":
            continue
        print(f"removing {md_file.relative_to(DOCS_ROOT)}")
        if not dry_run:
            md_file.unlink()

# Helper function to render a page for a module
def render_page(module: str, endpoints: list[tuple[str, str]]) -> str:
    # Render the page content for a module
    lines = [f"# {module.capitalize()}", ""]
    for path, method in endpoints:
        lines.append(f'{{% openapi-operation spec="{SPEC_NAME}" path="{path}" method="{method}" %}}')
        lines.append("{% endopenapi-operation %}")
        lines.append("")
    # Return the content as a string
    return "\n".join(lines).rstrip("\n") + "\n"

# Helper function to write module pages
def write_module_pages(api_ref_dir: Path, modules: dict[str, list[tuple[str, str]]], dry_run: bool) -> None:
    # Iterate all the modules and enpoints
    for module, endpoints in modules.items():
        # Set the path
        page_path = api_ref_dir / f"{module}.md"
        # Create the content by rendering the page
        content = render_page(module, sort_endpoints(endpoints))
        print(f"writing {page_path.relative_to(DOCS_ROOT)} ({len(endpoints)} endpoints)")
        if not dry_run:
            page_path.write_text(content)

# Helper function to update the SUMMARY.md file
def update_summary(summary_file: Path, api_ref_dir: Path, modules: dict[str, list[tuple[str, str]]], dry_run: bool) -> None:
    # Read the SUMMARY.md file
    text = summary_file.read_text()
    lines = text.split("\n")

    # Find the anchor line in the SUMMARY.md file
    anchor_idx = next((i for i, line in enumerate(lines) if line.strip() == SUMMARY_ANCHOR), None)
    if anchor_idx is None:
        raise SystemExit(f"Could not find anchor line {SUMMARY_ANCHOR!r} in {summary_file}")

    # Create a regex pattern to match the existing module entries
    rel_dir = api_ref_dir.relative_to(DOCS_ROOT).as_posix()
    entry_re = re.compile(rf"^  \* \[.*\]\({re.escape(rel_dir)}/.*\.md\)$")

    # Find the end index of the existing module entries
    end_idx = anchor_idx + 1
    while end_idx < len(lines) and entry_re.match(lines[end_idx]):
        end_idx += 1

    # Create new entries for the modules
    new_entries = [
        f"  * [{module.capitalize()}]({rel_dir}/{module}.md)"
        for module in sorted(modules)
    ]

    # Replace the existing module entries with the new entries
    lines[anchor_idx + 1:end_idx] = new_entries
    new_text = "\n".join(lines)

    # Print the update info and write
    print(f"updating {summary_file.relative_to(DOCS_ROOT)} with {len(new_entries)} module entries")
    if not dry_run:
        summary_file.write_text(new_text)

# main is the entry point of the script
def main() -> None:
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--swagger", type=Path, required=True, help="Path to Swagger/OpenAPI JSON file")
    parser.add_argument("--api-ref-dir", type=Path, default=DEFAULT_API_REF_DIR, help="Output directory for generated pages")
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY_FILE, help="Path to SUMMARY.md")
    parser.add_argument("--skip-summary", action="store_true", help="Do not touch SUMMARY.md")
    parser.add_argument("--dry-run", action="store_true", help="Print what would happen without writing files")
    args = parser.parse_args()

    # Load the paths from the Swagger file and group them by module
    paths = load_paths(args.swagger)
    modules = group_by_module(paths)

    # Clear the old pages from the documentation
    clear_old_pages(args.api_ref_dir, args.dry_run)
    # Write the new module pages to the documentation
    write_module_pages(args.api_ref_dir, modules, args.dry_run)

    # Update the SUMMARY.md file unless the user requested to skip it
    if not args.skip_summary:
        update_summary(args.summary, args.api_ref_dir, modules, args.dry_run)

# Run main if main
if __name__ == "__main__":
    main()
