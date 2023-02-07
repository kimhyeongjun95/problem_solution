function timeConversion(s) {
    // Write your code here
    let line = s.slice(8);
    let time = s.slice(0, 8);
    let [hour, min, sec] = time.split(":");
    if (line === "PM" && hour !== "12") hour = String(parseInt(hour) + 12);
    else if (line === "PM" && hour === "12") hour = "12";
    else if (line === "AM" && hour === "12") hour = "00";
    const answer = [hour, min, sec].join(":");
    return answer;
}

console.log(timeConversion("07:05:45PM"));
