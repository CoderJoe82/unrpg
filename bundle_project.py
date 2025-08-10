import os
import pyperclip  # A library to copy text to the clipboard.
                  # Install it with: pip install pyperclip

def bundle_project_files(project_root="."):
    """
    Scans the project directory, bundles specified file types into a single
    string, and copies it to the clipboard.
    """
    
    # --- CONFIGURATION ---
    # List of file extensions to include in the bundle
    include_extensions = {".py", ".txt", ".json"} 
    
    # List of directories to exclude from the scan
    # *** CORRECTED: "states" has been REMOVED from this list ***
    exclude_dirs = {"venv", ".git", "__pycache__"} 
    
    # List of specific files to exclude
    exclude_files = {"bundle_project.py"} # Don't include this script in the bundle!
    # -------------------

    bundled_content = []
    
    print("Starting project scan (Corrected Version)...")
    
    for root, dirs, files in os.walk(project_root, topdown=True):
        # Modify the list of directories *in place* to prevent os.walk from descending into them
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        # Sort files for consistent order
        for file in sorted(files):
            # Check if the file should be excluded
            if file in exclude_files:
                continue

            # Check if the file has an included extension
            if any(file.endswith(ext) for ext in include_extensions):
                file_path = os.path.join(root, file)
                
                # Use a clear separator to indicate the file's origin, works for subdirectories
                relative_path = os.path.relpath(file_path, project_root).replace(os.sep, '/')
                separator = f"# From {relative_path}:"
                bundled_content.append(separator)
                
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        bundled_content.append(f.read())
                except Exception as e:
                    bundled_content.append(f"# Error reading file: {e}")
                
                # Add a blank line for better separation between files
                bundled_content.append("\n")

    full_bundle = "\n".join(bundled_content)
    
    try:
        pyperclip.copy(full_bundle)
        print("\n✅ Project content bundled and copied to clipboard!")
        print(f"   Total characters: {len(full_bundle)}")
    except pyperclip.PyperclipException:
        print("\n❌ Could not copy to clipboard. Pyperclip may not be configured correctly.")
        print("   You can manually copy the output from 'bundle_output.txt'.")
        with open("bundle_output.txt", "w", encoding="utf-8") as f:
            f.write(full_bundle)

if __name__ == "__main__":
    bundle_project_files()