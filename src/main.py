from exceptions import EmailInvalido
from menu import list_contacts, add_contact, remove_contact, edit_contact

def main():
    options = {
        "1": ("Listar Contatos", list_contacts),
        "2": ("Adicionar Contato", add_contact),
        "3": ("Remover Contato", remove_contact),
        "4": ("Editar Contato", edit_contact)
    }

    while True:
        print(f"\n=== Gerenciador de Contatos ===")
        for k, (desc, _) in options.items():
            print(f"  {k}. {desc}")
        print("  0. Sair")

        option = input("\nOpção: ").strip()
        if option == "0":
            break
        elif option in options:
            try:
                options[option][1]()
            except EmailInvalido as e:
                print("Erro de Validação", e)
            except Exception as e:
                print("Erro Inesperado:", e)
        else:
            print("Opção Inválida")

if __name__ == "__main__":
    main()