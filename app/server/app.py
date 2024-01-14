from fastapi import FastAPI

from server.routes.supplier import router as SupplierRouter

app = FastAPI()

app.include_router(SupplierRouter, tags=["Supplier"], prefix="/supplier")

@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

