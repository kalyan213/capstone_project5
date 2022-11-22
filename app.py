from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
	       <h1 style='color: red;'>Capstone Project</h1>
	       <h1 style='color: red;'>.................</h1>
	       <p>This is initial version of capstone project V2<p>
           <p>Author by Kalyan</p>
           """
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)