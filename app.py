from re import search

from model import model_lead
import control

def add_lead():

    name = input("Nome: ")
    email = input("E-mail: ")
    status = input("Status do fluxo de vendas: ")
    
    # Validar os dados
    #agora preciso modelar os dados
    #Para isso, vamos usar o model.py
    #Preciso modelar os dados como um dict
    model_lead(name, email, status)
    print(model_lead(name, email, status))

    # Com os dadso modelados... preciso enviar para o .json
    # Vou usar o control para enviar o dicionario do lead
    control.create_lead(model_lead(name, email, status))

    print("Lead adicionado (func)")

def list_leads():
    leads = control.read_leads()
    print(f"## | {"nome":<10} | E_mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]}")
    # Criar tabela como o 0
    # exel

def search_leads():
    query = input("Buscar por: ").strip()
    if not query:
        print("Consulta vazia")
        return

    # com query digitada (busca)... preciso enviar para o controlo
    # o control irá comparar  a query com os dados do leads .json
    # e irá retornar os resultados da busca
    leads_found = control.read_leads_search(query)

    print(f"## | {"nome":<10} | E_mail")
    for i, lead in leads_found:
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]}")

def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Nãp foi possivel exportar")
    else:
        print(f"Exportado para {path_csv}")


def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar lead")
        print("[3] Buscar (nome/ email)")
        print("[4] Exportar para csv")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Ate mais...")
            break
        else:
            print("Opção invalida")

if __name__ == "__main__":
    main()