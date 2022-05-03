// 프로그래머스 가장 큰 정사각형 찾기

// 0과 1로 이루어진 표
// 1로 이루어진 가장 큰 정사각형 찾기

function solution(board)
{
    let answer = 0 ;
	let visited = Array.from(Array(board.length), () => Array(board[0].length).fill(0));
	for (let i = 0 ; i < board.length; i++) {
		for (let j = 0; j < board[0].length; j++) {
			if (board[i][j] === 1 && visited[i][j] === 0) {
				let nextIdx = j;
				while (board[i][nextIdx] === 1 || nextIdx < board[0].length) {
					visited[i][nextIdx] = 1;
					nextIdx += 1;
				}
				let left = j;
				let right = nextIdx - 1;
				let downIdx = 
				while (board[])
			}
		}
	}
}

console.log(solution(
	[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
))
// 9
console.log(solution(
	[[0,0,1,1],[1,1,1,1]]
))
// 4