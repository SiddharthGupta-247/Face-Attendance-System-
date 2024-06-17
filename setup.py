import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Program Files\Python312\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Program Files\Python312\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "Facial Recognition Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'images','data','database','AttendanceReport',r"C:\Users\gsidd\AppData\Roaming\Python\Python312\site-packages\mysql\connector"]}},
    version = "2.0",
    description = "Face Recognition Attendace System",
    executables = executables
    )
