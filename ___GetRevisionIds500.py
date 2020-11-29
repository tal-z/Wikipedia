import requests

def get_revisions500(Title):
    BASE_URL = "http://en.wikipedia.org/w/api.php"
    TITLE = Title

    parameters = { 'action': 'query',
                   'format': 'json',
                   'continue': '',
                   'titles': TITLE,
                   'prop': 'revisions',
                   'rvprop': 'ids|userid',
                   'rvlimit': 'max'}

    wp_call = requests.get(BASE_URL, params=parameters)
    response = wp_call.json()
    query = response['query']
    pages = (query['pages'])
    page_id_list = list(pages.keys())
    page_id = page_id_list[0]
    page_info = pages[str(page_id)]
    revisions = page_info['revisions']


    revision_list = []
    for entry in revisions:
        revision_list.append(entry['revid'])

    return revision_list
