from app import application

@app.route('/')
def index():
    return 'Hello World!'
