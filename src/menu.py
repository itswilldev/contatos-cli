from exceptions import ContatoNaoEncontrado, EmailInvalido
from models import Contact
from repository import load, save, search_by_id
import re

def validate_email(email: str) -> bool:
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def list_contacts():
    contacts = load()
    if not contacts:
        print("Nenhum contato cadastrado.")
        return
    for c in contacts:
        print(f"[{c.id}] {c.name} | {c.phone} | {c.email}")

def add_contact():
    name = input("Nome: ").strip()
    phone = input("Telefone: ").strip()
    email = input("Email: ").strip()

    if not validate_email(email):
        raise EmailInvalido(f"'{email} não é um email válido.")
    
    contacts = load()
    contacts.append(Contact(name=name, phone=phone, email=email))
    save(contacts)
    print("Contato adicionado")

def remove_contact():
    list_contacts()
    _id = input("ID do contato a remover: ").strip()
    contacts = load()
    try:
        contact = search_by_id(contacts, _id)
        contacts.remove(contact)
        save(contacts)
        print("Contato removido.")
    except ContatoNaoEncontrado as e:
        print(f"Erro: {e}")

def edit_contact():
    list_contacts()
    _id = input("ID do contato a editar: ").strip()
    contacts = load()
    try:
        contact = search_by_id(contacts, _id)
        contact.name = input(f"Novo nome [{contact.name}]: ").strip() or contact.name
        contact.phone = input(f"Novo nome [{contact.phone}]: ").strip() or contact.phone
        contact.email = input(f"Novo nome [{contact.email}]: ").strip() or contact.email
        save(contacts)
        print("Contato atualizado!")
    except ContatoNaoEncontrado as e:
        print(f"Erro: {e}")

add_contact()
add_contact()
remove_contact()
edit_contact()