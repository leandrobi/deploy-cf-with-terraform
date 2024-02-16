import json
from flask import Flask, jsonify

def hello_http(request):
    # Criar um dicionário com os dados que você deseja retornar no JSON
    data = {
        "nome": "Joao",
        "idade": 30,
        "email": "joao@example.com",
        "endereço": {
            "rua": "Rua das Flores",
            "cidade": "Cidade Exemplo",
            "estado": "EX"
        },
        "interesses": ["python", "IA", "Cloud Computing"],
        "ultima_compra": {
            "produto": "Livro de Python",
            "preço": 29.99,
            "data": "2024-02-08"
        }
    }

    # Converter o dicionário para uma string JSON
    response_json = json.dumps(data)

    print(None)
    
    # Retornar a resposta HTTP com o JSON
    return jsonify(data)
