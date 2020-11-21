const onlyUnique = (value: string, index: number, self: string[]) => {
  return self.indexOf(value) === index
}

const getUniqueAreasFromTemplateArea = (element: Element) => {
  const ta = getComputedStyle(element).gridTemplateAreas
  const areaArray = ta
    .replace(/("|\.)/g, '')
    .replace(/\s+/g, ' ')
    .split(' ')
  return areaArray.filter(onlyUnique)
}

const showUsedElements = () => {
  const container = document.querySelector('.container')
  const uniqueAreas = getUniqueAreasFromTemplateArea(container)
  console.log(uniqueAreas)
  for (const area of uniqueAreas) {
    const usedArea = document.querySelector(`.${area}`)
    if (usedArea) {
      usedArea.classList.remove('hidden')
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  let base_url = '.'
  const devPortHelperDiv = document.querySelector('div[data-dev-port]')
  if (devPortHelperDiv) {
    base_url = `http://localhost:${devPortHelperDiv.getAttribute(
      'data-dev-port'
    )}`
  }
  showUsedElements()
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
