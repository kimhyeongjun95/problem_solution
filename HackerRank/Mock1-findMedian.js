function findMedian(arr) {
    const N = arr.length;
    arr.sort((a, b) => a - b);
    return arr[(N - 1) / 2];
}

console.log(findMedian([5, 3, 1, 2, 4]));
