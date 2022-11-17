// 프로그래머스 타겟 넘버

// n개의 음이 아닌 정수
// 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버
// 타겟 넘버를 만드는 방법의 수 return

function solution(numbers, target) {
    let answer = 0;
    const N = numbers.length;
    const find = (idx, now) => {
        if (idx === N) {
            if (now === target) answer += 1;
            return;
        }
        find(idx + 1, now + numbers[idx]);
        find(idx + 1, now - numbers[idx]);
    };
    find(0, 0);
    return answer;
}

console.log(solution([1, 1, 1, 1, 1], 3));
// 5
console.log(solution([4, 1, 2, 1], 4));
// 2
