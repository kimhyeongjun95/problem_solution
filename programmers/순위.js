// 프로그래머스 순위

// n명의 권투선수
// 1 ~ n번
// 결과를 가지고 선수들의 순위
// 몇몇 경기 결과 분실

// [A, B] A 선수가 B를 이김

function solution(n, results) {
  let winner = results.reduce((acc, cur) => {
    acc[0] = cur[1] ? cur[1] : cur[1]
  }, {})
  return winner;
}

console.log(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
// 2