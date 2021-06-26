import yaml

# for shop in list(shops.keys()):
#     for item in shops[shop].keys():
#         shops[shop][item]['buy'] = shops[shop][item]['buy'] * 4.25

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    shops = None
    with open('plugins/EconomyShopGUI/shops.yml', 'r') as stream:
        try:
            shops = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return shops