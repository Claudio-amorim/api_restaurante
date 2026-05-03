from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models
import schemas
import crud


Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/clientes", response_model=schemas.ClienteResponse)
def criar_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.criar_cliente(db, cliente.nome, cliente.email)


@app.get("/clientes")
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(models.Cliente).all()



@app.post("/pedidos", response_model=schemas.PedidoResponse)
def criar_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    
    cliente = db.query(models.Cliente).filter(models.Cliente.id == pedido.cliente_id).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return crud.criar_pedido(db, pedido.descricao, pedido.cliente_id)


@app.get("/pedidos")
def listar_pedidos(db: Session = Depends(get_db)):
    return db.query(models.Pedido).all()


@app.put("/pedidos/{pedido_id}")
def atualizar_status(pedido_id: int, status: str, db: Session = Depends(get_db)):
    
    pedido = db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    valid_status = ["preparando", "pronto", "entregue"]

    if status not in valid_status:
        raise HTTPException(status_code=400, detail="Status inválido")

    pedido.status = status

    db.commit()
    db.refresh(pedido)

    return pedido

@app.get("/")
def home():
    return {"mensagem": "API Restaurante funcionando"}


@app.get("/clientes/{cliente_id}/pedidos")
def listar_pedidos_cliente(cliente_id: int, db: Session = Depends(get_db)):
    
    pedidos = db.query(models.Pedido).filter(models.Pedido.cliente_id == cliente_id).all()

    return pedidos



@app.get("/pedidos/{pedido_id}")
def buscar_pedido(pedido_id: int, db: Session = Depends(get_db)):
    
    pedido = db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    return pedido