'''
use this snippet to display the chunked image

io.imshow(chunk_img('/Users/talzaken/Library/Application Support/JetBrains/PyCharmCE2020.1/scratches/Little Red LighthouseLongShot.png', 300))
io.show()
'''

from skimage import data, io, segmentation
import cv2
import imageio


def chunk_img(filepath, chunk_height):
    pic = cv2.imread(filepath)
    #pic = cv2.cvtColor(pic, cv2.COLOR_BGR2BGRA)

    pic_height = pic.shape[0]

    #chunk_height = 1000

    num_chunks = int(pic_height/chunk_height)

    offset = 0

    piclist = []
    for i in range(num_chunks):
        littlepic = pic[offset:offset+chunk_height:,:pic.shape[1]:]
        piclist.append(littlepic)
        offset+=chunk_height

    conc_chunks = cv2.hconcat(piclist)
    conc_chunks = cv2.cvtColor(conc_chunks, cv2.COLOR_BGR2BGRA)

    return conc_chunks


#imageio.imwrite('/Users/talzaken/PycharmProjects/WikipediaVisualizer/Castro/Trees of New York City_movie/chunk.png' , chunk_img('/Users/talzaken/PycharmProjects/WikipediaVisualizer/Castro/Max Blumenthal_movie/page_150.png', 300))
