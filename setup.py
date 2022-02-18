import cx_Freeze
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("PetalmServices.py", base=base,icon="icon.ico")]

cx_Freeze.setup(
    name = "Petalm Africa Services",
    options = {"build_exe": {"packages":["PyQt5","openpyxl","os"], "include_files":["icon.ico","database.py","database.sqlite","test.xlsx"]}},
    version = "1.0",
    author = "Nyasha Chizampeni",
    description = "Petalm Africa Services EWD Report Generator",
    executables = executables
    )
