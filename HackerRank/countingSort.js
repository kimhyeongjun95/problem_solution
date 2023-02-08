function countingSort(arr) {
    const check = Array(100).fill(0);
    arr.forEach((v) => (check[v] += 1));
    return check;
}

console.log(countingSort([1, 1, 3, 2, 1]));
