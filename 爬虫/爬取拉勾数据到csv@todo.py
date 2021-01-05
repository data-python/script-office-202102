# https://blog.csdn.net/qq_25202521/article/details/107964515
# 1.导入工具库
import requests, json, csv, time

# 2.获取数据
session = requests.session()
# 模拟浏览器向网站发起请求
headers = {
    'referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?&px=default&city=%E5%85%A8%E5%9B%B',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
session.get('https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/p-city_0?px=default', headers=headers)
# 模拟拉勾网请求内部数据
url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
kd = input("请输入你想查找的岗位：")
for i in range(1, 30):
    print(f'开始爬取第{i}页')
    data = {
        'first': 'false',
        'pn': str(i),
        'kd': kd,
        'sid': '3a604e19a96a40669b9b84b799726000'
    }
    reponse = session.post(url=url, headers=headers, data=data, cookies=session.cookies)
    text = json.loads(reponse.text)
    # @todo 提示操作太频繁
    print(text)
    data = text.get('content').get('positionResult').get('result')

    # 3.解析数据
    for i in data:
        info = []
        info.append(i['positionName'])
        info.append(i['companyShortName'])
        info.append(i['industryField'])
        info.append(i['city'])
        info.append(i['salary'])
        info.append(i['education'])
        info.append(i['jobNature'])
        print(info)

        # 4.保存数据
        with open('拉勾复现.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(info)

        # 睡眠1秒，防止封ip
        time.sleep(1)
