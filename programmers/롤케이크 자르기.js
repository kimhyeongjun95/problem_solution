// 프로그래머스 롤케이크 자르기

// 롤케이크를 두 조각으로 잘라 동생과 한 조각씩
// 각 조각에 동일한 가짓수의 토핑이 올라가면 공평하게 나누어진 것으로 생각

// 공평하게 자르는 방법의 수 return

function solution(topping) {
    const rightCheck = {};
    for (let i = 0; i < topping.length; i++) {
        rightCheck[topping[i]] = rightCheck[topping[i]]
            ? rightCheck[topping[i]] + 1
            : 1;
    }

    let left = 0;
    let right = Object.keys(rightCheck).length;
    let count = 0;
    const leftCheck = {};
    for (let i = 0; i < topping.length; i++) {
        if (!leftCheck[topping[i]]) {
            leftCheck[topping[i]] = 1;
            left += 1;
        }
        if (rightCheck[topping[i]]) rightCheck[topping[i]] -= 1;
        if (!rightCheck[topping[i]]) right -= 1;
        if (left === right) count += 1;
    }
    return count;
}

console.log(solution([1, 2, 1, 3, 1, 4, 1, 2]));
// 2
console.log(solution([1, 2, 3, 1, 4]));
// 0
