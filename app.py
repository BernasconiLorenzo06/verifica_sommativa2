from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    import pandas as pd
    df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name = "customers")
    c = list(set(df["city"]))
    c.sort()
    return render_template('home.html', lista = c)



@app.route('/esercizio1',methods = ["GET"])
def esercizio1():
   import pandas as pd
   df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name = "customers")
   nome = request.args.get('nome')
   cognome = request.args.get('cognome')
   table = df[(df["first_name"] == nome) & (df["last_name"] == cognome)]
   tabella = table.to_html()
   return render_template('esercizio1.html', tabella = tabella)

@app.route('/esercizio2/<citti>',methods = ["GET"])
def esercizio2(citti):
   import pandas as pd
   df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name = "customers")
   table = df[df["city"] == citti]
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


@app.route('/esercizio5')
def esercizio5():
    import pandas as pd
    import matplotlib.pyplot as plt
    import os 
    df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name = "customers")
    df_clienti = df.groupby("state")[["first_name"]].count().reset_index()
    labels = df_clienti['state']
    dati = df_clienti['first_name'] 
    #primo grafico
    fig, ax = plt.subplots(figsize=(10,8))
    ax.bar(labels, dati, label='totale vaccinati in ogni regione')
    dir = "static/images"
    file_name = "graf.png"
    save_path = os.path.join(dir, file_name)
    plt.savefig(save_path, dpi = 100)
    #secondo grafico
    labels = df_clienti['state']
    dati = df_clienti['first_name'] 
    fig, ax = plt.subplots(figsize=(15,8))
    ax.barh(labels, dati, label='totale vaccinati in ogni regione')
    dir = "static/images"
    file_name = "graf2.png"
    save_path = os.path.join(dir, file_name)
    plt.savefig(save_path, dpi = 100)
    #terzo grafico
    labels = df_clienti['state']
    dati = df_clienti['first_name'] 
    plt.figure(figsize=(16, 8))
    plt.pie(dati, labels=labels, autopct='%1.1f%%')
    plt.show()
    dir = "static/images"
    file_name = "graf3.png"
    save_path = os.path.join(dir, file_name)
    plt.savefig(save_path, dpi = 100)
    return render_template('grafici.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)