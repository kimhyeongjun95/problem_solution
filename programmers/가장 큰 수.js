// 프로그래머스 가장 큰 수

// 가장 큰 수 return

function solution(numbers) {
	let Seen = numbers.map((num) => String(num));
    Seen.sort((a, b) => {
		return (b + a) - (a + b)
	});
	if (Seen[0] == 0) {
		return '0'
	}
	return Seen.join('');
}

console.log(solution([6, 10, 2]))
// 6210
console.log(solution([3, 30, 34, 5, 9]))
// "9534330"

