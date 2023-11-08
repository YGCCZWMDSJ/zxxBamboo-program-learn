from urllib import request
import re
import ssl

def getHtml(url):
    ssl._create_default_https_context=ssl._create_unverified_context
    page =request.urlopen(url)
    html=page.read()
    return html

html=getHtml('https://www.ddosi.org/')