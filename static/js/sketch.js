var symbolSize=20;
var streams =[];

function setup() {
	var canvas = createCanvas(210, 1700);
	canvas.parent('dancing_blocks');
	var x=0;
	for (var i = 0; i <=width/symbolSize;i++) {
		var stream=new Stream();
		stream.generateSymbols(x,random(-700,0));
		streams.push(stream);
		x+=symbolSize;
	}
	textSize(symbolSize);
	frameRate(20);
}
function draw(){
	background(255);
	streams.forEach(function(stream){
		stream.render();
	});
}

function Symbol(x,y,speed){
	this.x=x;
	this.y=y;
	this.value;
	this.speed=speed;
	this.swithInterval=round(random(2,20));

	this.setRandomSymbol=function(){
		if(frameCount% this.swithInterval == 0){
			this.value=String.fromCharCode(
			    0x0980+round(random(0,112))
			);			
		}

	}

	this.rain=function(){
		this.y=(this.y>=height)?0:this.y+=this.speed;
	}
}

function Stream(){
	this.symbols=[];
	this.totalSymbols=round(random(5,15));
	this.speed=random(5,20);

	this.generateSymbols=function(x,y){

		for (var i = 0; i <=this.totalSymbols; i++) {
			symbol =new Symbol(x,y,this.speed);
			symbol.setRandomSymbol();
			this.symbols.push(symbol);
			y-=symbolSize;
		}
	}

	this.render=function(){
		this.symbols.forEach(function(symbol){
			fill(25);
			text(symbol.value,symbol.x,symbol.y);
			symbol.rain();
			symbol.setRandomSymbol();
		});
	}
}
