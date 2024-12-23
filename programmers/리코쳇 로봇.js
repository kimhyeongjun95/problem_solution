// 상하좌우,
// 장애물이나 가장자리까지 부딪힐때까지 미끄러져 움직임

// .  빈 공간
// R 로봇의 처음 위치
// D 장애물 위치
// G 목표 지점

// 최소 몇 번 이동하는지 return or -1
// 구석 가장 자리에 있는지, 장애물 옆에 없으면 -1임.

// 1. 처음 위치와 목표 지점 확인
// 2. 장애물 또는 벽을 만날 때 까지 이동
// 3. minCount return

function solution(board) {
  const dxy = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  const N = board.length;
  const M = board[0].length;

  let minCount = Infinity;
  let [rx, ry] = [null, null];
  let [gx, gy] = [null, null];

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (board[i][j] === "R") [rx, ry] = [i, j];
      if (board[i][j] === "G") [gx, gy] = [i, j];
    }
  }
  const queue = [[rx, ry, 1]];
  const visited = Array.from(Array(N), () => Array(M).fill(0));

  while (!!queue.length) {
    const [x, y, count] = queue.shift();
    visited[x][y] = 1;

    for (const [dx, dy] of dxy) {
      let [nx, ny] = [x, y];
      while (nx + dx >= 0 && nx + dx < N && ny + dy >= 0 && ny + dy < M) {
        if (board[nx + dx][ny + dy] === "D") break;
        nx += dx;
        ny += dy;
      }

      if (!visited[nx][ny]) {
        if (board[nx][ny] === "G") {
          minCount = Math.min(count, minCount);
        } else {
          visited[nx][ny] = 1;
          queue.push([nx, ny, count + 1]);
        }
      }
    }
  }
  return minCount === Infinity ? -1 : minCount;
}

console.log(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]));
// 7

console.log(solution([".D.R", "....", ".G..", "...D"]));
// -1
