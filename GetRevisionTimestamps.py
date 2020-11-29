import requests
def get_revision_timestamps(Title):
    TITLE = Title
    BASE_URL = "http://en.wikipedia.org/w/api.php"

    revision_list = []


    ## first API call
    while not revision_list:
        revision_list = []
        parameters = { 'action': 'query',
                       'format': 'json',
                       'continue': '',
                       'titles': TITLE,
                       'prop': 'revisions',
                       'rvprop': 'ids|userid|timestamp',
                       'rvlimit': '500'}

        wp_call = requests.get(BASE_URL, params=parameters)
        response = wp_call.json()

        query = response['query']
        pages = query['pages']
        page_id_list = list(pages.keys())
        page_id = page_id_list[0]
        page_info = pages[str(page_id)]
        revisions = page_info['revisions']

        for entry in revisions:
            revision_list.append(entry['timestamp'])





## next series of passes, until you're done.
    else:
        while str(len(revisions)) == parameters['rvlimit']:
            start_id = revision_list[-1]
            parameters = { 'action': 'query',
                           'format': 'json',
                           'continue': '',
                           'titles': TITLE,
                           'prop': 'revisions',
                           'rvprop': 'ids|userid|timestamp',
                           'rvlimit': '500',
                           'rvstart': start_id} ## this needs to be set equal to the last value in your prior result list.

            wp_call = requests.get(BASE_URL, params=parameters)
            response = wp_call.json()

            query = response['query']
            pages = query['pages']
            page_id_list = list(pages.keys())
            page_id = page_id_list[0]
            page_info = pages[str(page_id)]
            revisions = page_info['revisions']

            for entry in revisions[1:]:
                revision_list.append(entry['timestamp'])


    return revision_list


