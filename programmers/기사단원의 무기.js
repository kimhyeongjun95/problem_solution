// 기사단원의 무기

// 기사단의 각 기사에게는
// 1번부터 number까지 번호가 지정
// 기사들은 무기점에서 무기를 구매하려고 함

// 각 기사는 자신의 기사 번호의
// 약수 개수에 해당하는 공격력을 가진 무기를
// 구매하려고 한다.

// 단 이웃나라와의 협약에 의해
// 공격력의 제한수치를 정하고
// 제한수치보다 큰 공격력을 가진 무기를
// 구매해야하는 기사는
// 협약기관에서 정한 공격력을 가지는 무기를 구매해야 한다

// 무기의 공격력 1당 1kg의 철이 필요
// 무기점에서 무기를 모두 만들기 위해 필요한 철의 무게 미리 계산

function solution(number, limit, power) {
    const arr = Array(number).fill(0);
    arr[0] = 1;
    for (let i = 2; i < number + 1; i++) {
        let count = 1;
        for (let j = 1; j < i / 2 + 1; j++) {
            if (i % j === 0) count += 1;
        }
        arr[i - 1] = count;
    }
    const result = arr.map((e) => {
        if (e > limit) return power;
        return e;
    });
    return result.reduce((a, b) => a + b);
}

console.log(solution(5, 3, 2));
// 10
console.log(solution(10, 3, 2));
// 21
