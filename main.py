import fastapi
import uvicorn
import fastapi_chameleon
from views import home

app = fastapi.FastAPI()


def main():  # starts the app
    configure()
    uvicorn.run(app)


def configure():  # call the routes and templates configurations
    configure_templates()
    configure_routes()


def configure_templates():  # this is a fuction so if you refactor anything would be easier
    fastapi_chameleon.global_init("templates")


def configure_routes():  # just to let the app grow in a health way then you can just bring the routes easily
    app.include_router(home.router)


if __name__ == "__main__":
    main()
else:
    configure()  # this is needed for running in production environment

# to run this file you can use both commands:
# python main.py
# uvicorn main:app (better for production evironment)
