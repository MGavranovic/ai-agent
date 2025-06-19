import os

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    true_path = os.path.join(abs_working_directory, file_path)
    if not true_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    elif not os.path.exists(true_path):
        try:
            path = os.path.dirname(true_path)
            if len(path) > 0:
                os.makedirs(path, exist_ok=True)
            else:
                pass
        except OSError as e:
            return f'Error: issue with {e}'
        
    try:
        with open(true_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except OSError as e:
        return f'Error: issue with {e}'
        