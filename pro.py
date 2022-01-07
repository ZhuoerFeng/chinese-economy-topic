import pandas
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd

def pro():
    nobs = 100
    X = np.random.random((nobs, 2))
    X = sm.add_constant(X)
    beta = [1, .1, .5]
    e = np.random.random(nobs)
    y = np.dot(X, beta) + e
    results = sm.OLS(y, X).fit()
    print(results.summary())

import csv
import xlrd

PROV_LIST = ['北京', '天津', '上海', '重庆市', '湖北省', '广东省']

def merge():
    data = list()
    # [prov, time, gdp, pergdp, ei, il, lnpergdp, ui, pilot, post, lnlctfp]
    energy = open('control variables/能源消费总量.csv')
    f = open('control variables/外商固定资产投资.csv')
    ind = open('control variables/第二产业占比.csv')
    pergdp = open('control variables/人均GDP.csv')
    gdp = open('control variables/地区GDP.csv')
    urban = open('control variables/城镇人口比.csv')
    # gdp
    reader = list(csv.reader(gdp))
    for line in reader[1:331]: 
        if int(line[2]) <= 2016:
            data.append([
                line[1], int(line[2]), float(line[3])
            ])
        
    # per gdp
    cnt = 0
    reader = list(csv.reader(pergdp))
    for idx, line in enumerate(reader[1:331]):
        if int(line[2]) <= 2016:
            data[cnt].append(float(line[3]))
            cnt += 1

    # ei
    cnt = 0
    reader = list(csv.reader(energy))
    for idx, line in enumerate(reader[1:331]):
        if int(line[1]) <= 2016:
            data[cnt].append(float(line[2]) / data[cnt][2])
            cnt += 1

    cnt = 0
    # fdi
    reader = list(csv.reader(f))
    for idx, line in enumerate(reader[1:301]):
        if int(line[2]) <= 2016:
            data[cnt].append( float(line[3]) / data[cnt][2])
            cnt += 1
        
    # il
    cnt = 0
    reader = list(csv.reader(ind))
    for idx, line in enumerate(reader[1:331]):
        if int(line[2]) <= 2016:
            data[cnt].append( float(line[3]) / 100)
            cnt += 1

    # lnpergdp
    for i in range(len(data)):
        data[i].append(np.log(data[i][3]))
    
    # ui
    cnt = 0
    reader = list(csv.reader(urban))
    for idx, line in enumerate(reader[1:331]):
        if int(line[2]) <= 2016:
            data[cnt].append( float(line[3]) / 100)
            cnt += 1
    
    # pilot, post
    for i in range(len(data)):
        prov = data[i][0]
        if prov in PROV_LIST:
            data[i].append(1)
        else:
            data[i].append(0)
        prov = data[i][-1]
        year = data[i][1]
        # if year < 2013 and year >= 2008:
        #     data[i].append(0)
        # elif year >= 2013 and year <= 2016:
        #     data[i].append(1)
        # else:
        #     print('illegal data')
            
        if year < 2009:
            data[i].append(0)
        else:
            data[i].append(1)
        data[i].append(data[i][-1] * prov)  
        
        if year < 2010:
            data[i].append(0)
        else:
            data[i].append(1)
        data[i].append(data[i][-1] * prov)  
            
        if year < 2011:
            data[i].append(0)
        else:
            data[i].append(1)
        data[i].append(data[i][-1] * prov)  
            
        if year < 2012:
            data[i].append(0)
        else:
            data[i].append(1)
        data[i].append(data[i][-1] * prov)  
            
        if year < 2013:
            data[i].append(0)
        else:
            data[i].append(1)
        data[i].append(data[i][-1] * prov)  
            
        if year < 2014:
            data[i].append(0)
        else:
            data[i].append(1)
        data[i].append(data[i][-1] * prov)  
            
        if year < 2015:
            data[i].append(0)
        else:
            data[i].append(1)
        data[i].append(data[i][-1] * prov)  
            
        if year < 2016:
            data[i].append(0)
        else:
            data[i].append(1)
        data[i].append(data[i][-1] * prov)  

    # lnlctfp

    worksheet = xlrd.open_workbook('lnlctfp.xlsx')
    sheet = worksheet.sheet_by_name('Sheet1')
    cnt = 0
    for row in range(2, 29):
        for col in range(2, 11):
            c = sheet.cell(row, col)
            data[cnt].append(np.log(c.value))
            cnt += 1
        if cnt == 20*9:
            cnt = 22*9
        if cnt == 27*9:
            cnt = 28*9
            
    # lnlci
    worksheet = xlrd.open_workbook('lnlci.xlsx')
    sheet = worksheet.sheet_by_name('Sheet1')
    cnt = 0
    for row in range(2, 29):
        for col in range(2, 11):
            c = sheet.cell(row, col)
            data[cnt].append(np.log(c.value))
            cnt += 1
        if cnt == 20*9:
            cnt = 22*9
        if cnt == 27*9:
            cnt = 28*9

    # eps
    worksheet = xlrd.open_workbook('eps.xlsx')
    sheet = worksheet.sheet_by_name('Sheet1')
    cnt = 0
    for row in range(1, 28):
        for col in range(2, 11):
            c = sheet.cell(row, col)
            data[cnt].append(c.value)
            cnt += 1
        if cnt == 20*9:
            cnt = 22*9
        if cnt == 27*9:
            cnt = 28*9
        
    # ind_num1
    worksheet = xlrd.open_workbook('industrial_num.xls')
    sheet = worksheet.sheet_by_name('Sheet1')
    cnt = 0
    print(len(data))
    for row in range(1, 28):
        for col in range(2, 11):
            c = sheet.cell(row, col)
            data[cnt].append(np.log(c.value))
            cnt += 1
        if cnt == 20*9:
            cnt = 22*9
        if cnt == 27*9:
            cnt = 28*9
    
    # ind_num2
    worksheet = xlrd.open_workbook('industrial_num.xls')
    sheet = worksheet.sheet_by_name('Sheet2')
    cnt = 0
    print(len(data))
    for row in range(1, 28):
        for col in range(2, 11):
            c = sheet.cell(row, col)
            data[cnt].append(np.log(c.value))
            cnt += 1
        if cnt == 20*9:
            cnt = 22*9
        if cnt == 27*9:
            cnt = 28*9
            
    # ind_num3
    worksheet = xlrd.open_workbook('industrial_num.xls')
    sheet = worksheet.sheet_by_name('Sheet3')
    cnt = 0
    print(len(data))
    for row in range(1, 28):
        for col in range(2, 11):
            c = sheet.cell(row, col)
            data[cnt].append(np.log(c.value))
            cnt += 1
        if cnt == 20*9:
            cnt = 22*9
        if cnt == 27*9:
            cnt = 28*9
            
    # ind_num4
    worksheet = xlrd.open_workbook('industrial_num.xls')
    sheet = worksheet.sheet_by_name('Sheet4')
    cnt = 0
    print(len(data))
    for row in range(1, 28):
        for col in range(2, 11):
            c = sheet.cell(row, col)
            data[cnt].append(np.log(c.value))
            cnt += 1
        if cnt == 20*9:
            cnt = 22*9
        if cnt == 27*9:
            cnt = 28*9
    
    # forest1
    worksheet = xlrd.open_workbook('forest.xls')
    sheet = worksheet.sheet_by_name('Sheet1')
    cnt = 0
    print(len(data))
    for row in range(1, 28):
        for col in range(2, 11):
            c = sheet.cell(row, col)
            data[cnt].append((c.value))
            cnt += 1
        if cnt == 20*9:
            cnt = 22*9
        if cnt == 27*9:
            cnt = 28*9

    # forest2
    worksheet = xlrd.open_workbook('forest.xls')
    sheet = worksheet.sheet_by_name('Sheet2')
    cnt = 0
    print(len(data))
    for row in range(1, 28):
        for col in range(2, 11):
            c = sheet.cell(row, col)
            data[cnt].append((c.value))
            cnt += 1
        if cnt == 20*9:
            cnt = 22*9
        if cnt == 27*9:
            cnt = 28*9
            
    # forest3
    worksheet = xlrd.open_workbook('forest.xls')
    sheet = worksheet.sheet_by_name('Sheet3')
    cnt = 0
    print(len(data))
    for row in range(1, 28):
        for col in range(2, 11):
            c = sheet.cell(row, col)
            data[cnt].append((c.value))
            cnt += 1
        if cnt == 20*9:
            cnt = 22*9
        if cnt == 27*9:
            cnt = 28*9
    
    outfile = open('did_data.csv', 'w')
    writer = csv.writer(outfile)
    writer.writerow(['prov', 'time', 'gdp', 'pergdp', 'ei', 'fdi', 'il', 'lnpergdp', 'ui', 
                     'pilot', 'post09', 'cross09', 'post10', 'cross10', 'post11', 'cross11', 'post12', 'cross12', 'post13', 'cross13', 
                     'post14', 'cross14', 'post15', 'cross15', 'post16', 'cross16',
                     'lnlctfp', 'lnlci', 'eps', 'ind_num1', 'ind_num2', 'ind_num3', 'ind_num4', 'forest1', 'forest2', 'forest3'])
    
    writer.writerows(data)
    
