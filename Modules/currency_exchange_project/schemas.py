import re
from typing import List
from pydantic import BaseModel, Field, field_validator

class ConverterInput(BaseModel):
    price: float = Field(gt=0)
    to_currencias: List[str]
    
    @field_validator
    def validate_currencies(cls, value):
        for currency in value:
            if not re.match("^[A-Z]{3}$", currency):
                raise ValueError(f"Invalid currency {currency}")
            return value
        
        