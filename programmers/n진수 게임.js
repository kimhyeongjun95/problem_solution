// 프로그래머스 (2018 카카오 3차) n진수 게임

// 첫 번째: 0, 두 번째: 1 ..... 열 번째 : 9
// 10 이상의 숫자는 한 자리씩 끊어 말하기
// 열한 번째: 1, 열두 번째: 0

// 이진수로 진행하기도 함.

// n : 진법
// t : 미리 구할 숫자의 갯수
// m : 게임에 참가하는 인원
// p : 튜브의 순서

// 1. n진법으로 변환
// 2. 문자열로 모두의 순서 구하기
// 3. 튜브꺼만 가져오기

function solution(n, t, m, p) {
	let queue = '';

	for (let i = 0; i < t * m; i++) {
		// 1, 2
		queue += i.toString(n);
	}

	result = '';
	for (i = p - 1; result.length < t; i += m) {
		result += queue[i];
	}
	return result.toUpperCase();
}

console.log(solution(2, 4, 2, 1))
// "0111"
console.log(solution(16, 16, 2, 1))
// "02468ACE11111111"
console.log(solution(16, 16, 2, 2))
// "13579BDF01234567"
