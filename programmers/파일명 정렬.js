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
		return [num, file.slice(file.length, file.length)];
	}	

	const transNums = (num) => {
		for (let i = 0; i < num.length; i++) {
			if (num[i] !== '0') {
				return num.slice(i, num.length);
			}
		}
		return '';
	}

	let result = [];
	for (let i = 0; i < files.length; i++) {
		let file = files[i]
		let [head, rest] = findHeader(file);
		let [num, tail] = findNum(rest);
		let transHead = head.join('').toLowerCase();
		let transNum = 0;
		if (num[0] === '0') {
			let sum = num.reduce((a, b) => Number(a + b), 0);
			if (sum !== 0) {
				transNum = Number(transNums(num).join(''));
			} else {
				transNum = '';
			}
		} else {
			transNum = Number(num.join(''));
		}
		result.push([head, transHead, num, transNum, tail]);
	}
	result.sort((a, b) => {
		if (a[1] > b[1]) {
			return 1;
		} else if (a[1] < b[1]) {
			return -1;
		}
		

		if (a[3] > b[3]) {
			return 1;
		} else if (a[3] < b[3]) {
			return -1;
		}
		return 0;
	})
	console.log(result);
	for (let i of result) {
		answer.push(i[0].join('') + i[2].join('') + i[4])
	}

    return answer;
}

console.log(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
console.log(solution(["img000012345", "img1.png","img2","IMG02"]))
// console.log(solution(["img0000123aa", "img00000.345", "img001a00png", "img2", "IMG02"]))
// console.log(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
// console.log(solution(["img00000.345"]))
// ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

// if (a[1] > b[1]) {
// 	return 1;
// } else if (a[1] < b[1]) {
// 	return -1;
// }

