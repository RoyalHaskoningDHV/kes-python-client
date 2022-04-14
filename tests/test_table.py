import unittest
from unittest.mock import Mock
from uuid import uuid4

from .tables import CategoryAssetRow, category_asset_table_def
from kes.table import Table


class TestRow(unittest.TestCase):
    def test_isolation(self):
        # should run against generated rows.

        row1 = CategoryAssetRow()
        row2 = CategoryAssetRow()

        self.assertIsNot(row1.location, row2.location)
        self.assertIsNot(row1.image, row2.image)


class TestTable(unittest.TestCase):
    def setUp(self):
        self.tableStub = Mock()
        self.tableUuid = uuid4()
        self.activityUuid = uuid4()
        self.table = Table[CategoryAssetRow](
            self.tableStub, self.activityUuid, CategoryAssetRow, self.tableUuid, category_asset_table_def.property_map
        )

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
