import re

str = 'g/%E7%81%8C%E7%AF%AE%E9%AB%98%E6%89%8B%E5%85%A8%E5%9B%BD%E5%A4%A7%E8%B5%9B%E7%AF%87%28%E5%85%A8%E5%BD%A9%29/%E7%81%8C%E7%AF%AE%E9%AB%98%E6%89%8B%E5%85%A8%E5%9B%BD%E5%A4%A7%E8%B5%9B%E7%AF%87_CH01/015.jpg'

searchObj = re.search(r'([^\/]*?)$', str)

if searchObj:
    print(searchObj.group(1))
else:
    print
    "Nothing found!!"


