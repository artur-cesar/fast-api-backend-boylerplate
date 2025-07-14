from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID
from decimal import Decimal

class ExampleCreate(BaseModel):
    name: str
    price: Decimal = Field(..., gt=0, decimal_places=2)
    description: Optional[str] = None

class ExampleRead(BaseModel):
    id: UUID
    name: str
    price: Decimal
    description: Optional[str] = None

    # Config to convert snake_case into camelCase based on aliases
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")

    # Config to convert snake_case into camelCase based on aliases
    class Config:
        allow_population_by_field_name = True
        allow_population_by_alias = True
        from_attributes = True
        populate_by_name = True 
        orm_mode = True
        json_encoders = {Decimal: lambda v: float(v)}
