console.log(new Array(26).fill(65).map((a,i)=>String.fromCharCode(a+i+32*(i%2))).join(" "));