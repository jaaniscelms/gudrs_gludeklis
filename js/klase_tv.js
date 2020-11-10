fetch('/json/klase_tv.json')
  .then(response => response.json())
  .then(data => data.forEach(element =>
    document.querySelector('.stundas').innerHTML += `
        <li>
          <span class="stunda">${element.stunda}</span>
          <span class="laiks">${element.laiks}</span>
        </li>
      `
    )
  )
