from fastapi import FastAPI
from sqlalchemy import text

from app.database import mecanismo_banco


app = FastAPI(
    title="API de Livros",
    version="1.0.0",
    description="API didática para gerenciamento de livros.",
)


@app.get("/health", tags=["Saúde"])
def health_check():
    with mecanismo_banco.connect() as conexao:
        conexao.execute(text("SELECT 1"))

    return {"status": "ok", "database": "connected"}

@app.get("/livros", response_model=list[LivroResposta], tags=["Livros"])
def listar_livros(sessao_banco: Session = Depends(obter_sessao_banco)):
    consulta = select(Livro)
    resultado = sessao_banco.execute(consulta)
    livros = resultado.scalars().all()

    return livros