// 프로그래머스 [3차] 파일명 정렬

// 이름 순으로 정렬된 파일 목록은 보기 불편

// 숫자를 반영한 정렬 기능을 구현하기로 했다.

// 파일명은 HEAD, NUMBER, TAIL로 구성
// HEAD : 문자
// NUMBER : 숫자
// TAIL : 나머지, null 일수도

// 1. HEAD 사전 순 정렬 (대소문자 구분 X)
// 2. 숫자순 정렬 (9 < 10 < 0011 < 012 < 13 < 014)
// 3. 입력순

function solution(files) {

	let answer = [];

	const findHeader = (file) => {
		let head = [];
		for (let i = 0; i < file.length; i++) {
			// 문자열이면
			if (isNaN(file[i])) {
				head.push(file[i]);
			} else {
				return [head, file.slice(i, file.length)];
			}
		}
	}

	const findNum = (file) => {
		let num = [];
		for (let i = 0; i < file.length; i++) {
			// 숫자라면
			if (!isNaN(file[i])) {
				num.push(file[i]);
			} else {
				return [num, file.slice(i, file.length)];
			}
		}
	}	

	const transNums = (num) => {
		for (let i = 0; i < num.length; i++) {
			if (num[i] !== '0') {
				return num.slice(i, num.length);
			}
		}
	}
	let result = [];
	for (let i = 0; i < files.length; i++) {
		let file = files[i]
		let [head, rest] = findHeader(file);
		let [num, tail] = findNum(rest);
		let transHead = head.join('').toLowerCase();
		let transNum = 0;
		if (num[0] === '0') {
			transNum = Number(transNums(num).join(''));
		} else {
			transNum = Number(num.join(''));
		}

		result.push([head, transHead, num, transNum, tail]);
	}
	console.log(result);
	result.sort((a, b, c, d, e) => {
		return b - d - e
	})
	console.log(result, 'sorted');

    return answer;
}

console.log(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
// ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]