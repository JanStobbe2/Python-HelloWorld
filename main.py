from flask import Flask
app = Flsk(__name__)

@app.route('/')
def hello_world():
 return 'Hello, World'
 
 if __name == '__main__':
 app.run()
 
