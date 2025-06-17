import os

def get_files_info(working_directory, directory=None):
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(directory)
    if not abs_directory.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(abs_directory):
        return f'Error: "{directory}" is not a directory'
    else:
        rtrn_str = ""
        for f in os.listdir(directory):
            path = os.path.join(directory, f)
            rtrn_str += f"- {f}: file_size={os.path.getsize(path)}, is_dir={os.path.isdir(path)}\n"
        return rtrn_str