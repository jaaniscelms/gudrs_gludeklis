let rinda=[];
rinda[1]= document.querySelector('.pirmdiena');
rinda[2]= document.querySelector('.otrdiena');
rinda[3]= document.querySelector('.tresdiena');
rinda[4]= document.querySelector('.ceturtdiena');
rinda[5]= document.querySelector('.piektdiena');
async function iegutDatus()
{
    let datiNoApi = await fetch('http://janiscelms.com/gudrs_gludeklis/json/klase_edit.json')
    let datiJson = await datiNoApi.json();
    return datiJson;
}
async function raditDatus()
{
    
    let stundasJson = await iegutDatus();
    for (let i = 0; i < stundasJson["stundas"].length; i++) 
    {
     rinda[stundasJson["stundas"][i].diena].innerHTML+=`
        <tr>
        <td>`+stundasJson["stundas"][i].nr+`</td>
        <td>`+stundasJson["stundas"][i].prieksmets+`</td>
        <td>`+stundasJson["stundas"][i].pasniedzejs+`</td>
        <td>`+stundasJson["stundas"][i].laiks+`</td>
        <td><input type="checkbox"`+stundasJson["stundas"][i].nenotiek+`></td>
        <td>
        <div class="buttons">
          <input class="button" type="button" value="Labot">
          <input class="button button_error" type="button" value="Dzēst">
        </div>
        <td>
        </tr>
        `;
    }
}
raditDatus();