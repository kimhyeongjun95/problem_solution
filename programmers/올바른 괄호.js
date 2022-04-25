// 프로그래머스 올바른 괄호

// (로 열렸으면 반드시 짝지어서 )로 닫혀야 함

function solution(s){
    let stack = [];

	for (let i of s) {
		if (i == '(') {
			stack.push(i);
		} else if (stack[stack.length - 1] == '(' && i == ')') {
			stack.pop();
		} else if (stack[stack.length - 1] == '(' && i == '(') {
			return false;
		} else {
            return false;
        }
	}
	if (stack.length > 0) {
		return false;
	}
	return true;
}

console.log(solution("()()"))
// true
console.log(solution("(())()"))
// true
console.log(solution(")()("))
// false
console.log(solution("(()("))
// false