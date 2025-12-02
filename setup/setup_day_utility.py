import pathlib
import sys
import argparse
from typing import Optional

# --- Configuration ---
# 1. Determine the directory where this script is located (e.g., /project/setup)
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

# 2. Define the project root as the parent of the script's directory (e.g., /project)
# This allows the script to be run from a subfolder like 'setup' but output to the parent.
PROJECT_ROOT = SCRIPT_DIR.parent

# Set the template file path, assuming it stays within the SCRIPT_DIR ('setup' folder).
TEMPLATE_FILENAME = "template.py"
# ---------------------


def create_day_structure(year: int, day: int, template_content: str):
    """
    Creates the required folder structure and initial files for a new AOC day,
    placing the output in the PROJECT_ROOT.
    """
    day_folder_name = f"d{day:02d}"

    # Define paths relative to the PROJECT_ROOT (e.g., /project)
    aoc_year_path = PROJECT_ROOT / f"aoc_{year}"
    data_path = aoc_year_path / "data"
    data_day_path = data_path / day_folder_name

    # 📌 FIX: Use the new, more explicit naming pattern
    solution_file_path = aoc_year_path / f"aoc{year}_day{day:02d}.py"

    input_file_path = data_day_path / "input.txt"
    test_file_path = data_day_path / "test.txt"

    print(f"\n--- Setting up AOC {year} Day {day:02d} ({day_folder_name}) ---")
    print(f"Outputting to project root: {PROJECT_ROOT}")

    # 1. Create Data Folders
    try:
        data_day_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created data directory: {data_day_path}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return

    # 2. Create input.txt and test.txt (if they don't exist)
    if not input_file_path.exists():
        input_file_path.touch()
        print(f"✅ Created empty input file: {input_file_path.name}")
    else:
        print(f"⚠️ Input file already exists: {input_file_path.name}")

    if not test_file_path.exists():
        test_file_path.touch()
        print(f"✅ Created empty test file: {test_file_path.name}")
    else:
        print(f"⚠️ Test file already exists: {test_file_path.name}")

    # 3. Create Solution Script from Template
    # We already checked for empty template_content in main(), but keep this check for safety.
    if not template_content:
        print(f"❌ Template content is empty. Skipping solution file creation.")
        return

    if not solution_file_path.exists():
        try:
            # Substitute dynamic values into the template
            content = template_content.replace(
                "{AOC_URL_PLACEHOLDER}", f"# https://adventofcode.com/{year}/day/{day}"
            )
            content = content.replace("{AOC_YEAR_PLACEHOLDER}", str(year))
            content = content.replace("{AOC_DAY_PLACEHOLDER}", str(day))
            content = content.replace(
                "{EXTRA_IMPORTS_PLACEHOLDER}", ""
            )  # Start with no extra imports
            content = content.replace(
                "{CUSTOM_FUNCTIONS_PLACEHOLDER}", ""
            )  # Start with no custom functions
            content = content.replace(
                "{PART1_BODY_PLACEHOLDER}", "pass # Your solution for Part 1 goes here"
            )
            content = content.replace(
                "{PART2_BODY_PLACEHOLDER}", "pass # Your solution for Part 2 goes here"
            )

            # Remove the placeholder comments from the function bodies if they exist
            content = content.replace("    # pass", "    pass")

            solution_file_path.write_text(content, encoding="UTF-8")
            print(f"✅ Created solution script: {solution_file_path.name}")

        except Exception as e:
            print(f"❌ Error creating solution file: {e}")
    else:
        print(f"⚠️ Solution script already exists: {solution_file_path.name}. Skipping.")


def main():
    """Parses command-line arguments and initiates the folder creation."""
    parser = argparse.ArgumentParser(
        description="AOC Day Setup Utility: Creates folder structure and solution file from a template."
    )
    parser.add_argument("year", type=int, help="The Advent of Code year (e.g., 2024).")
    parser.add_argument("day", type=int, help="The Advent of Code day (1-25).")

    args = parser.parse_args()

    if not 1 <= args.day <= 25:
        print("Error: Day must be between 1 and 25.")
        sys.exit(1)

    # 1. Load Template (Template is assumed to be in the SCRIPT_DIR, e.g., 'setup' folder)
    template_path = SCRIPT_DIR / TEMPLATE_FILENAME
    template_content: Optional[str] = None

    if not template_path.exists():
        print(
            f"Error: Template file '{template_path.name}' not found at {template_path.resolve()}."
        )
        print(
            "Please ensure 'template.py' is located in the same directory as 'setup_day_utility.py'."
        )
        sys.exit(1)

    try:
        template_content = template_path.read_text(encoding="UTF-8")
    except Exception as e:
        print(f"Error reading template file '{template_path.name}': {e}")
        sys.exit(1)

    if not template_content.strip():
        print(f"Error: Template file '{template_path.name}' is empty.")
        sys.exit(1)

    # 2. Execute creation
    create_day_structure(args.year, args.day, template_content)


if __name__ == "__main__":
    main()
