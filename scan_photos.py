import os
import json

# Configuration
IMAGE_DIR = 'images'  # The folder where your actual photos live
OUTPUT_FILE = 'data.js' # The file we will generate

# valid extensions to look for
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.mp4', '.webp')

def generate_file_list():
    # Check if image directory exists
    if not os.path.exists(IMAGE_DIR):
        print(f"Error: Directory '{IMAGE_DIR}' not found.")
        print("Please make sure this script is next to your 'images' folder.")
        return

    print(f"Scanning '{IMAGE_DIR}' for photos...")
    
    file_list = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(IMAGE_DIR):
        for filename in files:
            if filename.lower().endswith(VALID_EXTENSIONS):
                # We just want the filename, assuming a flat structure inside 'images'
                # If you have subfolders, we might need to adjust this.
                file_list.append(filename)

    # Sort files to keep order consistent
    file_list.sort()
    
    # Calculate stats
    count = len(file_list)
    print(f"Found {count} files.")

    # Create the JavaScript content
    # We use json.dumps to safely format the list as a Javascript array string
    js_content = f"const rawFileList = {json.dumps(file_list, indent=4)};"

    # Write to file
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(js_content)
        print(f"Success! Generated '{OUTPUT_FILE}'.")
    except Exception as e:
        print(f"Error writing file: {e}")

if __name__ == "__main__":
    generate_file_list()
    input("\nPress Enter to exit...")

