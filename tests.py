import os
# from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

# print(os.getcwd())
# print(os.path.abspath("calculator"))

# print(get_file_content(".", "."))
print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))