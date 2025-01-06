import os

def remove_null_bytes_from_files(directory):
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".py"):  # Only target Python files
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'rb') as f:
                    content = f.read()
                # Check if there are null bytes
                if b'\0' in content:
                    print(f"Null bytes found in {file_path}")
                    # Remove null bytes and rewrite the file
                    with open(file_path, 'wb') as f:
                        f.write(content.replace(b'\0', b''))
                    print(f"Null bytes removed from {file_path}")

# Run the function for your project directory
remove_null_bytes_from_files(r'C:\Users\ayoub\OneDrive\Bureau\finalProjectIOt\myapp')
