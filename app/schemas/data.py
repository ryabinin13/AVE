from pydantic import BaseModel, field_validator
import re


class AddDataSchema(BaseModel):
    phone: str
    address: str

    @field_validator("phone")
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{11}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать 11 цифр')
        return values