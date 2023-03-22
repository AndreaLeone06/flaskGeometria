from flask import Flask, request, render_template
import math
app = Flask(__name__)
def aR(a,b):
    return a * b

def dR(a,b):
    return math.sqrt(a**2 + b**2)

@app.route('/')
def home():
    return render_template('tre_1.html')

@app.route('/data', methods=['POST',"GET"])
def data():
    base = float(request.form['base'])
    altezza = float(request.form['altezza'])
    calcolo=request.form['calcolo']
    if calcolo == "area":
        risultato=aR(base,altezza)
    else:
        risultato=dR(base,altezza)
    return render_template('tre_2.html', base=base, altezza=altezza, calcolo=calcolo, risultato=risultato)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)