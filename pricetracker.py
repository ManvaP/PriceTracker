from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        with closing(get(url, stream=True, headers=headers)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)


raw_html = simple_get('https://www.amazon.com/s?k=laptop&ref=nb_sb_noss_2')

print(raw_html)

html = BeautifulSoup(raw_html, 'html.parser')

links = html.select('a.a-link-normal.a-text-normal')

for tag in links:
    print(tag.attrs['href'])

