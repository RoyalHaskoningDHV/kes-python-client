from io import BytesIO
from uuid import UUID
from tables import CategoryParentAssetRow, CategoryAssetRow, Multipleselect, Singleselect, category_asset_table_def, category_parent_asset_table_def
from kes.client import Client, Config
import os
from PIL import Image
from PIL.ImageShow import show

# Fetch config
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN', 'token')

# Initialize client
config = Config(access_token=ACCESS_TOKEN)
client = Client(config)

# Open project
project = client.open_project_by_id(UUID("870f7d2b-e9e6-4667-aaf4-690996e8ec00"))   # by id
projects = client.load_project_by_master_id("master666")  # by master project id
project = projects[0]
# Create a table
activity = project.activities[0]
table = activity.build_table(category_asset_table_def)

# Read existing rows
table.load()

# Deleting row if it exists
if len(table) > 0:
    table.clear()

# Create a row
row = CategoryAssetRow(
    singleselect=Singleselect.A,
    multipleselect=Multipleselect.D | Multipleselect.F,
    text="Text",
    amount=12.0
)

# Add a location
row.location.add_point(address="Meppel - Assen",
                       latitude=52.77035725849205,
                       longitude=6.49079267010161,
                       name="Switch")
# Add a image
scriptPath = os.path.realpath(__file__)
filePath = os.path.join(os.path.dirname(scriptPath), "test_image.png")
imageFile = open(filePath, "rb")
table.save_image(row.image, "Image name", imageFile.read())

# Add the row and get a reference
ref = table.append_row(row)

# Retrieve and show the image
table.load()
image_data = table.load_image(table[0].image)
if image_data is None:
    raise RuntimeError("No image found.")
image = Image.open(BytesIO(bytes(image_data)))
show(image, "Test image")

# Create a row in parent asset and set reference
parent_table = activity.build_table(category_parent_asset_table_def)
parent_table.load()
if len(parent_table) > 0:
    del parent_table[0]
parent_row = CategoryParentAssetRow(relationship=ref)
parent_table.append_row(parent_row)
