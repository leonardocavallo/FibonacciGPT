document.addEventListener('DOMContentLoaded', function() {
    const loadingDiv = document.getElementById('loading-div');
    const sendButton = document.getElementById('send-button');
    const promptInput = document.getElementById('prompt-input');
    const responseContainer = document.getElementById('response-div');
    const promptText = document.getElementById('prompt-text');
    const responseText = document.getElementById('response-text');

    sendButton.addEventListener('click', function() {
        const prompt = promptInput.value.trim();

        if (!prompt) {
            alert('Il prompt non può essere vuoto o contenere solo spazi.');
            return;
        }
        loadingDiv.style.display = 'block';
        const headers = {
            'Content-Type': 'application/json',
            'chiavesupersegreta': 'malig'
        };
        const body = JSON.stringify({ prompt: prompt });

        fetch('/api/ai-response', {
            method: 'POST',
            headers: headers,
            body: body
        })
        .then(response => response.json())
        .then(data => {
            loadingDiv.style.display = 'none';
            promptText.innerText = prompt;
            responseText.innerText = data.response;
            responseContainer.style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
    });

    document.querySelector("#prompt-input").addEventListener("keyup", event => {
        if(event.key == "Enter") {
            document.querySelector("#send-button").click(); // Things you want to do.
            event.preventDefault(); // No need to `return false;`.
        }; 
    });

});