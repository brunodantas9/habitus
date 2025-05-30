from package.user import Usuario
from package.habit import Habito
from package.categoria import Categoria
from package.storage import salvar_dados, carregar_dados
from datetime import date

def main():
    usuario = carregar_dados()
    if not usuario:
        usuario = Usuario("Flávia")

    cat_saude = Categoria("Saúde", "verde")
    hab_beber_agua = Habito("Beber 2L de água", "Meta diária de hidratação", cat_saude, "diário")

    usuario.adicionar_habito(hab_beber_agua)
    hab_beber_agua.registrar(date.today())

    salvar_dados(usuario)

    print("Hábitos registrados:")
    for h in usuario.listar_habitos():
        print(f"- {h.nome}: {h.progresso()} dias concluídos")

if __name__ == '__main__':
    main()
