// 프로그래머스 영어 끝말잇기

// 1부터 n까지 번호가 붙어있는 n명의 사람

// 1번부터 차례대로 단어를 말함
// 마지막 사람이 말하고 1번부터 다시 시작
// 앞사람이 말한 단어의 마지막 문자로 시작
// 중복 X
// 한 글자 X

// [번호, 몇 번째 차례] return

function solution(n, words) {
    let count = 2;
	let turn = 1;
	let check = [words[0]];
	for (let i=1; i < words.length; i++) {
		let prev = words[i-1];
		let now = words[i];
		if (prev[prev.length-1] !== now[0]) {
			return [count, turn]
		}

		if (check.includes(words[i])) {
			return [count, turn];
		}
		check.push(words[i]);

		count += 1;
		if (count == n+1) {
			count = 1;
			turn += 1;
		}
	}
	return [0, 0];
}

console.log(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
// [3, 3]
console.log(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
// [0, 0]
console.log(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
// [1, 3]
console.log(solution(10, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
// [9, 1]
console.log(solution(2, ["ewe", "ewq"]))
// [0, 0]
console.log(solution(2, ["ewe", "ewe"]))
// [2, 1]
console.log(solution(2, ["qwe", "eqwe", "eqqwe", "eqqwe"]))
// [1, 2]

