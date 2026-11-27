# import libs / pkgs
from fastapi import FastAPI
from dotenv import load_dotenv

# import database
from core.database.postgres import engine

# import routes
from modules.ai_team.router import ai_agent_router

# middlewares
from middlewares.authenticate import api_authenticate_key

# load DB
load_dotenv()
engine()


app = FastAPI()
app.middleware("http")(api_authenticate_key)

app.include_router(ai_agent_router, tags=["Dev Team"])