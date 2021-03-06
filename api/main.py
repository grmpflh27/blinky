from fastapi import FastAPI
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


from colors import COLORS

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


cur_color = None


@app.get("/color")
def get_color():
    return {"color": cur_color}


@app.post("/color")
def change_color(color: str):
    uc_color = color.upper()
    if uc_color not in COLORS:
        return JSONResponse(status_code=404, content={"message": f"Color {uc_color} not valid"})

    global cur_color
    cur_color = color 
    # TODO: set color on neopixel

    return {"message": f"color changed to {color}"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8127)