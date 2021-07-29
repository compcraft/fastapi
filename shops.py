import yaml

with open('minecraft/plugins/EconomyShopGUI/shops.yml', 'r') as stream:
    try:
        shops = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# for shop in list(shops.keys()):
shop = 'Enchanting'
for item in shops[shop].keys():
    shops[shop][item]['buy'] = shops[shop][item]['buy'] * 3
    if shops[shop][item]['buy'] < 0:
        shops[shop][item]['buy'] = shops[shop][item]['buy'] * -1

    shops[shop][item]['sell'] = shops[shop][item]['sell'] * 1
    if shops[shop][item]['sell'] < 0:
        shops[shop][item]['sell'] = shops[shop][item]['sell'] * -1

with open('minecraft/plugins/EconomyShopGUI/shops.yml', 'w') as fp:
    try:
        fp.write(yaml.dump(shops))
    except yaml.YAMLError as exc:
        print(exc)
