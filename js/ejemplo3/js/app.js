var op

        var n1,n2,resultado

op=parseInt( prompt(" escoja una opcion del menu"));


switch (op) {
    case 1:
        n1=parseInt(prompt("dijite un numero"))
        n2=parseInt(prompt("dijite un numero"))
        resultado=n1+n2
        document.write("la suma de : " +n1+ " + " +n2+ "es: "+resultado)
        break;
        case 2:
            n1=parseInt(prompt("dijite un numero"))
            n2=parseInt(prompt("dijite un numero"))
            resultado=n1-n2
            document.write("la resta de : " +n1+ " - " +n2+ "es: "+resultado)
            break; 
            case 3:
                n1=parseInt(prompt("dijite un numero"))
                n2=parseInt(prompt("dijite un numero"))
                resultado=n1*n2
                document.write("la multiplicacion de : " +n1+ " * " +n2+ "es: "+resultado)
            break; 
            case 4:
                
                n1=parseFloat(prompt("dijite un numero"))
                n2=parseFloat(prompt("dijite un numero"))
                resultado=n1/n2
                document.write("la divicion  de : " +n1+ " / " +n2+ "es: "+resultado)
                
            break;
document.write(" escova una opcion valida de este menu")
    default:
        break;
}