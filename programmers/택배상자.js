// 프로그래머스 택배상자
// 1번 ~ n번
// 번호가 증가하는 순서대로 컨테이너 벨트

// 컨테이너 벨트에 놓인 순서대로 택배상자를 내려
// 바로 트럭에 싣게 되면 순서가 맞지않게됨

// 벨트의 맨 앞에 있는 상자가 순사가 아니라면 다른 곳에 보관
// 보조 컨테이너 벨트는 앞 뒤로 이동가능,
// 맨 앞의 상자만 뺼 수 있음(가장 마지막에 넣은 상자)

// 보조 컨테이너를 이용해도 기사님이 원하는 순서대로 싣지 못한다면
// 더이상 싣기 X

function solution(order) {
    const N = order.length;

    let count = 0;
    let idx = 0;
    const stack = [];

    for (let i = 1; i < N + 1; i++) {
        if (stack && stack[stack.length - 1] === order[idx]) {
            stack.pop();
            idx += 1;
            count += 1;
        }
        if (i === order[idx]) {
            idx += 1;
            count += 1;
        } else {
            stack.push(i);
        }
    }

    while (stack.length) {
        if (stack[stack.length - 1] === order[idx]) {
            stack.pop();
            idx += 1;
            count += 1;
        } else return count;
    }

    return count;
}

console.log(solution([4, 3, 1, 2, 5]));
// 2
console.log(solution([5, 4, 3, 2, 1]));
// 5
