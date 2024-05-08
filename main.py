from fastapi import FastAPI
from feeds import feeds_controller

app = FastAPI()
app.include_router(feeds_controller.router)


@app.get("/")
def root():
    return ""
