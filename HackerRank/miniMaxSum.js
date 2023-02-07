function miniMaxSum(arr) {
    // Write your code here
    arr.sort((a, b) => a - b);
    let minNum = 0;
    let maxNum = 0;
    let sum = 0;
    arr.forEach((v, idx) => {
        if (idx === 0) minNum += v;
        else if (idx === 4) maxNum += v;
        else {
            minNum += v;
            maxNum += v;
        }
        sum += v;
    });
    console.log(`${minNum} ${maxNum}`);
}

console.log(miniMaxSum([1, 3, 5, 7, 9]));
console.log(miniMaxSum([7, 69, 2, 221, 8974]));
// 299 9271
