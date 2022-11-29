// 1. 열린 bracket은 같은 type의 bracket으로 닫아야 한다.
// 2. 열린 bracket은 in correct order로 닫아야 한다.
// 3. 모든 close bracket은 대응하는 open bracket이 존재한다.

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    const stack = [];
    for (let i of s) {
        if (
            stack.length &&
            stack[stack.length - 1] === "(" &&
            (i === "}" || i === "]")
        )
            return false;
        else if (stack.length && stack[stack.length - 1] === "(" && i === ")")
            stack.pop();
        else if (
            stack.length &&
            stack[stack.length - 1] === "[" &&
            (i === "}" || i === ")")
        )
            return false;
        else if (stack.length && stack[stack.length - 1] === "[" && i === "]")
            stack.pop();
        else if (
            stack.length &&
            stack[stack.length - 1] === "{" &&
            (i === "]" || i === ")")
        )
            return false;
        else if (stack.length && stack[stack.length - 1] === "{" && i === "}")
            stack.pop();
        else if (i === "(" || i === "{" || i === "[") stack.push(i);
        else if ((!stack.length && i === ")") || i === "}" || i === "]")
            return false;
    }
    if (stack.length) return false;
    return true;
};

// console.log(isValid("()"));
// true
// console.log(isValid("()[]{}"));
// true
// console.log(isValid("(]"));
// false
console.log(isValid("{[]}"));
// true
