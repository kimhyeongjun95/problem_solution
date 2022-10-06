// HackerRank Strong Password

// random string of length
// =>
// length >= 6
// contains one digit
// contains one lower
// contains one upper
// contains one special

// 1. lower
// 2. upper
// 3. digit
// 4. special
// 5. length

function minimumNumber(n, password) {
    let answer = 0;
    let nLength = n;
    const specials = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+'];

    function checkLower(password) {
        for (let i of password) {
            if (specials.includes(i)) continue;
            if (isNaN(i) && i === i.toLowerCase()) return false;
        }
        return true;
    }
    function checkUpper(password) {
        for (let i of password) {
            if (specials.includes(i)) continue;
            if (isNaN(i) && i === i.toUpperCase()) return false;
        }
        return true;
    }
    function checkStr(password) {
        for (let i of password) {
            if (isNaN(i)) return true;
        }
        return false;
    }
    function checkDigit(password) {
        for (let i of password) {
            if (!isNaN(i)) return true;
        }
        return false;
    }
    function checkSpecial(password) {
        for (let i of password) {
            if (specials.includes(i)) return true;
        }
        return false;
    }

    let check = false;

    if (checkLower(password)) {
        answer += 1;
        nLength += 1;
        check = true;
    }
    if (checkUpper(password)) {
        answer += 1;
        nLength += 1;
        check = true;
    }
    if (!check && !checkStr(password)) {
        answer += 2;
        nLength += 2;
    }
    if (!checkDigit(password)) {
        answer += 1;
        nLength += 1;
    }
    if (!checkSpecial(password)) {
        answer += 1;
        nLength += 1;
    }
    if (nLength < 6) answer += 6 - nLength;
    return answer;
}

// console.log(minimumNumber(3, "Ab1"))
// 3
// console.log(minimumNumber(11, "#HackerRank"))
// 1
// console.log(minimumNumber(4, "4700"))
// 3
// console.log(minimumNumber(4, "goxg"))
// 3
// console.log(minimumNumber(4, "&+^&"))
// 3
// console.log(minimumNumber(6, "v6k61z"))
// 2
console.log(minimumNumber(2, "12"))
// 4