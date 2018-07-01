# - * - coding:utf-8 - * -
import pandas as pd
import numpy as np
clean_data = []


def select_dataposition():
    data = pd.read_csv('0630_51job-data_analysis.csv',header = 0,encoding= 'gbk')
    df = pd.DataFrame(data)
    # df = df[True - df.name.duplicatde()]
    df = df[df.position.str.contains(r'.*?数据.*?|.*?爬虫.*?|.*?分析.*?')]
    # df = df[df.dropna(df.salary ='')]
    df.to_excel('data_51.xlsx')


def get_file_elements():
    file = pd.read_excel('data_51.xlsx')
    file = pd.DataFrame(file)
    rows = len(file)
    print(rows)
    for i in range(0, rows):
        try:
            raw_data = {}
            raw_data['公司'] = file['name'][i]
            raw_data['职位'] = file['position'][i]
            if '-' in file['location'][i]:
                plc_1 = str(file['location'][i]).find('-')
                raw_data['城市'] = file['location'][i][:plc_1]
            else:
                raw_data['城市'] = file['location'][i]
    #        print(file['salary'][i])
            if str(file['salary'][i]).strip() == '':
                raw_data['最低工资'] = ''
                raw_data['最高工资'] = ''
            elif '-' in str(file['salary'][i]):
                plc_2 = str(file['salary'][i]).find('-')
        #       print(plc_2)
                low_salary = file['salary'][i][:plc_2]
                high_salary = file['salary'][i][plc_2 + 1 :].rstrip('万/月|千/月|万/年')
        #       print(raw_data['high_salary'])
                if '万/月' in file['salary'][i]:
                    raw_data['最低工资'] = float(low_salary) * 10
                    raw_data['最高工资'] = float(high_salary) * 10
                elif '千/月' in file['salary'][i]:
                    raw_data['最低工资'] = float(low_salary)
                    raw_data['最高工资'] = float(high_salary)
                elif '万/年' in file['salary'][i]:
                    raw_data['最低工资'] = float(low_salary) * 10 / 12
                    raw_data['最高工资'] = float(high_salary) * 10 / 12
            else:
                raw_data['最低工资'] = file['salary'][i]
                raw_data['最高工资'] = file['salary'][i]
            raw_data['网址'] = file['pos_url'][i]
            raw_data['更新日期'] = file['update_date'][i]
            clean_data.append(raw_data)
            print('Processing with line ' + str(i) + '------')
            print('Still have ' + str(rows + 1 - i) + ' rows to complete------')
        except:
            print('ERROR line ' + str(i) + '------')
    return clean_data


def save_clean_data():
    lt = pd.DataFrame(clean_data)
    lt.to_excel('final_result.xlsx')
    print("Successfully Saved My File!")


# select_dataposition()
# get_file_elements()
# save_clean_data()
