import sys
import subprocess

subprocess.Popen('echo "' + sys.argv[1] + '"', shell=True)
