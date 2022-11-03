import unittest
from ..pen import Pen


class PenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test_pen = Pen("dummy name", "dummy colour", "dummy type")

    def test_empty_pen_instantiates(self):
        test_pen = Pen()
        self.assertIsInstance(test_pen, Pen)

    def test_pen_instantiates(self):
        self.assertIsInstance(self.test_pen, Pen)

    def test_get_pen_name(self):
        name = self.test_pen.name
        self.assertEqual(name, "dummy name")

    def test_get_pen_type(self):
        pen_type = self.test_pen.pen_type
        self.assertEqual(pen_type, "dummy type")

    def test_get_pen_ink(self):
        ink_colour = self.test_pen.ink_colour
        self.assertEqual(ink_colour, "dummy colour")

    def test_set_pen_name(self):
        self.test_pen.name = "another dummy name"
        self.assertEqual(self.test_pen.name, "another dummy name")

    def test_set_pen_type(self):
        self.test_pen.pen_type = "another dummy pen_type"
        self.assertEqual(self.test_pen.pen_type, "another dummy "
                                                 "pen_type")

    def test_set_pen_ink(self):
        self.test_pen.ink_colour = "another dummy ink_colour"
        self.assertEqual(self.test_pen.ink_colour,
                         "another dummy ink_colour")


if __name__ == '__main__':
    unittest.main()
