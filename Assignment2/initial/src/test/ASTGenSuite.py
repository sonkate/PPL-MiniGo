#  Tran Thanh Son - 2053405
import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {}"""
        input = """func main() {};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """var x int ;"""
        expect = str(Program([VarDecl("x", IntType(), None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_call_without_parameter(self):
        """More complex program"""
        input = """func main () {}; var x int ;"""
        expect = str(
            Program(
                [
                    FuncDecl("main", [], VoidType(), Block([])),
                    VarDecl("x", IntType(), None),
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_function_with_parameters(self):
        """Function with parameters"""
        input = """func add(a int, b,c float) float {};"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "add",
                        [
                            ParamDecl("a", IntType()),
                            ParamDecl("b", FloatType()),
                            ParamDecl("c", FloatType()),
                        ],
                        FloatType(),
                        Block([]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_method_declaration(self):
        """Method declaration"""
        input = """func (r Receiver) methodName(a int, b,c float) float {};"""
        expect = str(
            Program(
                [
                    MethodDecl(
                        "r",
                        Id("Receiver"),
                        FuncDecl(
                            "methodName",
                            [
                                ParamDecl("a", IntType()),
                                ParamDecl("b", FloatType()),
                                ParamDecl("c", FloatType()),
                            ],
                            FloatType(),
                            Block([]),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_interface_declaration(self):
        """Interface declaration"""
        input = """
        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset();
            SayHello(name string);
        }
        """
        expect = str(
            Program(
                [
                    InterfaceType(
                        "Calculator",
                        [
                            Prototype("Add", [IntType(), IntType()], IntType()),
                            Prototype(
                                "Subtract",
                                [FloatType(), FloatType(), IntType()],
                                FloatType(),
                            ),
                            Prototype("Reset", [], VoidType()),
                            Prototype("SayHello", [StringType()], VoidType()),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_array_cell_declaration(self):
        """Array cell declaration"""
        input = """var arr [10]int;"""
        expect = str(
            Program(
                [
                    VarDecl("arr", ArrayType([IntLiteral(10)], IntType()), None),
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_two_dimensional_array_declaration(self):
        """Two-dimensional array declaration"""
        input = """var arr [10][20]int;"""
        expect = str(
            Program(
                [
                    VarDecl(
                        "arr",
                        ArrayType([IntLiteral(10), IntLiteral(20)], IntType()),
                        None,
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_array_cell_assignment(self):
        """Array cell assignment"""
        input = """var a = arr[1][2] + 3;"""
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        None,
                        BinaryOp(
                            "+",
                            ArrayCell(Id("arr"), [IntLiteral(1), IntLiteral(2)]),
                            IntLiteral(3),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    # # # statement test
    def test_var_decl(self):
        """Variable declaration"""
        input = """func main() { var x int; };"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main", [], VoidType(), Block([VarDecl("x", IntType(), None)])
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_const_decl(self):
        """Constant declaration"""
        input = """func main() { const y = 10; }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block([ConstDecl("y", None, IntLiteral(10))]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_struct_decl(self):
        """Struct declaration"""
        input = """func main() { type Person struct { name string; age int; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                StructType(
                                    "Person",
                                    [("name", StringType()), ("age", IntType())],
                                    [],
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_method_decl(self):
        """Method declaration"""
        input = (
            """func main() { func (p Person) getName() string { return p.name; } }"""
        )
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                MethodDecl(
                                    "p",
                                    Id("Person"),
                                    FuncDecl(
                                        "getName",
                                        [],
                                        StringType(),
                                        Block([Return(FieldAccess(Id("p"), "name"))]),
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_struct_with_field_and_method(self):
        """Struct with field and method"""
        input = """
        type Calculator struct {
            value int;
        }
        func (c Calculator) Add(x int) int {
            return c.value + x;
        }
        """
        expect = str(
            Program(
                [
                    StructType("Calculator", [("value", IntType())], []),
                    MethodDecl(
                        "c",
                        Id("Calculator"),
                        FuncDecl(
                            "Add",
                            [ParamDecl("x", IntType())],
                            IntType(),
                            Block(
                                [
                                    Return(
                                        BinaryOp(
                                            "+", FieldAccess(Id("c"), "value"), Id("x")
                                        )
                                    )
                                ]
                            ),
                        ),
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_assign_stmt_simple(self):
        """Assignment statement"""
        input = """func main() { x := 5; }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main", [], VoidType(), Block([Assign(Id("x"), IntLiteral(5))])
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_assign_stmt_all_op(self):
        """Assignment statement"""
        input = """func main() {
                        a := 1;
                        a += 1;
                        a -= 1;
                        a *= 1;
                        a /= 1;
                        a %= 1;
                    }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                Assign(Id("a"), IntLiteral(1)),
                                Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))),
                                Assign(Id("a"), BinaryOp("-", Id("a"), IntLiteral(1))),
                                Assign(Id("a"), BinaryOp("*", Id("a"), IntLiteral(1))),
                                Assign(Id("a"), BinaryOp("/", Id("a"), IntLiteral(1))),
                                Assign(Id("a"), BinaryOp("%", Id("a"), IntLiteral(1))),
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_assign_array_element(self):
        """Assignment to array element"""
        input = """func main() { arr[2] *= 3; }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                Assign(
                                    ArrayCell(Id("arr"), [IntLiteral(2)]),
                                    BinaryOp(
                                        "*",
                                        ArrayCell(Id("arr"), [IntLiteral(2)]),
                                        IntLiteral(3),
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_assign_struct_field(self):
        """Assignment to struct field"""
        input = """func main() { person.age := 30; }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [Assign(FieldAccess(Id("person"), "age"), IntLiteral(30))]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_if_stmt(self):
        """If statement"""
        input = """func main() { if (x > 0) { y := 1; } else { y := 2; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(">", Id("x"), IntLiteral(0)),
                                    Block([Assign(Id("y"), IntLiteral(1))]),
                                    Block([Assign(Id("y"), IntLiteral(2))]),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_if_stmt_without_else(self):
        """If statement without else"""
        input = """func main() { if (x > 0) { y := 1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(">", Id("x"), IntLiteral(0)),
                                    Block([Assign(Id("y"), IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_if_elif_else_stmt(self):
        """If-Else If-Else statement"""
        input = """func main() {
            if (x > 0) {
                y := 1
            } else if (x == 0) {
                y := 0
            } else {
                y := -1
            }
        }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(">", Id("x"), IntLiteral(0)),
                                    Block([Assign(Id("y"), IntLiteral(1))]),
                                    If(
                                        BinaryOp("==", Id("x"), IntLiteral(0)),
                                        Block([Assign(Id("y"), IntLiteral(0))]),
                                        Block(
                                            [
                                                Assign(
                                                    Id("y"), UnaryOp("-", IntLiteral(1))
                                                )
                                            ]
                                        ),
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_if_two_elif_no_else_stmt(self):
        """If statement with two Else If clauses but no Else clause"""
        input = """func main() {
            if (x > 0) {
                y := 1;
            } else if (x == 0) {
                y := 0;
            } else if (x < 0) {
                y := -1;
            }
        }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(">", Id("x"), IntLiteral(0)),
                                    Block([Assign(Id("y"), IntLiteral(1))]),
                                    If(
                                        BinaryOp("==", Id("x"), IntLiteral(0)),
                                        Block([Assign(Id("y"), IntLiteral(0))]),
                                        If(
                                            BinaryOp("<", Id("x"), IntLiteral(0)),
                                            Block(
                                                [
                                                    Assign(
                                                        Id("y"),
                                                        UnaryOp("-", IntLiteral(1)),
                                                    )
                                                ]
                                            ),
                                            None,
                                        ),
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_init_for_stmt(self):
        """For statement"""
        input = """func main() { for i := 0; i < 10; i += 1 { sum := sum + i; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForStep(
                                    Assign(Id("i"), IntLiteral(0)),
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Assign(
                                        Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))
                                    ),
                                    Block(
                                        [
                                            Assign(
                                                Id("sum"),
                                                BinaryOp("+", Id("sum"), Id("i")),
                                            )
                                        ]
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_basic_for_loop(self):
        """Basic For Loop"""
        input = """func main() {
            for i < 10 {
                sum += i;
                i += 1;
            }
        }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForBasic(
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Block(
                                        [
                                            Assign(
                                                Id("sum"),
                                                BinaryOp("+", Id("sum"), Id("i")),
                                            ),
                                            Assign(
                                                Id("i"),
                                                BinaryOp("+", Id("i"), IntLiteral(1)),
                                            ),
                                        ]
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_range_for_loop_with_array_declaration(self):
        """Range For Loop with Array Declaration"""
        input = """func main() {
            arr := [3]int{10, 20, 30};
            for index, value := range arr {
                sum += value;
            }
        }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                Assign(
                                    Id("arr"),
                                    ArrayLiteral(
                                        [IntLiteral(3)],
                                        IntType(),
                                        [
                                            IntLiteral(10),
                                            IntLiteral(20),
                                            IntLiteral(30),
                                        ],
                                    ),
                                ),
                                ForEach(
                                    Id("index"),
                                    Id("value"),
                                    Id("arr"),
                                    Block(
                                        [
                                            Assign(
                                                Id("sum"),
                                                BinaryOp("+", Id("sum"), Id("value")),
                                            )
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_break_stmt(self):
        """Break statement"""
        input = """func main() { for i := 0; i < 10; i := i + 1 { if (i == 5) { break; } } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForStep(
                                    Assign(Id("i"), IntLiteral(0)),
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Assign(
                                        Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))
                                    ),
                                    Block(
                                        [
                                            If(
                                                BinaryOp("==", Id("i"), IntLiteral(5)),
                                                Block([Break()]),
                                                None,
                                            )
                                        ]
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_continue_stmt(self):
        """Continue statement"""
        input = """func main() { for i := 0; i < 10; i := i + 1 { if (i % 2 == 0) { continue; } } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForStep(
                                    Assign(Id("i"), IntLiteral(0)),
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Assign(
                                        Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))
                                    ),
                                    Block(
                                        [
                                            If(
                                                BinaryOp(
                                                    "==",
                                                    BinaryOp(
                                                        "%", Id("i"), IntLiteral(2)
                                                    ),
                                                    IntLiteral(0),
                                                ),
                                                Block([Continue()]),
                                                None,
                                            )
                                        ]
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_call_stmt(self):
        """Call statement"""
        input = """func main() { foo(); }"""
        expect = str(
            Program([FuncDecl("main", [], VoidType(), Block([FuncCall("foo", [])]))])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_call_stmt_with_params(self):
        """Call statement with parameters"""
        input = """func main() { foo(1, 2, 3); }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                FuncCall(
                                    "foo", [IntLiteral(1), IntLiteral(2), IntLiteral(3)]
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_return_stmt(self):
        """Return statement"""
        input = """func main() { return; }"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_body(self):
        """Body"""
        input = """func main() { { var x int; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block([Block([VarDecl("x", IntType(), None)])]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_if_stmt_with_logical_and(self):
        """If statement with logical AND"""
        input = """func main() { if (x > 0 && y < 10) { z := 1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(
                                        "&&",
                                        BinaryOp(">", Id("x"), IntLiteral(0)),
                                        BinaryOp("<", Id("y"), IntLiteral(10)),
                                    ),
                                    Block([Assign(Id("z"), IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_if_stmt_with_logical_or(self):
        """If statement with logical OR"""
        input = """func main() { if (x > 0 || y < 10) { z := 1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(
                                        "||",
                                        BinaryOp(">", Id("x"), IntLiteral(0)),
                                        BinaryOp("<", Id("y"), IntLiteral(10)),
                                    ),
                                    Block([Assign(Id("z"), IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_if_stmt_with_nested_if(self):
        """If statement with nested if"""
        input = """func main() { if (x > 0) { if (y < 10) { z := 1; } } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(">", Id("x"), IntLiteral(0)),
                                    Block(
                                        [
                                            If(
                                                BinaryOp("<", Id("y"), IntLiteral(10)),
                                                Block([Assign(Id("z"), IntLiteral(1))]),
                                                None,
                                            )
                                        ]
                                    ),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_if_stmt_with_logical_not(self):
        """If statement with logical NOT"""
        input = """func main() { if (!(x > 0)) { z := 1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    UnaryOp("!", BinaryOp(">", Id("x"), IntLiteral(0))),
                                    Block([Assign(Id("z"), IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_if_stmt_with_comparison(self):
        """If statement with comparison"""
        input = """func main() { if (x == y) { z := 1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp("==", Id("x"), Id("y")),
                                    Block([Assign(Id("z"), IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_if_stmt_with_arithmetic(self):
        """If statement with arithmetic"""
        input = """func main() { if (x + y > 10) { z := 1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(
                                        ">",
                                        BinaryOp("+", Id("x"), Id("y")),
                                        IntLiteral(10),
                                    ),
                                    Block([Assign(Id("z"), IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_if_stmt_with_function_call(self):
        """If statement with function call"""
        input = """func main() { if (foo() > 10) { z := 1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(">", FuncCall("foo", []), IntLiteral(10)),
                                    Block([Assign(Id("z"), IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_if_stmt_with_array_access(self):
        """If statement with array access"""
        input = """func main() { if (arr[0] > 10) { z := 1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(
                                        ">",
                                        ArrayCell(Id("arr"), [IntLiteral(0)]),
                                        IntLiteral(10),
                                    ),
                                    Block([Assign(Id("z"), IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_if_stmt_with_struct_field_access(self):
        """If statement with struct field access"""
        input = """func main() { if (person.age > 30) { z := 1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(
                                        ">",
                                        FieldAccess(Id("person"), "age"),
                                        IntLiteral(30),
                                    ),
                                    Block([Assign(Id("z"), IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_if_stmt_with_method_call(self):
        """If statement with method call"""
        input = """func main() { if (person.getAge() > 30) { z := 1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(
                                        ">",
                                        MethCall(Id("person"), "getAge", []),
                                        IntLiteral(30),
                                    ),
                                    Block([Assign(Id("z"), IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_if_stmt_with_multiple_conditions(self):
        """If statement with multiple conditions"""
        input = """func main() { if (x > 0 && y < 10 || z == 5) { a := 1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(
                                        "||",
                                        BinaryOp(
                                            "&&",
                                            BinaryOp(">", Id("x"), IntLiteral(0)),
                                            BinaryOp("<", Id("y"), IntLiteral(10)),
                                        ),
                                        BinaryOp("==", Id("z"), IntLiteral(5)),
                                    ),
                                    Block([Assign(Id("a"), IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_if_stmt_with_nested_blocks(self):
        """If statement with nested blocks"""
        input = """func main() { if (x > 0) { { y := 1; } } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(">", Id("x"), IntLiteral(0)),
                                    Block([Block([Assign(Id("y"), IntLiteral(1))])]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_if_stmt_with_else_if(self):
        """If statement with else if"""
        input = (
            """func main() { if (x > 0) { y := 1; } else if (x < 0) { y := -1; } }"""
        )
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(">", Id("x"), IntLiteral(0)),
                                    Block([Assign(Id("y"), IntLiteral(1))]),
                                    If(
                                        BinaryOp("<", Id("x"), IntLiteral(0)),
                                        Block(
                                            [
                                                Assign(
                                                    Id("y"), UnaryOp("-", IntLiteral(1))
                                                )
                                            ]
                                        ),
                                        None,
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_if_stmt_with_else_if_and_else(self):
        """If statement with else if and else"""
        input = """func main() { if (x > 0) { y := 1; } else if (x < 0) { y := -1; } else { y := 0; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(">", Id("x"), IntLiteral(0)),
                                    Block([Assign(Id("y"), IntLiteral(1))]),
                                    If(
                                        BinaryOp("<", Id("x"), IntLiteral(0)),
                                        Block(
                                            [
                                                Assign(
                                                    Id("y"), UnaryOp("-", IntLiteral(1))
                                                )
                                            ]
                                        ),
                                        Block([Assign(Id("y"), IntLiteral(0))]),
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_if_stmt_with_multiple_else_if(self):
        """If statement with multiple else if"""
        input = """func main() { if (x > 0) { y := 1; } else if (x == 0) { y := 0; } else if (x < 0) { y := -1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(">", Id("x"), IntLiteral(0)),
                                    Block([Assign(Id("y"), IntLiteral(1))]),
                                    If(
                                        BinaryOp("==", Id("x"), IntLiteral(0)),
                                        Block([Assign(Id("y"), IntLiteral(0))]),
                                        If(
                                            BinaryOp("<", Id("x"), IntLiteral(0)),
                                            Block(
                                                [
                                                    Assign(
                                                        Id("y"),
                                                        UnaryOp("-", IntLiteral(1)),
                                                    )
                                                ]
                                            ),
                                            None,
                                        ),
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_if_stmt_with_nested_else_if(self):
        """If statement with nested else if"""
        input = """func main() { if (x > 0) { if (y > 0) { z := 1; } else { z := -1; } } else { z := 0; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(">", Id("x"), IntLiteral(0)),
                                    Block(
                                        [
                                            If(
                                                BinaryOp(">", Id("y"), IntLiteral(0)),
                                                Block([Assign(Id("z"), IntLiteral(1))]),
                                                Block(
                                                    [
                                                        Assign(
                                                            Id("z"),
                                                            UnaryOp("-", IntLiteral(1)),
                                                        )
                                                    ]
                                                ),
                                            )
                                        ]
                                    ),
                                    Block([Assign(Id("z"), IntLiteral(0))]),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_if_stmt_with_logical_and_or(self):
        """If statement with logical AND and OR"""
        input = """func main() { if (x > 0 && y < 10 || z == 5) { a := 1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(
                                        "||",
                                        BinaryOp(
                                            "&&",
                                            BinaryOp(">", Id("x"), IntLiteral(0)),
                                            BinaryOp("<", Id("y"), IntLiteral(10)),
                                        ),
                                        BinaryOp("==", Id("z"), IntLiteral(5)),
                                    ),
                                    Block([Assign(Id("a"), IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_if_stmt_with_nested_logical_and_or(self):
        """If statement with nested logical AND and OR"""
        input = """func main() { if ((x > 0 && y < 10) || (z == 5 && w != 0)) { a := 1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp(
                                        "||",
                                        BinaryOp(
                                            "&&",
                                            BinaryOp(">", Id("x"), IntLiteral(0)),
                                            BinaryOp("<", Id("y"), IntLiteral(10)),
                                        ),
                                        BinaryOp(
                                            "&&",
                                            BinaryOp("==", Id("z"), IntLiteral(5)),
                                            BinaryOp("!=", Id("w"), IntLiteral(0)),
                                        ),
                                    ),
                                    Block([Assign(Id("a"), IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_if_stmt_with_nested_logical_not(self):
        """If statement with nested logical NOT"""
        input = """func main() { if (!(x > 0 && !(y < 10))) { a := 1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    UnaryOp(
                                        "!",
                                        BinaryOp(
                                            "&&",
                                            BinaryOp(">", Id("x"), IntLiteral(0)),
                                            UnaryOp(
                                                "!",
                                                BinaryOp("<", Id("y"), IntLiteral(10)),
                                            ),
                                        ),
                                    ),
                                    Block([Assign(Id("a"), IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_if_stmt_with_nested_logical_not_and_or(self):
        """If statement with nested logical NOT, AND, and OR"""
        input = """func main() { if (!(x > 0 && !(y < 10 || z == 5))) { a := 1; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                If(
                                    UnaryOp(
                                        "!",
                                        BinaryOp(
                                            "&&",
                                            BinaryOp(">", Id("x"), IntLiteral(0)),
                                            UnaryOp(
                                                "!",
                                                BinaryOp(
                                                    "||",
                                                    BinaryOp(
                                                        "<", Id("y"), IntLiteral(10)
                                                    ),
                                                    BinaryOp(
                                                        "==", Id("z"), IntLiteral(5)
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                    Block([Assign(Id("a"), IntLiteral(1))]),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_for_loop_with_simple_increment(self):
        """For loop with simple increment"""
        input = """func main() { for i := 0; i < 10; i += 1 { sum += i; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForStep(
                                    Assign(Id("i"), IntLiteral(0)),
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                                    Block([Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("i")))])
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_for_loop_with_simple_decrement(self):
        """For loop with simple decrement"""
        input = """func main() { for i := 10; i > 0; i -= 1 { sum += i; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForStep(
                                    Assign(Id("i"), IntLiteral(10)),
                                    BinaryOp(">", Id("i"), IntLiteral(0)),
                                    Assign(Id("i"), BinaryOp("-", Id("i"), IntLiteral(1))),
                                    Block([Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("i")))])
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_for_loop_with_nested_loops(self):
        """For loop with nested loops"""
        input = """func main() { for i := 0; i < 10; i += 1 { for j := 0; j < 5; j += 1 { sum += i + j; } } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForStep(
                                    Assign(Id("i"), IntLiteral(0)),
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                                    Block(
                                        [
                                            ForStep(
                                                Assign(Id("j"), IntLiteral(0)),
                                                BinaryOp("<", Id("j"), IntLiteral(5)),
                                                Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1))),
                                                Block([Assign(Id("sum"), BinaryOp("+", Id("sum"), BinaryOp("+", Id("i"), Id("j"))))])
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_for_loop_with_break(self):
        """For loop with break statement"""
        input = """func main() { for i := 0; i < 10; i += 1 { if (i == 5) { break; } sum += i; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForStep(
                                    Assign(Id("i"), IntLiteral(0)),
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                                    Block(
                                        [
                                            If(
                                                BinaryOp("==", Id("i"), IntLiteral(5)),
                                                Block([Break()]),
                                                None
                                            ),
                                            Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("i")))
                                        ]
                                    )
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_for_loop_with_continue(self):
        """For loop with continue statement"""
        input = """func main() { for i := 0; i < 10; i += 1 { if (i % 2 == 0) { continue; } sum += i; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForStep(
                                    Assign(Id("i"), IntLiteral(0)),
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                                    Block(
                                        [
                                            If(
                                                BinaryOp("==", BinaryOp("%", Id("i"), IntLiteral(2)), IntLiteral(0)),
                                                Block([Continue()]),
                                                None
                                            ),
                                            Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("i")))
                                        ]
                                    )
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_for_loop_with_function_call(self):
        """For loop with function call"""
        input = """func main() { for i := 0; i < 10; i += 1 { foo(i); } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForStep(
                                    Assign(Id("i"), IntLiteral(0)),
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                                    Block([FuncCall("foo", [Id("i")])])
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_for_loop_with_array_access(self):
        """For loop with array access"""
        input = """func main() { for i := 0; i < 10; i += 1 { sum += arr[i]; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForStep(
                                    Assign(Id("i"), IntLiteral(0)),
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                                    Block([Assign(Id("sum"), BinaryOp("+", Id("sum"), ArrayCell(Id("arr"), [Id("i")])))]),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_for_loop_with_struct_field_access(self):
        """For loop with struct field access"""
        input = """func main() { for i := 0; i < 10; i += 1 { sum += person.age; } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForStep(
                                    Assign(Id("i"), IntLiteral(0)),
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                                    Block([Assign(Id("sum"), BinaryOp("+", Id("sum"), FieldAccess(Id("person"), "age")))]),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_for_loop_with_method_call(self):
        """For loop with method call"""
        input = """func main() { for i := 0; i < 10; i += 1 { sum += person.getAge(); } }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                ForStep(
                                    Assign(Id("i"), IntLiteral(0)),
                                    BinaryOp("<", Id("i"), IntLiteral(10)),
                                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                                    Block([Assign(Id("sum"), BinaryOp("+", Id("sum"), MethCall(Id("person"), "getAge", [])))]),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))
    def test_array_declaration_with_int_type(self):
        """Array declaration with int type"""
        input = """var arr [5]int;"""
        expect = str(
            Program(
                [
                    VarDecl("arr", ArrayType([IntLiteral(5)], IntType()), None),
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_array_declaration_with_float_type(self):
        """Array declaration with float type"""
        input = """var arr [5]float;"""
        expect = str(
            Program(
                [
                    VarDecl("arr", ArrayType([IntLiteral(5)], FloatType()), None),
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_two_dimensional_array_declaration(self):
        """Two-dimensional array declaration"""
        input = """var arr [5][10]int;"""
        expect = str(
            Program(
                [
                    VarDecl("arr", ArrayType([IntLiteral(5), IntLiteral(10)], IntType()), None),
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_three_dimensional_array_declaration(self):
        """Three-dimensional array declaration"""
        input = """var arr [5][10][15]int;"""
        expect = str(
            Program(
                [
                    VarDecl("arr", ArrayType([IntLiteral(5), IntLiteral(10), IntLiteral(15)], IntType()), None),
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_array_assignment_with_int_literal(self):
        """Array assignment with int literal"""
        input = """func main() { arr[0] := 10; }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), IntLiteral(10))
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_array_assignment_with_float_literal(self):
        """Array assignment with float literal"""
        input = """func main() { arr[0] := 10.5; }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), FloatLiteral(10.5))
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_array_assignment_with_expression(self):
        """Array assignment with expression"""
        input = """func main() { arr[0] := 10 + 5; }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), BinaryOp("+", IntLiteral(10), IntLiteral(5)))
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_array_assignment_with_function_call(self):
        """Array assignment with function call"""
        input = """func main() { arr[0] := foo(); }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), FuncCall("foo", []))
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_array_assignment_with_array_access(self):
        """Array assignment with array access"""
        input = """func main() { arr[0] := arr[1]; }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), ArrayCell(Id("arr"), [IntLiteral(1)]))
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_array_assignment_with_struct_field_access(self):
        """Array assignment with struct field access"""
        input = """func main() { arr[0] := person.age; }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), FieldAccess(Id("person"), "age"))
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))
    
    def test_array_assignment_with_simple_array_literal(self):
        """Array assignment with simple array literal"""
        input = """func main() { arr := [3]int{1, 2, 3}; }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                Assign(
                                    Id("arr"),
                                    ArrayLiteral(
                                        [IntLiteral(3)],
                                        IntType(),
                                        [IntLiteral(1), IntLiteral(2), IntLiteral(3)]
                                    )
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_array_assignment_with_nested_array_literal(self):
        """Array assignment with nested array literal"""
        input = """func main() { arr := [2][2]int{{1, 2}, {3, 4}}; }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                Assign(
                                    Id("arr"),
                                    ArrayLiteral(
                                        [IntLiteral(2), IntLiteral(2)],
                                        IntType(),
                                        [[IntLiteral(1), IntLiteral(2)], [IntLiteral(3), IntLiteral(4)]]
                                    )
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))


    def test_array_assignment_with_empty_array_literal(self):
        """Array assignment with empty array literal"""
        input = """func main() { arr := [1]int{}; }"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        [],
                        VoidType(),
                        Block(
                            [
                                Assign(
                                    Id("arr"),
                                    ArrayLiteral(
                                        [IntLiteral(1)],
                                        IntType(),
                                        []
                                    )
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))