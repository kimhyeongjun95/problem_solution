// 프로그래머스 (2020 카카오) 문자열 압축
// 재풀이

function solution(s) {
    var answer = s.length;
    for (let i = 1; i < Math.floor(s.length/2)+1; i++) {
        let temp = '';
        let prev = s.slice(0, i);
        let count = 1;
        for (let j = i; j < s.length; j += i) {
            if (prev === s.slice(j, j+i)) {
                count += 1;
            } else {
                if (count >= 2) {
                    temp += String(count) + prev
                } else {
                    temp += prev;
                }
                count = 1;
                prev = s.slice(j, j+i);
            }
        }

        if (count >= 2) {
            temp += String(count) + prev
        } else {
            temp += prev;
        }

        answer = Math.min(answer, temp.length);
    }
    return answer;
}

console.log(solution("aabbaccc"))
// 7
console.log(solution("ababcdcdababcdcd"))
// // 9