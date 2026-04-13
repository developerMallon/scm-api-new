from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from core.config import settings

# Criação da engine assíncrona (echo ativado apenas em desenvolvimento)
engine = create_async_engine(
    settings.DATABASE_URL, 
    echo=(settings.ENVIRONMENT == "development")
)

# Criação da fábrica de sessões assíncronas
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)

# Classe base para os modelos do SQLAlchemy
Base = declarative_base()

# Dependência (Dependency Injection) para usar no FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
