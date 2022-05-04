// 프로그래머스 (2018 카카오) 프렌즈4블록 

// 2 x 2 형태로 4개가 붙어있으면 사라지면서 점수
// 한꺼번에 지워지고 위의 블록이 아래로 떨어짐
// 반복
// 4개 이상 직사각형

// 지워지는 블록 갯수 return

// m = row, n = col

// 1. 순회해서 매 알파벳마다 우, 하, 우하로 4개 이상인지 확인
// 2. 

function solution(m, n, board) {

	board = board.map((v) => v.split(''))
	while (true) {
		let check = [];
		for (let i = 0; i < m-1; i++) {
			for (let j = 0; j < n-1; j++) {
				if (
					board[i][j] &&
					board[i][j] === board[i+1][j] &&
					board[i][j] == board[i][j+1] &&
					board[i][j] == board[i+1][j+1]
				) {
					check.push([i, j]);
				}
			}
		}
		if (!check.length) {
			let result = board.reduce((acc, cur) => {
				acc += cur.filter((v) => !v).length;
				return acc;
			}, 0)
			console.log(board);
			return result;
		}

		for (let i = 0; i < check.length; i++) {
			let row = check[i][0]
			let col = check[i][1];
			board[row][col] = 0;
			board[row][col + 1] = 0;
			board[row + 1][col] = 0;
			board[row + 1][col + 1] = 0;
		}
		
		for (let i = m - 1; i > 0; i--) {
			if (!board[i].some((v) => !v)) {
				continue
			}

			for (let j = 0; j < n; j++) {
				for (let k = i - 1; k >= 0 && !board[i][j]; k--) {
					if (board[k][j] != 0) {
						board[i][j] = board[k][j];
						board[k][j] = 0;
						break;
					}
				}
			}
		}

	}
}

console.log(solution(
	4, 5,
	["CCBDE", "AAADE", "AAABF", "CCBBF"]	
))

// 14