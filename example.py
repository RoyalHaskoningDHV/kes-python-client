from geocoder.location import Location
from geopy import MapBox
from generated import TestCategoryTestAssetRow, test_category_test_asset_table
from kes import LocationField

# Form Row
asset = TestCategoryTestAssetRow(string_test_property="Test String Python",
                                 decimal_test_property=9.999,
                                 )
f = open("image.png", "rb")
asset.image_property.saveImage(f.name, f.read())

geocoder = MapBox(api_key="pk.....")
rs: Location = geocoder.reverse(query=(52.057557132353644, 4.949373509877396))
asset.location_property.append(LocationField.Point("Naushad's Python Location", rs.latitude, rs.longitude, rs.address))
asset.location_property.append(LocationField.Point("Naushad's Python Location1", rs.latitude, rs.longitude, rs.address))

# create Row in KES
test_category_test_asset_table.appendRow(asset)

# load row
test_category_test_asset_table.load()

# delete row
del test_category_test_asset_table[0]
