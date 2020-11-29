from typing import List

import cv2
import os
import re


def ImageCompiler(imgfilepath, TITLE):
    image_folder = imgfilepath
    video_name = TITLE + '.avi'

    print(image_folder)

    fps = 25  # frames per second

    # define custom key using regex pattern
    r = re.compile(r'page_(\d+)')

    def key_func(m):
        return int(r.search(m).group(1))

    # get images from imgfilepath and sort them in reverse order according to the custom key
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort(key=key_func, reverse=True)

    print(images)

    # create frame from the first image in imgfilepath
    #this is my problem. The frame height/width needs to be set to the size specified in ImageCompiler
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # add images to frame, set framerate
    video = cv2.VideoWriter(video_name, 0, fps, (width, height))
    print(video)
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()

    return

