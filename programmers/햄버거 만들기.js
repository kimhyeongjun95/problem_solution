// 빵 - 야채 - 고기 - 빵
// 정해진 순서
// 1, 2, 3 : 빵, 야채, 고기

function solution(ingredient) {
  const stack = [];
  let count = 0;
  for (const ing of ingredient) {
    stack.push(ing);
    let lastIdx = stack.length - 1;
    while (
      stack.length &&
      stack.length >= 4 &&
      stack[lastIdx] === 1 &&
      stack[lastIdx - 1] === 3 &&
      stack[lastIdx - 2] === 2 &&
      stack[lastIdx - 3] === 1
    ) {
      stack.pop();
      stack.pop();
      stack.pop();
      stack.pop();
      count += 1;
      lastIdx = stack.length - 1;
    }
  }

  return count;
}

console.log(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]));
// 2

console.log(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]));
// 0
