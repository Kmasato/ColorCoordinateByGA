class Model{
    constructor(bodyColor=0, bottomColor=0, footColor=0){
        /*
        this.bodyColor = bodyColor;
        this.bottomColor = bottomColor;
        this.footColor = footColor;
        */

        // for debug
        this.bodyColor = randomColor();
        this.bottomColor = randomColor();
        this.footColor = randomColor();
    }

    draw(){
        var canvas = document.getElementById("mainCanvas");
        var context = canvas.getContext("2d");

        context.fillStyle = this.bodyColor;
        context.fillRect(10,10,100,100);

        console.log(this.bodyColor);
    }
}

function randomColor(){
    var H = Math.random() * 360.0;
    var S = Math.random();
    var V = Math.random();

    var color = HSVToRGB(H, S, V);

    return color;
};

function HSVToRGB(H, S, V) {

    var C = V * S;
    var Hp = H / 60;
    var X = C * (1 - Math.abs(Hp % 2 - 1));

    var R, G, B;
    if (0 <= Hp && Hp < 1) {[R,G,B]=[C,X,0]};
    if (1 <= Hp && Hp < 2) {[R,G,B]=[X,C,0]};
    if (2 <= Hp && Hp < 3) {[R,G,B]=[0,C,X]};
    if (3 <= Hp && Hp < 4) {[R,G,B]=[0,X,C]};
    if (4 <= Hp && Hp < 5) {[R,G,B]=[X,0,C]};
    if (5 <= Hp && Hp < 6) {[R,G,B]=[C,0,X]};

    var m = V - C;
    [R, G, B] = [R+m, G+m, B+m];

    R = Math.floor(R * 255);
    G = Math.floor(G * 255);
    B = Math.floor(B * 255);

    return "rgb("+ R + "," + G + "," + B +")";
}

var model = new Model();
model.draw();
