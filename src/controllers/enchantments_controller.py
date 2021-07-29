from utils import yaml, json
from libs.db import CompCraftMONGO
from libs.models import Enchantment
from pprint import pprint


def verify_enchantments():
    base = CompCraftMONGO().enchantments()

    enchantments = []
    for ench in base.find({}):
        enchantments.append(Enchantment(**ench))

    return enchantments


def list_default_enchantments():
    db = CompCraftMONGO().enchantments()

    enchantments = []

    for ench in db.find({"source": {"$eq": "default"}}).sort('name'):
        enchantments.append(Enchantment(**ench))

    return enchantments


def list_custom_enchantments():
    db = CompCraftMONGO().enchantments()

    enchantments = []

    for ench in db.find({"source": {"$eq": "advanced_enchantments"}}).sort('name'):
        enchantments.append(Enchantment(**ench))

    return enchantments
