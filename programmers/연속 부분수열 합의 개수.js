// 프로그래머스 연속 부분 수열 합의 개수

// 원형 수열은 처음과 끝이 연결되어 끊기는 부분이 X
// 연속하는 부분 수열도 일반적인 수열보다 많아집니다.

// 원형 수열의 연속 부분 수열 합으로
// 만들 수 있는 수의 개수 return

function solution(elements) {
    const check = new Set();
    for (let i = 1; i < elements.length + 1; i++) {
        for (let j = 0; j < elements.length; j++) {
            if (i + j > elements.length) {
                const temp = elements.slice(j);
                const temp2 = elements.slice(0, i + j - elements.length);
                const r1 = temp.reduce((a, b) => a + b);
                const r2 = temp2.reduce((a, b) => a + b);
                const res = r1 + r2;
                check.add(res);
            } else check.add(elements.slice(j, j + i).reduce((a, b) => a + b));
        }
    }
    return check.size;
}

console.log(solution([7, 9, 1, 1, 4]));
// 18
