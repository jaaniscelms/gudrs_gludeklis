fetch('/json/klase_tv.json')
  .then(response => response.json())
  .then(data => data.forEach(element =>
    document.querySelector('.stundas tbody').innerHTML += `
      <tr>
        <td>${element.stunda}</td>
        <td>${element.laiks}</td>
      </tr>`
    )
  )

document.getElementById('pievieno').addEventListener('click', function(){
  const table_body = document.querySelector(".stundas tbody");
  var rinda = document.createElement("tr");
  rinda.innerHTML = `
    <td><input type="text" placeholder="Stunda"></td>
    <td><input type="text" placeholder="Laiks"></td>
  `;
  table_body.appendChild(rinda);
  rinda.classList.add('row_edit')

  document.querySelectorAll(".save").forEach(function(currentIndex){
    currentIndex.onclick = function(){
      for(i=0;i<8;i++){
        var cells = this.closest('tr').children[i]
        cells.innerHTML = cells.querySelector('input').value
      }
    }
  })
});
