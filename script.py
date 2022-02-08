
from generated import Expertise, ProgrammerRow, SweatShopRow, sweat_shop_table
from meta import ImageField


sweat_shop = SweatShopRow(name="Race to the bottom")
sweat_shop_table.appendRow(sweat_shop)

programmer = ProgrammerRow(
    name="Roel de Jong",
    aliases=["Twiggler", "Twijgje"],
    age=39,
    expertise=Expertise.BACKEND | Expertise.FRONTEND,
    mug_shot=ImageField(),
    sweat_shop=sweat_shop_table.getRowReference(0)
)
