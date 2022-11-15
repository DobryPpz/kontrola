class Fibo {
    getFib(n){
        if(n<=0) return 0;
        if(n==1) return 1;
        let a = 0;
        let b = 1;
        for(let i=2;i<=n;i++){
            let zm = a+b;
            a = b;
            b = zm; 
        }
        return b;
    }
    checkIsItFiboElement(n){
        let a = 0;
        let b = 1;
        if(n<=1) return true;
        while(b < n){
            let zm = a+b;
            a = b;
            b = zm;
        }
        return b==n;
    }
}

module.exports = Fibo;