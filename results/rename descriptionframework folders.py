import os
from pathlib import Path

# Define the pattern to remove
PATTERN_TO_REMOVE = "-1.2-0.9-1-Llama-3.1-70B-Instruct"


def rename_subfolders_recursively(root_folder):
    """Recursively rename subfolders by removing a specific pattern from their names."""
    for folder in sorted(Path(root_folder).rglob('*'), key=lambda x: -len(str(x))):
        if folder.is_dir():  # Ensure it's a directory
            new_name = folder.name.replace(PATTERN_TO_REMOVE, "")

            if new_name != folder.name:  # Rename only if different
                new_path = folder.parent / new_name
                try:
                    folder.rename(new_path)
                    print(f"Renamed: {folder} ➝ {new_path}")
                except Exception as e:
                    print(f"Error renaming {folder}: {e}")


# Example usage:
if __name__ == "__main__":
    root_directory = "./results"  # Change this to your directory
    rename_subfolders_recursively(root_directory)
