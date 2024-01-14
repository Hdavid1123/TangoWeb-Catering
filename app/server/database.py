import os
import motor.motor_asyncio
from bson.objectid import ObjectId

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["DB_URL"])

database = client.suppliers

supplier_collection = database.get_collection("suppliers_collection")

def supplier_helper(supplier) -> dict:
    return {
        "id": str(supplier["_id"]),
        "name": supplier["name"],
        "lastname": supplier["lastname"],
        "email": supplier["email"],
        "phone": supplier["phone"],
        "address": supplier["address"],
        "city": supplier["city"],
        "state": supplier["state"],
        "zip_code": supplier["zip_code"],
        "country": supplier["country"],
        "active": supplier["active"],
    }

# Operaciones del CRUD

async def retrieve_suppliers():
    suppliers = []
    async for supplier in supplier_collection.find():
        suppliers.append(supplier_helper(supplier))
    return suppliers

async def add_supplier(supplier_data: dict) -> dict:
    supplier = await supplier_collection.insert_one(supplier_data)
    new_supplier = await supplier_collection.find_one({"_id": supplier.inserted_id})
    return supplier_helper(new_supplier)

async def retrieve_supplier(id: str) -> dict:
    supplier = await supplier_collection.find_one({"_id": ObjectId(id)})
    if supplier:
        return supplier_helper(supplier)
    
async def update_supplier(id: str, data: dict):
    if len(data) < 1:
        return False
    supplier = await supplier_collection.find_one({"_id": ObjectId(id)})
    if supplier:
        updated_supplier = await supplier_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_supplier:
            return True
        return False
    
async def delete_supplier(id: str):
    supplier = await supplier_collection.find_one({"_id": ObjectId(id)})
    if supplier:
        await supplier_collection.delete_one({"_id": ObjectId(id)})
        return True