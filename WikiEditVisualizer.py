import GetLongestRevisionHeight as gh
from skimage import data, io
from matplotlib import pyplot as plt

import GetWikiPicsImprove as gp
import ImageCompiler as ic
import os
import shutil



def visualize_wiki_revisions(Title, filepath):
    bigpic_size = gh.get_big_page_size(Title)
    #print(f'Max height to trim: {bigpic.shape[0]}')
    #plt.imshow(bigpic)
    #plt.show()
    #INPUT_HEIGHT = bigpic.shape[0]
    HEIGHT = bigpic_size[1] #int(INPUT_HEIGHT)
    WIDTH = bigpic_size[0]
    print(f'Height is {HEIGHT}')
    print(f'Width is {WIDTH}')
    wikipics = gp.GetWikiPics(Title, filepath, HEIGHT, WIDTH)
    ic.ImageCompiler(wikipics[0], wikipics[1])
#    print(os.path.join(os.path.dirname(wikipics[0]), (wikipics[1]) + '.avi'))
    shutil.move(os.path.join(os.path.dirname(wikipics[0]), (wikipics[1]) + '.avi'), os.path.join(os.path.dirname(wikipics[0]), (wikipics[1] + '_movie')))


visualize_wiki_revisions('Max Blumenthal', '/Users/talzaken/PycharmProjects/WikipediaVisualizer/')


