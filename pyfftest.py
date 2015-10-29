import subprocess
import sys
filename = sys.argv[1]
#http://bytes.com/topic/python/answers/649282-how-add-extension-input-filename
output = filename + ".mov"
final = output + ".mkv"
print filename
print output


subprocess.call(['ffmpeg','-i', filename, '-c:v', 'v210', output ])
subprocess.call(['ffmpeg','-i', output, '-c:v', 'prores', final ])
