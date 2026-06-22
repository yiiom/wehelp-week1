import urllib.request  #負責抓網路資料
import json           #負責處理json格式的資料

url1="https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
url2="https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"

response1=urllib.request.urlopen(url1)  #打開url1
response2=urllib.request.urlopen(url2)  #打開url2

data1=response1.read()  #讀取url1的資料
data2=response2.read()  #讀取url2的資料

data1=json.loads(data1)  #將json資料轉成 python dictionary
data2=json.loads(data2)  #將json資料轉成 python dictionary

file = open("districts.csv", "w", encoding="utf-8")
file.write("DistrictName,HotelCount,RoomCount\n")

districts={}
for i in range(len(data1["list"])):
    chinese_hotel = data1["list"][i]
    district = chinese_hotel["地址"][3:6]

    if district not in districts:
        districts[district] = {

            "HotelCount":1,
            "RoomCount":int(chinese_hotel["房間數"])
        }
    else:
        districts[district]["HotelCount"] += 1
        districts[district]["RoomCount"] += int(chinese_hotel["房間數"])
        
for district in districts:
    file.write(district+","+str(districts[district]["HotelCount"])+","+str(districts[district]["RoomCount"])+"\n")
    print(district,districts[district]["HotelCount"],districts[district]["RoomCount"])

file.close()