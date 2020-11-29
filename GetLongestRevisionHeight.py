import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from skimage import data, io
from skimage.transform import rescale, resize
from skimage import img_as_ubyte


def get_big_page_id(Title):
    TITLE = Title
    BASE_URL = "http://en.wikipedia.org/w/api.php"

    rev_lengths = []

    while not rev_lengths:
        # print('in while loop')
        parameters = {'action': 'query',
                      'format': 'json',
                      'titles': TITLE,
                      'prop': 'revisions',
                      'rvprop': 'ids|size',
                      'rvlimit': '500'}

        wp_call = requests.get(BASE_URL, params=parameters)
        response = wp_call.json()

        query = response['query']
        pages = query['pages']
        page_id = list(pages.keys())[0]
        pages_info = pages[page_id]
        pages_revisions = pages_info['revisions']

        for d in pages_revisions:
            tup = (d['revid'], d['size'])
            rev_lengths.append(tup)
    else:
        while str(len(pages_revisions)) == parameters['rvlimit']:
            # print('tuple list size: ' + str(len(rev_lengths)))
            start_id = (rev_lengths[-1])[0]
            parameters = {'action': 'query',
                          'format': 'json',
                          'titles': TITLE,
                          'prop': 'revisions',
                          'rvprop': 'ids|size',
                          'rvlimit': '500',
                          'rvstartid': start_id}

            wp_call = requests.get(BASE_URL, params=parameters)
            response = wp_call.json()
            query = response['query']
            pages = query['pages']
            page_id = list(pages.keys())[0]
            pages_info = pages[page_id]
            pages_revisions = pages_info['revisions']

            for d in pages_revisions[1:]:
                tup = (d['revid'], d['size'])
                rev_lengths.append(tup)
        if len(pages_revisions) > 0 and len(pages_revisions) < int(parameters['rvlimit']):
            # print('tuple list size: ' + str(len(rev_lengths)))
            for d in pages_revisions[1:]:
                tup = (d['revid'], d['size'])
                rev_lengths.append(tup)

    biggest = max(rev_lengths)[1]

    for tup in rev_lengths:
        if biggest in tup:
            bigtup = tup

    longestpage = bigtup[0]

    return longestpage


def get_big_page_size(Title):
    TITLE = Title
    BASE_URL = "http://en.wikipedia.org/w/api.php"

    rev_lengths = []

    while not rev_lengths:
        # print('in while loop')
        parameters = {'action': 'query',
                      'format': 'json',
                      'titles': TITLE,
                      'prop': 'revisions',
                      'rvprop': 'ids|size',
                      'rvlimit': '500'}

        wp_call = requests.get(BASE_URL, params=parameters)
        response = wp_call.json()

        query = response['query']
        pages = query['pages']
        page_id = list(pages.keys())[0]
        pages_info = pages[page_id]
        pages_revisions = pages_info['revisions']

        for d in pages_revisions:
            tup = (d['revid'], d['size'])
            rev_lengths.append(tup)
    else:
        while str(len(pages_revisions)) == parameters['rvlimit']:
            # print('tuple list size: ' + str(len(rev_lengths)))
            start_id = (rev_lengths[-1])[0]
            parameters = {'action': 'query',
                          'format': 'json',
                          'titles': TITLE,
                          'prop': 'revisions',
                          'rvprop': 'ids|size',
                          'rvlimit': '500',
                          'rvstartid': start_id}

            wp_call = requests.get(BASE_URL, params=parameters)
            response = wp_call.json()
            query = response['query']
            pages = query['pages']
            page_id = list(pages.keys())[0]
            pages_info = pages[page_id]
            pages_revisions = pages_info['revisions']

            for d in pages_revisions[1:]:
                tup = (d['revid'], d['size'])
                rev_lengths.append(tup)
        if len(pages_revisions) > 0 and len(pages_revisions) < int(parameters['rvlimit']):
            # print('tuple list size: ' + str(len(rev_lengths)))
            for d in pages_revisions[1:]:
                tup = (d['revid'], d['size'])
                rev_lengths.append(tup)

    biggest = max(rev_lengths)[1]

    for tup in rev_lengths:
        if biggest in tup:
            bigtup = tup

    longestpage = bigtup[0]

    # start selenium section
    snapshot_url = f'https://en.wikipedia.org/w/index.php?title={TITLE}'

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')

    page_id_param = f'&oldid={longestpage}'
    full_url = snapshot_url + page_id_param
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(full_url)
    #time.sleep(2)
    #driver.implicitly_wait(1)

    width = driver.execute_script("return document.body.scrollWidth")
    height = driver.execute_script("return document.body.scrollHeight")
    # print(f'page {longestpage} height: {height}')
    driver.quit()

    return width, height


