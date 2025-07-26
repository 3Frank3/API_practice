import requests
import json
import sqlite3
import datetime

conn = sqlite3.connect('DrugStore.db')
c = conn.cursor()

# 新增且清空資料表

c.execute('''CREATE TABLE if not exists pharmacies
             (city text, counts text, createdAt datetime)''')
c.execute('''DELETE FROM pharmacies''')

conn.commit()

# 新增資料

# 利用 requests 對 API 來源發送一個請求
response = requests.get("https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json")

'''
# 檢查請求是否成功
if response.status_code != 200:
    print("Error: Unable to fetch data")
    exit() 
# 如果成功，則印出狀態碼
print(response.status_code)  
'''

# 將請求回應的內容存成一個字串格式
data = response.text

# 將長得像 json 格式的字串解析成字典或列表
data = json.loads(data)

# 印出解析後的資料
#print(data)

med_count = {}

# 填入欄位名稱
for d in data['features']:
    county = d['properties']['county']
    if county not in med_count:
         med_count[county] = 0
    med_count[county] += 1


#print(med_count) # {'台北市': 123, '新北市': 456 ...}


# 建立一個空的字典來存放口罩數量
mask_count = {}

# 填入欄位名稱
for d in data['features']:
    county = d['properties']['county']
    mask_count[county] = d['properties']['mask_adult']
# 如果字典中沒有這個縣市，就初始化為 0
    if county not in mask_count:
        mask_count[county] = 0
    # 將口罩數量加到對應的縣市
    mask_count[county] += d['properties']['mask_adult']


# 將結果從大到小排列
mask_count = dict(sorted(mask_count.items(), key=lambda item: item[1], reverse=True))

#print(mask_count)# {'台北市': 12345, '新北市': 45678 ...}

counts = {}

for d in data['features']:
    city = d['properties']['county']

    # 如果字典中沒有這個縣市，就初始化為 0
    if city not in counts:
        counts[city] = 0
    # 將口罩數量加到對應的縣市
    counts[city] += 1

# 將資料插入到資料庫中
t = datetime.datetime.now()
for city, counts in counts.items():
    print(f"INSERT INTO stocks VALUES ('{city}', {counts}, '{t}')")
    c.execute(f"INSERT INTO pharmacies VALUES ('{city}', {counts}, '{t}')")
conn.commit()

# 查詢資料
c.execute('''SELECT * FROM pharmacies''')
print(c.fetchall())

conn.close()