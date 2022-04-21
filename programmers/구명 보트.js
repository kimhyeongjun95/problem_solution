// 프로그래머스 구명보트

// 무게제한 100kg => 2,4 같이 O / 1,3 같이 X
// 한 번에 최대 2명
// 구명보트를 최대한 적게 사용 모든사람 구출
// 구명보트 개수의 최솟값 return

// 1. 제일 무거운 + 제일 가벼운 > 한계 ?
// 1-1. 제일 무거운만 태우기
// 2. 제일 가벼운 + 제일 가벼운 + 1 > 한계 ?
// 2-2. 제일 가벼운만 태우기

function solution(people, limit) {
	people.sort((a, b) => a - b)
	let answer = 0;
	let i = 0;
	let j = people.length-1;
	while (i <= j) {
	// for (let i = 0, j = people.length - 1; i < j; i++) {
		if (people[i] + people[j] > limit) {
			answer += 1;
			j -= 1;
		} else {
			j -= 1;
			i += 1;
			answer += 1;
		}
	}

	return answer;
}

console.log(solution([70, 50, 80, 50], 100))
// 3
console.log(solution([70, 80, 50], 100))
// // 3