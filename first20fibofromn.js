const Fibo = require("./Fibo");
const memo = {};
const fiboCalculator = new Fibo();
const limit = +process.argv[2];
for(let i=limit;i<limit+20;i++){
    console.log(fiboCalculator.getFib(i,memo));
}