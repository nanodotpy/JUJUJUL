import cx_Freeze

target = cx_Freeze.Executable(
    script="JUJUJUL.py",
    base = "Win32GUI",
    icon=r"E:\putting 1s and 0s in the right order\Le J\Google Chrome.ico"
    )


cx_Freeze.setup(
        name = "JUJUJUL",
        
        options = {"build_exe" : {"packages": ["ctypes", "winsound"], "include_files" : ["JUJUJUL.jpg" , "Jul - On Mappelle Lovni  Clip Officiel  2016.wav"] } } ,
        
        description = "Le J",
        executables = [target],
        version = "6.9"
        )
