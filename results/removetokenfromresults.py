import os
import json
from pathlib import Path

def find_args_dict_json(root_folder):
    """Find all 'args_dict.json' files in the given root folder and its subfolders."""
    return list(Path(root_folder).rglob('args_dict.json'))

def remove_token_field(file_path):
    """Read the JSON file, remove the 'token' field if it exists, and save it back."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Remove the 'token' field if it exists
        if 'token' in data:
            del data['token']

            # Save the modified JSON back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)

            print(f"Updated: {file_path}")
        else:
            print(f"'token' not found in: {file_path}")

    except (json.JSONDecodeError, IOError) as e:
        print(f"Error processing {file_path}: {e}")

def process_json_files(root_directory):
    """Find and process all 'args_dict.json' files in the root directory."""
    found_files = find_args_dict_json(root_directory)

    if not found_files:
        print("No 'args_dict.json' files found.")
        return

    for file_path in found_files:
        remove_token_field(file_path)

# Example usage:
if __name__ == "__main__":
    root_directory = "./results"
    process_json_files(root_directory)
