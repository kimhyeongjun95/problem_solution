// 프로그래머스 핸드폰 번호 가리기

function solution(phone_number) {
  let answer = '';
  answer += '*'.repeat(phone_number.length-4)
  for (let i = (phone_number.length)-4; i < phone_number.length; i++) {
	  answer += phone_number[i]
  }
  return answer
}

console.log(solution("01033334444"))
"*******4444"
