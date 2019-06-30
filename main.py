import requests
import csv
import os
import re
import pdfkit
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
    download_item('https://manhua.dmzj.com/lanqiufeirenquancai/12515.shtml', '第1话')


def download_item(item_url, item_name):
    option = webdriver.ChromeOptions()
    option.add_argument('log-level=3')

    browser = webdriver.Chrome(options=option)

    browser.get(item_url)

    arr_pages = browser.execute_script("return arr_pages;")
    # print(r)

    file_dir = './{0}/{1}'.format(name, item_name)

    if not os.path.exists(file_dir):
        os.mkdir(file_dir)

    for (index, item) in enumerate(arr_pages):
        img_url = 'https://images.dmzj.com/' + item
        img_save_file = file_dir + '/' + re.search(r'([^\/]*?)$', item).group(1)

        with open(img_save_file, 'wb')as p:
            p.write(requests.get(img_url).content)





if __name__ == '__main__':
    pdfkit.from_file('./灌篮高手/第1话/001.jpg', './灌篮高手/第1话/test.pdf')

    # main()
    # input()
