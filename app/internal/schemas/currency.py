from pydantic import BaseModel
from typing import List

class Symbol(BaseModel):

    symbol: str

class Symbols(BaseModel):

    symbols: List[Symbol]