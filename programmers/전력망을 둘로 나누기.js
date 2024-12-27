// 트리 형태
// 전선들 중 하나를 끊어
// 전력망 네트워크를 2개로 분할

// 개수가 최대한 비슷하도록 나눌 때, 개수의 차이 return
function solution(n, wires) {
  let count = Infinity;
  const trees = Array.from(Array(n + 1), () => []);
  for (const wire of wires) {
    const [v1, v2] = wire;
    trees[v1].push(v2);
    trees[v2].push(v1);
  }

  const check = (root, toExclude) => {
    const visited = Array(n + 1).fill(0);
    const stack = [root];
    let currentCount = 1;

    visited[root] = 1;

    while (stack.length) {
      const popped = stack.pop();
      trees[popped].forEach((v) => {
        if (!visited[v] && v !== toExclude) {
          visited[v] = 1;
          stack.push(v);
          currentCount += 1;
        }
      });
    }
    return currentCount;
  };

  for (const wire of wires) {
    const [v1, v2] = wire;
    const firstCount = check(v1, v2);
    const secondCount = check(v2, v1);
    count = Math.min(Math.abs(firstCount - secondCount), count);
  }

  return count;
}

console.log(
  solution(9, [
    [1, 3],
    [2, 3],
    [3, 4],
    [4, 5],
    [4, 6],
    [4, 7],
    [7, 8],
    [7, 9],
  ])
);
// 3

console.log(
  solution(4, [
    [1, 2],
    [2, 3],
    [3, 4],
  ])
);
// 0

console.log(
  solution(7, [
    [1, 2],
    [2, 7],
    [3, 7],
    [3, 4],
    [4, 5],
    [6, 7],
  ])
);
// 1
