from flask import Flask, request, render_template
app = Flask(__name__)
def aR(a,b):
    return a * b

@app.route('/')
def home():
    return render_template('uno_1.html')

@app.route('/data', methods=['POST',"GET"])
def data():
    base = float(request.form['base'])
    altezza = float(request.form['altezza'])
    areaRett = aR(base,altezza)
    return render_template('uno_2.html', base=base, altezza=altezza, areaRett=areaRett)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)