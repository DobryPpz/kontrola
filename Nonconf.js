const Fibo = require("./Fibo");
const Punkt = require("./Punkt");

console.log("Pierwszy feature");
console.log("Drugi feature");
const p1 = new Punkt(4,3.3,8);
console.log(p1.listCoords());
console.log(p1.dist(new Punkt(0,0,0)));
const f = new Fibo();
console.log(f.getFib(10));