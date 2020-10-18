const add = document.getElementById('pievieno');
add.addEventListener('click', function() {
    
    var tabula = document.getElementById("pasniedzejs"); 
    var rinda = document.createElement("tr");
    rinda.innerHTML = `
       <td><input id="dati0" class ="dati" type="text"></td>
       <td><input id="dati1" class ="dati" type="text"></td>
       <td><input id="dati2"class ="dati" type="text"></td>
       <td><input id="dati3"class ="dati" type="text"></td>
       <td><input class="button" onclick="save()" type="button" value="Saglabāt" ></td>
    `;            
    tabula.appendChild(rinda);    
});

function save(){
    var tabula = document.getElementById("pasniedzejs"); 
    var rinda = tabula.rows[ tabula.rows.length - 1 ];
    for(i=0;i<4;i++){
         rinda.cells[i].innerHTML=document.getElementById("dati"+i).value;
    }
    rinda.cells[4].innerHTML = `
        <div class="buttons">
        <input class="button" type="button" value="Labot">
        <input class="button button_error" type="button" value="Dzēst">
        </div>
        `; 
    
}
