/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function plusMinus(arr) {
    // Write your code here
    let pos = 0;
    let neg = 0;
    let zeros = 0;
    arr.forEach((v) => {
        if (v > 0) pos += 1;
        else if (v < 0) neg += 1;
        else zeros += 1;
    });
    let sum = pos + neg + zeros;
    const result = [pos / sum, neg / sum, zeros / sum];
    result.forEach((v) => {
        let val = v.toFixed(6);
        console.log(val);
    });
}

plusMinus([55, 48, 48, 45, 91, 97, 45, 1]);
plusMinus([-4, 3, -9, 0, 4, 1]);
