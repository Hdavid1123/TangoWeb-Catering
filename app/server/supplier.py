from typing import Optional
from pydantic import BaseModel, EmailStr, Field, constr, conint
        
        
class SchemaSupplier(BaseModel):
    name: constr(min_length=3, max_length=50, strict=True) = Field(...)
    lastname: constr(min_length=3, max_length=50, strict=True) = Field(...)
    email: EmailStr = Field(...)
    phone: conint(min_length=10, max_length=10,strict=True) = Field(...)
    address: constr(min_length=3, max_length=50, strict=True) = Field(...)
    city: constr(min_length=3, max_length=50, strict=True) = Field(...)
    state: constr(min_length=2, max_length=2, strict=True) = Field(...)
    zip_code: conint(min_length=5, max_length=5, strict=True) = Field(...)
    country: constr(min_length=3, max_length=50, strict=True) = Field(...)
    active: bool = Field(True)

    class Config:
        schema_extra = {
            "example": {
                "name": "Supplier Name",
                "lastname": "Supplier Lastname",
                "email": "supplier@email.com",
                "phone": 1234567890,
                "address": "Supplier Address",
                "city": "Supplier City",
                "state": "Supplier State",
                "zip_code": 12345,
                "country": "Supplier Country",
                "active": True
                }
            }

# Update Supplier

class SchemaSupplierUpdate(BaseModel):
    name: Optional[constr(min_length=3, max_length=50, strict=True)]
    lastname: Optional[constr(min_length=3, max_length=50, strict=True)]
    email: Optional[EmailStr]
    phone: Optional[conint(min_length=10, max_length=10,strict=True)]
    address: Optional[constr(min_length=3, max_length=50, strict=True)]
    city: Optional[constr(min_length=3, max_length=50, strict=True)]
    state: Optional[constr(min_length=2, max_length=2, strict=True)]
    zip_code: Optional[conint(min_length=5, max_length=5, strict=True)]
    country: Optional[constr(min_length=3, max_length=50, strict=True)]
    active: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "name": "Supplier Name",
                "lastname": "Supplier Lastname",
                "email": "supplier@email.com",
                "phone": 1234567890,
                "address": "Supplier Address",
                "city": "Supplier City",
                "state": "Supplier State",
                "zip_code": 12345,
                "country": "Supplier Country",
                "active": True
                }
            }


def ResponseModelSupplier(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorRespondeModelSupplier(error, code, message):
    return {"error": error, "code": code, "message": message}