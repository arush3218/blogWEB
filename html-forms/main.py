from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', method = ['POST'])
def recieve_data():
        username = request.form['username']
        password = request.form['password']
        return f"<h1>Name: {username}, Password: {password}</h1>"
    
@app.route('/form-entry', method = ['GET'])
def recieve_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Successfully sent your message</h1>"
    


if __name__ == "__main__":
    app.run(debug=True)