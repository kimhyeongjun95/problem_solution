// 프로그래머스 문자열 다루기 기본

// length 4 or 6 숫자로만 구성

function solution(s) {
  for (let i = 0; i < s.length; i++) {
    if (isNaN(s[i]) == true) {
      return false
    }
  }
  if (s.length == 4 || s.length == 6) {
    return true
  }
  return false
}

console.log(solution("a1234"))