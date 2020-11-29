import requests

def get_page_sections(Title):
    TITLE = Title
    BASE_URL = "http://en.wikipedia.org/w/api.php"

    section_names = []

    ## first API call
    parameters = {'action': 'parse',
                  'page': TITLE,
                  #'revid': "",
                  'redirects': 'True',
                  'prop': 'sections',
                  'format': 'json'
                  }

    wp_call = requests.get(BASE_URL, params=parameters)
    response = wp_call.json()

    sections_list = response['parse']['sections']
    for d in sections_list:
        section_names.append(d['line'])


    return section_names
