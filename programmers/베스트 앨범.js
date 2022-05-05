// 프로그래머스 베스트 앨범

// 정렬 순
// 1. 속한 노래가 많이 재생된 장르 먼저 수록
// 2. 장르 내에서 많이 재생된 노래 먼저 수록
// 3. 고유 번호가 낮은 노래 먼저 수록

// 장르 별 많이 재생된 노래 두 개씩 모아 앨범 출시
// 장르에 속한 곡이 하나라면, 하나의 곡만 선택

// 1. 장르당 재생 수 구하기
// 1-1. 장르 재생 순으로 정렬
// 2. 장르당 많이 재생된 노래 구하기
// 2-2. 2개씩 구하기
// 3. 고유 번호 순 저장

function solution(genres, plays) {
    let check = {};
	// 1
	for (let i = 0; i < genres.length; i++) {
		check[genres[i]] = check[genres[i]] ? check[genres[i]] + plays[i] : plays[i]
	}

	let temp = [];
	for (let [key, val] of Object.entries(check)) {
		temp.push([key, val])
	}
	temp.sort((a, b) => {
		if (a[1] > b[1]) return -1;
		if (b[1] > a[1]) return 1;
		return 0;
	})
	// 1-1
	temp = temp.map((v) => v[0]);

	// 2
	let songs = [];
	for (let i = 0; i < genres.length; i++) {
		songs.push([genres[i], plays[i], i])
	}
	songs.sort((a, b) => {
		if (a[0] > b[0]) return -1;
		if (a[0] < b[0]) return 1;

		if (a[1] > b[1]) return -1;
		if (a[1] < b[1]) return 1;
		return 0;
	});
	// 2-1
	let result = [];
	for (let genre of temp) {
		let count = 0;
		for (let i = 0; i < genres.length; i++) {
			if (genre === songs[i][0]) {
				count += 1;
				result.push(songs[i][2])
			}
			if (count > 1) break; 
		}
	}
	return result;
}

console.log(solution(
	["classic", "pop", "classic", "classic", "pop"],
	[500, 600, 150, 800, 2500],
))
// [4, 1, 3, 0]