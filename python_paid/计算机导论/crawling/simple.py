from urllib import request
from bs4 import BeautifulSoup
import os
import ssl

def getHtml(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    req = request.Request(url, headers=headers)
    page = request.urlopen(req)
    html = page.read()
    return html

def getImg(html):
    soup = BeautifulSoup(html, 'html.parser')
    img_tags = soup.find_all('img', src=True)
    
    # 创建一个名为 "images" 的文件夹，如果它不存在的话
    if not os.path.exists('images'):
        os.mkdir('images')
    
    for img_tag in img_tags:
        img_url = img_tag['src']
        # 使用os.path.join构建保存图片的完整路径，保证跨平台兼容性
        img_filename = os.path.join('images', os.path.basename(img_url))
        request.urlretrieve(img_url, img_filename)

html = getHtml('https://movie.douban.com/top250')
getImg(html)
