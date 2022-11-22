const Fibo = require("./Fibo");
const memo = {};
const fiboCalculator = new Fibo();
for(let i=0;i<20;i++){
    console.log(fiboCalculator.getFib(i,memo));
}