from library import CategoryAssetRow, Multipleselect, Singleselect
from kes.client import Client, Config
from library import category_asset_table_def
import os

# Initialize client
config = Config(kes_service_address='localhost:50051')
client = Client(config)

# Lookup project
project = client.open_project("Preview Python client example")

# Create a table
activity = project.activities[0]
table = activity.build_table(category_asset_table_def)

# Read existing rows
table.load()

# Deleting row if it exists
if len(table) > 0:
    del table[0]

# Create a row
row = CategoryAssetRow(
    singleselect=Singleselect.A,
    multipleselect=Multipleselect.D | Multipleselect.F,
    text="Text",
    amount=12.0
)

# Add a location
row.location.addPoint(address="Meppel - Assen",
                      latitude=52.77035725849205,
                      longitude=6.49079267010161,
                      name="Switch")
# Add a image
scriptPath = os.path.realpath(__file__)
filePath = os.path.join(os.path.dirname(scriptPath), "goofy.png")
imageFile = open(filePath, "rb")
table.saveImage(row.image, "Goofy", imageFile.read())

# Add the row
table.appendRow(row)
