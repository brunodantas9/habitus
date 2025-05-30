import pickle

def salvar_dados(usuario, caminho='dados.pkl'):
    with open(caminho, 'wb') as f:
        pickle.dump(usuario, f)

def carregar_dados(caminho='dados.pkl'):
    try:
        with open(caminho, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None
