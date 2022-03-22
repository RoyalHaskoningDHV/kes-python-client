from geocoder.location import Location
from geopy import MapBox
from generated import TestCategoryTestAssetRow, test_category_test_asset_table
from kes import LocationField
import os

# Form Row
asset = TestCategoryTestAssetRow(string_test_property="Test String Python",
                                 decimal_test_property=9.999,
                                 )
f = open("image.png", "rb")
asset.image_property.save(f.name, f.read())

geocoder = MapBox(api_key=os.environ.get('REACT_APP_MAPBOX_TOKEN'))
location1: Location = geocoder.reverse(query=(52.057557132353644, 4.949373509877396))
asset.location_property.append(LocationField.Point("Demo Python Location1", location1.latitude, location1.longitude, location1.address))

location2: Location = geocoder.reverse(query=(52.357407, 4.883361))
asset.location_property.append(LocationField.Point("Demo Python Location2", location2.latitude, location2.longitude, location2.address))

# create Row in KES
test_category_test_asset_table.appendRow(asset)

# load row
test_category_test_asset_table.load()


# Downloaded image
downloadedImage = test_category_test_asset_table[0].image_property.load()
with open("downloaded Pingu.jpeg", "wb") as binary_file:

    # Write bytes to file
    binary_file.write(downloadedImage)

# # delete row
del test_category_test_asset_table[0]
