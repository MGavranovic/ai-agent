import os

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    true_path = os.path.join(abs_working_directory, file_path)
    if not true_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(true_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    else:
        MAX_CHARS = 10000
        try:
            with open(true_path, "r") as f:
                file_content = f.read(MAX_CHARS)
                more = f.read(1)
                if len(more) > 0:
                    return file_content + '[...File "{file_path}" truncated at 10000 characters]'
                else:
                    return file_content
        except OSError as e:
            return f'Error: issue with {e}'
        pass