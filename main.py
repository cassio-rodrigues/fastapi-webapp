import fastapi
import uvicorn
import fastapi_chameleon
from fastapi_chameleon import template

app = fastapi.FastAPI()

fastapi_chameleon.global_init("templates")


@app.get("/")
@template(template_file="index.html")
def index(user: str = "Test user"):
    return {"user_name": user}


if __name__ == "__main__":
    uvicorn.run(app)

# to run this file you can use both commands:
# python main.py
# uvicorn main:app (better for production evironment)
