import uvicorn
from fastapi import FastAPI
from profiles import routes as profile_routes
from tweets import routes as tweet_routes
from profiles import models as profile_models
from oauth2 import router as oauth2_router
from tweets import models as tweet_models
from auth import routes as auth_routes
from services.database_connection import SessionLocal
from services.database_connection import engine


app = FastAPI(root_path='/api')


@app.get('/opentelemetry-fastapi')
def about():
    return "hello"

app.include_router(profile_routes.router)
app.include_router(tweet_routes.router)
app.include_router(auth_routes.router)


if __name__ == "__main__":
    profile_models.Base.metadata.create_all(bind=engine)
    tweet_models.Base.metadata.create_all(bind=engine)
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
    