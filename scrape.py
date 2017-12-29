import requests
from bs4 import BeautifulSoup

def get_image_src(word):
    url = "https://www.google.com.br/search?q=%s&tbm=isch" % (word)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    html = list(soup.children)[1]
    body = list(html.children)[1]
    table = list(body.children)[4]
    tbody = list(table.children)[3]
    tr = list(tbody.children)[1]
    td = list(tr.children)[1]
    center_col = list(td.children)[0]
    res = list(center_col.children)[1]
    ires = list(res.children)[1]
    inner_ires = list(ires.children)[0]
    table = list(inner_ires.children)[0]
    inner_tr = list(table.children)[0]
    first_td = list(inner_tr)[0]
    a_img = list(first_td)[0]
    img_tag = list(a_img)[0]
    img_src = img_tag['src']
    return str(img_src)
