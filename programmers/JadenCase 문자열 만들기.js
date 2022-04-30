// 프로그래머스 JadenCase 문자열 만들기

// 첫 문자가 대문자, 나머지 소문자
// 첫 문자가 알파벳 X => 나머지 소문자

function solution(s) {
  let answer = '';
  s = s.split(' ');
  for (let i of s) {
    i = i.toLowerCase().split('');
    if (typeof i[0] === "string") {
      i[0] = i[0].toUpperCase();
    }
    answer += (i.join('')) + ' '
  }
  return answer.trim();
}

// console.log(solution("3people unFollowed me"))
// "3people Unfollowed Me"
console.log(solution("3people  unFollowed me"))
// "3people Unfollowed Me"



