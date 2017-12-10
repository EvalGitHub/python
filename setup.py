#encoding utf-8

import sys
from cx_Freeze import setup,Executable
import os

os.environ['TCL_LIBRARY']= r"F:\python\install\tcl\tcl8.6"

os.environ['TK_LIBRARY']= r"F:\python\install\tcl\tk8.6"


include_files =[
    r"F:\python\install\DLLs\tcl86t.dll",
    r"F:\python\install\DLLs\tkl86t.dll"
]


#最中打包的程序需要包含呢写文件
build_exe_options = {"packages":["os","tkinter"],"include_files":include_files}

base= None

if sys.platform =='win64':
    base ="Win64GUI"

setup(
    name="myDict",
    version="0.1",
    description="learn you best",
    options={"build_exe":build_exe_options},
    executables=[Executable("window.by",base=base)])
