fetch('/klasesdati/dati')
  .then(response => response.json())
  .then(data => data.forEach(element =>
    document.querySelector('.school_classes tbody').innerHTML += `
      <tr>
        <td>${element.klase}</td>
        <td>${element.vards} ${element.uzvards}</td>
        <td>
          <div class="buttons">
            <input class="button" type="button" value="Labot">
            <input class="button button_error" type="button" value="Dzēst">
          </div>
        </td>
      </tr>`
    )
  )