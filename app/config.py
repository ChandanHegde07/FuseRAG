import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    # ---- Project Metadata ----
    PROJECT_NAME: str = "FuseRAG"
    DESCRIPTION: str = (
        "FuseRAG: Retrieval-Augmented Generation API Platform "
        "powered by Gemini and ChromaDB"
    )
    API_VERSION: str = "v1"

    # ---- Security ----
    MASTER_API_KEY: str  # API key for authenticating users (Bearer token)

    # ---- LLM Provider Config ----
    LLM_PROVIDER: str = "gemini"

    # Gemini configuration
    GEMINI_API_KEY: str  
    GEMINI_MODEL: str = "gemini-1.5-flash"  

    # OpenAI (optional fallback)
    OPENAI_API_KEY: str | None = None
    OPENAI_MODEL: str = "gpt-4o-mini"

    # Ollama (optional local fallback)
    OLLAMA_MODEL: str = "mistral"

    # ---- Embedding Config ----
    # You can still use OpenAI embeddings (or switch to local later)
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 100

    # ---- Vector Database ----
    VECTOR_DB_PATH: str = str(BASE_DIR / "data" / "vector_store")
    VECTOR_DB_COLLECTION: str = "fuserag_docs"

    # ---- File Storage ----
    UPLOAD_DIR: str = str(BASE_DIR / "data" / "uploads")

    # ---- Logging ----
    LOG_LEVEL: str = "INFO"

    # ---- Runtime Environment ----
    ENVIRONMENT: str = "development"  # or "production"
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    DEBUG_MODE: bool = True

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


# Instantiate global settings
settings = Settings()

# Ensure required folders exist
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
os.makedirs(settings.VECTOR_DB_PATH, exist_ok=True)


# Optional Helper: Print config summary at startup
def print_startup_banner():
    print("=" * 60)
    print(f"Starting {settings.PROJECT_NAME} ({settings.ENVIRONMENT})")
    print(f"LLM Provider : {settings.LLM_PROVIDER}")
    if settings.LLM_PROVIDER == "gemini":
        print(f"Gemini Model : {settings.GEMINI_MODEL}")
    elif settings.LLM_PROVIDER == "openai":
        print(f"OpenAI Model : {settings.OPENAI_MODEL}")
    elif settings.LLM_PROVIDER == "ollama":
        print(f"Ollama Model : {settings.OLLAMA_MODEL}")
    print(f"Vector DB Path: {settings.VECTOR_DB_PATH}")
    print(f"Upload Folder : {settings.UPLOAD_DIR}")
    print("=" * 60)