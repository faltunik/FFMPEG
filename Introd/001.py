import os
import subprocess
import sys
from random import randint

# ffmpeg -loop 1 -i img.jpg -i music.mp3 -shortest -acodec copy -vcodec mjpeg result.mkv


def create_video():
    try:
        img_input = 'Introd\elon.jpg'
        music_input = 'Introd\manmera.mp3'
        s = f"ffmpeg -loop 1 -i {img_input} -i {music_input} -acodec copy -vcodec libx264 result.mp4"
        cmd = s.split(" ")
        subprocess.check_output(cmd)
    
    except Exception as e:
        print('error is ', e)


if __name__ == '__main__':
    create_video()

    