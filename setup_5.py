import os
from cx_Freeze import setup, Executable
import sys

os.environ['TCL_LIBRARY'] = "C:\\python34\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\python34\\tcl\\tk8.6"

setup(
    name = "Car Mania",
    version = "0.1",
    options = {"build_exe": {"packages":["pygame","sys","pickle","dbm"],
                           "include_files":[os.path.join('C:\python34','DLLs','tk86t.dll'),os.path.join('C:\python34','DLLs','tcl86t.dll'),"icon.png","explode.png","Car.jpg","intro_1.jpg","Road.jpg","Grass.jpg","crash.wav","Ahrix.ogg","Alan_1.ogg","car_1.png","car_2.png","car_3.png","car_4.png","car_5.png","car_6.png","car_7.png","car_8.png","car_9.png","car_10.png"]}},
    executables = [Executable(script = "Car_Mania.py", base = "Win32GUI", icon = "icon.ico")]
    )
