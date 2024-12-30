// 세로 n 가로 m

// 시추관은 가장 아래 끝까지 뻗어나감
// 뽑을 수 있는 석유량: 지나가는 석유 덩어리들의 크기를 모두 합한 값

// 가장 많은 석유량 return

function solution(land) {
  const dxy = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];
  const N = land.length;
  const M = land[0].length;
  const result = Array(M).fill(0);
  const visited = Array.from(Array(N), () => Array(M).fill(0));

  for (let i = 0; i < M; i++) {
    for (let j = 0; j < N; j++) {
      let count = 0;
      let startY = i;
      let endY = 0;
      if (land[j][i] === 1 && !visited[j][i]) {
        const stack = [[j, i]];
        visited[j][i] = 1;
        while (stack.length) {
          const [cx, cy] = stack.pop();
          count += 1;
          endY = Math.max(endY, cy);
          for (const [dx, dy] of dxy) {
            const nx = dx + cx;
            const ny = dy + cy;
            if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx][ny] && land[nx][ny] === 1) {
              stack.push([nx, ny]);
              visited[nx][ny] = 1;
            }
          }
        }

        for (let k = startY; k < endY + 1; k++) {
          result[k] += count;
        }
      }
    }
  }
  return Math.max(...result);
}

console.log(
  solution([
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1],
  ])
);
// 9

console.log(
  solution([
    [1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
  ])
);
// 16