EAST = ['北京', '天津', '河北省', '辽宁省', '上海', '江苏省', '浙江省', '福建省', '山东省', '广东省', '海南']
MIDDLE = ['山西省', '吉林省', '黑龙江省', '安徽省', '江西省', '河南省', '湖北省', '湖南省']
WEST = ['内蒙古自治区', '广西壮族自治区', '重庆', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区']
    
def split():
    file = open('did_input.csv')
    reader = list(csv.reader(file))
    east = list()
    mid = list()
    west = list()
    for line in reader[1:]:
        if line[0] in EAST:
            east.append(line)
        elif line[0] in MIDDLE:
            mid.append(line)
        elif line[0] in WEST:
            west.append(line)
        else:
            print(line[0])
            exit(0)

    fout = open('east.csv', 'w')
    writer = csv.writer(fout)
    writer.writerow(reader[0])
    writer.writerows(east)
    
    fout = open('middle.csv', 'w')
    writer = csv.writer(fout)
    writer.writerow(reader[0])
    writer.writerows(mid)

    fout = open('west.csv', 'w')
    writer = csv.writer(fout)
    writer.writerow(reader[0])
    writer.writerows(west)   
    
def main():
    merge()
    split()
    df = pd.read_csv('did_input.csv')
    print(df.tail)
    # prov_dummy = pd.get_dummies(df['prov'], prefix="Prov_dum")
    # print(prov_dummy.head())
    # df = df.join(prov_dummy)
    # print(df)

    prov = df['prov']
    new_prov = list()
    rcd = dict()
    cnt = 0
    for item in prov:
        if item not in rcd:
            rcd[item] = cnt
            cnt += 1
        new_prov.append(rcd[item])
    new_prov = pandas.DataFrame({"id_prov": new_prov})
    df = df.join(new_prov)
    idx = list(range(243))
    id = pandas.DataFrame({"id": idx})
    df = df.join(id)
    print(df)
    
    est = smf.ols(formula='lnlctfp ~ forest1 + cross13 + ei + fdi + il + lnpergdp + ui + C(id_prov, Treatment) + C(time, Treatment)', data=df).fit()
    
    print(est.summary())
    print(est.params)
    
if __name__ == '__main__':
    main()