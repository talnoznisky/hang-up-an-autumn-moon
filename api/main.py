from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from hang_up_an_autumn_moon_over_the_mountain.oracle.main import Oracle
from hang_up_an_autumn_moon_over_the_mountain.oracle.assets.texts import cards, project_credit, guidebook_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# text query endpoints
@app.get("/v1/spread")
def initiate_oracle(sparrow_mode=False):
    o = Oracle(sparrow_mode)
    return o

@app.get("/v1/oracle")
def get_oracle(idx: int, sparrow_mode=False):
    o = Oracle(sparrow_mode)
    return(o.run_oracle(idx))
