from fastapi import FastAPI
import uvicorn
from server.routes.supplier import router as SupplierRouter

app = FastAPI()

app.include_router(SupplierRouter, tags=["Supplier"], prefix="/supplier")

@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
