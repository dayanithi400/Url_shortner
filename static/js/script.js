document.getElementById('url-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const originalUrl = document.getElementById('original-url').value;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ original_url: originalUrl })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `<a href="${data.short_url}" target="_blank">${data.short_url}</a>`;
    });
});
