import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import GetRevisionIDs as gr
import GetRevisionTimestamps as gs
import GetLongestRevisionHeight as rh
from PIL import Image


def GetWikiPics(Title, filepath):
    page_title = Title
    snapshot_url = f'https://en.wikipedia.org/w/index.php?title={page_title}'
    rev_pic_num = 1

    imgfilepath = os.path.join(filepath, page_title + '_movie')

    if not os.path.exists(imgfilepath):
        os.makedirs(imgfilepath)

    height = (rh.get_big_page_height(page_title))

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
        time.sleep(2)

        print(f'page {rev_pic_num} height: {height}')

        imgpath = os.path.join(imgfilepath, f'page_{rev_pic_num}.png')

        driver.set_window_size(1920, height)  # the trick
        time.sleep(2)
        driver.save_screenshot(imgpath)
        driver.quit()
        rev_pic_num += 1

    return imgfilepath, page_title
