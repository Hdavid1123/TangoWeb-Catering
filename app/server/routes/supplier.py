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