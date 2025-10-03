# app.py - Main application file
import os
from flask import Flask, render_template, request, send_file, redirect, url_for
from werkzeug.utils import secure_filename
import tempfile
from text_processor import extract_text_from_file
from presentation_generator import generate_presentation
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    # Check if OpenAI API key is configured
    if not os.environ.get('OPENAI_API_KEY'):
        return render_template('index.html', error="OpenAI API key not configured. Please set the OPENAI_API_KEY environment variable.")
    
    # Get text input method
    input_method = request.form.get('input_method', 'text')
    
    # Process based on input method
    if input_method == 'text':
        text_content = request.form.get('text_content', '')
        if not text_content.strip():
            return render_template('index.html', error="Please enter some text content")
    else:  # File upload
        if 'file' not in request.files:
            return render_template('index.html', error="No file selected")
        
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error="No file selected")
        
        # Save uploaded file to temp directory
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Extract text from file
        try:
            text_content = extract_text_from_file(file_path)
            if not text_content.strip():
                return render_template('index.html', error="Could not extract text from the file")
        except Exception as e:
            return render_template('index.html', error=f"Error processing file: {str(e)}")
        finally:
            # Clean up temp file
            if os.path.exists(file_path):
                os.remove(file_path)
    
    # Get presentation settings
    title = request.form.get('presentation_title', 'Generated Presentation')
    style = request.form.get('presentation_style', 'professional')
    
    # Generate presentation
    try:
        output_file = os.path.join(app.config['UPLOAD_FOLDER'], 'generated_presentation.pptx')
        generate_presentation(text_content, output_file, title, style)
        return send_file(output_file, as_attachment=True, download_name='generated_presentation.pptx')
    except Exception as e:
        return render_template('index.html', error=f"Error generating presentation: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
