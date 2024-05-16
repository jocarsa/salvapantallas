class Pez{
	constructor(){
		this.x = Math.random()*anchura
		this.y = Math.random()*altura
		this.a = Math.random()*Math.PI*2
		this.edad = (Math.random()*2+2)/2;
		this.tiempo = Math.random();
		this.avancevida = Math.random()/10
		this.r = Math.round(Math.random()*255)
		this.g = Math.round(Math.random()*255)
		this.b = Math.round(Math.random()*255)
		this.energia = Math.random();
		this.direcciongiro = Math.round(Math.random()*2-1)
		this.numeroelementos = 10
		this.numeroelementoscola = 5
		this.colorr = new Array()
		this.colorg = new Array()
		this.colorb = new Array()
		this.reproducido = 0
		this.sexo = Math.round(Math.random())
		if(this.sexo == 0){
			this.r = Math.round(Math.random()*127)+127
			this.g = this.r/3
			this.b = this.r/3
			for(var i = -1;i<this.numeroelementos;i++){
				this.colorr[i] = this.r+Math.round((Math.random()-0.5)*100)
				this.colorg[i] = this.g+Math.round((Math.random()-0.5)*100)
				this.colorb[i] = this.b+Math.round((Math.random()-0.5)*100)
			}
		}else{
			this.g = Math.round(Math.random()*127)+127
			this.r = this.g/3
			
			this.b = this.g/3
			for(var i = -1;i<this.numeroelementos;i++){
				this.colorr[i] = this.r+Math.round((Math.random()-0.5)*100)
				this.colorg[i] = this.g+Math.round((Math.random()-0.5)*100)
				this.colorb[i] = this.b+Math.round((Math.random()-0.5)*100)
			}
		}
		this.anguloanterior = 0;
		this.giro = 0;
	}
	dibuja(){
		// Sensores
		/*
		for(var i = -2; i<2;i+=0.1){
			var datos = contexto.getImageData(
				this.x + Math.cos(this.a+i)*50,
				this.y + Math.sin(this.a+i)*50,
				1,
				1
			)
			if(datos.data[3] != 0){
			//console.log(datos.data[3])
			}
			if(datos.data[3] != 0){
				//this.a -= 1/i*0.01
				this.direcciongiro = i
				this.x -= Math.cos(i)*0.1
				this.y -= Math.sin(i)*0.1
			}
			
		}
		*/
		
		if(this.energia > 0){
		contexto.fillStyle = "rgb("+this.r+","+this.g+","+this.b+")"
		}else{
			contexto.fillStyle = "grey"
		}
		var numeroelementos = 10
		var numeroelementoscola = 5
		// Dibujo el cuerpo
		//contexto.filter = "blur(4px)";
		
			
		for(var i = -1;i<this.numeroelementos;i++){
			
			
			if(i == 1){
				contexto.fillStyle = "white"
				// ojo 1
					contexto.beginPath()
					contexto.arc(
						this.x+i*Math.cos(this.a+Math.PI/2)*4*this.edad-i*Math.cos(this.a)*1*this.edad+Math.sin(this.a)*Math.sin((i/5)-this.tiempo)*4,
						this.y+i*Math.sin(this.a+Math.PI/2)*4*this.edad-i*Math.sin(this.a)*1*this.edad+Math.cos(this.a)*Math.sin((i/5)-this.tiempo)*4,
						(this.edad*0.4*(numeroelementos-i)+1)/3,
						0,
						Math.PI*2,
						true)
					contexto.closePath();
					contexto.fill()
				// ojo 2
					contexto.beginPath()
					contexto.arc(
						this.x-i*Math.cos(this.a+Math.PI/2)*4*this.edad-i*Math.cos(this.a)*1*this.edad+Math.sin(this.a)*Math.sin((i/5)-this.tiempo)*4,
						this.y-i*Math.sin(this.a+Math.PI/2)*4*this.edad-i*Math.sin(this.a)*1*this.edad+Math.cos(this.a)*Math.sin((i/5)-this.tiempo)*4,
						(this.edad*0.4*(numeroelementos-i)+1)/3,
						0,
						Math.PI*2,
						true)
					contexto.closePath();
					contexto.fill()
			}
			contexto.fillStyle = "rgb("+this.r+","+this.g+","+this.b+")"
			if(i == Math.round(this.numeroelementos/2) || i == Math.round(this.numeroelementos/1.1)){
				// Aleta 1
					contexto.beginPath()
					contexto.ellipse(
						this.x+i*Math.cos(this.a+Math.PI/2)*0.3*this.edad-i*Math.cos(this.a)*1*this.edad+Math.sin(this.a)*Math.sin((i/5)-this.tiempo)*4,
						this.y+i*Math.sin(this.a+Math.PI/2)*0.3*this.edad-i*Math.sin(this.a)*1*this.edad+Math.cos(this.a)*Math.sin((i/5)-this.tiempo)*4,
						(this.edad*0.4*(numeroelementos-i)+1)*2,
						(this.edad*0.4*(numeroelementos-i)+1)*1,
						this.a+Math.PI/2-Math.cos(this.tiempo*2),
						0,
						Math.PI*2,
						true)
					contexto.closePath();
					contexto.fill()
				// Aleta 2
					contexto.beginPath()
					contexto.ellipse(
						this.x-i*Math.cos(this.a+Math.PI/2)*0.3*this.edad-i*Math.cos(this.a)*1*this.edad+Math.sin(this.a)*Math.sin((i/5)-this.tiempo)*4,
						this.y-i*Math.sin(this.a+Math.PI/2)*0.3*this.edad-i*Math.sin(this.a)*1*this.edad+Math.cos(this.a)*Math.sin((i/5)-this.tiempo)*4,
						(this.edad*0.4*(numeroelementos-i)+1)*2,
						(this.edad*0.4*(numeroelementos-i)+1)*1,
						this.a+Math.PI/2+Math.cos(this.tiempo*2),
						0,
						Math.PI*2,
						true)
					contexto.closePath();
					contexto.fill()
			}
			}
			for(var i = -1;i<this.numeroelementos;i++){
			contexto.fillStyle = "rgb("+this.colorr[i]+","+this.colorg[i]+","+this.colorb[i]+")"
			if(i == -1){
			contexto.beginPath()
			contexto.arc(
				this.x-i*Math.cos(this.a)*5*this.edad+Math.sin(this.a)*Math.sin((i/5)-this.tiempo)*4,
				this.y-i*Math.sin(this.a)*5*this.edad+Math.cos(this.a)*Math.sin((i/5)-this.tiempo)*4,
				((this.edad*0.4*(numeroelementos-i)+5)*0.5+((Math.cos(this.tiempo)+1)*3))/3,
				0,
				Math.PI*2,
				true)
			contexto.closePath();
			contexto.fill()
			
			}else{
				contexto.beginPath()
			contexto.arc(
				this.x-i*Math.cos(this.a)*2*this.edad+Math.sin(this.a)*Math.sin((i/5)-this.tiempo)*4,
				this.y-i*Math.sin(this.a)*2*this.edad+Math.cos(this.a)*Math.sin((i/5)-this.tiempo)*4,
				(this.edad*0.4*(numeroelementos-i)+1)/1,
				0,
				Math.PI*2,
				true)
			contexto.closePath();
			contexto.fill()
			}
		}
		contexto.fillStyle = "rgb("+Math.round(this.r/1.5)+","+Math.round(this.g/1.5)+","+Math.round(this.b/1.5)+")"
		for(var i = 0;i<this.numeroelementos;i++){
			
			contexto.beginPath()
			contexto.arc(
				this.x-i*Math.cos(this.a)*2*this.edad+Math.sin(this.a)*Math.sin((i/5)-this.tiempo)*4,
				this.y-i*Math.sin(this.a)*2*this.edad+Math.cos(this.a)*Math.sin((i/5)-this.tiempo)*4,
				(this.edad*0.4*(numeroelementos-i)+1)/3,
				0,
				Math.PI*2,
				true)
			contexto.closePath();
			contexto.fill()
		}
		// Dibujo la aleta de cola
		for(var i = this.numeroelementos;i<this.numeroelementos+this.numeroelementoscola;i++){
			contexto.beginPath()
			contexto.arc(
				this.x-(i-3)*Math.cos(this.a)*2*this.edad+Math.sin(this.a)*Math.sin((i/5)-this.tiempo)*4,
				this.y-(i-3)*Math.sin(this.a)*2*this.edad+Math.cos(this.a)*Math.sin((i/5)-this.tiempo)*4,
				0-this.edad*0.4*(numeroelementos-i)*2+1,
				0,
				Math.PI*2,
				true)
			contexto.closePath();
			contexto.fill()
		}
		
	}
	vive(){
		
		
		if(Math.random() < 0.002){
			this.direcciongiro = 0-this.direcciongiro
		}
		
		if(this.energia > 0){
			this.tiempo += this.avancevida
			
			this.mueve()
		}else{
			//this.y -= 0.1
		}
		
		
		this.energia -= 0.00003
		this.edad += 0.00001
		//console.log(this.edad)
		if(this.edad > 3){
			this.energia = 0
		}
		
		if(this.energia > 0){
			this.dibuja()
		}
	}
	mueve(){
		
		this.x += Math.cos(this.a)*this.avancevida*this.edad*5
		this.y += Math.sin(this.a)*this.avancevida*this.edad*5
		this.a += (Math.random()-0.5)*0.01
		//this.colisiona()
		
	}
	colisiona(){
		
		if(this.x < 0 || this.x > anchura || this.y < 0 || this.y > altura){
			//this.a += Math.PI
			//this.direcciongiro = Math.round(Math.random()*2-1)
		}
		if(this.x < 0){this.x = 40;this.a = 0}
		if(this.y < 0){this.y = 40;this.a = 0+Math.PI/2}
		if(this.x > anchura){this.x = anchura-40;this.a = Math.PI}
		if(this.y > altura){this.y = altura-40;this.a = 0-Math.PI/2}
		if(this.x < 200 || this.x > anchura-200 || this.y < 200 || this.y > altura-200){
			this.a += 0.05*this.direcciongiro
			//console.log(this.direcciongiro)
		}
		
		
	}
	
}