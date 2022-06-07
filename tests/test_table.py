import unittest
from unittest.mock import Mock, patch
from uuid import uuid4

from kes.proto.table_pb2 import AddRowsRequest, ReadTableRequest, Rows

from tables import CategoryAssetRow, Multipleselect, Singleselect, category_asset_table_def
from kes.table import Table


class TestRow(unittest.TestCase):
    def test_isolation(self):
        # should run against generated rows.

        row1 = CategoryAssetRow()
        row2 = CategoryAssetRow()

        self.assertIsNot(row1.location, row2.location)
        self.assertIsNot(row1.image, row2.image)


@patch('kes.table.uuid4')
class TestTable(unittest.TestCase):
    def setUp(self):
        self.tableStub = Mock()
        self.tableUuid = uuid4()
        self.activityUuid = uuid4()
        self.rowId = uuid4()
        self.table = Table[CategoryAssetRow](
            self.tableStub, self.activityUuid, CategoryAssetRow, self.tableUuid, category_asset_table_def.property_map
        )
        self.row = CategoryAssetRow(
            singleselect=Singleselect.A,
            multipleselect=Multipleselect.F | Multipleselect.D,
            amount=3.0,
            text="Text"
        )

    def test_append_row(self, mock_uuid: Mock):
        mock_uuid.return_value = self.rowId
        ref = self.table.append_row(self.row)

        req = AddRowsRequest()
        row = req.rows.add()
        row.assetId = str(self.rowId)
        req.activityId = str(self.activityUuid)
        req.tableId = str(self.tableUuid)
        field_singleselect = row.fields.add()
        field_singleselect.propertyId = 'd0165c6c-3a53-4126-b701-44cab335853a'
        field_singleselect.members.elements.append(3)
        field_text = row.fields.add()
        field_text.propertyId = 'da1df664-e1ae-4b00-aef5-8e5d86ec74da'
        field_text.strings.elements.append("Text")
        field_number = row.fields.add()
        field_number.propertyId = 'f03d4f5f-a76c-4f20-ab89-5e452b437627'
        field_number.numbers.elements.append(3.0)
        field_multiselect = row.fields.add()
        field_multiselect.propertyId = '7cfdbda8-02e3-47b5-9dae-aa8246baf5d3'
        field_multiselect.members.elements.append(1)
        field_multiselect.members.elements.append(3)
        self.tableStub.addRows.assert_called_once_with(req)    # type: ignore

        self.assertEqual(ref.asset_type_id, self.tableUuid)

    def test_append_empty_row(self, mock_uuid: Mock):
        mock_uuid.return_value = self.rowId
        emptyRow = CategoryAssetRow()
        self.table.append_row(emptyRow)

        req = AddRowsRequest()
        row = req.rows.add()
        row.assetId = str(self.rowId)
        req.activityId = str(self.activityUuid)
        req.tableId = str(self.tableUuid)

        self.tableStub.addRows.assert_called_once_with(req)    # type: ignore

    def test_append_integer(self, mock_uuid: Mock):
        mock_uuid.return_value = self.rowId
        rowWithInteger = CategoryAssetRow(amount=3)
        self.table.append_row(rowWithInteger)

        req = AddRowsRequest()
        row = req.rows.add()
        row.assetId = str(self.rowId)
        req.activityId = str(self.activityUuid)
        req.tableId = str(self.tableUuid)
        field_number = row.fields.add()
        field_number.propertyId = 'f03d4f5f-a76c-4f20-ab89-5e452b437627'
        field_number.numbers.elements.append(3.0)

        self.tableStub.addRows.assert_called_once_with(req)    # type: ignore

    def test_load_row(self):
        response = Rows()
        row = response.rows.add()
        row.assetId = str(self.rowId)
        field_number = row.fields.add()
        field_number.propertyId = 'f03d4f5f-a76c-4f20-ab89-5e452b437627'
        field_number.multi = False
        field_number.numbers.elements.append(3.0)
        field_text = row.fields.add()
        field_text.propertyId = 'da1df664-e1ae-4b00-aef5-8e5d86ec74da'
        field_text.multi = False
        field_text.strings.elements.append('Text')
        field_single_select = row.fields.add()
        field_single_select.propertyId = 'd0165c6c-3a53-4126-b701-44cab335853a'
        field_single_select.multi = False
        field_single_select.members.elements.append(3)
        field_multi_select = row.fields.add()
        field_multi_select.propertyId = '7cfdbda8-02e3-47b5-9dae-aa8246baf5d3'
        field_multi_select.multi = False
        field_multi_select.members.elements.append(1)
        field_multi_select.members.elements.append(3)
        mockLoad = Mock(return_value=response)
        self.tableStub.attach_mock(mockLoad, 'readTable')
        self.table.load()

        req = ReadTableRequest()
        req.activityId = str(self.activityUuid)
        req.tableId = str(self.tableUuid)
        mockLoad.assert_called_once_with(req)

        self.assertSequenceEqual(self.table, [self.row])

    def test_iteration(self):
        row1 = CategoryAssetRow(text="Roel de Jong")
        row2 = CategoryAssetRow(text="John Carmack")
        self.table.append_row(row1)
        self.table.append_row(row2)

        programmer_iter = iter(self.table)
        programmer = next(programmer_iter)
        self.assertEqual(programmer.text, "Roel de Jong")
        programmer = next(programmer_iter)
        self.assertEqual(programmer.text, "John Carmack")
        with self.assertRaises(StopIteration):
            next(programmer_iter)

    def test_reverse_iteration(self):
        row1 = CategoryAssetRow(text="Roel de Jong")
        row2 = CategoryAssetRow(text="John Carmack")
        self.table.append_row(row1)
        self.table.append_row(row2)

        programmer_iter = reversed(self.table)
        programmer = next(programmer_iter)
        self.assertIs(programmer.text, "John Carmack")
        programmer = next(programmer_iter)
        self.assertEqual(programmer.text, "Roel de Jong")
        with self.assertRaises(StopIteration):
            next(programmer_iter)

    def test_len(self):
        self.assertEqual(len(self.table), 0)

        programmer = CategoryAssetRow()
        self.table.append_row(programmer)
        self.assertEqual(len(self.table), 1)


if __name__ == '__main__':
    unittest.main()
