// 프로그래머스 모음사전

// 모음만을 사용하여 만들 수 있는 길이 5 이하의 모든 단어가 수록
// "A", "AA", 마지막은 "UUUUU"

// 단어가 주어지면 이 단어가 사전에서 몇번째인지?

function solution(word) {
	let alpha = ["A", "E", "I", "O", "U"]
	let result = [];
	const find = (s) => {
		if (s.length === 5) {
			return;
		}

		for (let i = 0; i < 5; i++) {
			let temp = s + alpha[i];
			result.push(temp);
			find(temp);
		}
	}
	find("")
	let answer = result.indexOf(word) + 1;
	return answer;
}

console.log(solution("AAAAE"))
// 6
console.log(solution("AAAE"))
// 10
console.log(solution("I"))
// 1563
console.log(solution("EIO"))
// 1189