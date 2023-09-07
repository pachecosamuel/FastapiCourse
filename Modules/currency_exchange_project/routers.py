import pydantic
from asyncio import gather
from schemas import ConverterInput, ConverterOutput
from fastapi import APIRouter, Path, Query
from converter import (
    sync_version_exchange,
    async_version_exchange
)

router = APIRouter(prefix="/converter")

# Path parameter -> url/{value}
# Query parameter -> 
# Body parameter -> /url?to_currencies=USD,EUR,GB&price=5.55

@router.get("/sync/{from_currency}")
def sync_converter(from_currency: str, to_currencies: str, price: float):
    to_currencies = to_currencies.split(",")
    
    result = []
    
    for currency in to_currencies:
        response = sync_version_exchange(
            from_currency= from_currency,
            to_currency= currency,
            price= price
        )
        
        result.append(response)
        
    return result



@router.get("/async/{from_currency}")
async def async_converter(
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"), 
    to_currencies: str = Path(max_length=50, regex="^[A-Z]{3}(,[A-Z]{3}*)$"), 
    price: float = Query(gt=0)
):
    to_currencies = to_currencies.split(",")
    
    coroutines = []
    
    for currency in to_currencies:
        coroutine = async_version_exchange(
            from_currency= from_currency,
            to_currency= currency,
            price= price
        )
        
        coroutines.append(coroutine)
        
    result = await gather(*coroutines)
    return result



# 
@router.get("/async/v2/{from_currency}", response_model=ConverterOutput)
async def async_converter(
    body: ConverterInput,
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"), 
):
    to_currencies = body.to_currencies
    price = body.price
    
    coroutines = []
    
    for currency in to_currencies:
        coroutine = async_version_exchange(
            from_currency= from_currency,
            to_currency= currency,
            price= price
        )
        
        coroutines.append(coroutine)
        
    result = await gather(*coroutines)
    
    return ConverterOutput(
        message="Succeed",
        data=result
    )


