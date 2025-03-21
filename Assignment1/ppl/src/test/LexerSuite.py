import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        """Verify lowercase identifiers"""
        self.assertTrue(TestLexer.checkLexeme("a[2][3]", "xyz,<EOF>", 100))

    # def test_uppercase_identifier(self):
    #     """Verify uppercase identifiers"""
    #     self.assertTrue(TestLexer.checkLexeme("XYZ", "XYZ,<EOF>", 101))

    # def test_mixed_case_identifier(self):
    #     """Verify mixed case identifiers"""
    #     self.assertTrue(TestLexer.checkLexeme("aXy123", "aXy123,<EOF>", 102))

    # def test_identifier_with_underscore(self):
    #     """Verify identifiers containing underscores"""
    #     self.assertTrue(TestLexer.checkLexeme("_def", "_def,<EOF>", 103))

    # def test_identifier_starting_with_underscore(self):
    #     """Verify identifiers starting with an underscore"""
    #     self.assertTrue(TestLexer.checkLexeme("_def456", "_def456,<EOF>", 104))

    # def test_identifier_with_digit_in_middle(self):
    #     """Verify identifiers with digits"""
    #     self.assertTrue(TestLexer.checkLexeme("def456", "def456,<EOF>", 105))

    # def test_identifier_with_digit_and_underscore(self):
    #     """Verify identifiers with digits and underscores"""
    #     self.assertTrue(TestLexer.checkLexeme("def_456", "def_456,<EOF>", 106))

    # def test_invalid_identifier_starting_with_digit(self):
    #     """Check invalid identifiers starting with digits"""
    #     self.assertTrue(TestLexer.checkLexeme("456def", "456,def,<EOF>", 107))

    # def test_invalid_identifier_with_hyphen(self):
    #     """Check invalid identifiers with hyphens"""
    #     self.assertTrue(TestLexer.checkLexeme("def-456", "def,-,456,<EOF>", 108))

    # def test_invalid_identifier_with_special_symbol(self):
    #     """Check invalid identifiers with special symbols"""
    #     self.assertTrue(TestLexer.checkLexeme("def@456", "def,ErrorToken @", 109))

    # def test_keyword_if_statement(self):
    #     """Verify 'if' keyword"""
    #     self.assertTrue(TestLexer.checkLexeme("if", "if,<EOF>", 110))

    # def test_keyword_else_statement(self):
    #     """Verify 'else' keyword"""
    #     self.assertTrue(TestLexer.checkLexeme("else", "else,<EOF>", 111))

    # def test_keyword_for_loop(self):
    #     """Verify 'for' keyword"""
    #     self.assertTrue(TestLexer.checkLexeme("for", "for,<EOF>", 112))

    # def test_keyword_return_statement(self):
    #     """Verify 'return' keyword"""
    #     self.assertTrue(TestLexer.checkLexeme("return", "return,<EOF>", 113))

    # def test_keyword_func_declaration(self):
    #     """Verify 'func' keyword"""
    #     self.assertTrue(TestLexer.checkLexeme("func", "func,<EOF>", 114))

    # def test_keyword_type_declaration(self):
    #     """Verify 'type' keyword"""
    #     self.assertTrue(TestLexer.checkLexeme("type", "type,<EOF>", 115))

    # def test_integer_literal_decimal(self):
    #     """Test integer literals in decimal"""
    #     self.assertTrue(TestLexer.checkLexeme("456", "456,<EOF>", 116))

    # def test_integer_literal_binary_format(self):
    #     """Test binary integer literals"""
    #     self.assertTrue(TestLexer.checkLexeme("0b101010", "0b101010,<EOF>", 117))

    # def test_integer_literal_octal_format(self):
    #     """Test octal integer literals"""
    #     self.assertTrue(TestLexer.checkLexeme("0o123", "0o123,<EOF>", 118))

    # def test_integer_literal_hexadecimal_format(self):
    #     """Test hexadecimal integer literals"""
    #     self.assertTrue(TestLexer.checkLexeme("0x1F", "0x1F,<EOF>", 119))

    # def test_invalid_integer_literal_binary(self):
    #     """Test invalid binary integer literals"""
    #     self.assertTrue(TestLexer.checkLexeme("0b102", "0b10,2,<EOF>", 120))

    # def test_invalid_integer_literal_octal(self):
    #     """Test invalid octal integer literals"""
    #     self.assertTrue(TestLexer.checkLexeme("0o19", "0o1,9,<EOF>", 121))

    # def test_invalid_integer_literal_hexadecimal(self):
    #     """Test invalid hexadecimal integer literals"""
    #     self.assertTrue(TestLexer.checkLexeme("0xGH", "0,xGH,<EOF>", 122))

    # def test_float_literal(self):
    #     """Verify float literals"""
    #     self.assertTrue(TestLexer.checkLexeme("3.1415", "3.1415,<EOF>", 123))

    # def test_float_literal_with_exponent(self):
    #     """Verify float literals with exponent"""
    #     self.assertTrue(TestLexer.checkLexeme("1.23e4", "1.23e4,<EOF>", 124))

    # def test_boolean_literal_true(self):
    #     """Verify boolean literals - true"""
    #     self.assertTrue(TestLexer.checkLexeme("true", "true,<EOF>", 125))

    # def test_boolean_literal_false(self):
    #     """Verify boolean literals - false"""
    #     self.assertTrue(TestLexer.checkLexeme("false", "false,<EOF>", 126))

    # def test_operator_addition(self):
    #     """Verify the '+' operator"""
    #     self.assertTrue(TestLexer.checkLexeme("+", "+,<EOF>", 127))

    # def test_operator_multiplication(self):
    #     """Verify the '*' operator"""
    #     self.assertTrue(TestLexer.checkLexeme("*", "*,<EOF>", 128))

    # def test_operator_comparison(self):
    #     """Verify the '==' operator"""
    #     self.assertTrue(TestLexer.checkLexeme("==", "==,<EOF>", 129))

    # def test_separator_parentheses(self):
    #     """Verify parentheses separator"""
    #     self.assertTrue(TestLexer.checkLexeme("(", "(,<EOF>", 130))

    # def test_separator_semicolon(self):
    #     """Verify semicolon separator"""
    #     self.assertTrue(TestLexer.checkLexeme(";", ";,<EOF>", 131))

    # def test_single_line_comment(self):
    #     """Verify single-line comment"""
    #     self.assertTrue(TestLexer.checkLexeme("// comment", "<EOF>", 132))

    # def test_multi_line_comment(self):
    #     """Verify multi-line comment"""
    #     self.assertTrue(TestLexer.checkLexeme("/* multi-line comment */", "<EOF>", 133))

    # def test_mixed_tokens_with_comments(self):
    #     """Test tokens with comments"""
    #     self.assertTrue(TestLexer.checkLexeme("int x = 10; // initializing x", "int,x,=,10,;,<EOF>", 134))

    # def test_mixed_tokens_with_string_literal(self):
    #     """Test tokens with string literals"""
    #     self.assertTrue(TestLexer.checkLexeme('string str = "hello";', "string,str,=,hello,;,<EOF>", 135))

    # def test_mixed_tokens_with_float_literal(self):
    #     """Test tokens with float literals"""
    #     self.assertTrue(TestLexer.checkLexeme("float pi = 3.1415;", "float,pi,=,3.1415,;,<EOF>", 136))

    # def test_mixed_tokens_with_method(self):
    #     """test mixed tokens"""
    #     self.assertTrue(
    #         TestLexer.
    #         checkLexeme("""
    #                     func (r *Rectangle) scale(factor int) {
    #                     r.width *= factor
    #                     r.height *= factor
    #                 }""", "func,(,r,*,Rectangle,),scale,(,factor,int,),{,r,.,width,*=,factor,;,r,.,height,*=,factor,;,},<EOF>", 137))

    # def test_mixed_tokens_with_method_newline(self):
    #     """test mixed tokens"""
    #     self.assertTrue(
    #         TestLexer.
    #         checkLexeme("""
    #                     func (r *Rectangle) scale(factor int) {
    #                     r.width *= factor
    #                     r.height *= factor
    #                 }\n""", "func,(,r,*,Rectangle,),scale,(,factor,int,),{,r,.,width,*=,factor,;,r,.,height,*=,factor,;,},;,<EOF>", 138))
