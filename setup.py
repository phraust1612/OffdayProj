import sys
from cx_Freeze import setup, Executable

build_exe_options = dict(
        includes=["sys","PyQt5"],
        include_files=["CPortal.py","CRefine.py"]
)

setup(  name = "외박프로그램4.0",
        version = "4.0",
        description = "외박프로그램4.0",
        author = "phraust",
        options={"build_exe":build_exe_options},
        executables = [Executable("MainDialog.py", base="Win32GUI",targetName="외박프로그램.exe",icon="charm2.ico")])
