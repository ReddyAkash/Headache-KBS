document.getElementById('chatForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Get the symptoms from the textarea, split by comma, and trim extra spaces
    const symptoms = document.getElementById('symptoms').value.split(",").map(symptom => symptom.trim().toLowerCase());

    // Send a POST request to Flask backend
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: symptoms.join(", ") })
    })
    .then(response => response.json())
    .then(data => {
        // Display the response in the 'response' div
        const responseDiv = document.getElementById('response');
        responseDiv.style.display = 'block';
        responseDiv.textContent = data.response;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
