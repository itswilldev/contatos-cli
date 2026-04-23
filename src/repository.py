import json
from pathlib import Path
from models import Contact
from exceptions import ContatoNaoEncontrado

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
FILE = DATA_DIR / "contacts.json"

DATA_DIR.mkdir(exist_ok=True)
FILE.touch(exist_ok=True)

def load() -> list[Contact]:
    if not FILE.exists() or FILE.stat().st_size == 0:
        return []
    with open(FILE) as f:
        data = json.load(f)
    return [Contact(**d) for d in data]

def save(contacts: list[Contact]) -> None:
    with open(FILE, 'w') as f:
        from dataclasses import asdict
        json.dump([asdict(c) for c in contacts], f, indent=2)

def search_by_id(contacts: list[Contact], id: str) -> Contact:
    for c in contacts:
        if c.id == id:
            return c
    raise ContatoNaoEncontrado(f"Contato com id '{id}' não encontrado.")