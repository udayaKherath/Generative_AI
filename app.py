from flask import Flask, request, jsonify, render_template, session
from flask_session import Session
import google.generativeai as genai
from PIL import Image
import io
import base64
import os

app = Flask(__name__)

# Set secret key and session type
app.config['SECRET_KEY'] = os.urandom(24)  # or use a specific strong password
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# API key setup
api_key = "AIzaSyBR6kjF1Uy5ayVywZg2LTRBnencS2-ZzYw"
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-pro")

def get_gemini_response(input_text, image, prompt):
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file:
        bytes_data = uploaded_file.read()
        image_parts = [{'mime_type': uploaded_file.content_type, 'data': bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    try:
        image_data = input_image_details(file)
        input_prompt = """
        You are an expert in analyzing and explaining insights from visuals. 
        We will upload an image, and you will provide a detailed analysis of the key insights and 
        information that can be derived from that image. Please include any relevant 
        details such as patterns, trends, anomalies, context, and any other noteworthy observations. Always, carefully
        look at the legends.
        """
        response = get_gemini_response(input_prompt, image_data, "")
        
        # Convert image to base64 to display in HTML
        image = Image.open(io.BytesIO(image_data[0]['data']))
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        session['image_data'] = img_str  # Store image data in session
        session['conversation'] = []     # Initialize conversation history in session
        
        return jsonify({'response': response, 'image': img_str})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')
    image_data = session.get('image_data')
    
    if not question or not image_data:
        return jsonify({'error': 'Question or image data missing'}), 400
    
    try:
        image_parts = [{'mime_type': 'image/png', 'data': base64.b64decode(image_data)}]
        response = get_gemini_response(question, image_parts, "")
        
        # Update conversation history in session
        conversation = session.get('conversation', [])
        conversation.append({'question': question, 'response': response})
        session['conversation'] = conversation
        
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
