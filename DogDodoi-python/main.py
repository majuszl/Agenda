from flask import Flask, render_template, request
app = Flask(__name__) #instacia flask no aplicativo

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/calcula_idade', methods=['GET', 'POST'])
def calcula_idade():
  if request.method == 'POST':
    calculo = 0

    especie = request.form['especie']
    idade = request.form['idade']

    if especie == 'C':
      if idade == 1:
        mensagem = ('A idade dele é de 15 anos humanos (;')
      elif idade == 2:
        mensagem = ('A idade dele é de 24 anos humanos (;')
      elif idade == 3:
        mensagem = ('A idade dele é de 28 anos humanos (;')
      elif idade == 4:
        mensagem = ('A idade dele é de 32 anos humanos (;')
      elif idade == 5:
        mensagem = ('A idade dele é de 36 anos humanos (;')
      elif idade == 6:
        mensagem = ('A idade dele é de 40 anos humanos (;')
      elif idade == 7:
        mensagem = ('A idade dele é de 44 anos humanos (;')
      elif idade > 7:
        calculo = 44 + ((idade - 7) * 5)
        mensagem = (f'A idade dele é de {calculo}')


      if especie == "G":
        if idade == 1:
          mensagem = ("Seu gato tem 15 anos humano.")
        elif idade == 2:
         mensagem = ("Seu gato tem 24 anos humano.")
        elif idade == 3:
          mensagem = ("Seu gato tem 28 anos humano.")
        elif idade == 4:
          mensagem = ("Seu gato tem 32 anos humano.")
        elif idade == 5:
          mensagem = ("Seu gato tem 36 anos humano.")
        elif idade > 5:
          calculo = 36 + ((idade - 5) * 4)
        mensagem = (f'Seu gato tem {calculo} anos humano.')

    return render_template('calculo_idade.html', mensagem =mensagem)

if __name__ == '__main__':
    app.run(debug=True) #executa o aplicativo flask

