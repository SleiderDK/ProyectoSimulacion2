function Generar(){
    cantidad = parseInt(document.getElementById("num_muestra").value);
    ingreso="";

    for(i=1; i<=cantidad; i++){
        
        ingreso += `<input type="number" class="btn btn-sec m-4 col-md-5" step="0.01" name="input`+i+`" class="form-control" id="alfa" placeholder="Dato #`+i+`" required>`;
        
    }                
    document.getElementById("inputs_generados").innerHTML = ingreso;
}

function GenerarDoble(){
    cantidad = parseInt(document.getElementById("num_muestra").value);
    ingreso="";

    for(i=1; i<=cantidad; i++){
        
        ingreso += `<div class="input-group">
                    <input type="number" class="form-control" step="0.01" name="inputX`+i+`" class="form-control" id="alfa" placeholder="Dato X`+i+`" required>
                    <input type="number" class="form-control" step="0.01" name="inputY`+i+`" class="form-control" id="alfa" placeholder="Dato Y`+i+`" required>
                    </div>`;
        
    }                
    document.getElementById("inputs_generados").innerHTML = ingreso;
}