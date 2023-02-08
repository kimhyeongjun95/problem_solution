const obj = {
    abc: 1,
    fff: this,
    Cde: function () {
        console.log(this);
    },
};

console.log(obj);
console.log(this === global);
console.log(this);

function a() {
    console.log(this === global);
}
a();
