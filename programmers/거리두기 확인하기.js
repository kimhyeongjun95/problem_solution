// 프로그래머스 (2021 카카오 인턴) 거리두기 확인하기

// 대기실 5개, 5x5
// 맨해튼 거리로 2 이하 X
// 자리 사이가 파티션으로 막혀있으면 O

// P : 응시자
// O : 빈 테이블
// X : 파티션

// 각 대기실 별로 거리두기 O : return 1
// else : return 0


function solution(places) {
    let answer = [];
	dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

	const find = (idx, arr) => {
		for (let i = 0; i < arr.length; i++) {
			if (!toFind(idx, arr[i][0], arr[i][1])) {
				return 0;
			}
		}
		return 1
	}
	
	const toFind = (idx, j, k) => {
		let visited = Array.from(Array(5), () => Array(5).fill(0));
		let arr = [[j, k, 0]];
		visited[j][k] = 1;
		while (arr.length) {
			let [x, y, count] = arr.shift();
			count += 1;
			for (let i = 0; i < dxy.length; i++) {
				let nx = x + dxy[i][0]
				let ny = y + dxy[i][1]
				if (-1 < nx && nx < 5 && -1 < ny && ny < 5) {
					if (places[idx][nx][ny] == 'O' && visited[nx][ny] == 0) {
						visited[nx][ny] = 1;
						arr.push([nx, ny, count]);
					} else if (visited[nx][ny] == 0 && places[idx][nx][ny] == 'P' && count <= 2) {
						return 0;
					}
				}
			}
		}
		return 1;
	}

	for (let i = 0; i < places.length; i++) {
		let check = [];
		for (let j = 0; j < places.length; j++) {
			for (let k = 0; k < places.length; k++) {
				if (places[i][j][k] == 'P') {
					check.push([j, k]);
				}
			}
		}
		answer.push(find(i, check));
	}
	return answer;
}

console.log(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
// [1, 0, 1, 1, 1]