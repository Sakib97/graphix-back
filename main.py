from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.kbModule.repoParseAPI import kb_router

app = FastAPI()

origins = ["http://127.0.0.1:5174", 
           "http://localhost:5174",
           "https://graphix-rho.vercel.app/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # Specify the frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(kb_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"Message": "Welcome to graphix backend!"}


# command for 
    #  installing all from requirements.txt: 
            #  pip install -r requirements.txt
    # settign up venv:  python -m venv venv
    # activate venv: .\venv\Scripts\activate
    # deactivate venv: deactivate
    # see all inatalled libraries: pip list"
    # run uvicorn server: uvicorn main:app --reload --port 8080
# python -u "d:\graphix-back\graphix-back\core\tempCodeRunnerFile.py"
