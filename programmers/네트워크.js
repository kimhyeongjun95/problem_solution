function solution(n, computers) {
  let answer = 0;
  const visited = Array(n).fill(false);

  const find = (index) => {
    visited[index] = true;
    for (let i = 0; i < n; i++) {
      if (computers[index][i] === 1 && !visited[i]) {
        find(i);
      }
    }
  };

  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      answer += 1;
      find(i);
    }
  }

  return answer;
}

console.log(
  solution(3, [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
  ])
); // 2
console.log(
  solution(3, [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1],
  ])
); // 1
