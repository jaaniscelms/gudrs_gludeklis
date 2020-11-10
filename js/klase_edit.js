fetch('/json/klase_edit.json')
  .then(response => response.json())
  .then(data => {
    // Iet cauri katram objekta ierakstam un izveido tabulas virsrakstu un tabulu
    for (const diena in data) {
      document.querySelector('.dienas').innerHTML += `
        <h3>${diena[0].toUpperCase() + diena.slice(1)}</h3>
        <table class="${diena}">
          <thead>
            <tr>
              <th class="nr">Nr.</th>
              <th class="prieksmets">Priekšmets</th>
              <th class="vards">Pasniedzejs</th>
              <th class="laiks">Laiks</th>
              <th class="nenotiek">Nenotiek</th>
              <th>Darbības</th>
            </tr>
          </thead>
          <tbody></tbody>
        </table>
      `

      // Iet cauri katra objekta ieraksta vērtībai(masīvam) un populē attiecīgo tabulu
      data[diena].forEach((element, index) => {
        document.querySelector('.' + diena + ' tbody').innerHTML += `
          <tr>
            <td>${index}</td>
            <td>${element.prieksmets}</td>
            <td>${element.pasniedzejs}</td>
            <td>${element.prielaiksksmets}</td>
            <td><input type="checkbox" ${element.nenotiek}></td>
            <td>
              <div class="buttons">
                <input class="button" type="button" value="Labot">
                <input class="button button_error" type="button" value="Dzēst">
              </div>
            </td>
          </tr>
        `
      })
    }
  })
