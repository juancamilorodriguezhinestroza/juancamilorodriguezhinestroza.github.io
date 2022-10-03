var peso,dolar,convercion;

dolar=parseInt(prompt("Escribe una cantidad en dolares"));
peso=parseInt(prompt("Escribe el precio del peso COP"));

convercion=peso*dolar;

document.write("la cantidad de "+dolar+" dolares equivalen a "+convercion+" pesos");
