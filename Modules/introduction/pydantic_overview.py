from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    email: str
    salary: float
    
    
    def __str__(self) -> str:
        return super().__str__()
    
    @field_validator('email')
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError("Invalid Email")
        
        return value
    
    
def function_(user: User):
    user.salary
    pass

user = User(name="Samuca", email="samuca@g.com", salary=19520.68)
print(user)