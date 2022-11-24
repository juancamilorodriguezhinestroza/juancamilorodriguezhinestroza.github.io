function  sumar(){
    var x,y ,suma;

    x=document.getElementById("n1").value
    y=document.getElementById("n1").value 
    suma=parseInt(x)+parseInt(y)
    document.getElementById("resultado_suma").innerHTML="la suma es "+suma
}function  resta(){
    var x,y,resta;

    x=document.getElementById("n1").value
    y=document.getElementById("n1").value 
    resta=parseInt(x)-parseInt(y)
    document.getElementById("resultado_resta").innerHTML="la resta es "+resta

}function  multiplicasion(){
    var x,y,multiplicasion;

    x=document.getElementById("n1").value
    y=document.getElementById("n1").value 
    multiplicasion=parseInt(x)*parseInt(y)
    document.getElementById("resultado_multiplicacion").innerHTML="la multiplicasion es "+multiplicasion
}function  division(){
    var x,y,division;

    x=document.getElementById("n1").value
    y=document.getElementById("n1").value 
    division=parseFloat(x)/parseFloat(y)
    document.getElementById("resultado_division").innerHTML="la division es "+division

}
