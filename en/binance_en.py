import requests
from bs4 import BeautifulSoup

def get_topic_url():
    cookies = {
        'bnc-uuid': '149596f9-de60-4f38-8558-82577e2a45ac',
        'sajssdk_2015_cross_new_user': '1',
        'userPreferredCurrency': 'USD_USD',
        'BNC_FV_KEY': '3321a2505171a765b329893000801448f1bcf54d',
        'BNC_FV_KEY_EXPIRE': '1695654921752',
        'OptanonAlertBoxClosed': '2023-09-25T09:35:42.981Z',
        'source': 'referral',
        'campaign': 'www.binance.com',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218acb9f2e4c706-0f75a3fe9867f2-26031e51-2073600-18acb9f2e4d183a%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhY2I5ZjJlNGM3MDYtMGY3NWEzZmU5ODY3ZjItMjYwMzFlNTEtMjA3MzYwMC0xOGFjYjlmMmU0ZDE4M2EifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218acb9f2e4c706-0f75a3fe9867f2-26031e51-2073600-18acb9f2e4d183a%22%7D',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Sep+25+2023+15%3A21%3A34+GMT%2B0300+(GMT%2B03%3A00)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=1937c465-c6ef-4a4e-a324-29c972f706cc&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&geolocation=TR%3B34&AwaitingReconsent=false',
    }

    headers = {
        'authority': 'www.binance.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'bnc-uuid=149596f9-de60-4f38-8558-82577e2a45ac; sajssdk_2015_cross_new_user=1; userPreferredCurrency=USD_USD; BNC_FV_KEY=3321a2505171a765b329893000801448f1bcf54d; BNC_FV_KEY_EXPIRE=1695654921752; OptanonAlertBoxClosed=2023-09-25T09:35:42.981Z; source=referral; campaign=www.binance.com; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218acb9f2e4c706-0f75a3fe9867f2-26031e51-2073600-18acb9f2e4d183a%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhY2I5ZjJlNGM3MDYtMGY3NWEzZmU5ODY3ZjItMjYwMzFlNTEtMjA3MzYwMC0xOGFjYjlmMmU0ZDE4M2EifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218acb9f2e4c706-0f75a3fe9867f2-26031e51-2073600-18acb9f2e4d183a%22%7D; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Sep+25+2023+15%3A21%3A34+GMT%2B0300+(GMT%2B03%3A00)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=1937c465-c6ef-4a4e-a324-29c972f706cc&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&geolocation=TR%3B34&AwaitingReconsent=false',
        'if-none-match': 'W/"48840-ehDDiY6uYnb7iCY9idN+aD3Xl8I"',
        'referer': 'https://www.binance.com/tr/support/faq/binance-lite-modunda-kripto-al%C4%B1p-satmaya-ba%C5%9Flay%C4%B1n-227497e9e2bf4beb958ffc6bb94fbbe8',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    base_response = requests.get('https://www.binance.com/tr/support/faq', cookies=cookies, headers=headers)
    soup = BeautifulSoup(base_response.text,"html.parser")
    print(str(soup.prettify())[:1000])

    subjects=soup.find("div", {"class":["css-wue4m3"]}).find_all("div",attrs={"class":["css-vurnku"]})
    #print(konular)
    subjects_arr=[]
    for subject in subjects:
        subject_values=subject.find('a', {"class":["css-csw0qr"]})
        subject_href = subject_values["href"]
        subject_name=subject_values.find("div",{"class":["css-qvdhtp"]}).get_text()
        subject_json={subject_name:subject_href}
        subjects_arr.append(subject_json)
    return subjects_arr

#get all articles data with one page
def crawler_article():

    cookies = {
        'bnc-uuid': '149596f9-de60-4f38-8558-82577e2a45ac',
        'userPreferredCurrency': 'USD_USD',
        'BNC_FV_KEY': '3321a2505171a765b329893000801448f1bcf54d',
        'OptanonAlertBoxClosed': '2023-09-25T09:35:42.981Z',
        'source': 'referral',
        'campaign': 'www.binance.com',
        'BNC_FV_KEY_EXPIRE': '1695830304244',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218acb9f2e4c706-0f75a3fe9867f2-26031e51-2073600-18acb9f2e4d183a%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhY2I5ZjJlNGM3MDYtMGY3NWEzZmU5ODY3ZjItMjYwMzFlNTEtMjA3MzYwMC0xOGFjYjlmMmU0ZDE4M2EifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218acb9f2e4c706-0f75a3fe9867f2-26031e51-2073600-18acb9f2e4d183a%22%7D',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Sep+27+2023+15%3A00%3A56+GMT%2B0300+(GMT%2B03%3A00)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=1937c465-c6ef-4a4e-a324-29c972f706cc&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&geolocation=TR%3B34&AwaitingReconsent=false',
    }

    headers = {
        'authority': 'www.binance.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'bnc-uuid=149596f9-de60-4f38-8558-82577e2a45ac; userPreferredCurrency=USD_USD; BNC_FV_KEY=3321a2505171a765b329893000801448f1bcf54d; OptanonAlertBoxClosed=2023-09-25T09:35:42.981Z; source=referral; campaign=www.binance.com; BNC_FV_KEY_EXPIRE=1695830304244; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218acb9f2e4c706-0f75a3fe9867f2-26031e51-2073600-18acb9f2e4d183a%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhY2I5ZjJlNGM3MDYtMGY3NWEzZmU5ODY3ZjItMjYwMzFlNTEtMjA3MzYwMC0xOGFjYjlmMmU0ZDE4M2EifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218acb9f2e4c706-0f75a3fe9867f2-26031e51-2073600-18acb9f2e4d183a%22%7D; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Sep+27+2023+15%3A00%3A56+GMT%2B0300+(GMT%2B03%3A00)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=1937c465-c6ef-4a4e-a324-29c972f706cc&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&geolocation=TR%3B34&AwaitingReconsent=false',
        'if-none-match': 'W/"68d29-+dS/DhabbNf7KG4RMasSL8RgD20"',
        'referer': 'https://www.binance.com/en/support/faq/account-functions?c=1&navId=1',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    base_response = requests.get(
        'https://www.binance.com/en/support/faq/how-to-register-on-binance-app-360042718372',
        cookies=cookies,
        headers=headers,
    )

    soup = BeautifulSoup(base_response.text,"html.parser")
    soup_j=str(soup.prettify())

    f = open("page.txt", "a", encoding="utf8")
    f.write(soup_j)
    f.close()


def get_articleUrl():
    import json

    f = open("page_datas.json", "r", encoding="utf8")
    json_file=json_file=json.loads(f.read()) 

    catalogs=json_file["appState"]["loader"]["dataByRouteId"]["2a3f"]["catalogs"]
    article_arr=[]
    for catalog in catalogs:
        
        catalogName=catalog["catalogName"]
        parentCatalogName=""

        if(catalog["articles"] is not None):

            #print(catalogName+":"+str(len(catalog["articles"]))+" parent:"+" ")
            articles=catalog["articles"]
            for article in articles:
                title=article["title"]
                url=(title.lower().strip()).replace(" ","-").replace("+","-").replace("?","")+"-"+article["code"]
                article_json={"title":title,"parentCatalogName":parentCatalogName,"catalogName":catalogName, "url":url}
                
                if(article_json not in article_arr):
                    article_arr.append(article_json)
                
        else:
            catalogs2=catalog["catalogs"]


            for catalog2 in catalogs2:
                parentCatalogName=catalogName
                catalogName=catalog2["catalogName"]


                if(catalog2["articles"] is not None):
                    articles=catalog2["articles"]
                    #print(catalogName+":"+str(len(articles))+" parent:"+parentCatalogName)
                    for article in articles:
                        title=article["title"]
                        url=(title.lower().strip()).replace(" ","-").replace("?","").replace("+","-")+"-"+article["code"]
                        article_json={"title":title,"parentCatalogName":parentCatalogName,"catalogName":catalogName, "url":url}
                        
                        if(article_json not in article_arr):
                            article_arr.append(article_json)
                else:
                    catalogs3=catalog2["catalogs"]
                    for catalog3 in catalogs3:
                        
                        if(catalog3["articles"] is not None):
                            articles=catalog3["articles"]
                            #print(catalogName+":"+str(len(articles))+" parent:"+parentCatalogName)
                            for article in articles:
                                title=article["title"]
                                url=(title.lower().strip()).replace(" ","-").replace("?","").replace("+","-")+"-"+article["code"]
                                article_json={"title":title,"parentCatalogName":parentCatalogName,"catalogName":catalogName, "url":url}
                                
                                if(article_json not in article_arr):
                                    article_arr.append(article_json)
                                
                        else:
                            catalogs4=catalogs3["catalogs"]

                            for catalog4 in catalogs4:
                                parentCatalogName=catalogName
                                catalogName=catalog4["catalogName"]
                                
                                if(catalog4["articles"] is not None):
                                    articles=catalog4["articles"]
                                    #print(catalogName+":"+str(len(articles))+" parent:"+parentCatalogName)
                                    for article in articles:
                                        title=article["title"]
                                        title2=(title.lower().strip()).replace(" ","-").replace("?","").replace("+","-")
                                        title3=title2.replace("---","-")
                                        url=title3.replace("--","-")+"-"+article["code"]
                                        article_json={"title":title,"parentCatalogName":parentCatalogName,"catalogName":catalogName, "url":url}
                                        if(article_json not in article_arr):
                                            article_arr.append(article_json)
                
                
                
    f2 = open("articles_data.json", "a", encoding="utf8")
    f2.write(str(article_arr))
    f2.close()                
    return article_arr
          
    #print(catalogs)"""


#print(get_articleUrl())

def crawle_article(url):

    try:

        import requests

        cookies = {
            'bnc-uuid': '149596f9-de60-4f38-8558-82577e2a45ac',
            'userPreferredCurrency': 'USD_USD',
            'BNC_FV_KEY': '3321a2505171a765b329893000801448f1bcf54d',
            'OptanonAlertBoxClosed': '2023-09-25T09:35:42.981Z',
            'source': 'referral',
            'campaign': 'www.binance.com',
            'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218acb9f2e4c706-0f75a3fe9867f2-26031e51-2073600-18acb9f2e4d183a%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhY2I5ZjJlNGM3MDYtMGY3NWEzZmU5ODY3ZjItMjYwMzFlNTEtMjA3MzYwMC0xOGFjYjlmMmU0ZDE4M2EifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218acb9f2e4c706-0f75a3fe9867f2-26031e51-2073600-18acb9f2e4d183a%22%7D',
            'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Sep+28+2023+12%3A43%3A03+GMT%2B0300+(GMT%2B03%3A00)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=1937c465-c6ef-4a4e-a324-29c972f706cc&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&geolocation=TR%3B34&AwaitingReconsent=false',
            'BNC_FV_KEY_EXPIRE': '1695915783694',
        }

        headers = {
            'authority': 'www.binance.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # 'cookie': 'bnc-uuid=149596f9-de60-4f38-8558-82577e2a45ac; userPreferredCurrency=USD_USD; BNC_FV_KEY=3321a2505171a765b329893000801448f1bcf54d; OptanonAlertBoxClosed=2023-09-25T09:35:42.981Z; source=referral; campaign=www.binance.com; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218acb9f2e4c706-0f75a3fe9867f2-26031e51-2073600-18acb9f2e4d183a%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhY2I5ZjJlNGM3MDYtMGY3NWEzZmU5ODY3ZjItMjYwMzFlNTEtMjA3MzYwMC0xOGFjYjlmMmU0ZDE4M2EifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218acb9f2e4c706-0f75a3fe9867f2-26031e51-2073600-18acb9f2e4d183a%22%7D; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Sep+28+2023+12%3A43%3A03+GMT%2B0300+(GMT%2B03%3A00)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=1937c465-c6ef-4a4e-a324-29c972f706cc&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&geolocation=TR%3B34&AwaitingReconsent=false; BNC_FV_KEY_EXPIRE=1695915783694',
            'if-none-match': 'W/"69b9a-BvMmhpFcHyP71j0fFmyKlFhXVW8"',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        }

        response = requests.get(
            url,
            cookies=cookies,
            headers=headers,
        )

        soup = BeautifulSoup(response.text,"html.parser")
        question=soup.find("h1", {"class":["css-1cf3zsg"]}).get_text()

        answer_div=soup.find("article", {"class":["css-26lh8k"]})
        ans_tittle=answer_div.find("h2", {"class":["css-whcap1"]}).get_text()
        answers=answer_div.find_all("div", {"class":["css-a15ggx"]})

        answer_text=""
        for answer in answers:
            answer_text+=answer.get_text()+" \n "

        #print(answer_text)
        article_json={"question":question,"answer_tittle":ans_tittle,"answer":answer_text}
        return article_json
    except Exception as e:
        return {}
    

url="https://www.binance.com/en/support/faq/how-to-register-on-binance-app-360042718372"

#crawle_article(url)

#Binance Faq Crawler
def crawler():
    import json,time

    f = open("articles_data.json", "r", encoding="utf8")
    json_file=json_file=json.loads(f.read())

    crawle_arr=[]
    limit=len(json_file)
    for i in range(0,limit):
        print(i)
        url="https://www.binance.com/en/support/faq/"+json_file[i]["url"]
        response= crawle_article(url)
        if(response!={}):
            y={"title":json_file[i]["title"],"parentCatalogName":json_file[i]["parentCatalogName"],"catalogName":json_file[i]["catalogName"],"url":json_file[i]["url"],"answer_tittle":response["answer_tittle"].replace('"',"").replace("'",""),"answer":response["answer"].replace('"',"").replace("'","")}
        else:
            y={"title":json_file[i]["title"],"parentCatalogName":json_file[i]["parentCatalogName"],"catalogName":json_file[i]["catalogName"],"url":json_file[i]["url"],"answer_tittle":"","answer":""}

        if y not in crawle_arr:
            crawle_arr.append(y)
        
        time.sleep(3)

    f2 = open("binance_faq_en.json", "a", encoding="utf8")
    f2.write(str(crawle_arr))
    f2.close()   

#crawler()