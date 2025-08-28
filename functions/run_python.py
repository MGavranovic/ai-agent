import os
import subprocess
import sys
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    true_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
    if not true_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(true_path):
        return f'Error: File "{file_path}" not found.'
    elif not str.endswith(true_path, ".py"):
        return f'Error: "{file_path}" is not a Python file.'
    else:
        cmd = [sys.executable, true_path, *args]
        try:
            cp = subprocess.run(cmd, cwd=abs_working_directory, capture_output=True, text=True, timeout=30)
            lines = []
            if cp.stdout != "":
                lines.append(f"STDOUT: {cp.stdout}")
            if cp.stderr != "":
                lines.append(f"STDERR: {cp.stderr}")
            if cp.returncode != 0:
                lines.append(f"Process exited with code {cp.returncode}")
            if lines.__len__() == 0:
                return "No output produced."
            else:
                return "\n".join(lines)
        except Exception as e:
            return f"Error: executing Python file: {e}"
        

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the provided file with the provided args, constrained to the working directory. If no args exist, still runs the file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to a file for running, relative to the working directory."
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="The args to provide to the file (file_path) that is to be ran."
            )
        }
    )
)