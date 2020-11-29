import requests

def get_page_link_titles(Title):
    TITLE = Title
    BASE_URL = "http://en.wikipedia.org/w/api.php"

    link_title_list = []

    ## first API call
    while not link_title_list:
        revision_list = []
        parameters = {'action': 'query',
                      'format': 'json',
                      'continue': '',
                      'titles': TITLE,
                      'prop': 'links',
                      'pllimit': '500'}

        wp_call = requests.get(BASE_URL, params=parameters)
        response = wp_call.json()

        query = response['query']
        pages = query['pages']
        page_id_list = list(pages.keys())
        page_id = page_id_list[0]
        page_info = pages[str(page_id)]
        links = page_info['links']

        for entry in links:
            link_title_list.append(entry['title'])


    ## next series of passes, until you're done.
    else:
        while str(len(links)) == parameters['pllimit']:
            continue_val = response['continue']['plcontinue']

            parameters = {'action': 'query',
                          'format': 'json',
                          'continue': '',
                          'titles': TITLE,
                          'prop': 'links',
                          'pllimit': '500',
                          'plcontinue': continue_val}

            wp_call = requests.get(BASE_URL, params=parameters)
            response = wp_call.json()

            query = response['query']
            pages = query['pages']
            page_id_list = list(pages.keys())
            page_id = page_id_list[0]
            page_info = pages[str(page_id)]
            links = page_info['links']

            for entry in links[1:]:
                link_title_list.append(entry['title'])

    return link_title_list
