// 프로그래머스 기능개발

// 1. 매일 progresses[i]에 speeds[i] 만큼 +=
// 2. 만약 progresses[0]이 >= 100이면
// 2-1. while progress[0] >= 10 : shift();
// 3. count += 1
// 4. result push

function solution(progresses, speeds) {
    let result = [];

    while (true) {

        if (!progresses.length) {
            return result;
        }

        for (let i = 0; i < progresses.length; i++) {
            progresses[i] += speeds[i];
        }

        let count = 0;
        while (progresses[0] >= 100) {
            progresses.shift();
            speeds.shift();
            count += 1;
        }
        if (count > 0) result.push(count);

    }
}

console.log(solution([93, 30, 55], [1, 30, 5]))
// [2, 1]
console.log(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
// [1, 3, 2]