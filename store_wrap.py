import subprocess
import sys

APP_NAME = 'paintdotnet.exe'

def find_app_path():
    # to find the name of the package run Get-AppxPackage in PowerShell
    command = 'powershell.exe -Command "& {Get-AppxPackage -name dotPDNLLC.paint.net}"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # Wait for the command to finish and get the output
    stdout, stderr = process.communicate()
    output = stdout.decode('utf-8')
    for line in output.splitlines():
      if line.startswith('InstallLocation'):
          start = line.find(":") + 2
          dir =  line[start:]
          break
    return dir + '\\' + APP_NAME
        
def main():
    # total arguments
    n = len(sys.argv)
    if n != 2:
        raise ValueError("Expected one argument")

    paintNET = find_app_path()
    subprocess.Popen([paintNET, sys.argv[1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

if __name__ == '__main__':
    main()
