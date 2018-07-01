# - * - coding:utf-8 - * -
from bs4 import BeautifulSoup
import requests
import pandas as pd
url = r'https://search.51job.com/list/000000,000000,0000,00,9,99,' \
      r'%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,{}.html?' \
      r'lang=c&stype=1' \
      r'&postchannel=0000&workyear=99&cotype=99°reefrom=99&jobterm=99&companysize=99&lonlat=0%2' \
      r'C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
final = []
def get_contents():
    for i in range(1, 2001):
        url_real = url.format(i)
        try:
            res = requests.get(url_real)
            res.encoding = 'gbk'
            soup = BeautifulSoup(res.text, 'html.parser')
            total_content = soup.select('.dw_table')[0]
            companys = total_content.select('.el')
#           y = total_content.select('.t1 ')
#           print(y)
            for company in companys:
                total = {}
                position_all = company.select('.t1 ')[0]
                position_a = position_all.select('a')
                if len(position_a)>0:
                    total['name'] = company.select('.t2')[0].text.strip()
                    total['position'] = position_a[0]['title']
                    total['location'] = company.select('.t3')[0].text.strip()
                    total['salary'] = company.select('.t4')[0].text.strip()
                    total['update_date'] = company.select('.t5')[0].text.strip()
                    total['pos_url'] = position_a[0]['href'].strip()
#                    total = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(name,position,location,salary,update_date,pos_url)
                    print("Dealing with page " + str(i) + '  Please waiting------')
                    print('Company\'s name is  ' + total['name'] )
                    final.append(total)
        except:
            print('Failed with page ' + str(i) + '  ------')
    return final


def save_my_file():
# with open('data_analysis.csv','a+') as file_obj:
    df = pd.DataFrame(final)
    df.to_csv('0630_51job-data_analysis.csv', mode = 'a',encoding = 'gbk')


get_contents()
save_my_file()
print(len(final))
