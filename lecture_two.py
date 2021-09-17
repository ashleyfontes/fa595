from flask import Flask
app = Flask(__name__) # "__main__"


@app.route('/hello', methods=['GET']) # the @ is called a decorator, methods is a list, GET is a curl call (used to make an http call), 
                                      # /hello has something to do with the url 
def hello_world():
  return "Hello world."

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
  
