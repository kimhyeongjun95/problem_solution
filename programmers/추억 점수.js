// 추억 점수

function solution(name, yearning, photo) {
    const score = {};
    for (let i = 0; i < name.length; i++) {
        score[name[i]] = yearning[i];
    }

    const arr = [];
    for (const pho of photo) {
        let sum = 0;
        for (let i = 0; i < pho.length; i++) {
            if (score[pho[i]]) sum += score[pho[i]];
        }
        arr.push(sum);
    }
    return arr;
}

console.log(
    solution(
        ['may', 'kein', 'kain', 'radi'],
        [5, 10, 1, 3],
        [
            ['may', 'kein', 'kain', 'radi'],
            ['may', 'kein', 'brin', 'deny'],
            ['kon', 'kain', 'may', 'coni'],
        ]
    )
);
// [19, 15, 6]
console.log(
    solution(
        ['kali', 'mari', 'don'],
        [11, 1, 55],
        [
            ['kali', 'mari', 'don'],
            ['pony', 'tom', 'teddy'],
            ['con', 'mona', 'don'],
        ]
    )
);
// [67, 0, 55]
