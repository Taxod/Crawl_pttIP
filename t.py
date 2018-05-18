import requests
from bs4 import BeautifulSoup

def Get_LastPage_Url(html_soup):
    x = html_soup.find_all('a','btn wide',limit=2)
    return "https://www.ptt.cc" + x[1].get('href')

def find_PageHtmlText(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup

def find_ip_id(Html_soup):
    ID_href = {}
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
            if tmp_ip.string.find(' 140.') != -1:
                tmp_id = tmp.find('span', 'article-meta-value')
                if ID_href.get(tmp_id.string[:tmp_id.string.find(' ')]) == None:
                    ID_href[tmp_id.string[:tmp_id.string.find(' ')]] = tmp_ip.string[tmp_ip.string.find('140'):tmp_ip.string.find('\\')]
                else:
                    
                print(tmp_id.string[:tmp_id.string.find(' ')],end=' ')
                print(tmp_ip.string[tmp_ip.string.find('140'):],end ='')
    return ID_href

url = 'https://www.ptt.cc/bbs/prozac/index650.html'
ID_href = find_ip_id(find_PageHtmlText(url))

print("end-----------")
print(ID_href)