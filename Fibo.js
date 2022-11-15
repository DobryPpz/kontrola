class Fibo {
    getFib(n,memo={}){
        if(n in memo) return memo[n];
        if(n<=0) return 0;
        if(n==1) return 1;
        memo[n] = this.getFib(n-1,memo)+this.getFib(n-2,memo);
        return memo[n];
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