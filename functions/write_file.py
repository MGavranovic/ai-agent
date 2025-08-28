import os
from google.genai import types

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
        
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the provided content to the provided file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to a file to which to write the content to, relative to the working directory."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file provided, file_path."
            )
        }
    )
)