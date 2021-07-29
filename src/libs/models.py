from typing import List, Optional
from pydantic import BaseModel
from bson import ObjectId


class Enchantment(BaseModel):
    _id: ObjectId
    enchantment: str
    display_name: str
    description: str
    rarity: str
    max_level: int
    applies_to: List[str]
    source: str


class Talisman(BaseModel):
    name: str
    description: str
    category: str
    level: int


class User(BaseModel):
    username: str
    level: int


class Job(BaseModel):
    _id: ObjectId
    name: str
    description: List[str]
    toplist: Optional[List[User]] = None
    rewards: Optional[dict] = None


class ShopItem(BaseModel):
    _id: ObjectId
    material: str
    buy: float
    sell: float
    section: str
    enchantments: Optional[List[str]] = None
    potiontypes: Optional[List[str]] = None


class ShopSection(BaseModel):
    __root__: List[ShopItem]
