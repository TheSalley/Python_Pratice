import json

import requests
import pymysql
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55',
        'Referer': 'https://accounts.douban.com/',
        'Cookie': 'll="118172"; bid=E6nebXG-C-4; _vwo_uuid_v2=D7F9CBE43179683AF4782FDE8E9E4D35D|b37d6528133393155eced3a9216ccbec; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1671524828; gr_user_id=49cfd8b2-8d84-4b57-a1fe-adb109943194; __yadk_uid=82PkIbbvavGxnoXiBKyE4UEWEWe7dmpJ; _ga=GA1.1.1458815998.1673317401; __gpi=UID=00000914954e8aca:T=1671614734:RT=1673317407:S=ALNI_MbiifEsBiM6GeYuG0ivPZWf8G4vxg; _ga_RXNMP372GL=GS1.1.1673321899.2.1.1673321918.41.0.0; __gads=ID=9ada40f0997032bd-22abd63676d800c9:T=1671614734:S=ALNI_MaS1lfcY_GjWLfdkAgHBzgrOjvt-Q; viewed="30175598_30310340_26274202"; dbcl2="184377407:BfXusWUkM3E"; ck=8h9M; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1674024748%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1644228663.1671522240.1673331034.1674024748.14; __utmb=30149280.0.10.1674024748; __utmc=30149280; __utmz=30149280.1674024748.14.6.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.2045697358.1671522240.1672390941.1674024748.7; __utmb=223695111.0.10.1674024748; __utmc=223695111; __utmz=223695111.1674024748.7.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=7fce9965da68a2e7.1671522240.10.1674024756.1672969889.'
    }
    # for i in range(0, 250, 25):

    db = pymysql.connect(host='127.0.0.1',
                         port=8888,
                         user='root',
                         password='123456',
                         database='movie',
                         charset='utf8mb4')
    cursor = db.cursor()
    num = 225
    url = f'https://movie.douban.com/top250?start={num}&filter='
    res = requests.get(url, headers=headers, timeout=3)
    soup = BeautifulSoup(res.text, 'html.parser')
    picList = soup.select('.grid_view li .pic img')
    titleList = soup.select('.grid_view li .hd .title:first-child')
    scoreList = soup.select('.grid_view li .bd .rating_num')
    commentList = soup.select('.grid_view li .bd')
    # print(picList[0].get('src'))
    # print(titleList)
    for index, item in enumerate(picList):
        # a = 'alter table rank250 auto_increment=1; '
        # sql = f"""insert into rank250(title, score, comment, pic)
        #             values ('{titleList[index].text}','{scoreList[index].text}', '', '')"""

        # sql1 = f"""
        #         update rank250 set comment = "{'' if item.select('.inq') == [] else item.select('.inq')[0].text}" where id = {index + 1 + 225}
        #         """
        print(item.get('src'))
        sql1 = f"""
                update rank250 set pic = "{item.get('src')}" where id = {index + 1 + num}
                """

        # cursor.execute(a)
        cursor.execute(sql1)
        db.commit()

    # try:
    #     with open('F:\内容\桌面\douban.json', 'a+', encoding='utf-8') as file_object:
    #         # content = file_object.write(item.text + '\n')
    #
    #         result.append({'title': item.text})
    #         print(result)
    #         # content = file_object.write(str(result) + '\n')
    # except FileNotFoundError:
    #     pass
    # else:
    #     print(f'写入成功')
