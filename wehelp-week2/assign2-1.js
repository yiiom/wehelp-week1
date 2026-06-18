function func1(name) {      //name是參數
    const people = [
        ["悟空", 0, 0, "L"],
        ["辛巴", -3, 3, "L"],
        ["丁滿", -1, 4, "R"],
        ["貝吉塔", -4, -1, "L"],
        ["弗利沙", 4, -1, "R"],
        ["特南克斯", 1, -2, "L"]
    ];

    let targetX;                 //存目標角色的x座標
    let targetY;                 //存目標角色的y座標
    let targetSide;              //存目標角色的區域

    for (let person of people) {
        if (person[0] === name) {       //找到目標角色
            targetX = person[1];        //取得目標角色的x座標
            targetY = person[2];        //取得目標角色的y座標
            targetSide = person[3];     //取得目標角色的區域
        }
    }

    let farthestDistance = null;      //存最遠距離
    let farthestNames = [];           //存最遠距離的名字

    let closestDistance = null;       //存最近距離
    let closestNames = [];            //存最近距離的名字

    for (let other of people) {
        if (other[0] === name) {        //如果目標角色是自己就跳過
            continue;
        }

        let distance =
            Math.abs(targetX - other[1]) + //計算曼哈頓距離
            Math.abs(targetY - other[2]);

        if (targetSide !== other[3]) {     //如果目標角色和目標角色不在同一個區域就距離+2
            distance += 2;
        }

        if (farthestDistance === null) {      //判斷最遠距離
            farthestDistance = distance;
            farthestNames = [other[0]];
        } else if (distance > farthestDistance) {    //找到比較遠的人
            farthestDistance = distance;
            farthestNames = [other[0]];
        } else if (distance === farthestDistance) {  //找到距離一樣遠的人
            farthestNames.push(other[0]);
        }

        if (closestDistance === null) {
            closestDistance = distance;
            closestNames = [other[0]];
        } else if (distance < closestDistance) {
            closestDistance = distance;
            closestNames = [other[0]];
        } else if (distance === closestDistance) {
            closestNames.push(other[0]);
        }
    }

    console.log("最遠:", farthestNames);
    console.log("最近:", closestNames);
}

func1("辛巴");
func1("悟空");
func1("弗利沙");
func1("特南克斯");