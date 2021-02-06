function validarListasIguales(){

    var listaX = document.getElementById("TiempoDeLlegada").value;
    var listaY = document.getElementById("Probabilidad_Tiempo").value;

    liX = listaX.split(",");
    liY = listaY.split(",");
    
    if (liX.length != liY.length){
        alert("el numero de datos ingresados tiene que ser igual para ambas listas\n TiempoDeLlegada tiene: "+liX.length+" datos\n Probabilidad_Tiempo tiene: "+liY.length+" datos")
    } 

    var listaX2 = document.getElementById("TiempoDeServicio").value;
    var listaY2 = document.getElementById("Probabilidad_Servicio").value;

    liX2 = listaX2.split(",");
    liY2 = listaY2.split(",");
    
    if (liX2.length != liY2.length){
        alert("el numero de datos ingresados tiene que ser igual para ambas listas\n TiempoDeServicio tiene: "+liX2.length+" datos\n Probabilidad_Servicio tiene: "+liY2.length+" datos")
    }
}

function validacionPuntos(li_String){
    li_String
    i=0
    while (li_String.length < i){
        cadena = li_String[i]
        if (cadena[i].toLowerCase() === ".") indices.push(i);
        i++
    }
    return indices.length;     
}

function validateMyForm(){

   var listaX = document.getElementById("TiempoDeLlegada").value;
   var listaY = document.getElementById("Probabilidad_Tiempo").value;

   liX = listaX.split(",");
   liY = listaY.split(",");
  

   var listaX2 = document.getElementById("TiempoDeServicio").value;
   var listaY2 = document.getElementById("Probabilidad_Servicio").value;

    liX2 = listaX2.split(",");
    liY2 = listaY2.split(",");
    

   if (liX.length != liY.length || liX2.length != liY2.length){
        return false;
   }else {
        return true;
   }
}
