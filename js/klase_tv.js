fetch('/json/klase_tv.json')
  .then(response => response.json())
  .then(data => data.forEach(element =>
    document.querySelector('.stundas').innerHTML += `
      <ul>
        <li>${element.stunda}</li>
        <li>${element.laiks}</li>
        <li>${element.nenotiek}</li>
        <li>${element.patreiz_notiek}</li>
      </ul>`
    )
  )


