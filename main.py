import requests
import csv
import os
import re
from pyquery import PyQuery as pq
from selenium import webdriver
import img2pdf


url = 'https://manhua.dmzj.com/lanqiufeirenquancai/'
name = '灌篮高手'

option = webdriver.ChromeOptions()
option.add_argument('log-level=3')
browser = webdriver.Chrome(options=option)


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

        download_item(link, title)

    book_csv.close()


def download_item(item_url, item_name):

    browser.get(item_url)

    arr_pages = browser.execute_script("return arr_pages;")
    # print(r)

    file_dir = './{0}/{1}'.format(name, item_name)

    if not os.path.exists(file_dir):
        os.mkdir(file_dir)

    img_arr = []
    for (index, item) in enumerate(arr_pages):
        img_url = 'https://images.dmzj.com/' + item
        img_save_file = file_dir + '/' + re.search(r'([^\/]*?)$', item).group(1)
        img_arr.append(img_save_file)

        with open(img_save_file, 'wb')as p:
            p.write(requests.get(img_url).content)

    pdf_file = './{0}/{1}.pdf'.format(name, item_name)
    img2pdf.convert(img_arr, pdf_file, item_name)


if __name__ == '__main__':
    main()
    print('all finish')
