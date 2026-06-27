import urllib.request  #負責抓網路資料
import json           #負責處理json格式的資料
import csv            #負責處理csv格式的資料

url1="https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
url2="https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"

response1=urllib.request.urlopen(url1)  #打開url1
response2=urllib.request.urlopen(url2)  #打開url2

data1=response1.read()  #讀取url1的資料
data2=response2.read()  #讀取url2的資料

data1=json.loads(data1)  #將json資料轉成 python dictionary
data2=json.loads(data2)  #將json資料轉成 python dictionary

file=open("hotels.csv","w",encoding="utf-8",newline="")
writer=csv.writer(file)
writer.writerow(["ChineseName","EnglishName","ChineseAddress","EnglishAddress","Phone","RoomCount"])

for i in range(len(data1["list"])):   #會重複執行 len(data1["list"]) 次
    chinese_hotel = data1["list"][i]  #取得第 i 個中文hotel的資料
    english_hotel = data2["list"][i]  #取得第 i 個英文hotel的資料
    
    writer.writerow([
        chinese_hotel["旅宿名稱"],
        english_hotel["hotel name"],
        chinese_hotel["地址"],
        english_hotel["address"],
        chinese_hotel["電話或手機號碼"],
        chinese_hotel["房間數"]
    ])
    print(
        chinese_hotel["旅宿名稱"],          #印出中文hotel名稱
        english_hotel["hotel name"],        #印出英文hotel名稱
        chinese_hotel["地址"],              #印出中文hotel地址
        english_hotel["address"],          #印出英文hotel地址
        chinese_hotel["電話或手機號碼"],     #印出中文hotel電話
        chinese_hotel["房間數"]             #印出中文hotel房間數
        
    )
file.close()   
