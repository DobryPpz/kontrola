class Fibo {
    getFib(n,memo={}){
        if(n in memo) return memo[n];
        if(n<=0) return 0;
        if(n==1) return 1;
        memo[n] = this.getFib(n-1,memo)+this.getFib(n-2,memo);
        return memo[n];
    }
}

module.exports = Fibo;