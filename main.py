import subprocess


subprocess = subprocess.Popen("python transcribe.py random1.mp3", shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()
print(subprocess_return)