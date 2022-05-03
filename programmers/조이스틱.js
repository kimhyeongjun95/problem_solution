// 프로그래머스 조이스틱

// 알파벳으로 이름 완성, 맨 처음엔 A로만 이루어짐
// ex) 완성 글자가 세 글자면 AAA, 네 글자면 AAAA

// 조이스틱 조작횟수 최솟값 return 

// o : 목표 x : 안맞춰진 상태(A)
// 1. 아스키코드 변환
// 1-1. N 이하면 += N 이상이면 += (Z값 - 아스키코드 val)
// 2. x는 A에서부터 o까지 어디가 더 빠른지 확인(직진 또는 역순)
// 2-1. 더 적은값 +=
// 3. 현재 위치에서 x를 찾는데 왼쪽 또는 오른쪽이 더 효율적인지 확인
// 4. 이동
// 5. 일치하는지 확인

function solution(name) {
	let count = 0;

	let move = name.length - 1;

	// 각각의 상하로 알파벳 움직이는 값 계산
	for (let i = 0; i < name.length; i++) {
		let temp = name.charCodeAt(i)
		if (temp < 78) {
			// N 이하면
			count += temp - 65;
		} else {
			// N 이상 (뒤에서 접근)
			count += 91 - temp;
		}

		// 좌우 이동 인덱스
		let nextIndex = i + 1;

		while (nextIndex < name.length && name.charCodeAt(nextIndex) === 65) {
			nextIndex += 1;
		}
		// 왼쪽으로 돌아가는 것이 더 빠른 경우
		// 처음 위치로 돌아간 횟수(i * 2) + 문자열 길이 - A가 연속으로 나오는 지점의 다음값
		move = Math.min(move, (i*2) + name.length - nextIndex )
	}

	count += move;
	return count;
}

console.log(solution("JEROEN"))
// 56
console.log(solution("JAN"))
// 23
console.log(solution("JAZ"))
// 11