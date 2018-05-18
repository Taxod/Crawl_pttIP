import requests
from bs4 import BeautifulSoup

def find_PageHtmlText(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup


def find_ip_id(Html_soup):
    article_title_href = Html_soup.find_all('div', 'title')
    for i in article_title_href:
        A_tag =  i.find('a')
        if A_tag != None:
            single_href = i.get('href')#/bbs/prozac/M.1526572117.A.C0E.html
            url_string = "https://www.ptt.cc"+single_href


            
            re = requests.get(url_string)
            tmp = BeautifulSoup(re.text,'html.parser')
            tmp_ip = tmp.find('span','f2')
            tmp_id = tmp.find('span','article-meta-value')
            if tmp_ip == None:
                break
            if tmp_ip.string == None:
                break
            if tmp_ip.string.find('(ptt.cc),') != -1 & tmp_ip.string.find(' 140.') != -1:
               print(tmp_id.string[:tmp_id.string.find(' ')],end=' ')
               print(tmp_ip.string[tmp_ip.string.find('140'):],end =' ')


url = 'https://www.ptt.cc/bbs/prozac/index650.html'
find_ip_id(find_PageHtmlText(url))

def Get_LastPage_Url(html_text):
    x = html_text.find_all('a','btn wide',limit=2)
    return "https://www.ptt.cc" + x[1].get('href')
print("end-----------")