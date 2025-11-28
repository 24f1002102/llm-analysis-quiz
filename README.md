# LLM Analysis Quiz

## Project Overview
This project implements a Python Flask application to automatically solve quizzes that involve:
- Data sourcing (API, CSV, XLSX, JSON, PDF)
- Data cleaning and transformation
- Analysis (aggregation, filtering, reshaping)
- Visualization (histogram charts in base64)
- LLM-based answering using GPT-5-mini

The app also includes endpoints for:
- Prompt testing for system/user prompts
- Local form submissions

---

## Folder Structure
llm_quiz_24f1002102/
├── app.py  
├── test_api.py  
├── requirements.txt  
├── templates/quiz_template.html  
├── static/sample.csv  
├── downloads/  
└── LICENSE  

---

## Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Install Chrome + ChromeDriver
Install Google Chrome and the matching ChromeDriver in PATH.

Ensure Selenium can launch headless Chrome.

### 3. Add OpenAI API Key
Replace `YOUR_OPENAI_API_KEY` in `app.py` with your OpenAI API key.

### 4. Run Flask App
```bash
python app.py
```

### 5. Test /quiz endpoint
```bash
python test_api.py
```

### 6. Access local quiz form
Open `templates/quiz_template.html` in a browser.

Test local `/submit` endpoint.

---

## Endpoints

### **POST /quiz**
Accepts JSON:
```json
{ "email": "...", "secret": "...", "url": "..." }
```
Solves the quiz dynamically and returns JSON answers & optional plots.

### **POST /submit**
Receives manual submission form inputs.

### **POST /llm_test**
Simulates prompt evaluation for viva testing.

---

## Notes
- Max payload size: **1MB**
- Selenium retries **3 times** per page load
- Automatically solves multi-step quizzes
- Plots sent as **base64 images**

---

## LICENSE (MIT License)

```text
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
