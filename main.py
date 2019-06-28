import requests
import csv
import os
from pyquery import PyQuery as pq
from selenium import webdriver


url = 'https://manhua.dmzj.com/lanqiufeirenquancai/'
name = '灌篮高手'


def main():
    content = requests.get(url).text
    doc = pq(content)
    a_list = doc('.cartoon_online_border a').items()

    csv_file = './{0}/book.csv'.format(name)
    csv_dir = os.path.dirname(csv_file)

    if not os.path.isdir(csv_dir):
        os.makedirs(csv_dir)

    book_csv = open(csv_file, 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(book_csv)

    book_index = 1

    for item in a_list:
        link = 'https://manhua.dmzj.com' + item.attr('href')
        title = item.text()

        csv_writer.writerow((book_index, title, link))
        book_index += 1

    book_csv.close()
    download_item('https://manhua.dmzj.com/lanqiufeirenquancai/12515.shtml')


def download_item(url):
    option = webdriver.ChromeOptions()
    option.add_argument('log-level=3')

    browser = webdriver.Chrome(options=option)

    browser.get(url)

    arr_pages = browser.execute_script("return arr_pages;")
    # print(r)

    for item in arr_pages:
        print(item)

    # content = requests.get(url).text
    # doc = pq(content)
    #
    # img_src = doc('#center_box img').attr('src')
    # print(img_src)



if __name__ == '__main__':
    main()
    input()
