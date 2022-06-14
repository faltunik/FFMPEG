import os
import subprocess
import sys
from random import randint
import time


def delete_file(path,sleep):
    if os.path.exists(path):
        print('let me sleep first')
        time.sleep(sleep)
        print('time to wakeup')
        os.remove(path)
        print("file deleted")
    else:
        print("file not found")

def create_video():
    # ./musicalvideo/mus_vid.%03d.jpg
    input = "D:/Courses/FFMPEG/video_create/sample_img/img_%03d.jpg" #video_create
    input2 = "D:/Courses/FFMPEG/video_create/manmera.mp3"
    output = "D:/Courses/FFMPEG/video_create/sample_img_result.mp4"
    frame_rate = 1

    s = f"ffmpeg -framerate {frame_rate} -i {input} -i {input2} -c:v libx264 -r 30 -pix_fmt yuv420p {output}"
    # ffmpeg: we wanna use ffmpeg
    # -framerate: default: 25: framerate for output video
    # -i: input file
    # -c:v: video codec
    # in case it images are not sequential
    # ffmpeg -framerate 10 -pattern_type  glob -i "filename-*.jpg" output.mp4
    cmd = s.split(" ")
    subprocess.check_output(cmd)
    print("video created")
    return output


def create_gif():
    input = "D:/Courses/FFMPEG/video_create/sample_img/img_%03d.jpg" #video_create
    input2 = "D:/Courses/FFMPEG/video_create/manmera.mp3"
    output = "D:/Courses/FFMPEG/video_create/sample_img_result.gif"
    frame_rate = 3
    s = f"ffmpeg -framerate {frame_rate} -i {input} {output}"
    cmd = s.split(" ")
    subprocess.check_output(cmd)
    # ffmpeg -f image2 -framerate 1 -i simpimgs%03d.jpg -loop -1 simpson.gif


#not running properly
def create_vintage():
    """
    -i: input file
    -filter: v 
    """

    input = "D:/Courses/FFMPEG/video_create/inputvid.mp4"
    output = "D:/Courses/FFMPEG/video_create/outputvid.mp4"
    #s = f"ffmpeg -i {input} -filter:v fps=1.25 {output}"
    s = f"ffmpeg -i {input} -vf curves=vintage -pix_fmt yuv420p {output}"

    cmd = s.split(" ")
    subprocess.check_output(cmd)


def speed_audio():
    """
    Speed up the audio
    """
    input2 = "D:/Courses/FFMPEG/video_create/manmera.mp3"
    output = "D:/Courses/FFMPEG/video_create/manmera_speed.mp3"
    s = f"ffmpeg -i {input2} -filter:a atempo=2 {output}"
    cmd = s.split(" ")
    subprocess.check_output(cmd)




    









if __name__ == '__main__':
    #create_gif()
    # x = create_video()
    # delete_file(x, 30)
    create_vintage()
    #speed_audio()
    