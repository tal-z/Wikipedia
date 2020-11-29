import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import GetRevisionIDs as gr
import GetRevisionTimestamps as gs
import GetLongestRevisionHeight as rh
from PIL import Image
from skimage import data, io
from skimage.transform import rescale, resize
from skimage import img_as_ubyte


def GetWikiPics(Title, filepath, HEIGHT, WIDTH):
    page_title = Title
    snapshot_url = f'https://en.wikipedia.org/w/index.php?title={page_title}'
    rev_pic_num = 1

    height = HEIGHT

    imgfilepath = os.path.join(filepath, page_title + '_movie')

    if not os.path.exists(imgfilepath):
        os.makedirs(imgfilepath)


    rev_ids = gr.get_revisions(page_title)
    # timestamps = gs.get_revision_timestamps(page_title)

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')

    # later, test which is quicker
    for entry in rev_ids:
        page_id = entry
        page_id_param = f'&oldid={page_id}'
        full_url = snapshot_url + page_id_param
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(full_url)
        #time.sleep(2)
        #driver.implicitly_wait(1)

        print(f'page {rev_pic_num} height: {height}')

        imgpath = os.path.join(imgfilepath, f'page_{rev_pic_num}.png')

        driver.set_window_size(WIDTH, HEIGHT, windowHandle='current')  # the trick
        #time.sleep(2)
        #driver.implicitly_wait(1)
        driver.save_screenshot(imgpath)
        driver.quit()
        photo = io.imread(imgpath)
        photo_resized = resize(photo, (photo.shape[0] // 4,photo.shape[1] // 4))
        #smallerphoto = photo[::2, ::2]
        io.imsave(imgpath, img_as_ubyte(photo_resized))


        rev_pic_num += 1

    return imgfilepath, page_title
