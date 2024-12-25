async function getVisitors() {
    const response = await fetch('/visitors', {
        method:
            'GET'
    })
    const data = await response.json()

    visitorElement = document.getElementById("visitor-element");
    visitorElement.innerHTML = data.total;
}