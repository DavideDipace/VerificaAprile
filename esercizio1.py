from flask import Flask, render_template, request

app = Flask(__name__)

import pandas as pd

df = pd.read_excel('https://github.com/PolisenoRiccardo/perilPopolo/blob/main/milano_housing_02_2_23.xlsx?raw=true')

@app.route('/')
def home():
  return render_template('esercizio1.html')

@app.route('/es1', methods = ['GET'])
def es1():
    nome = request.args.get('nome')
    Quartiere = df[df['neighborhood'] == nome]
    Quartiere.sort_values("date")
    return render_template('esercizio1.html', risultato = df)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)