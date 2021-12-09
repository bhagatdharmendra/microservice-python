from flask import Flask, jsonify,render_template
import socket

app=Flask(__name__)
@app.route("/")
def hello_world():
    return "<p> Hello, World!</p>"
@app.route("/about")
def about():
    return jsonify(
        status="up"
    )
def fetchDetails():
     host_name = socket.gethostname()
     host_ip = socket.gethostbyname(host_name)
     return str(host_name), str(host_ip)
@app.route("/sysinfo")
def sysinfo():
    host_name, host_ip =fetchDetails()
    return render_template("index.html",hostname=host_name, ip=host_ip)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)