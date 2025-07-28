import os

class Config:
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    SECRET_KEY = os.getenv("SECRET_KEY", "FDGD851F8DGhgfhgf_fdsfewn543534_arqv30_enhanced_2024")
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))

    SUPABASE_URL = os.getenv("SUPABASE_URL", "https://fusgxmdnjkxaqyfgznsc.supabase.co")
    SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ1c2d4bWRuamt4YXF5Zmd6bnNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTM2MzAzNjcsImV4cCI6MjA2OTIwNjM2N30.UtELTQ2gh_cfiCkWaQlrvGPFrGFIcLfcDS2UCn0F4bA")
    SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ1c2d4bWRuamt4YXF5Zmd6bnNjIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzYzMDM2NywiZXhwIjoyMDY5MjA2MzY3fQ.vxZKHUnF0wswkFTu4etHQlLJBCt67KCx3ucf1lZspmM")
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:[jhBdemW9d$xRN3W]@db.fusgxmdnjkxaqyfgznsc.supabase.co:5432/postgres")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyDDaiQsGSEfWu5E8_mgPugVzxtBdaDhviQ")
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "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")
    HUGGINGFACE_MODEL_NAME = os.getenv("HUGGINGFACE_MODEL_NAME", "meta-llama/Meta-Llama-3-70B")

    MAX_LLM_CALL_PER_RUN = int(os.getenv("MAX_LLM_CALL_PER_RUN", 100))
    MAX_LENGTH = int(os.getenv("MAX_LENGTH", 32768))
    PYTHON_VERSION = os.getenv("PYTHON_VERSION", "3.11.0")

    GOOGLE_SEARCH_KEY = os.getenv("GOOGLE_SEARCH_KEY", "AIzaSyD3vio7yRg11GpIpG7QKHKvIf2U0ahbMVk")
    GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID", "017576662512468239146:omuauf_lfve")
    JINA_API_KEY = os.getenv("JINA_API_KEY", "jina_c2a8caea56f44dc09d3c76c534d77fd3Q5FjdnlZJemF3iAGs6zhnt-PDV0x")
    WEBSAILOR_ENABLED = os.getenv("WEBSAILOR_ENABLED", "true")


