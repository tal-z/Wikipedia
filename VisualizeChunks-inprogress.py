import GetLongestRevisionHeight as gh
from skimage import data, io
from matplotlib import pyplot as plt

import GetWikiPicsImprove as gp
import ImageCompiler as ic
import os
import shutil
import ImageChunks
import imageio


def visualize_wiki_chunked_revisions(Title, filepath):
    bigpic_size = gh.get_big_page_size(Title)
    HEIGHT = bigpic_size[1]  # int(INPUT_HEIGHT)
    WIDTH = bigpic_size[0]
    print(f'Height is {HEIGHT}')
    print(f'Width is {WIDTH}')
    wikipics = gp.GetWikiPics(Title, filepath, HEIGHT, WIDTH)

    ## loop through files, chunk them, then write the chunked files to a folder.
    filenames = os.listdir(wikipics[0])
    for name in filenames:
        read_filepath = os.path.join(wikipics[0], name)
        chunk_height = 50

    # This next code snippet has two parameters:
    # in the first parameter, it takes the absolute filepath of the file to write to.
    # be sure to include filename and extension
    # in the second parameter, it takes two arguments (arg1, arg2):
    #     arg1: the filepath of the image to chunk
    #     arg2: the desired column trim height

        imageio.imwrite(os.path.join(wikipics[0], name), ImageChunks.chunk_img(read_filepath, chunk_height))

    # then run that folder through ImageCompiler.
    ic.ImageCompiler(wikipics[0], wikipics[1])
    shutil.move(os.path.join(os.path.dirname(wikipics[0]), (wikipics[1]) + '.avi'), os.path.join(os.path.dirname(wikipics[0]), (wikipics[1] + '_movie')))


visualize_wiki_chunked_revisions('SKY', '/Users/talzaken/PycharmProjects/WikipediaVisualizer/')
