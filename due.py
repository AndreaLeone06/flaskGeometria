from flask import Flask, request, render_template
app = Flask(__name__)
def aR(a,b):
    return a * b

@app.route('/')
def home():
    return render_template('due_1.html')

@app.route('/data', methods=['POST',"GET"])
def data():
    if request.args.get('base').isdigit() and request.args.get('altezza').isdigit():
        base = float(request.args.get('base'))
        altezza = float(request.args.get('altezza'))
        areaRett = aR(base,altezza)
        return render_template('due_2.html', base=base, altezza=altezza, areaRett=areaRett)
    else:
        return "inserisci delle cifre valide"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)