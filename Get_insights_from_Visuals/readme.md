# AI Image Analysis

This project is a web application that allows users to upload an image and ask questions about it using an AI model. The application analyzes the image and provides insights based on user queries.

## Project Structure
![Figure 2](https://raw.githubusercontent.com/udayaKherath/Generative_AI/edit/main/Get_insights_from_Visuals/ps.png)




## Setup and Installation

### Prerequisites

- Python 3.12
- Flask
- PIL (Python Imaging Library)
- Google Generative AI API

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/ai-image-analysis.git
    cd ai-image-analysis
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the Google Generative AI API key:**

    Replace `'your_secret_key'` in `app.py` with your actual API key.

5. **Run the Flask application:**

    ```sh
    python app.py
    ```

6. **Open your browser and go to:**

    ```
    http://127.0.0.1:5000/
    ```

## Project Files

### app.py

This is the main server-side script that handles the Flask routes for uploading images and asking questions.

### templates/index.html

The main HTML file for the application. It contains the structure of the web page including file input, upload button, and question input.

### static/styles.css

The CSS file for styling the HTML elements. It includes styles for buttons, containers, and heading alignment.

### static/scripts.js

The JavaScript file that handles the client-side logic such as image upload, displaying the image, and sending questions to the server.

## Usage

1. **Upload an Image:**

    - Click the "Choose File" button to select an image file.
    - Click the "Upload" button to upload the image.

2. **Ask a Question:**

    - After uploading the image, a text input will appear.
    - Enter your question about the image in the text input.
    - Click the "Ask" button to get the AI's response.

3. **View Response:**

    - The AI's response will be displayed below the image.

## Customization

- **Change Button Colors:**
  
  Modify the CSS classes `.btn`, `.btn-upload`, and `.btn-ask` in `static/styles.css` to change the button colors.

- **Change Heading Color:**
  
  Modify the `color` property in the `h1` selector in `static/styles.css`.


