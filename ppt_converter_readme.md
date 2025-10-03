# Text to PowerPoint Converter using ChatGPT

A Python-based tool that converts text content into professionally formatted PowerPoint presentations using ChatGPT API.

## Features

- 🤖 AI-powered content structuring using ChatGPT
- 📊 Automatic slide generation with titles and bullet points
- 🎨 Customizable templates and themes
- 📝 Support for multiple input formats (TXT, MD, DOCX)
- 🖼️ Optional image integration
- 📈 Chart and graph generation support

## Sample Output

### Input Text
```
Artificial Intelligence in Healthcare

AI is transforming healthcare delivery. Machine learning algorithms can analyze medical images with high accuracy. Natural language processing helps in processing patient records. Predictive analytics improves patient outcomes. AI-powered chatbots provide 24/7 patient support.

Benefits include faster diagnosis, personalized treatment plans, reduced costs, and improved efficiency. Challenges involve data privacy concerns, integration with existing systems, and the need for regulatory frameworks.
```

### Generated Presentation Structure

**Slide 1: Title Slide**
- Title: "Artificial Intelligence in Healthcare"
- Subtitle: "Transforming Modern Medicine"

**Slide 2: AI Applications in Healthcare**
- Medical Image Analysis
  - High accuracy diagnosis
  - Faster detection of abnormalities
- Natural Language Processing
  - Automated patient record processing
  - Clinical documentation improvement
- Predictive Analytics
  - Patient outcome predictions
  - Risk assessment models

**Slide 3: Key Benefits**
- ⚡ Faster Diagnosis
- 👤 Personalized Treatment Plans
- 💰 Reduced Healthcare Costs
- 📈 Improved Operational Efficiency
- 🤖 24/7 Patient Support via AI Chatbots

**Slide 4: Current Challenges**
- 🔒 Data Privacy and Security Concerns
- 🔄 Integration with Legacy Systems
- ⚖️ Need for Regulatory Frameworks
- 👨‍⚕️ Healthcare Professional Training

**Slide 5: Future Outlook**
- Continued advancement in AI capabilities
- Greater adoption across healthcare facilities
- Enhanced patient care and outcomes

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/text-to-ppt-chatgpt.git

# Navigate to project directory
cd text-to-ppt-chatgpt

# Install required packages
pip install -r requirements.txt
```

## Requirements

```
openai>=1.0.0
python-pptx>=0.6.21
python-dotenv>=1.0.0
markdown>=3.4.0
python-docx>=0.8.11
```

## Configuration

1. Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_api_key_here
```

2. (Optional) Customize settings in `config.py`:
```python
DEFAULT_TEMPLATE = "modern"
MAX_BULLETS_PER_SLIDE = 5
FONT_SIZE_TITLE = 44
FONT_SIZE_BODY = 24
```

## Usage

### Basic Usage

```python
from text_to_ppt import TextToPPTConverter

# Initialize converter
converter = TextToPPTConverter(api_key="your_openai_api_key")

# Convert text file to PowerPoint
converter.convert(
    input_file="input.txt",
    output_file="presentation.pptx"
)
```

### Advanced Usage

```python
# With custom template and options
converter.convert(
    input_file="research_paper.txt",
    output_file="research_presentation.pptx",
    template="professional",
    max_slides=10,
    include_images=True,
    theme_color="blue"
)
```

### Command Line Interface

```bash
# Basic conversion
python main.py --input input.txt --output presentation.pptx

# With options
python main.py --input article.md --output slides.pptx --template modern --max-slides 15
```

## Sample Output Files

This repository includes sample outputs in the `/samples` directory:

- `sample_healthcare_ai.pptx` - Healthcare AI presentation
- `sample_climate_change.pptx` - Climate change presentation
- `sample_business_plan.pptx` - Business plan presentation
- `sample_tech_trends.pptx` - Technology trends presentation

## Project Structure

```
text-to-ppt-chatgpt/
│
├── main.py                 # Main application entry point
├── text_to_ppt.py         # Core converter class
├── chatgpt_processor.py   # ChatGPT API integration
├── slide_generator.py     # PowerPoint slide generation
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
│
├── templates/            # PowerPoint templates
│   ├── modern.pptx
│   ├── professional.pptx
│   └── minimal.pptx
│
├── samples/              # Sample output presentations
│   ├── sample_healthcare_ai.pptx
│   └── input_examples/
│       └── healthcare_ai.txt
│
└── tests/               # Unit tests
    ├── test_converter.py
    └── test_chatgpt.py
```

## How It Works

1. **Text Analysis**: The input text is sent to ChatGPT for analysis
2. **Content Structuring**: ChatGPT organizes content into logical slides
3. **Slide Generation**: Python-pptx creates slides based on the structure
4. **Formatting**: Applies templates and styling to the presentation

## API Usage Example

The tool uses ChatGPT with the following prompt structure:

```python
prompt = f"""
Analyze the following text and create a PowerPoint presentation structure:

{input_text}

Provide the output in the following JSON format:
{{
  "title": "Presentation Title",
  "slides": [
    {{
      "type": "title",
      "title": "Main Title",
      "subtitle": "Subtitle"
    }},
    {{
      "type": "content",
      "title": "Slide Title",
      "bullets": ["Point 1", "Point 2", "Point 3"]
    }}
  ]
}}
"""
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for the ChatGPT API
- python-pptx library for PowerPoint generation
- All contributors and users of this project

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/text-to-ppt-chatgpt](https://github.com/yourusername/text-to-ppt-chatgpt)

## Screenshots

### Input Processing
![Input Processing](screenshots/input_processing.png)

### Generated Slide Example
![Generated Slide](screenshots/sample_slide.png)

### Template Options
![Template Options](screenshots/templates.png)
