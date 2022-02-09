
from generated import Expertise, ProgrammerRow, SweatShopRow, sweat_shop_table, programmer_table

# Adding a row
sweat_shop = SweatShopRow(name="Race to the bottom")
sweat_shop_reference = sweat_shop_table.appendRow(sweat_shop)

programmer = ProgrammerRow(
    name="Roel de Jong",
    aliases=["Twiggler", "Twijgje"],
    age=39,
    expertise=Expertise.BACKEND | Expertise.FRONTEND,
    sweat_shop=sweat_shop_reference
)
programmer_table.appendRow(programmer)

print("name: ", programmer_table[0].name)

# remove row
del programmer_table[0]

# Alternative way to set reference
programmer.sweat_shop = sweat_shop_table.getReferenceByRowIndex(0)
