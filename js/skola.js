//Iegūstam datus no API 
async function iegutSkolotajuDatusNoApi()
{
    let datiNoApi = await fetch('json/skola.json')
    let datiJson = await datiNoApi.json();
    return datiJson;
}
//Datu izvadīšana
async function izvaditDatus()
{
    let tableMainPart = "";
    let teachersTable = "";
    //Tabulas augšdaļa.
    let tableUpPart = `
    <h2>Pasniedzēji</h2>
    <table>
      <thead>
        <tr>
          <th class="vards">Vārds, uzvārds</th>
          <th class="epasts">E-pasts</th>
          <th class="tel">Tel. nr.</th>
          <th class="prieksmets">Priekšmets</th>
          <th>Darbības</th>
        </tr>
      </thead>
      <tbody>`;
      //Tabulas apakšdaļa.
      let tableEndPart = `
      </tbody>
          </table>
          <input class="button" type="button" id="pievieno" value="Pievienot pasniedzēju" onclick="pievienotTeacher()">`;  
    let teachersList = await iegutSkolotajuDatusNoApi();
    for (let index = 0; index < teachersList["pasniedzeji"].length; index++) 
    {
      tableMainPart += `
      <tr>
      <td class="vards">`+ teachersList["pasniedzeji"][index].vards +" "+ teachersList["pasniedzeji"][index].uzvards + `</td>
      <td class="epasts">`+ teachersList["pasniedzeji"][index].epasts +`</td>
      <td class="tel">`+ teachersList["pasniedzeji"][index].tel_num +`</td>
      <td class="prieksmets">`+ teachersList["pasniedzeji"][index].prieksmets +`</td>
      <td>
        <div class="buttons">
          <input class="button" type="button" value="Labot">
          <input class="button button_error" type="button" value="Dzēst">
        </div>
      </td>
      </tr>`         
    }
    teachersTable = tableUpPart.concat(tableMainPart,tableEndPart);
    document.getElementById("teachers").innerHTML = teachersTable;      
}
izvaditDatus();

//Cita pierakstīts kods
/*document.getElementById('pievieno').addEventListener('click', */
function pievienotTeacher(){
  const table_body = document.querySelector(".teachers tbody");
  var rinda = document.createElement("tr");
  rinda.innerHTML = `
    <td><input type="text" placeholder="Vārds, uzvārds"></td>
    <td><input type="text" placeholder="E-pasts"></td>
    <td><input type="text" placeholder="Tel. nr."></td>
    <td><input type="text" placeholder="Priekšmets"></td>
    <td>
      <div class="buttons">
        <input class="button save" type="button" value="Saglabāt">
      </div>
    </td>
  `;
  table_body.appendChild(rinda);
  rinda.classList.add('row_edit')

  document.querySelectorAll(".save").forEach(function(currentIndex){
    currentIndex.onclick = function(){
      for(i=0;i<4;i++){
        var cells = this.closest('tr').children[i]
        cells.innerHTML = cells.querySelector('input').value
      }

      this.closest('tr').classList.remove('row_edit')

      this.parentElement.innerHTML = `
        <input class="button" type="button" value="Labot">
        <input class="button button_error" type="button" value="Dzēst">
      `;
    }
  })
};
