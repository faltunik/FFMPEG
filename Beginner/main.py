import os
import subprocess
import sys
from random import randint

# cmd = ['ffmpeg', '-i', input, output]
#         subprocess.check_output(cmd)



def extract_text():
    try:
        input = 'inputvid.mp4'
        output = 'output.txt'
        cmd = ['ffmpeg', '-i', input, output]
        subprocess.check_output(cmd)
    except Exception as e:
        print('error is ', e)

if __name__ == '__main__':
    extract_text()