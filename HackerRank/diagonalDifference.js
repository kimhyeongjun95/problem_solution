function diagonalDifference(arr) {
    const N = arr.length;
    let [sum1, sum2] = [0, 0];
    for (let i = 0; i < N; i++) {
        sum1 += arr[i][i];
        sum2 += arr[i][N - i - 1];
    }
    return Math.abs(sum1 - sum2);
}

console.log(
    diagonalDifference([
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9],
    ])
);
