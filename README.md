# News Summarizer

This is a simple web application that summarizes news articles. Users can input a URL, and the app will provide a concise summary using a machine learning model.

## Features

- **News Summarization**: Enter a URL, and the app will summarize the news article.
- **User-friendly Interface**: A clean, responsive design using HTML and CSS.
- **Model**: Uses a custom machine learning model for summarization.

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Machine Learning**: Custom model (see `model.py`)
- **Dependencies**: Listed in `requirements.txt`


## Installation

1. Clone the repository:
   ```bash
   git clone <https://github.com/Sharvani-123/ByteSync>

2. Navigate to the project directory:
   ```bash
   cd news-summarizer
   
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

5. Run the application:
   ```bash
   python app.py
6. Open your browser and go to:
   ```bash
   http://127.0.0.1:5000

## Folder Structure
```bash
news-summarizer/
│
├── app.py                  # Main application file
├── model.py                # Summarization model file
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates
│   └── index.html          # Main HTML file
├── static/                 # Static assets (CSS, images)
│   ├── styles.css          # CSS styles
│   ├── favicon.ico         # Favicon
│   └── news.png            # Placeholder news image
├── venv/                   # Virtual environment folder (ignored in Git)
└── __pycache__/            # Python cache files (ignored in Git)
