let arr = [
    [1, 10],
    [1, 20],
    [2, 20],
    [2, 20],
    [3, 30],
    [3, 30],
    [7, 90],
    [7, 100],
    [8, 100],
    [10, 150],
    [10, 180],
    [20, 200],
    [3, 200],
]

// negative => A first
// positive => B first
// 이해가 안감 이건

// 음수(오름차순) => a - b
// 양수(내림차순) => b - a
// *** a와 b의 

arr.sort((a, b) => {

    // 내림차순
    if (a[1] > b[1]) return -1;
    if (a[1] < b[1]) return 1;

    // 오름차순
    if (a[0] < b[0]) return -1;
    if (a[0] > b[0]) return 1;


});

// 오름차순
// arr.sort((a, b) => a - b)
// 내림차순
// arr.sort((a, b) => b - a);

console.log(arr);