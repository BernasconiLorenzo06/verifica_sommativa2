from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')



@app.route('/esercizio1',methods = ["GET"])
def esercizio1():
   import pandas as pd
   df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name = "customers")
   nome = request.args.get('nome')
   cognome = request.args.get('cognome')
   table = df[(df["first_name"] == nome) & (df["last_name"] == cognome)]
   tabella = table.to_html()
   return render_template('esercizio1.html', tabella = tabella)

@app.route('/esercizio2',methods = ["GET"])
def esercizio2():
   import pandas as pd
   df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name = "customers")
   citta = request.args.get('citta')
   table = df[df["city"] == citta]
   tabella = table.to_html()
   return render_template('esercizio2.html', tabella = tabella)



@app.route('/esercizio3',methods = ["GET"])
def esercizio3():
   import pandas as pd
   df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name = "customers")
   table = df.groupby("state")[["first_name"]].count().reset_index()
   tabella = table.to_html()
   return render_template('esercizio3.html', tabella = tabella)


@app.route('/esercizio4',methods = ["GET"])
def esercizio4():
   import pandas as pd
   df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name = "customers")
   df_clienti = df.groupby("state")[["first_name"]].count().reset_index()
   table = df_clienti[df_clienti["first_name"] == df_clienti["first_name"].max()][["state"]]
   tabella = table.to_html()
   return render_template('esercizio4.html', tabella = tabella)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)