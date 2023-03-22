from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('cinque_1.html')

@app.route('/data', methods=['POST',"GET"])
def data():
    figura_selezionata = request.form['figure']
    if figura_selezionata == 'cerchio':
        figura = "../static/img/cerchio.png"
    elif figura_selezionata == 'rettangolo':
        figura = "../static/img/rettangolo.png"
    elif figura_selezionata == 'quadrato':
        figura = "../static/img/quadrato.png"
    elif figura_selezionata == 'pentagono':
        figura = "../static/img/pentagono.png"
    return figura

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)