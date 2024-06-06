function uploadImage() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Please select an image file first.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const responseContainer = document.getElementById('responseContainer');
        const imageContainer = document.getElementById('imageContainer');
        const askSection = document.getElementById('askSection');

        if (data.error) {
            responseContainer.innerText = 'Error: ' + data.error;
            responseContainer.style.color = 'red';
        } else {
            responseContainer.innerText = data.response;
            responseContainer.style.color = 'black';

            // Display the uploaded image
            imageContainer.innerHTML = `<img src="data:image/png;base64,${data.image}" alt="Uploaded Image" style="max-width:100%;"/>`;

            // Store the image data in a hidden input for further questions
            const hiddenInput = document.createElement('input');
            hiddenInput.type = 'hidden';
            hiddenInput.id = 'imageData';
            hiddenInput.value = data.image;
            askSection.appendChild(hiddenInput);

            askSection.style.display = 'block';
        }
    })
    .catch(error => {
        alert('Error: ' + error);
    });
}

function askQuestion() {
    const questionInput = document.getElementById('questionInput');
    const imageData = document.getElementById('imageData').value;
    const question = questionInput.value;
    
    if (!question) {
        alert('Please enter a question.');
        return;
    }

    const payload = {
        question: question,
        image_data: imageData
    };

    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        const responseContainer = document.getElementById('responseContainer');
        
        if (data.error) {
            responseContainer.innerText = 'Error: ' + data.error;
            responseContainer.style.color = 'red';
        } else {
            responseContainer.innerText = data.response;
            responseContainer.style.color = 'black';
        }
    })
    .catch(error => {
        alert('Error: ' + error);
    });
}
