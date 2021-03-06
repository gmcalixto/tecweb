from utils import load_data, load_template, write_json
import json

def index(request):
    if request.startswith('POST'):
        

        request = request.replace('\r', '')  # Remove caracteres indesejados
        
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]

        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            params[chave_valor.split('=')[0]] = chave_valor.split('=')[1]
        
        write_json('notes.json',params)

        note_template = load_template('components/note.html')
        notes_li = [
            note_template.format(title=dados['titulo'], details=dados['detalhes'])
            for dados in load_data('notes.json')
        ]
        notes = '\n'.join(notes_li)

        return load_template('index.html').format(notes=notes).encode()
    
    else:
        print('Requisicao GET')
        # Cria uma lista de <li>'s para cada anotação
        # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        note_template = load_template('components/note.html')
        notes_li = [
            note_template.format(title=dados['titulo'], details=dados['detalhes'])
            for dados in load_data('notes.json')
        ]
        notes = '\n'.join(notes_li)

        return load_template('index.html').format(notes=notes).encode()