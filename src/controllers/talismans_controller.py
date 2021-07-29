from utils import yaml, json
from libs.db import CompCraftMONGO
from libs.models import Enchantment, Talisman
from os import walk
import re


def get_raw_talismans():
    f = []
    talismans = []
    path_dir = '../plugins/Talismans/talismans'

    for (dirpath, dirnames, filenames) in walk(path_dir):
        f.extend(filenames)
        break

    for file in f:
        section = yaml.read_file(f'{path_dir}/{file}')
        for index, level in enumerate(section['levels'].values()):
            talismans.append({
                'category': file.replace('.yml', ''),
                'name': re.sub(r'\&\w', '', level['name']),
                'description': level['description'],
                'level': int(list(section['levels'].keys())[index]),
            })
    return talismans


def insert_talismans():
    db = CompCraftMONGO().talismans()

    talismans = get_raw_talismans()

    for talisman in talismans:
        db.insert_one(talisman)

    return talismans


def list_talismans(categories: bool = False):
    db = CompCraftMONGO().talismans()

    if categories:
        talismans = {}
    else:
        talismans = []

    for talisman in db.find({}).sort('name'):
        if categories:
            if talisman['category'] not in talismans:
                talismans[talisman['category']] = []
            talismans[talisman['category']].append(Talisman(**talisman))
        else:
            talismans.append(Talisman(**talisman))

    return talismans


def list_category_talismans(category: str):
    db = CompCraftMONGO().talismans()

    talismans = []

    for talisman in db.find({'category': category}).sort('name'):
        talismans.append(Talisman(**talisman))

    return talismans
