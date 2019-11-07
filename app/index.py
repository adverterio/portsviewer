from flask import Flask, render_template

app = Flask(__name__)

def get_ports_data():
    import subprocess
    p = subprocess.Popen(['netstat', '-ltup'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    console_data = stdout.decode().split('\n')
    formated_data = []
    for line in range(1, len(console_data)):
        newline = console_data[line].split()
        formated_data.append(newline)
    formated_data[0] = ['Proto', 'Recv-Q', 'Send-Q', 'Local Address', 'Foreign Address', 'State', 'PID/Program name']
    return formated_data

@app.route('/')
def index():
    return render_template('index.html', portsdata=get_ports_data())

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')