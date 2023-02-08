function lonelyinteger(a) {
    const check = {};
    a.forEach((v) => (check[v] = check[v] + 1 || 1));
    for (const [key, val] of Object.entries(check)) {
        if (val === 1) return key;
    }
}

console.log(lonelyinteger([1, 2, 3, 4, 3, 2, 1]));
console.log(lonelyinteger([0, 0, 1, 2, 1]));
