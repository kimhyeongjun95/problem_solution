// 프로그래머스 순위

// n명의 권투선수
// 1 ~ n번
// 결과를 가지고 선수들의 순위
// 몇몇 경기 결과 분실

// [A, B] A 선수가 B를 이김

function solution(n, results) {
  let answer = 0;
  arr = Array.from(Array(n+1), () => Array(n+1).fill(0));

  results.map((val) => {
    let [win, lose] = val;
    arr[win][lose] = 1;
    arr[lose][win] = -1;
  })

  for (let k = 1; k < n+1; k++) {
		for (let i=1; i<n+1; i++) {
      for (let j=1; j<n+1; j++) {
        // 자기 자신 X 승패 여부를 아직 모름(0)
        if (i !== j && arr[i][j] == 0) {
					// A가 B를 이기고 B가 C를 이기면 A가 B를 이긴다.
          if (arr[i][k] == 1 && arr[k][j] == 1) {
						arr[i][j] = 1;
          } else if (arr[i][k] == -1 && arr[k][j] == -1) {
						arr[i][j] = -1;
					}
        }
      }
    }
  }

	// 경기 결과를 모른다면 0
	// 각 선수에 대해 0이 하나라면(자기 자신이란 뜻) answer += 1
	for (let i = 1; i<n+1; i++) {
		let count = 0;
		for (let j=1; j<n+1; j++) {
			if (arr[i][j] === 0) {
				count += 1;
			}
		}
		answer += count === 1 ? 1 : 0;
	}
	
  return answer;
}

console.log(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
// 2