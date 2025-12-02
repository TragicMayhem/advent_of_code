import pathlib
import sys
import argparse
from typing import Optional

# --- Configuration ---
# Set the root of your project. This script assumes it is run from the folder
# containing the 'aoc_YYYY' directory (e.g., the parent of aoc_2024).
# We use __file__.resolve().parent to reliably find the script's location.
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

# Set the template file path relative to this script's location.
TEMPLATE_FILENAME = "template.py"
# ---------------------


def create_day_structure(year: int, day: int, template_content: str):
    """
    Creates the required folder structure and initial files for a new AOC day.
    """
    day_folder_name = f"d{day:02d}"

    # Define paths
    aoc_year_path = SCRIPT_DIR / f"aoc_{year}"
    data_path = aoc_year_path / "data"
    data_day_path = data_path / day_folder_name

    solution_file_path = aoc_year_path / f"{day_folder_name}_solution.py"
    input_file_path = data_day_path / "input.txt"
    test_file_path = data_day_path / "test.txt"

    print(f"\n--- Setting up AOC {year} Day {day:02d} ({day_folder_name}) ---")

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

    # 1. Load Template
    template_path = SCRIPT_DIR / TEMPLATE_FILENAME
    template_content: Optional[str] = None

    if template_path.exists():
        try:
            template_content = template_path.read_text(encoding="UTF-8")
        except Exception as e:
            print(f"Error reading template file '{template_path.name}': {e}")
            sys.exit(1)
    else:
        print(
            f"Error: Template file '{template_path.name}' not found at {template_path.resolve()}."
        )
        print(
            "Using a basic template structure without the specific custom placeholders."
        )
        # If the specific template is missing, we use a minimal one to still create the file.
        template_content = (
            "import pathlib\nimport time\n\n"
            "CURRENT_AOC_YEAR = {AOC_YEAR_PLACEHOLDER}\n"
            "DAY_NUMBER = {AOC_DAY_PLACEHOLDER}\n"
            "\n# Complete the rest of the file using the standard template structure."
        )

    # 2. Execute creation
    create_day_structure(args.year, args.day, template_content)


if __name__ == "__main__":
    main()
