class Punkt {
    constructor(x,y,z){
        this.x = x;
        this.y = y;
        this.z = z;
    }
    listCoords(){
        return `x:${this.x}  y:${this.y}  z:${this.z}`;
    }
    dist(point){
        return Math.sqrt(Math.pow(this.x-point.x,2)+Math.pow(this.y-point.y,2)+Math.pow(this.z-point.z,2));
    }
}

module.exports = Punkt;