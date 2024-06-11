from pathlib import Path

def write_file(file_name, file_content):
    """
    Writes the given content to the specified file.
    Adds the.txt extension if it's not present.
    Creates the file if it doesn't exist.
    """
    # Convert file_name to a Path object if it's not already one
    if isinstance(file_name, str):
        file_name = Path(file_name)
    
    # Ensure the file has a.txt extension
    if not file_name.suffix == '.txt':
        file_name = file_name.with_suffix('.txt')
    
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """
    Appends the given content to the specified file.
    Adds the.txt extension if it's not present.
    Creates the file if it doesn't exist.
    """
    # Convert file_name to a Path object if it's not already one
    if isinstance(file_name, str):
        file_name = Path(file_name)
    
    # Ensure the file has a.txt extension
    if not file_name.suffix == '.txt':
        file_name = file_name.with_suffix('.txt')
    
    with open(file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    """
    Reads the content of the specified file.
    Adds the.txt extension if it's not present.
    Raises FileNotFoundError if the file does not exist.
    """
    # Convert file_name to a Path object if it's not already one
    if isinstance(file_name, str):
        file_name = Path(file_name)
    
    # Ensure the file has a.txt extension
    if not file_name.suffix == '.txt':
        file_name = file_name.with_suffix('.txt')
    
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return None
