// Aizpilda teachers tbody ar skola.json skolotaju datiem
fetch('/json/skola.json')
  .then(response => response.json())
  .then(data => data.forEach(element => {
      let tr = document.createElement("tr");

      tr.innerHTML = `
        <td>${element.vards} ${element.uzvards}</td>
        <td>${element.epasts}</td>
        <td>${element.tel_num}</td>
        <td>${element.prieksmets}</td>
        <td>
          <div class="buttons">
            <input class="button" type="button" value="Labot">
            <input class="button button_error" type="button" value="Dzēst">
          </div>
        </td>
      `

      document.querySelector('.teachers tbody').appendChild(tr)
    })
  )

// Pievienot pasniedzeju
document.getElementById('pievieno').addEventListener('click', function(){
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
});
