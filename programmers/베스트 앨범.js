// 프로그래머스 베스트 앨범

// 정렬 순
// 1. 속한 노래가 많이 재생된 장르 먼저 수록
// 2. 장르 내에서 많이 재생된 노래 먼저 수록
// 3. 고유 번호가 낮은 노래 먼저 수록

// 장르 별 많이 재생된 노래 두 개씩 모아 앨범 출시
// 장르에 속한 곡이 하나라면, 하나의 곡만 선택

// 1. 장르당 재생 수 구하기
// 2. 장르당 많이 재생된 노래 구하기
// 3. 고유 번호 순 저장

function solution(genres, plays) {
	// let check = {};
	// // 1
	// for (let i = 0; i < plays.length; i++) {
	// 	check[genres[i]] = (!check[genres[i]]) ? plays[i] : check[genres[i]] + plays[i];
	// 	console.log(check);
	// }

	let play = {};
	for(let i=0; i < genres.length; i++){
		play[genres[i]] = (!play[genres[i]]) ? plays[i] : play[genres[i]] + plays[i];
	}
	// 장르 순서만
	let order = [];
	// 역순 정렬
	play = Object.entries(play).sort((a,b)=>b[1]-a[1]);
	console.log(play);
	for(let i in play){
			order.push(play[i][0]);
	}
	console.log(order);
	
	let answer = [];
	for (let i = 0; i < order.length; i++) {
		let gen = order[i];
		let stack = {};
		console.log(gen);
		for (let j = 0; j < genres.length; j++) {
			if (genres[j] === gen) {
				stack[j] = plays[j]
			}
		}
		console.log(stack, '1');
		stack = Object.entries(stack).sort((a, b) => b[1] - a[1]);
		let count = 0;
		for (let k =0; k < stack.length; k++) {
			count += 1;
			if (count > 2) {
				break;
			}
			answer.push(Number(stack[k][0]))
		}
		console.log(stack)
		console.log(answer);
	}
	return answer;
}


console.log(solution(
	["classic", "pop", "classic", "classic", "pop"],
	[500, 600, 150, 800, 2500]
))
// [4, 1, 3, 0]