from flask import Flask, render_template

app = Flask(__name__)

def get_ports_data():
    import subprocess
    p = subprocess.Popen(['netstat', '-ltup'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    data1 = stdout.decode().split('\n')
    data2 = []
    for line in range(1, len(data1)):
        newline = data1[line].split()
        data2.append(newline)
        data2[0] = ['Proto', 'Recv-Q', 'Send-Q', 'Local Address', 'Foreign Address', 'State', 'PID/Program name']
    return data2

@app.route('/')
def index():
    return render_template('index.html', portsdata=get_ports_data())

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')