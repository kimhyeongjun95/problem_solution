// 프로그래머스 다리를 지나는 트럭

// 일차선 다리를 트럭이 순차적으로 건넌다.
// 모든 트럭이 건너려면 최소 몇초?

// bridge_length만큼 최대 올라갈 수 있음
// 다리는 weight 이하의 무게를 견딤
// 다리에 오르지 않은 트럭의 무게는 무시

// 1초에 1 length만큼 전진
// -> 하나의 트럭이 올라가는데 1초가 걸림

// 1. 매 초 계산
// 2. 다리 여유 무게 계산
// 2-1. truck_weights의 첫번째 대기가 들어올 수 있는지 확인
// 2-2. 들어올 수 있다면 onBridge에 birdge_length와 함께 push
// 3. 매 초마다 onBridge[i][1] -= 1
// 4. if onBridge[i][1] === -1: 빼주기
// 5. truck_weights와 onBridge가 비어있으면 시간 return

function solution(bridge_length, weight, truck_weights) {
    let time = 0;
    let onBridge = [];
    while (true) {
        
        
        truck = truck_weights.shift();
        onBridge.push(truck);

        time += 1;
    }
}

console.log(solution(2, 10, [7,4,5,6]))
// 8
console.log(solution(100, 100, [10]))
// 101
console.log(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
// 110
