function sumar(){

var x,y, suma; 

x=parseInt(document.getElementById("n1").value)

y=parseInt( document.getElementById("n2").value)

suma=x+y

document.getElementById("resultado").innerHTML= "la suma es" +suma
}