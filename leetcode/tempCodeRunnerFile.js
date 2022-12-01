eckPalindrome = (sub) => {
        for (let k = 0; k < parseInt(sub.length / 2); k++) {
            if (sub[k] !== sub[sub.length - k]) return false;
        }
        return true;
    };