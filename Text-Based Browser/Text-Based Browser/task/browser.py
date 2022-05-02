import os
import re
import sys
import requests
from colorama import Fore, Style
from bs4 import BeautifulSoup, NavigableString
from urllib.error import URLError


def show_content(p_url):
    secure = "https://"
    if not re.match(secure, p_url):
        p_url = secure + p_url

    req = p_url

    try:
        req = requests.get(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    else:
        return req.text


def save(directory, file, content):
    wd = directory + '/' + file
    with open(wd, 'w+', encoding="utf-8") as f:
        f.write(content)


def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))


def start():
    history = []
    # 1. Accept a command-line argument which is a directory for saved tabs.
    dir_name = sys.argv[1]
    #tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li', 'div']
    tags = ['p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    while True:
        input_url = input()

        search = '.'
        idx = input_url.find(search)
        file_name = input_url[
                    :idx]  # To get the name of the file, remove the last dot from the page name and everything that comes after it
        if search in input_url or 'back' == input_url:
            if input_url != "back":
                website = input_url.strip()
                if not website.startswith('https://'):
                    website = 'https://' + website
                try:
                    headers = {'User-Agent': 'Mozilla/5.0'}
                    response = requests.get(website, headers=headers)
                except requests.exceptions.ConnectionError:
                    print('Incorrect URL')
                else:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    text_items = [item for item in soup.stripped_strings]
                    content_r = '\n'.join(text_items)
                    # print(content_r)
                    for tag in soup.find_all(tags):
                        if tag:
                            if tag.string:
                                if tag.string != "":
                                    if tag.name == 'a':
                                        print(Fore.BLUE + tag.string)
                                    else:
                                        print(Fore.WHITE + tag.string)
                                        #print(Style.RESET_ALL, tag.string)

                    # save it to a file in the aforementioned directory.
                    save(dir_name, file_name, content_r)
            elif input_url == "back":
                # 3-6 1. The program should show the previous web page saved to a file
                if len(history) >= 2:
                    content_r = show_content(history[-2])
                    history.pop()
                    print(content_r)
                    # 3-6 2. If there are no more pages in the browser history, don?t output anything.
            elif input_url == "exit":
                exit()
            else:
                print('Error - Incorrect URL')
            if input_url != 'back':
                history.append(input_url)
        else:
            # 2. Check if the user has entered a valid URL. It must contain at least one dot
            if input_url == "exit":
                exit()
            print('Error: Incorrect URL')


if __name__ == '__main__':
    start()
