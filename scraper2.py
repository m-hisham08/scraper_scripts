from bs4 import BeautifulSoup
import requests

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.6',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://search.brave.com/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Brave";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'cf_clearance=Jelrv3aPuppQDNc414JTfq2v_p1Oup70bRww.YAnivI-1739804258-1.2.1.1-PcxO82MkyvGdn.twd7JWysPeazQ3_G6jAIqX8MjNsonsH4NhNdxKWtDS4QaOZRt026Fy_yx5Ab9axkw_DHzOz7H.EX4ErB5UKcLfxkTZtKxyy.5IGW0NAZkkC0osg4nCcKhTguRIQTjTVJWHxVuvK6aVjuCDkG8QRqgf3l0DMUNX7jrBqIjHvmiFUQsU02WHjnZPRPfqje_T_WuW8DliBvEKcMQVMDQKfmxD_8f2JDHhDdssOm4_5HBymynEu8D5moSNR_rxdAX83kQZ8awhSLApwZ3Eyqr25yKxAxOFuIg; ASP.NET_SessionId=ts0qqt0trx1c5otnzue0ncaj; __cf_bm=AwY_RelMggK_d0DG6dcaB73QOunUPSWUrRAXPCHxsAk-1739804258-1.0.1.1-vJBwN1fHIYWk._2TKvdKyD36bboOsHqQ0fxyJpoZnmfM8y7CO3HcRt0iSc7_oMV0qQqtp.oQmK.tJlOcvvt5OQ',
}

session = requests.Session()
r = session.get('https://biz.sosmt.gov/search/business', headers=headers)
print(r.cookies)

soup = BeautifulSoup(r.text).prettify()
print(soup)