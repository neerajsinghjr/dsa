from flask import Flask

app = Flask(__name__)


@app.route('/about')
def about():
    return "ABOUT PAGE"

@app.route('/')
def home():
    return "HOME PAGE"

def contact():
    return "CONTACT PAGE"

def project_v3():
    return "Project V3"

def project_v2():
    return "Project V2"

def project_v1():
    return "Project V1"

def main(name):
    print(">>>>> user-type: ", type)
    return "Hello World"
    # if type == 'project1':
    #     print(">>>>>>")
    # elif type == 'project2':
    #     print(">>>>>>")
    # elif type == 'project3':
    #     print(">>>>>>")

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = 5050
    debug = True
    app.run(
        host=ip,
        port=port,
        debug=True
    )
