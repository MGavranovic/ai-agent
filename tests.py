import os
from functions.get_files_info import get_files_info

print(os.getcwd())
print(os.path.abspath("calculator"))

print(get_files_info(".", "."))
print(get_files_info("calculator", "calculator/pkg"))
print(get_files_info(".", "/bin"))
print(get_files_info(".", "../"))