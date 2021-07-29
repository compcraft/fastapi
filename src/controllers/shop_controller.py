from libs.db import CompCraftMONGO
from libs.models import ShopItem
from utils import yaml


def list_items():
    db = CompCraftMONGO().shops()
    shop_items = []
    for shop in db.find():
        shop_items.append(ShopItem(**shop))
    return shop_items


def list_items_section(section: str):
    db = CompCraftMONGO().shops()
    shop_items = []
    for shop in db.find({'section': section.lower()}):
        shop_items.append(ShopItem(**shop))
    return shop_items


def deprecated_list_items():
    return yaml.read_file('../plugins/EconomyShopGUI/shops.yml')


def insert_all():
    db = CompCraftMONGO().shops()
    shops = deprecated_list_items()
    for section in shops.keys():
        for item in shops[section].keys():
            shop_item = shops[section][item]
            shop_item['section'] = section.lower()
            db.insert_one(shop_item)
