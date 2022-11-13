class Mueble{
  constructor(nombre, material,precio){
    this.nombre= nombre;
    this.material = material;
    this.categoria = categoria;
    this.precio = precio;
  }

  getDatosBasicos(){
    return(this.nombre+" "+this.precio);
  }
  getDatos(){
    return("Este mueble es: "+this.nombre+" "+" su material es: "+this.material+" "+"y su precio es: "+this.precio);
  }
}

class Persona{
 constructor(nombre,apellido,correo,contraseña){
 this.nombre= nombre;
 this.apellido= apellido;
 this.correo= correo;
 this.contraseña= contraseña;
}
getusuario(){
  return("su usuario es "+this.correo+ "su contraseña es "+this.contraseña);
}


var Mueble= new Mueble(Zafiro, Roble, 700.000);
datos.innerHTML += Muebles.getDatos(); 


var texto = "Holi, buena suerte";
ver datos = document.getElementById("datos");
datos.innerHTML += texto+n\