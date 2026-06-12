from datetime import datetime
from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import declarative_base

from . import db


class Operacao(db.Model):
    """Model — dados e acesso ao banco (tabela operacoes)."""

    __tablename__ = "operacoes"

    # crie a tabela e crie um campo para a tabela de datetime o campo deve chamar criado_em
    id = db.Column(db.Integer, primary_key=True)
    num1 = db.Column(db.String(100), nullable=True)
    num2 = db.Column(db.String(120), nullable=False)
    operacao = db.Column(db.String(120), nullable=False) 
    # TODO: Resolver erro de etapas
    resultado = db.Column(db.String(120),   nullable=False)
    criado_em = db.Column(DateTime, default=datetime.now)


    @classmethod
    def salvar(cls, num1, num2, operacao, etapas, resultado):
        registro = cls(
            num1=num1,
            num2=num2,
            operacao=operacao,
            etapas=etapas,
            resultado=str(resultado),
        )
        # adicione os métodos de adicionar e commit 
        db.session.commit()
        return registro

    @classmethod
    def listar_recentes(cls, limite=10):
        return (
            cls.query.order_by(cls.criado_em.desc()).limit(limite).all()
            
        )

    def __repr__(self):
        return f"<Operacao {self.id}: {self.etapas}>"