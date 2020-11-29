# Issues: Nones are not handled correctly in list splitting. They don't always fall in the last split group...
# Issues: Grabbing screen height from the wrong div element.

import itertools
import numpy as np
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import GetRevisionIDs as gr
import GetRevisionTimestamps as gs
import GetLongestRevisionHeight as rh


def GetWikiPics(Title, filepath):
    page_title = Title
    snapshot_url = f'https://en.wikipedia.org/w/index.php?title={page_title}'
    rev_pic_num = 1

    imgfilepath = os.path.join(filepath, page_title + '_movie')

    if not os.path.exists(imgfilepath):
        os.makedirs(imgfilepath)

    height = rh.get_big_page_height(page_title)

    rev_ids = gr.get_revisions(page_title)
    split_rev_ids = np.array_split(rev_ids, 5)

    timestamps = gs.get_revision_timestamps(page_title)
    split_timestamps = np.array_split(timestamps, 5)

    chunk0 = split_rev_ids[0]
    chunk1 = split_rev_ids[1]
    chunk2 = split_rev_ids[2]
    chunk3 = split_rev_ids[3]
    chunk4 = split_rev_ids[4]

    schunk0 = split_timestamps[0]
    schunk1 = split_timestamps[1]
    schunk2 = split_timestamps[2]
    schunk3 = split_timestamps[3]
    schunk4 = split_timestamps[4]

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')

    for (a, b, c, d, e, aa, bb, cc, dd, ee) in itertools.zip_longest(chunk0, chunk1, chunk2, chunk3, chunk4, schunk0, schunk1, schunk2, schunk3, schunk4):
        if None in (a, b, c, d, e):
            print(f'acquiring page ids | timestamps: {a, b, c, d} | {aa, bb, cc, dd}')

        # Open browser session
            # a block
            page_id_a = a
            page_id_param_a = f'&oldid={page_id_a}'
            full_url_a = snapshot_url + page_id_param_a
            driver_a = webdriver.Chrome(options=chrome_options)
            driver_a.get(full_url_a)

            # b block
            page_id_b = b
            page_id_param_b = f'&oldid={page_id_b}'
            full_url_b = snapshot_url + page_id_param_b
            driver_b = webdriver.Chrome(options=chrome_options)
            driver_b.get(full_url_b)

            # c block
            page_id_c = c
            page_id_param_c = f'&oldid={page_id_c}'
            full_url_c = snapshot_url + page_id_param_c
            driver_c = webdriver.Chrome(options=chrome_options)
            driver_c.get(full_url_c)

            # d block
            page_id_d = d
            page_id_param_d = f'&oldid={page_id_d}'
            full_url_d = snapshot_url + page_id_param_d
            driver_d = webdriver.Chrome(options=chrome_options)
            driver_d.get(full_url_d)
            time.sleep(2)

        # Take pics
            # a block
            imgpath_a = os.path.join(imgfilepath, f'img_{a}_{aa}.png')
            driver_a.set_window_size(1920, height)

            # b block
            imgpath_b = os.path.join(imgfilepath, f'img_{b}_{bb}.png')
            driver_b.set_window_size(1920, height)

            # c block
            imgpath_c = os.path.join(imgfilepath, f'img_{c}_{cc}.png')
            driver_c.set_window_size(1920, height)

            # d block
            imgpath_d = os.path.join(imgfilepath, f'img_{d}_{dd}.png')
            driver_d.set_window_size(1920, height)
            time.sleep(2)

        # Save pics
            # a block
            driver_a.save_screenshot(imgpath_a)
            driver_a.quit()

            # b block
            driver_b.save_screenshot(imgpath_b)
            driver_b.quit()

            # c block
            driver_c.save_screenshot(imgpath_c)
            driver_c.quit()

            # d block
            driver_d.save_screenshot(imgpath_d)
            driver_d.quit()

        else:
            print(f'acquiring page ids | timestamps: {a, b, c, d, e} | {aa, bb, cc, dd, ee}')

        # Open browser session
            # a block
            page_id_a = a
            page_id_param_a = f'&oldid={page_id_a}'
            full_url_a = snapshot_url + page_id_param_a
            driver_a = webdriver.Chrome(options=chrome_options)
            driver_a.get(full_url_a)
            #time.sleep(2)

            # b block
            page_id_b = b
            page_id_param_b = f'&oldid={page_id_b}'
            full_url_b = snapshot_url + page_id_param_b
            driver_b = webdriver.Chrome(options=chrome_options)
            driver_b.get(full_url_b)
            #time.sleep(2)

            # c block
            page_id_c = c
            page_id_param_c = f'&oldid={page_id_c}'
            full_url_c = snapshot_url + page_id_param_c
            driver_c = webdriver.Chrome(options=chrome_options)
            driver_c.get(full_url_c)
            #time.sleep(2)

            # d block
            page_id_d = d
            page_id_param_d = f'&oldid={page_id_d}'
            full_url_d = snapshot_url + page_id_param_d
            driver_d = webdriver.Chrome(options=chrome_options)
            driver_d.get(full_url_d)
            #time.sleep(2)

            # e block
            page_id_e = e
            page_id_param_e = f'&oldid={page_id_e}'
            full_url_e = snapshot_url + page_id_param_e
            driver_e = webdriver.Chrome(options=chrome_options)
            driver_e.get(full_url_e)
            time.sleep(2)


        # Take pics
            # a block
            imgpath_a = os.path.join(imgfilepath, f'img_{a}_{aa}.png')
            driver_a.set_window_size(1920, height)

            # b block
            imgpath_b = os.path.join(imgfilepath, f'img_{b}_{bb}.png')
            driver_b.set_window_size(1920, height)

            # c block
            imgpath_c = os.path.join(imgfilepath, f'img_{c}_{cc}.png')
            driver_c.set_window_size(1920, height)

            # d block
            imgpath_d = os.path.join(imgfilepath, f'img_{d}_{dd}.png')
            driver_d.set_window_size(1920, height)

            # e block
            imgpath_e = os.path.join(imgfilepath, f'img_{e}_{ee}.png')
            driver_e.set_window_size(1920, height)
            time.sleep(2)

        # Save pics
            # a block
            driver_a.save_screenshot(imgpath_a)
            driver_a.quit()

            # b block
            driver_b.save_screenshot(imgpath_b)
            driver_b.quit()

            # c block
            driver_c.save_screenshot(imgpath_c)
            driver_c.quit()

            # d block
            driver_d.save_screenshot(imgpath_d)
            driver_d.quit()

            # e block
            driver_e.save_screenshot(imgpath_e)
            driver_e.quit()

    '''
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
    '''


