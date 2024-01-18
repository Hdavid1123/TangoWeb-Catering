from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_suppliers,
    add_supplier,
    retrieve_supplier,
    update_supplier,
    delete_supplier,
)

from server.models.supplier import (
    ErrorResponseModelSupplier,
    ResponseModelSupplier,
    SchemaSupplier,
)

router = APIRouter()

@router.post("/", response_description="Supplier data added into the database")
async def add_supplier_data(supplier: SchemaSupplier = Body(...)):
    supplier = jsonable_encoder(supplier)
    new_supplier = await add_supplier(supplier)
    return ResponseModelSupplier(new_supplier, "Supplier added successfully.")

@router.get("/", response_description="Suppliers retrieved")
async def get_suppliers():
    suppliers = await retrieve_suppliers()
    if suppliers:
        return ResponseModelSupplier(suppliers, "Suppliers data retrieved successfully")
    return ResponseModelSupplier(suppliers, "Empty list returned")

@router.get("/{id}", response_description="Supplier retrieved by ID")
async def get_supplier_id(id):
    supplier = await retrieve_supplier(id)
    if supplier:
        return ResponseModelSupplier(supplier, "Supplier data retrieved successfully")
    return ErrorResponseModelSupplier("An error occurred.", 404, "Supplier doesn't exist.")

@router.put("/{id}")
async def update_supplier_id(id: str, req: SchemaSupplier = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_supplier = await update_supplier(id, req)
    if updated_supplier:
        return ResponseModelSupplier(
            "Supplier with ID: {} update is successful".format(id),
            "Supplier updated successfully",
        )
    return ErrorResponseModelSupplier(
        "An error occurred",
        404,
        "There was an error updating the supplier data.",
    )

@router.delete("/{id}", response_description="Supplier data deleted from the database")
async def delete_supplier_data(id: str):
    deleted_supplier = await delete_supplier(id)
    if deleted_supplier:
        return ResponseModelSupplier(
            "Supplier with ID: {} removed".format(id), "Supplier deleted successfully"
        )
    return ErrorResponseModelSupplier(
        "An error occurred", 404, "Supplier with id {0} doesn't exist".format(id)
    )