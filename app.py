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
    print(leads)
    # Criar tabela como o 0
    # exel
def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar lead")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Ate mais...")
            break
        else:
            print("Opção invalida")

if __name__ == "__main__":
    main()