function func4(sp, stat, n) {
    let bestIndex = -1;
    let bestDiff = null;

    for (let i = 0; i < sp.length; i++) {
        if (stat[i] === "0") {
            let diff = Math.abs(sp[i] - n);

            if (bestDiff === null) {
                bestDiff = diff;
                bestIndex = i;
            } else if (diff < bestDiff) {
                bestDiff = diff;
                bestIndex = i;
            }
        }
    }

    console.log(bestIndex);
}

func4([3, 1, 5, 4, 3, 2], "101000", 2);
func4([1, 0, 5, 1, 3], "10100", 4);
func4([4, 6, 5, 8], "1000", 4);