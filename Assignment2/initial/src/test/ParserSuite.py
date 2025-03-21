import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 4: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 6: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_struct(self):
        input = """func main() { type Person struct { name string; age int; } }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_for_statement(self):
        input = """func main() { for i := 0; i < 10; i += 1 { sum := sum + i; } }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))