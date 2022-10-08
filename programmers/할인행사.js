// 프로그래머스 할인 행사

// 일정한 금액 => 10일 동안 회원 자격 부여
// 회원 대상 매일 한 가지 제품 행사
// 제품 하루에 하나씩 구매가능
// 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치하는 경우 회원가입

function solution(want, number, discount) {
    const need = {};
    let answer = 0;
    const checkCount = (check) => {
        for (let i = 0; i < want.length; i++) {
            if (check[want[i]] !== need[want[i]]) return false;
        }
        return true;
    }
    for (let i = 0; i < want.length; i++) {
        need[want[i]] = number[i];
    }
    for (let i = 0; i < discount.length-9; i++) {
        const check = {};
        for (let j = i; j < i+10; j++) {
            check[discount[j]] ? check[discount[j]] += 1 : check[discount[j]] = 1;
        }
        if (checkCount(check)) answer += 1;
    }
    return answer;
}

console.log(solution(
    ["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
))
// 3
console.log(solution(
    ["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
))
// 0