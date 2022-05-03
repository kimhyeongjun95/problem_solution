// 프로그래머스 방문 길이

// 4가지 명령어
// UDRL

// 0, 0 에서 시작
// x : -5 ~ 5
// y : -5 ~ 5
// 움직인 길이가 9지만 처음 걸어본 길의 길이는 7
// 바깥으로 나가는 명령은 무시

// 처음 걸어본 길의 길이 return

function solution(dirs) {
  let dxy = [
    [-1, 0], // U
    [1, 0], // D
    [0, 1], // R
    [0, -1] // L
  ]

  let cmd = []
  let check = new Set();
  let x = 0;
  let y = 0;
  let nx = 0;
  let ny = 0;
  for (let dir of dirs) {
    if (dir === 'U') {
      cmd = dxy[0]
    } else if (dir === 'D') {
      cmd = dxy[1]
    } else if (dir === 'R') {
      cmd = dxy[2]
    } else if (dir === 'L') {
      cmd = dxy[3]
    }

    nx = x + cmd[0]
    ny = y + cmd[1]

    if (-6 < nx && nx < 6 && -6 < ny && ny < 6) {
      check.add("" + x + y + nx + ny)
      check.add("" + nx + ny + x + y)
      x = nx;
      y = ny;
    }
    

  }

  return check.size / 2;
}

console.log(solution("ULURRDLLU"))
// 7
console.log(solution("LULLLLLLU"))
// 7


