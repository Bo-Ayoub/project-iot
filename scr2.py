def remove_bom_from_file(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()

    # Check if BOM exists at the start of the file (UTF-8 BOM: 0xEF, 0xBB, 0xBF)
    if content.startswith(b'\xef\xbb\xbf'):
        content = content[3:]  # Remove the BOM (first 3 bytes)

    with open(file_path, 'wb') as f:
        f.write(content)


# Specify the path to your models.py file
remove_bom_from_file(r'C:\Users\ayoub\OneDrive\Bureau\finalProjectIOt\myapp\models.py')
