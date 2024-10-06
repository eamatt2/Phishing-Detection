document.getElementById('uploadForm').addEventListener('submitImg', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const statusText = document.getElementById('status');
    statusText.innerText = 'Waiting for processing';

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response = response.json())
    .then(data => {
        if (data.error) {
            statusText.innerText = data.error; // Show the error message
        } else {
            return fetch(`/result/${data.filename}`);
        }
    })
    .then(data => {
        if (data && data.error) {
            document.getElementById('result').innerText = "Error: " + data.error;
        } else {
            // Update the result with the processed output
            document.getElementById('result').innerText = data.result;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = "Error processing the request.";
    });
});