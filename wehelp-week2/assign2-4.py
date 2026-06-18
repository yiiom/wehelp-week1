def func4(sp, stat, n):
    best_index = -1
    best_diff = None

    for i in range(len(sp)):
        if stat[i] == "0":
            diff = abs(sp[i] - n)

            if best_diff == None:
                best_diff = diff
                best_index = i

            elif diff < best_diff:
                best_diff = diff
                best_index = i
    print(best_index)

func4([3,1,5,4,3,2], "101000", 2)
func4([1,0,5,1,3], "10100", 4)
func4([4,6,5,8], "1000", 4)