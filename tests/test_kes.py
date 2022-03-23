import unittest
from uuid import UUID

from generated1 import ProgrammerRow, programmer_row_property_map
from kes import Table


class TestRow(unittest.TestCase):
    def test_isolation(self):
        # should run against generated rows.

        programmer1 = ProgrammerRow()
        programmer2 = ProgrammerRow()

        self.assertIsNot(programmer1.aliases, programmer2.aliases)
        self.assertIsNot(programmer1.mug_shot, programmer2.mug_shot)


class TestTable(unittest.TestCase):
    def setUp(self):
        self.table = Table[ProgrammerRow](
            UUID("cf69ae6a-41ef-43cc-9b43-700d8269ccf8"), programmer_row_property_map
        )

    def test_iteration(self):
        programmer1 = ProgrammerRow(name="Roel de Jong")
        programmer2 = ProgrammerRow(name="John Carmack")
        self.table.appendRow(programmer1)
        self.table.appendRow(programmer2)

        self.assertListEqual

        programmer_iter = iter(self.table)
        programmer = next(programmer_iter)
        self.assertEqual(programmer.name, "Roel de Jong")
        programmer = next(programmer_iter)
        self.assertEqual(programmer.name, "John Carmack")
        with self.assertRaises(StopIteration):
            next(programmer_iter)

    def test_reverse_iteration(self):
        programmer1 = ProgrammerRow(name="Roel de Jong")
        programmer2 = ProgrammerRow(name="John Carmack")
        self.table.appendRow(programmer1)
        self.table.appendRow(programmer2)

        programmer_iter = reversed(self.table)
        programmer = next(programmer_iter)
        self.assertIs(programmer.name, "John Carmack")
        programmer = next(programmer_iter)
        self.assertEqual(programmer.name, "Roel de Jong")
        with self.assertRaises(StopIteration):
            next(programmer_iter)

    def test_len(self):
        self.assertEqual(len(self.table), 0)

        programmer = ProgrammerRow()
        self.table.appendRow(programmer)
        self.assertEqual(len(self.table), 1)


if __name__ == '__main__':
    unittest.main()
