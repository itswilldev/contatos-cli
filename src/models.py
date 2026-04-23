from dataclasses import dataclass, field
import uuid

@dataclass
class Contato:
    nome: str
    telefone: str
    email: str
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])