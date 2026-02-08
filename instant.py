from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from main import generateSubject

app = FastAPI()

# Your notebook logic here (e.g., loading a model)
# model = load_my_model()

class EmailRequest(BaseModel):
    email: str

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <body style="font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px;">
        <h1>Email Subject Generator</h1>
        <textarea id="email" style="width: 100%; height: 150px; padding: 10px;" 
                  placeholder="Paste your email here..."></textarea>
        <br><br>
        <button onclick="generate()" style="padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer;">
            Generate Subject
        </button>
        <div id="result" style="margin-top: 20px; padding: 15px; background: #f0f0f0; display: none;"></div>
        
        <script>
            async function generate() {
                const email = document.getElementById('email').value;
                const result = document.getElementById('result');
                
                result.innerHTML = 'Generating...';
                result.style.display = 'block';
                
                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({email: email})
                });
                
                const data = await response.json();
                result.innerHTML = '<strong>Subject:</strong> ' + data.result;
            }
        </script>
    </body>
    </html>
    """

@app.post("/predict")
def predict(request: EmailRequest):
    result = generateSubject(request.email)
    return {"result": result}