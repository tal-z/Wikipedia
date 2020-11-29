import requests


def wiki_extract_summary(Title):


    request = requests.get(f'https://en.wikipedia.org/api/rest_v1/page/summary/{Title}?redirect=true').json()
    summary = request['extract']

    return summary

