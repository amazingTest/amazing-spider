# - * - coding:utf-8 - * -
from bs4 import BeautifulSoup
import requests
import pandas as pd
url = r'http://www.dy10000.com/source/{}.html'
# for i in reversed(range(10000, 15000)):
#     url_real = url.format(i)
#     res = requests.get(url_real)
#     res.encoding = 'gbk'
#     soup = BeautifulSoup(res.text, 'html.parser')
#     if '404' not in soup.title:
#         print(i)
#         break

# res = requests.get(url.format(3756))
# # res.encoding = 'gbk'
# soup = BeautifulSoup(res.text, 'html.parser')
#
# movie_info = soup.select('.panel-primary')[0]
# movie_title = movie_info.select('h1')[0].text.strip()
# movie_href = movie_info.select('a')[-1]['href']
# print(movie_title)
# print(movie_href)

final = []


def get_contents():
    for i in range(3756, 13703):
        try:
            total = {}
            url_real = url.format(i)
            res = requests.get(url_real)
            # res.encoding = 'gbk'
            soup = BeautifulSoup(res.text, 'html.parser')
            movie_info = soup.select('.panel-primary')[0]
            movie_title = movie_info.select('h1')[0].text.strip()
            movie_href = movie_info.select('a')[-1]['href']
            total['movie_name'] = movie_title
            total['movie_href'] = movie_href
            print("Dealing with page " + str(i) + '  Please waiting------')
            print('Movie\'s name is  ' + total['movie_name'])
            print('Movie\'s href is  ' + total['movie_href'])
            final.append(total)
        except:
            print('Failed with page ' + str(i) + '  ------')
    return final


def save_my_file():
    df = pd.DataFrame(final,columns=['movie_name', 'movie_href'])
    df.to_csv('Movies.csv', mode = 'a')


get_contents()
save_my_file()
print(len(final))

