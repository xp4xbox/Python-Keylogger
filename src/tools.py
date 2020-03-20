import subprocess

def get_env_var(var):
    command = subprocess.Popen(f"echo {var}", stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE, shell=True)
    return ((command.stdout.read()).decode("utf-8").splitlines()[0]).replace("\\", "/")
