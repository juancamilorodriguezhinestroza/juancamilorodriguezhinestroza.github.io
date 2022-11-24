var edad

edad=parseFloat(prompt("ingrese su edad"))

if (edad<=19 &&edad>=17) {
    document.write("usted es mayor de edad con " +edad+"años")
} else {
    document.write("usted no es mayor de edad con " +edad+"años")
}