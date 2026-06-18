#名字,x座標,y座標,黑線的哪一邊
people = [
    ["悟空", 0, 0, "L"],
    ["辛巴", -3, 3, "L"],
    ["丁滿", -1, 4, "R"],
    ["貝吉塔", -4, -1, "L"],
    ["弗利沙", 4, -1, "R"],
    ["特南克斯", 1, -2, "L"]
]
def func1(name):
    for person in people:
        if person[0] == name:        #找到目標角色
            target_x = person[1]     #取得目標座標
            target_y = person[2]
            target_side = person[3]

            farthest_distance = None
            farthest_name = []
            closest_distance = None
            closest_name = []
            
            for other in people:        #迴圈走其他角色
                if other[0] == name:    #如果目標角色是自己就跳過
                    continue
                distance = abs(target_x - other[1]) + abs(target_y - other[2]) #計算曼哈頓距離
                
                if target_side != other[3]: #如果目標角色和目標角色不在同一個區域就距離+2
                    distance += 2
                if farthest_distance == None:  #判斷最遠距離
                    farthest_distance = distance
                    farthest_name = [other[0]]

                elif distance > farthest_distance:
                    farthest_distance = distance
                    farthest_name = [other[0]]
                elif distance == farthest_distance:
                    farthest_name.append(other[0])

                if closest_distance == None:  #判斷最近距離
                    closest_distance = distance
                    closest_name = [other[0]]
                elif distance < closest_distance: #找到比較近的人
                    closest_distance = distance
                    closest_name = [other[0]]
                elif distance == closest_distance: #找到距離一樣近的人
                    closest_name.append(other[0])
            print("最遠:", farthest_name)
            print("最近:", closest_name)
func1("辛巴");
func1("悟空");
func1("弗利沙");
func1("特南克斯");
