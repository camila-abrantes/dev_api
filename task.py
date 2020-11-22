from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tasks = [
    {   'id':'0',
        'responsavel':'Rafael',
        'tarefa':'Lavar os pratos',
        'status':'não concluído'
    }
]

# devolve uma task pelo ID, também altera e deleta uma task
@app.route("/tasks/<int:id>/", methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = tasks[id]
        except IndexError:
            mensagem = 'Task de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido.'
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tasks[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        tasks.pop(id)
        return jsonify({'status':'sucesso','mensagem':'Registro excluído'})

#lista todos os desenvolvedores e permite incluir um novo desevolvedor
@app.route('/tasks/', methods=['POST','GET'])
def lista_desenvolvedores(status):
    if request.method == 'POST':
        tasks[status] = 'concluido'
        return jsonify(status)
    elif request.method == 'GET':
        return jsonify(tasks)


if __name__=="__main__":
    app.run(debug=True)