const dxy = [
  [0, 1],
  [1, 0],
  [-1, 0],
  [0, -1],
];

function solution(maps) {
  const N = maps.length;
  const M = maps[0].length;
  const visited = Array.from(Array(N), () => Array(M).fill(1000));

  const stack = [[0, 0]];
  visited[0][0] = 1;
  while (stack.length) {
    const popped = stack.shift();
    const [x, y] = popped;
    for (const nxy of dxy) {
      const [nx, ny] = [x + nxy[0], y + nxy[1]];
      if (nx === N - 1 && ny === M - 1) {
        return visited[x][y] + 1;
      }

      if (nx >= 0 && nx < N && ny >= 0 && ny < M && maps[nx][ny] === 1 && visited[nx][ny] === 1000) {
        visited[nx][ny] = visited[x][y] + 1;
        stack.push([nx, ny]);
      }
    }
  }

  return visited[N - 1][M - 1] === 1000 ? -1 : visited[N - 1][M - 1];
}

console.log(
  solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
  ])
); // 11
console.log(
  solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
  ])
); // -1
