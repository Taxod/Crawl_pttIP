import requests
from bs4 import BeautifulSoup#需要額外安裝


#得到ptt上一頁的url
def Get_LastPage_Url(html_soup):
    x = html_soup.find_all('a','btn wide',limit=2)
    return "https://www.ptt.cc" + x[1].get('href')


#回傳soup，soup.text是html的文字檔(soup是名字可以亂取)
def find_PageHtmlText(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup

def find_ip_id(Html_soup,ID_href):
    #tag跟class'div' 'title'
    article_title_href = Html_soup.find_all('div', 'title')
    for i in article_title_href:
        A_tag =  i.find('a')
        if A_tag != None:
            single_href = A_tag.get('href')#/bbs/prozac/M.1526572117.A.C0E.html
            url_string = "https://www.ptt.cc"+single_href
            tmp = find_PageHtmlText(url_string)
            tmp_ip = tmp.find('span','f2')
            if tmp_ip == None:
                break
            if tmp_ip.string == None:
                break
            if tmp_ip.string.find(' 140.112') != -1:
                tmp_id = tmp.find('span', 'article-meta-value')
                ID = tmp_id.string[:tmp_id.string.find(' ')]
                IP = tmp_ip.string[tmp_ip.string.find('140'):tmp_ip.string.find('\\')]
                if ID_href.get(ID) == None:
                    ID_href[ID] = [[IP]+[url_string]]
                else:
                    ID_href[ID] = (ID_href.get(ID)) + [[IP]+[url_string]]
    return ID_href

ID_href = {}
# for i in range(500,515):
#     url = "https://www.ptt.cc/bbs/prozac/index"+ str(i) +".html"
#     ID_href = find_ip_id(find_PageHtmlText(url),ID_href)
#
count = 0
url = "https://www.ptt.cc/bbs/prozac/index.html"

# while (url != None) & (count < 1000):
while count < 1000:
    ID_href = find_ip_id(find_PageHtmlText(url),ID_href)
    if url != "https://www.ptt.cc/bbs/prozac/index1.html":
        url =  Get_LastPage_Url(find_PageHtmlText(url))
        count += 1
        print(count)#測試用--
    else:
        break
print(ID_href)#結果
print("-------")
# print(count)#測試