def get_big_page_url(Title):
    TITLE = Title
    BASE_URL = "http://en.wikipedia.org/w/api.php"

    rev_lengths = []

    while not rev_lengths:
        # print('in while loop')
        parameters = {'action': 'query',
                      'format': 'json',
                      'titles': TITLE,
                      'prop': 'revisions',
                      'rvprop': 'ids|size',
                      'rvlimit': '500'}

        wp_call = requests.get(BASE_URL, params=parameters)
        response = wp_call.json()

        query = response['query']
        pages = query['pages']
        page_id = list(pages.keys())[0]
        pages_info = pages[page_id]
        pages_revisions = pages_info['revisions']

        for d in pages_revisions:
            tup = (d['revid'], d['size'])
            rev_lengths.append(tup)
    else:
        while str(len(pages_revisions)) == parameters['rvlimit']:
            # print('tuple list size: ' + str(len(rev_lengths)))
            start_id = (rev_lengths[-1])[0]
            parameters = {'action': 'query',
                          'format': 'json',
                          'titles': TITLE,
                          'prop': 'revisions',
                          'rvprop': 'ids|size',
                          'rvlimit': '500',
                          'rvstartid': start_id}

            wp_call = requests.get(BASE_URL, params=parameters)
            response = wp_call.json()
            query = response['query']
            pages = query['pages']
            page_id = list(pages.keys())[0]
            pages_info = pages[page_id]
            pages_revisions = pages_info['revisions']

            for d in pages_revisions[1:]:
                tup = (d['revid'], d['size'])
                rev_lengths.append(tup)
        if len(pages_revisions) > 0 and len(pages_revisions) < int(parameters['rvlimit']):
            # print('tuple list size: ' + str(len(rev_lengths)))
            for d in pages_revisions[1:]:
                tup = (d['revid'], d['size'])
                rev_lengths.append(tup)

    biggest = max(rev_lengths)[1]

    for tup in rev_lengths:
        if biggest in tup:
            bigtup = tup

    longestpage = bigtup[0]
    print(type(longestpage), longestpage)

    # start selenium section
    snapshot_url = f'https://en.wikipedia.org/w/index.php?title={TITLE}'

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')

    page_id_param = f'&oldid={longestpage}'
    full_url = snapshot_url + page_id_param
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(full_url)
    time.sleep(2)

    height = driver.execute_script("return document.body.scrollHeight")
    # print(f'page {longestpage} height: {height}')
    driver.quit()

    return full_url


def get_big_page_pic(Title):
    TITLE = Title
    BASE_URL = "http://en.wikipedia.org/w/api.php"

    rev_lengths = []

    while not rev_lengths:
        print('Initializing Browser')
        parameters = {'action': 'query',
                      'format': 'json',
                      'titles': TITLE,
                      'prop': 'revisions',
                      'rvprop': 'ids|size',
                      'rvlimit': '500'}

        wp_call = requests.get(BASE_URL, params=parameters)
        response = wp_call.json()

        query = response['query']
        pages = query['pages']
        page_id = list(pages.keys())[0]
        pages_info = pages[page_id]
        print('Getting a picture of the wrong page height...')
        pages_revisions = pages_info['revisions']

        for d in pages_revisions:
            tup = (d['revid'], d['size'])
            rev_lengths.append(tup)
    else:
        while str(len(pages_revisions)) == parameters['rvlimit']:
            # print('tuple list size: ' + str(len(rev_lengths)))
            start_id = (rev_lengths[-1])[0]
            parameters = {'action': 'query',
                          'format': 'json',
                          'titles': TITLE,
                          'prop': 'revisions',
                          'rvprop': 'ids|size',
                          'rvlimit': '500',
                          'rvstartid': start_id}

            wp_call = requests.get(BASE_URL, params=parameters)
            response = wp_call.json()
            query = response['query']
            pages = query['pages']
            page_id = list(pages.keys())[0]
            pages_info = pages[page_id]
            pages_revisions = pages_info['revisions']

            for d in pages_revisions[1:]:
                tup = (d['revid'], d['size'])
                rev_lengths.append(tup)
        if len(pages_revisions) > 0 and len(pages_revisions) < int(parameters['rvlimit']):
            # print('tuple list size: ' + str(len(rev_lengths)))
            for d in pages_revisions[1:]:
                tup = (d['revid'], d['size'])
                rev_lengths.append(tup)

    biggest = max(rev_lengths)[1]

    for tup in rev_lengths:
        if biggest in tup:
            bigtup = tup

    longestpage = bigtup[0]

    # start selenium section
    snapshot_url = f'https://en.wikipedia.org/w/index.php?title={TITLE}'

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')

    page_id_param = f'&oldid={longestpage}'
    full_url = snapshot_url + page_id_param
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(full_url)
    driver.implicitly_wait(2)

    height = driver.execute_script("return document.body.scrollHeight")
    width = driver.execute_script("return document.body.scrollWidth")
    imgpath = os.path.join(os.path.curdir, f'{TITLE}LongShot.png')

    driver.set_window_size(width, height)  # the trick
    time.sleep(2)
    driver.save_screenshot(imgpath)
    driver.quit()
    photo = io.imread(imgpath)
    photo_resized = resize(photo, (photo.shape[0], photo.shape[1]))
    #smallerphoto = photo[::2, ::2]
    io.imsave(imgpath, img_as_ubyte(photo_resized))


    # print(f'page {longestpage} height: {height}')
    driver.quit()

    return os.path.abspath(imgpath)
