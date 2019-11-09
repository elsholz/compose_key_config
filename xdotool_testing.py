import subprocess

for c in 'Hello World':
	subprocess.call(f'xdotool key {c}'.split(' '))
