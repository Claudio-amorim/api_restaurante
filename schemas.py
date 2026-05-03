from pydantic import BaseModel


class ClienteCreate(BaseModel):
    nome: str
    email: str


class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True


class PedidoCreate(BaseModel):
    descricao: str
    cliente_id: int


class PedidoResponse(BaseModel):  # ✅ singular corrigido
    id: int
    descricao: str
    status: str
    cliente_id: int

    class Config:
        from_attributes = True