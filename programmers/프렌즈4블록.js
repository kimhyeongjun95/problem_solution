// 프로그래머스 (2018 카카오) 프렌즈4블록 

// 2 x 2 형태로 4개가 붙어있으면 사라지면서 점수
// 한꺼번에 지워지고 위의 블록이 아래로 떨어짐
// 반복
// 4개 이상 직사각형

// 지워지는 블록 갯수 return

// m = row, n = col

// 1. 순회해서 매 알파벳마다 우, 하, 우하로 일치하는지 확인
// 1-1. arr에 담아두기
// 2. 저장해둔 위치 0 처리
// 3. 밑으로 떨어지게 하기
// 4. 1-1에서 담긴 값이 없는지 확인
// 4-1. board에서 0 숫자 갯수 확인

function solution(m, n, board) {

	board = board.map((v) => v.split(''))

	while (true) {
		let toRemove = [];
		// 1
		for (let i = 0; i < m-1; i++) {
			for (let j = 0; j < n-1; j++) {
				if (
					board[i][j] &&
					board[i][j] === board[i][j+1] &&
					board[i][j] === board[i+1][j] &&
					board[i][j] === board[i+1][j+1]
				) {
					// 1-1
					toRemove.push([i, j]);
				}
			}
		}

		// 4
		if (!toRemove.length) {
			// 4-1
			let count = 0;
			for (let i = 0; i < m; i++) {
				for (let j = 0; j < n; j++) {
					if (board[i][j] === 0) {
						count += 1;
					}
				}
			}
			return count;
		}
		// 2
		while (toRemove.length > 0) {
			[x, y] = toRemove.pop();
			board[x][y] = 0;
			board[x+1][y] = 0;
			board[x][y+1] = 0;
			board[x+1][y+1] = 0;
		}
		
		// 3
		for (let i = m-1; i > -1; i--) {
			if (!board[i].includes(0)) continue;
			for (let j = 0; j < n; j++) {
				let idx = 0;
				if (board[i][j] === 0) {
					while (true) {
						if (board[i+idx][j] !== 0) {
							let temp = board[i+idx][j];
							board[i][j] = temp;
							board[i+idx][j] = 0;
							break;
						}
						idx -= 1;
						if ((idx + i) === -1) break;
					}
				}
			}
		}

	}
}

console.log(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
// 14

// 3번 이러는 방법도 있음.
// for (let i = m - 1; i > 0; i--) {
// 	if (!board[i].some((v) => !v)) {
// 		continue
// 	}

// 	for (let j = 0; j < n; j++) {
// 		for (let k = i - 1; k >= 0 && !board[i][j]; k--) {
// 			if (board[k][j] != 0) {
// 				board[i][j] = board[k][j];
// 				board[k][j] = 0;
// 				break;
// 			}
// 		}
// 	}
// }