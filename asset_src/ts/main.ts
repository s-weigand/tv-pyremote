document.addEventListener('DOMContentLoaded', () => {
  let base_url = '.'
  const devPortHelperDiv = document.querySelector('div[data-dev-port]')
  if (devPortHelperDiv !== undefined && devPortHelperDiv !== null) {
    base_url = `http://localhost:${devPortHelperDiv.getAttribute(
      'data-dev-port'
    )}`
  }
  const callApiRole = (role: string) => {
    console.log('clicked element with role', role)

    fetch(`${base_url}/api/v1/role/${role}`)
      .then((response) => response.json())
      .then((data) => console.log(data))
  }
  for (const anchor of document.querySelectorAll('a[data-role]')) {
    const role = anchor.getAttribute('data-role')
    anchor.addEventListener('click', (ev: MouseEvent) => {
      callApiRole(role)
    })
  }
})
