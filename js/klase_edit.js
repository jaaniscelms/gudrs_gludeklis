let rinda=[];
rinda[0]= document.querySelector('.pirmdiena');
rinda[1]= document.querySelector('.otrdiena');
rinda[2]= document.querySelector('.tresdiena');
rinda[3]= document.querySelector('.ceturtdiena');
rinda[4]= document.querySelector('.piektdiena');
let elements=["pirmdiena","otrdiena","tresdiena","ceturtdiena","piektdiena"]
async function iegutDatus()
{
    let datiNoApi = await fetch('/json/klase_edit.json')
    let datiJson = await datiNoApi.json();
    return datiJson;
}
async function raditDatus()
{
    let stundasJson = await iegutDatus();
    for (let k=0; k<5;k++)
    {
        for (let i = 0; i < stundasJson[elements[k]].length; i++) 
        {
        rinda[k].innerHTML+=`
            <tr>
            <td>`+stundasJson[elements[k]][i].nr+`</td>
            <td>`+stundasJson[elements[k]][i].prieksmets+`</td>
            <td>`+stundasJson[elements[k]][i].pasniedzejs+`</td>
            <td>`+stundasJson[elements[k]][i].laiks+`</td>
            <td><input type="checkbox"`+stundasJson[elements[k]][i].nenotiek+`></td>
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
}
raditDatus();