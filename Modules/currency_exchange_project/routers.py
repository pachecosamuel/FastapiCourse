from fastapi import APIRouter


router = APIRouter()

# Path parameter -> url/{value}
# Query parameter -> url?q=value
@router.get("/converter/{from_currency}")
def converter(from_currency: str, to_currencies: str, price: float):
    return "It works"

