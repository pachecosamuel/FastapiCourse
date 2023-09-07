import re
from typing import List
from pydantic import BaseModel, Field, field_validator, validator

class ConverterInput(BaseModel):
    price: float = Field(gt=0)
    to_currencies: List[str]
    
    @validator('to_currencies')
    def validate_currencies(cls, value):
        for currency in value:
            if not re.match("^[A-Z]{3}$", currency):
                raise ValueError(f"Invalid currency {currency}")
            return value
        
class ConverterOutput(BaseModel):
    message: str
    data: List[dict]