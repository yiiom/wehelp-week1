#建立第一組數字
def func3(index):
    base = [25, 23, 20, 21] #第0組
    group=index//4  #算第幾組
    pos=index%4     #算位置
    answer=base[pos]-group*2
    print(answer)  

func3(1)
func3(5)
func3(10)
func3(30) 