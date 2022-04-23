// 프로그래머스 카펫

// 중앙 노란색
// 테두리 1줄 갈색

// 격자의 개수는 기억, 전체 카펫의 크기 기억 X
// 카펫의
// [가로 크기, 세로 크기] return
// 가로 >= 세로

// 노란색이 가로로 1줄일때부터 brown 갯수가 맞는지 확인
// brown 갯수 : yellow 세로 * 2 + ((yellow 가로 * 2) + 4)
// brown 갯수가 맞으면 return

function solution(brown, yellow) {
	let count = 1;

	while (true) {
		let yellowRow = yellow / count;
		let yellowCol = yellow / yellowRow

		let guessBrown = (yellowCol * 2) + ((yellowRow * 2) + 4);
		if (guessBrown == brown) {
			return [yellowRow + 2, yellowCol + 2]
		}
		count += 1;
	}	
}

console.log(solution(10, 2))
// [4, 3]
console.log(solution(8, 1))
// [3, 3]
console.log(solution(24, 24))
// [8, 6]