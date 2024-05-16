class Comida{
	constructor(){
		this.x = Math.random()*anchura
		this.y = Math.random()*altura
		this.visible = true
		this.vida = 0
		this.radio = Math.random()*10
		this.a = 0+Math.PI*2*Math.random()
		this.v = Math.random()/4
		this.transparencia = 1;
	}
	dibuja(){
		if(this.visible == true){
		contexto2.shadowColor = "rgba(255,255,255,"+this.transparencia+")";
		contexto2.shadowBlur = this.radio;
		contexto2.fillStyle = "rgba(255,255,255,"+this.transparencia+")"
		contexto2.beginPath()
		contexto2.arc(
			this.x,
			this.y,
			this.radio,
			0,
			Math.PI*2,
			true)
		contexto2.closePath();
		contexto2.fill()
		}	
	}
	vive(){
		this.vida++;
		//this.mueve()
		this.dibuja()
	}
	mueve(){
		//this.y+=0.1 
		this.a+=(Math.random()-0.5)*0.1
		this.x+=Math.cos(this.a)*this.v
		this.y+=Math.sin(this.a)*this.v
	}
}
