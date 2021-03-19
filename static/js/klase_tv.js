fetch('/stundas_tv/dati')
  .then(response => response.json())
  .then(data => data.forEach(element =>
    document.querySelector('.stundas').innerHTML += `
        <li>
          
          <span class="stunda">${element.stundasid} ${element.prieksmeti}</span>
          <span class="laiks">${element.laiks}</span>
        </li>
      `
    )
  )
