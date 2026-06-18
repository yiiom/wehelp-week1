function func3(index) {
    let base = [25, 23, 20, 21];

    let group = Math.floor(index / 4);
    let pos = index % 4;

    let answer = base[pos] - group * 2;

    console.log(answer);
}

func3(1);
func3(5);
func3(10);
func3(30);