import models



def criar_cliente(db,nome,email):
    cliente = models.Cliente(nome=nome,email=email)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente




def criar_pedido(db, descricao, cliente_id):
    pedido = models.Pedido(
        descricao=descricao,
        status="preparando",
        cliente_id=cliente_id

    )
    db.add(pedido)
    db.commit()
    db.refresh(pedido)
    return pedido