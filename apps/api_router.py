from fastapi import APIRouter

api_router = APIRouter()

# Rota raiz - para verificar se a API está rodando
@api_router.get("/")
def read_root():
    return {
        "status": "success",
        "message": "API is running"
    }


# Aqui você centraliza a inclusão de todos os routers da sua aplicação
from apps.user.routes.user import router as user_router
api_router.include_router(user_router)

# Exemplo de como incluir futuras rotas:
# from apps.indicadores.routes import router as indicadores_router
# api_router.include_router(indicadores_router, prefix="/indicadores", tags=["Indicadores"])
