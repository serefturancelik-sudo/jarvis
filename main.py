from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Web arayüzünü tanıtıyoruz
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

@app.get("/komut-calistir/{komut}")
async def calistir(komut: str):
    # Burada services klasöründeki modülleri çağırabilirsin
    return {"durum": f"{komut} başarıyla tetiklendi"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
