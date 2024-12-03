from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    # Data e hora final para o cronômetro (31/12/2024 às 23h59)
    deadline = datetime(2024, 12, 31, 23, 59)  
    return render_template('index.html', deadline=deadline)

if __name__ == "__main__":
    app.run(debug=True)
