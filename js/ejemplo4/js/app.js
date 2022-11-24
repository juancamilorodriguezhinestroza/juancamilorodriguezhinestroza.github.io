
var peso,estatura,imc

peso=parseFloat(prompt("Digite el peso en kg:"))

estatura=parseFloat(prompt("Digite la estatura"))

imc=peso/(estatura*estatura)

if (imc<18.5) {
    document.write("bajo de peso")

    
}else if( imc>=18.5 && imc<=29.9){
    document.write("peso normal")

}else if( imc>=25 && imc<=29.9){
    document.write("sobre peso")
}else if( imc>=30 && imc<=39.9){
    document("obesidad 1")
}else if( imc>=40 && imc<=49.9){
    document.write("obesidad 2")

}else if( imc>=50 && imc<=69.9){
    document.write("obesidad 3")

} else{
    document.write("gracias por participar señor usuario")
}
