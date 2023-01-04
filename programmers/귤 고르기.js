// 프로그래머스 귤 고르기

// 수확한 귤 중 k개를 골라
// 상자 하나에 담아 판매하려고 한다.

// 귤을 크기별로 분류했을 때
// 서로 다른 종류의 수를 최소화하려고 한다.

function solution(k, tangerine) {
    const check = {};
    tangerine.forEach((t) => (check[t] = check[t] + 1 || 1));
    const arr = [];
    for (const val of Object.values(check)) {
        arr.push(val);
    }
    arr.sort((a, b) => b - a);
    let answer = 0;
    let count = 0;
    for (let i = 0; i < arr.length; i++) {
        answer += 1;
        count += arr[i];
        if (count >= k) return answer;
    }
    return answer;
}

console.log(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]));
// 3
console.log(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]));
// 2
console.log(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]));
// 1
