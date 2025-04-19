import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_redeclared_variable(self):
        input = """var a int; var b int; var a int;"""
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redeclared_constant(self):
        input = """const a = 1; const a = 2;"""
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclared_function(self):
        input = """func a() {} func a() {}"""
        expect = "Redeclared Function: a\n"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclared_parameter(self):
        input = """func a(x int, x float) {}"""
        expect = "Redeclared Parameter: x\n"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_type_mismatch_variable_declaration(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_type_mismatch_constant_declaration(self):
        input = """const a int = 1.2;"""
        expect = "Type Mismatch: ConstDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_type_mismatch_function_return(self):
        input = """func a() int { return 1.2; }"""
        expect = "Type Mismatch: Return(FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_type_mismatch_function_call(self):
        input = """func a(x int) {} func main() { a(1.2); }"""
        expect = "Type Mismatch: FuncCall(a,[FloatLiteral(1.2)])\n"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_undeclared_variable(self):
        input = """var a int = b;"""
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_undeclared_function(self):
        input = """func main() { a(); }"""
        expect = "Undeclared Function: a\n"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_undeclared_field(self):
        input = """
        type A struct { x int; }
        var a A = A { y: 1 };
        """
        expect = "Undeclared Field: y\n"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_type_mismatch_binary_op(self):
        input = """var a int = 1 + true;"""
        expect = "Type Mismatch: BinaryOp(IntLiteral(1),+,BooleanLiteral(true))\n"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_type_mismatch_unary_op(self):
        input = """var a int = -true;"""
        expect = "Type Mismatch: UnaryOp(-,BooleanLiteral(true))\n"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_type_mismatch_array_literal(self):
        input = """var a [3]int = [3]int {1, 2.2, 3};"""
        expect = "Type Mismatch: ArrayLiteral([IntLiteral(3)],IntType,[IntLiteral(1),FloatLiteral(2.2),IntLiteral(3)])\n"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_type_mismatch_array_index(self):
        input = """var a [3]int; var b = a[1.2];"""
        expect = "Type Mismatch: ArrayCell(Id(a),[FloatLiteral(1.2)])\n"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_type_mismatch_if_condition(self):
        input = """func main() { if (1) {} }"""
        expect = "Type Mismatch: IntLiteral(1)\n"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_type_mismatch_for_condition(self):
        input = """func main() { for (1) {} }"""
        expect = "Type Mismatch: For(IntLiteral(1),Block([]))\n"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_type_mismatch_return_void(self):
        input = """func a() int { return; }"""
        expect = "Type Mismatch: Return()\n"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_type_mismatch_return_non_void(self):
        input = """func a() { return 1; }"""
        expect = "Type Mismatch: Return(IntLiteral(1))\n"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_type_mismatch_struct_literal(self):
        input = """
        type A struct { x int; }
        var a A = A { x: 1.2 };
        """
        expect = "Type Mismatch: StructLiteral(A,[(x,FloatLiteral(1.2))])\n"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_type_mismatch_field_access(self):
        input = """
        type A struct { x int; }
        var a A;
        var b = a.y;
        """
        expect = "Undeclared Field: y\n"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_type_mismatch_method_call(self):
        input = """
        type A struct {}
        func (a A) foo(x int) {}
        var a A;
        func main() { a.foo(1.2); }
        """
        expect = "Type Mismatch: MethodCall(Id(a),foo,[FloatLiteral(1.2)])\n"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_type_mismatch_array_type(self):
        input = """var a [3]int = [3]float {1.1, 2.2, 3.3};"""
        expect = "Type Mismatch: VarDecl(a,ArrayType(IntType,[IntLiteral(3)]),ArrayLiteral([IntLiteral(3)],FloatType,[FloatLiteral(1.1),FloatLiteral(2.2),FloatLiteral(3.3)]))\n"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_type_mismatch_array_assignment(self):
        input = """
        func main() {
            var a [3]int;
            a := [3]float {1.1, 2.2, 3.3};
        }
        """
        expect = "Type Mismatch: Assign(Id(a),ArrayLiteral([IntLiteral(3)],FloatType,[FloatLiteral(1.1),FloatLiteral(2.2),FloatLiteral(3.3)]))\n"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_type_mismatch_function_argument_count(self):
        input = """func a(x int) {} func main() { a(1, 2); }"""
        expect = "Type Mismatch: FuncCall(a,[IntLiteral(1),IntLiteral(2)])\n"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_type_mismatch_function_argument_type(self):
        input = """func a(x int) {} func main() { a(true); }"""
        expect = "Type Mismatch: FuncCall(a,[BooleanLiteral(true)])\n"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_type_mismatch_return_array(self):
        input = """func a() [3]int { return [3]float {1.1, 2.2, 3.3}; }"""
        expect = "Type Mismatch: Return(ArrayLiteral([IntLiteral(3)],FloatType,[FloatLiteral(1.1),FloatLiteral(2.2),FloatLiteral(3.3)]))\n"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_type_mismatch_return_struct(self):
        input = """
        type A struct { x int; }
        func a() A { return A { x: 1.2 }; }
        """
        expect = "Type Mismatch: StructLiteral(A,[(x,FloatLiteral(1.2))])\n"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_type_mismatch_return_interface(self):
        input = """
        type I interface { foo() int; }
        type A struct {}
        func a() I { return A {}; }
        """
        expect = "Type Mismatch: Return(StructLiteral(A,[]))\n"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_type_mismatch_return_void_in_interface(self):
        input = """
        type I interface { foo() int; }
        type A struct {}
        func (a A) foo() {}
        func a() I { return A {}; }
        """
        expect = "Type Mismatch: Return(StructLiteral(A,[]))\n"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_type_mismatch_return_array_dimension(self):
        input = """func a() [3]int { return [4]int {1, 2, 3, 4}; }"""
        expect = "Type Mismatch: Return(ArrayLiteral([IntLiteral(4)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))\n"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_type_mismatch_return_array_element_type(self):
        input = """func a() [3]int { return [3]float {1.1, 2.2, 3.3}; }"""
        expect = "Type Mismatch: Return(ArrayLiteral([IntLiteral(3)],FloatType,[FloatLiteral(1.1),FloatLiteral(2.2),FloatLiteral(3.3)]))\n"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_type_mismatch_return_struct_field_type(self):
        input = """
        type A struct { x int; }
        func a() A { return A { x: 1.2 }; }
        """
        expect = "Type Mismatch: StructLiteral(A,[(x,FloatLiteral(1.2))])\n"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_type_mismatch_return_struct_field_missing(self):
        input = """
        type A struct { x int; y int; }
        func a() A { return A { x: 1 }; }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_type_mismatch_return_struct_field_extra(self):
        input = """
        type A struct { x int; }
        func a() A { return A { x: 1, y: 2 }; }
        """
        expect = "Undeclared Field: y\n"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_type_mismatch_return_struct_field_type_mismatch(self):
        input = """
        type A struct { x int; }
        func a() A { return A { x: true }; }
        """
        expect = "Type Mismatch: StructLiteral(A,[(x,BooleanLiteral(true))])\n"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_type_mismatch_return_struct_field_order(self):
        input = """
        type A struct { x int; y int; }
        func a() A { return A { y: 1, x: 2 }; }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_type_mismatch_return_struct_field_duplicate(self):
        input = """
        type A struct { x int; }
        func a() A { return A { x: 1, x: 2 }; }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_type_mismatch_return_struct_field_missing_and_extra(self):
        input = """
        type A struct { x int; y int; }
        func a() A { return A { x: 1, z: 2 }; }
        """
        expect = "Undeclared Field: z\n"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_type_mismatch_return_struct_field_missing_and_type_mismatch(self):
        input = """
        type A struct { x int; y int; }
        func a() A { return A { x: true, y: 1 }; }
        """
        expect = "Type Mismatch: StructLiteral(A,[(x,BooleanLiteral(true)),(y,IntLiteral(1))])\n"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_type_mismatch_return_struct_field_extra_and_type_mismatch(self):
        input = """
        type A struct { x int; }
        func a() A { return A { x: true, y: 1 }; }
        """
        expect = "Type Mismatch: StructLiteral(A,[(x,BooleanLiteral(true)),(y,IntLiteral(1))])\n"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_redeclared_prototype(self):
        input = """
        type A interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Add()
        }
        """
        expect = "Redeclared Prototype: Add\n"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_valid_struct_definition(self):
        input = """
        type Person struct {
            name string
            height float
            weight int
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_redeclared_field(self):
        input = """
        type Person struct {
            name string
            height float
            weight int
            name int
        }
        """
        expect = "Redeclared Field: name\n"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_valid_struct_instance(self):
        input = """
        type Employee struct {
            name string
            salary float
            id int
            active boolean
        }
        var e Employee;
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_valid_struct_with_field_init(self):
        input = """
        type Employee struct {
            name string
            salary float
            id int
            active boolean
        }
        var e Employee = Employee {name: "John"};
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_undeclared_field(self):
        input = """
        type Employee struct {
            name string
            salary float
            id int
            active boolean
        }
        var e Employee = Employee {name: "John", position: "Manager"};
        """
        expect = "Undeclared Field: position\n"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_type_mismatch_struct_field(self):
        input = """
        type Employee struct {
            name string
            salary float
            id int
            active boolean
        }
        var e Employee = Employee {name: "John", salary: "High"};
        """
        expect = "Type Mismatch: StructLiteral(Employee,[(name,StringLiteral(\"John\")),(salary,StringLiteral(\"High\"))])\n"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_valid_nested_struct(self):
        input = """
        type Owner struct {
            name string
            age int
        }
        type Pet struct {
            name string
            owner Owner
        }
        var pet Pet = Pet {name: "Buddy", owner: Owner {name: "Alice", age: 30}};
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_type_mismatch_nested_struct(self):
        input = """
        type Owner struct {
            name string
            age int
        }
        type Animal struct {
            species string
        }
        type Pet struct {
            name string
            owner Owner
        }
        var pet Pet = Pet {name: "Buddy", owner: Animal {species: "Dog"}};
        """
        expect = "Type Mismatch: StructLiteral(Pet,[(name,StringLiteral(\"Buddy\")),(owner,StructLiteral(Animal,[(species,StringLiteral(\"Dog\"))]))])\n"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_valid_deep_nested_struct(self):
        input = """
        type Address struct {
            city string
            zip int
        }
        type Owner struct {
            name string
            address Address
        }
        type Pet struct {
            name string
            owner Owner
        }
        var pet Pet = Pet {name: "Buddy", owner: Owner {name: "Alice", address: Address {city: "New York", zip: 10001}}};
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_undeclared_field_in_nested_struct(self):
        input = """
        type Address struct {
            city string
            zip int
        }
        type Owner struct {
            name string
            address Address
        }
        type Pet struct {
            name string
            owner Owner
        }
        var pet Pet = Pet {name: "Buddy", owner: Owner {name: "Alice", address: Address {city: "New York", state: "NY"}}};
        """
        expect = "Undeclared Field: state\n"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_valid_struct_assignment(self):
        input = """
        type Address struct {
            city string
            zip int
        }
        type Owner struct {
            name string
            address Address
        }
        type Pet struct {
            name string
            owner Owner
        }
        var pet1 Pet = Pet {name: "Buddy", owner: Owner {name: "Alice", address: Address {city: "New York", zip: 10001}}};
        var pet2 Pet = pet1;
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_valid_interface_implementation(self):
        input = """
        type Vehicle interface {
            GetSpeed() int
            SetSpeed(speed int)
        }
        type Car struct {
            speed int
        }
        func (c Car) GetSpeed() int {
            return 3;
        }
        func (c Car) SetSpeed(speed int) {
            var a = 12;
        }
        var v Vehicle = Car {speed: 10};
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_incomplete_interface_implementation(self):
        input = """
        type Vehicle interface {
            GetSpeed() int
            SetSpeed(speed int)
        }
        type Car struct {
            speed int
        }
        func (c Car) GetSpeed() int {
            return 3;
        }
        var v Vehicle = Car {speed: 10};
        """
        expect = "Type Mismatch: VarDecl(v,Id(Vehicle),StructLiteral(Car,[(speed,IntLiteral(10))]))\n"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_function_as_variable(self):
        input = """
        func Test() int {
            var a int = 3;
            return a;
        }
        var a int = Test;
        """
        expect = "Type Mismatch: VarDecl(a,IntType,Id(Test))\n"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_function_call_as_variable(self):
        input = """
        func Test() int {
            var a int = 3;
            return a;
        }
        var a int = Test();
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_valid_if_return(self):
        input = """
        func Test() int {
            var a int = 3;
            if (a <= 5) {
                var b int = 4;
                if (b <= 5) {
                    return a;
                } else {
                    return b;
                }
                return b;
            }
            return a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_type_mismatch_function_return(self):
        input = """
        func Test() int {
            var a int = 3;
            if (a <= 5) {
                var b int = 4;
                if (b <= 5) {
                    return a;
                } else if (b > 5) {
                    return b + 1.2;
                } else {
                    return a + b;
                }
                return b;
            }
            return a + 1.2;
        }
        """
        expect = "Type Mismatch: Return(BinaryOp(Id(b),+,FloatLiteral(1.2)))\n"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_valid_struct_return(self):
        input = """
        type Vehicle interface {
            GetSpeed() int
            SetSpeed(speed int)
        }
        type Car struct {
            speed int
        }
        func (c Car) GetSpeed() int {
            return 3;
        }
        func Test() Car {
            var a int = 3;
            if (a <= 5) {
                var b Car = Car {speed: 4};
                const c = 15;
                if (c + 4 <= 5) {
                    return Car {speed: a};
                } else {
                    return b;
                }
                return b;
            }
            return Car {speed: a};
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_type_mismatch_float_to_int_return(self):
        input = """
        func Test() float {
            var a int = 3;
            if (a <= 5) {
                var b int = 4;
                return b;
            }
            return a;
        }
        """
        expect = "Type Mismatch: Return(Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_valid_array_initialization(self):
        input = """
        var arr [5]int = [5]int {1, 2, 3, 4, 5};
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_array_initialization_with_expression(self):
        input = """
        var size = 5;
        var arr [size]int = [size]int {1, 2, 3, 4, 5};
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_array_size_mismatch_error(self):
        input = """
        var arr [4]int = [5]int {1, 2, 3, 4, 5};
        """
        expect = "Type Mismatch: VarDecl(arr,ArrayType(IntType,[IntLiteral(4)]),ArrayLiteral([IntLiteral(5)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))\n"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_array_element_type_mismatch(self):
        input = """
        var arr [3]int = [3]int {1, 2.5, 3};
        """
        expect = "Type Mismatch: ArrayLiteral([IntLiteral(3)],IntType,[IntLiteral(1),FloatLiteral(2.5),IntLiteral(3)])\n"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_valid_multidimensional_array(self):
        input = """
        var matrix [2][3]int = [2][3]int {{1, 2, 3}, {4, 5, 6}};
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_multidimensional_array_type_mismatch(self):
        input = """
        var matrix [2][3]int = [2][3]float {{1.1, 2.2, 3.3}, {4.4, 5.5, 6.6}};
        """
        expect = "Type Mismatch: VarDecl(matrix,ArrayType(IntType,[IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(2),IntLiteral(3)],FloatType,[[FloatLiteral(1.1),FloatLiteral(2.2),FloatLiteral(3.3)],[FloatLiteral(4.4),FloatLiteral(5.5),FloatLiteral(6.6)]]))\n"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_valid_struct_with_array_field(self):
        input = """
        type Student struct {
            name string
            grades [3]int
        }
        var s Student = Student {name: "Alice", grades: [3]int {90, 85, 88}};
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_struct_array_field_type_mismatch(self):
        input = """
        type Student struct {
            name string
            grades [3]int
        }
        var s Student = Student {name: "Alice", grades: [3]float {90.5, 85.2, 88.1}};
        """
        expect = "Type Mismatch: StructLiteral(Student,[(name,StringLiteral(\"Alice\")),(grades,ArrayLiteral([IntLiteral(3)],FloatType,[FloatLiteral(90.5),FloatLiteral(85.2),FloatLiteral(88.1)]))])\n"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_valid_array_assignment(self):
        input = """
        func main() {
            var arr [3]int;
            arr := [3]int {1, 2, 3};
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_array_assignment_type_mismatch(self):
        input = """
        func main() {
            var arr [3]int;
            arr := [3]float {1.1, 2.2, 3.3};
        }
        """
        expect = "Type Mismatch: Assign(Id(arr),ArrayLiteral([IntLiteral(3)],FloatType,[FloatLiteral(1.1),FloatLiteral(2.2),FloatLiteral(3.3)]))\n"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_valid_function_returning_array(self):
        input = """
        func getArray() [3]int {
            return [3]int {1, 2, 3};
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_function_returning_array_type_mismatch(self):
        input = """
        func getArray() [3]int {
            return [3]float {1.1, 2.2, 3.3};
        }
        """
        expect = "Type Mismatch: Return(ArrayLiteral([IntLiteral(3)],FloatType,[FloatLiteral(1.1),FloatLiteral(2.2),FloatLiteral(3.3)]))\n"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_valid_array_index_access(self):
        input = """
        func main() {
            var arr [3]int = [3]int {1, 2, 3};
            var x = arr[1];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_array_index_access_type_mismatch(self):
        input = """
        func main() {
            var arr [3]int = [3]int {1, 2, 3};
            var x = arr[1.5];
        }
        """
        expect = "Type Mismatch: ArrayCell(Id(arr),[FloatLiteral(1.5)])\n"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_valid_array_in_struct(self):
        input = """
        type Matrix struct {
            data [2][2]int
        }
        var m Matrix = Matrix {data: [2][2]int {{1, 2}, {3, 4}}};
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_array_in_struct_type_mismatch(self):
        input = """
        type Matrix struct {
            data [2][2]int
        }
        var m Matrix = Matrix {data: [2][2]float {{1.1, 2.2}, {3.3, 4.4}}};
        """
        expect = "Type Mismatch: StructLiteral(Matrix,[(data,ArrayLiteral([IntLiteral(2),IntLiteral(2)],FloatType,[[FloatLiteral(1.1),FloatLiteral(2.2)],[FloatLiteral(3.3),FloatLiteral(4.4)]]))])\n"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_valid_array_return_in_function(self):
        input = """
        func getMatrix() [2][2]int {
            return [2][2]int {{1, 2}, {3, 4}};
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_array_return_in_function_type_mismatch(self):
        input = """
        func getMatrix() [2][2]int {
            return [2][2]float {{1.1, 2.2}, {3.3, 4.4}};
        }
        """
        expect = "Type Mismatch: Return(ArrayLiteral([IntLiteral(2),IntLiteral(2)],FloatType,[[FloatLiteral(1.1),FloatLiteral(2.2)],[FloatLiteral(3.3),FloatLiteral(4.4)]]))\n"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_valid_array_field_access(self):
        input = """
        type Matrix struct {
            data [2][2]int
        }
        func main() {
            var m Matrix = Matrix {data: [2][2]int {{1, 2}, {3, 4}}};
            var x = m.data[0][1];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_array_field_access_type_mismatch(self):
        input = """
        type Matrix struct {
            data [2][2]int
        }
        func main() {
            var m Matrix = Matrix {data: [2][2]int {{1, 2}, {3, 4}}};
            var x = m.data[0.5][1];
        }
        """
        expect = "Type Mismatch: ArrayCell(FieldAccess(Id(m),data),[FloatLiteral(0.5),IntLiteral(1)])\n"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_valid_nested_field_access(self):
        input = """
        type Address struct {
            city string
            zip int
        }
        type Person struct {
            name string
            address Address
        }
        func main() {
            var p Person = Person {name: "John", address: Address {city: "New York", zip: 10001}};
            var city = p.address.city;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_undeclared_nested_field_access(self):
        input = """
        type Address struct {
            city string
            zip int
        }
        type Person struct {
            name string
            address Address
        }
        func main() {
            var p Person = Person {name: "John", address: Address {city: "New York", zip: 10001}};
            var state = p.address.state;
        }
        """
        expect = "Undeclared Field: state\n"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_type_mismatch_nested_field_access(self):
        input = """
        type Address struct {
            city string
            zip int
        }
        type Person struct {
            name string
            address Address
        }
        func main() {
            var p Person = Person {name: "John", address: Address {city: "New York", zip: 10001}};
            var zip string = p.address.zip;
        }
        """
        expect = "Type Mismatch: VarDecl(zip,StringType,FieldAccess(FieldAccess(Id(p),address),zip))\n"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_valid_deep_nested_field_access(self):
        input = """
        type Address struct {
            city string
            zip int
        }
        type Company struct {
            name string
            address Address
        }
        type Employee struct {
            name string
            company Company
        }
        func main() {
            var e Employee = Employee {name: "Alice", company: Company {name: "TechCorp", address: Address {city: "San Francisco", zip: 94105}}};
            var city = e.company.address.city;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_undeclared_deep_nested_field_access(self):
        input = """
        type Address struct {
            city string
            zip int
        }
        type Company struct {
            name string
            address Address
        }
        type Employee struct {
            name string
            company Company
        }
        func main() {
            var e Employee = Employee {name: "Alice", company: Company {name: "TechCorp", address: Address {city: "San Francisco", zip: 94105}}};
            var state = e.company.address.state;
        }
        """
        expect = "Undeclared Field: state\n"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_type_mismatch_deep_nested_field_access(self):
        input = """
        type Address struct {
            city string
            zip int
        }
        type Company struct {
            name string
            address Address
        }
        type Employee struct {
            name string
            company Company
        }
        func main() {
            var e Employee = Employee {name: "Alice", company: Company {name: "TechCorp", address: Address {city: "San Francisco", zip: 94105}}};
            var zip string = e.company.address.zip;
        }
        """
        expect = "Type Mismatch: VarDecl(zip,StringType,FieldAccess(FieldAccess(FieldAccess(Id(e),company),address),zip))\n"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_valid_field_access_with_function_call(self):
        input = """
        type Address struct {
            city string
            zip int
        }
        type Person struct {
            name string
            address Address
        }
        func getPerson() Person {
            return Person {name: "John", address: Address {city: "New York", zip: 10001}};
        }
        func main() {
            var city = getPerson().address.city;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_undeclared_field_access_with_function_call(self):
        input = """
        type Address struct {
            city string
            zip int
        }
        type Person struct {
            name string
            address Address
        }
        func getPerson() Person {
            return Person {name: "John", address: Address {city: "New York", zip: 10001}};
        }
        func main() {
            var state = getPerson().address.state;
        }
        """
        expect = "Undeclared Field: state\n"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_type_mismatch_field_access_with_function_call(self):
        input = """
        type Address struct {
            city string
            zip int
        }
        type Person struct {
            name string
            address Address
        }
        func getPerson() Person {
            return Person {name: "John", address: Address {city: "New York", zip: 10001}};
        }
        func main() {
            var zip string = getPerson().address.zip;
        }
        """
        expect = "Type Mismatch: VarDecl(zip,StringType,FieldAccess(FieldAccess(FuncCall(getPerson,[]),address),zip))\n"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_valid_field_access_with_array(self):
        input = """
        type Address struct {
            city string
            zip int
        }
        type Person struct {
            name string
            address Address
        }
        func main() {
            var people [2]Person = [2]Person {Person {name: "John", address: Address {city: "New York", zip: 10001}}, Person {name: "Alice", address: Address {city: "Los Angeles", zip: 90001}}};
            var city = people[1].address.city;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_undeclared_field_access_with_array(self):
        input = """
        type Address struct {
            city string
            zip int
        }
        type Person struct {
            name string
            address Address
        }
        func main() {
            var people [2]Person = [2]Person {Person {name: "John", address: Address {city: "New York", zip: 10001}}, Person {name: "Alice", address: Address {city: "Los Angeles", zip: 90001}}};
            var state = people[1].address.state;
        }
        """
        expect = "Undeclared Field: state\n"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_type_mismatch_field_access_with_array(self):
        input = """
        type Address struct {
            city string
            zip int
        }
        type Person struct {
            name string
            address Address
        }
        func main() {
            var people [2]Person = [2]Person {Person {name: "John", address: Address {city: "New York", zip: 10001}}, Person {name: "Alice", address: Address {city: "Los Angeles", zip: 90001}}};
            var zip string = people[1].address.zip;
        }
        """
        expect = "Type Mismatch: VarDecl(zip,StringType,FieldAccess(FieldAccess(ArrayCell(Id(people),[IntLiteral(1)]),address),zip))\n"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_valid_array_cell_access(self):
        input = """
        func main() {
            var arr [5]int = [5]int {1, 2, 3, 4, 5};
            var x = arr[2];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_array_of_struct_type_mismatch(self):
        input = """
        type Book struct {
            title string
            pages int
        }
        func main() {
            var books [2]Book = [2]Book {Book {title: "ok", pages: "ok"}}
        }
        """
        expect = """Type Mismatch: StructLiteral(Book,[(title,StringLiteral("ok")),(pages,StringLiteral("ok"))])\n"""
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_array_cell_access_with_float_index(self):
        input = """
        func main() {
            var arr [5]int = [5]int {1, 2, 3, 4, 5};
            var x = arr[2.5];
        }
        """
        expect = "Type Mismatch: ArrayCell(Id(arr),[FloatLiteral(2.5)])\n"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_array_cell_access_with_boolean_index(self):
        input = """
        func main() {
            var arr [5]int = [5]int {1, 2, 3, 4, 5};
            var x = arr[true];
        }
        """
        expect = "Type Mismatch: ArrayCell(Id(arr),[BooleanLiteral(true)])\n"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_valid_multidimensional_array_cell_access(self):
        input = """
        func main() {
            var matrix [3][3]int = [3][3]int {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
            var x = matrix[1][2];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_multidimensional_array_cell_access_with_float_index(self):
        input = """
        func main() {
            var matrix [3][3]int = [3][3]int {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
            var x = matrix[1.5][2];
        }
        """
        expect = "Type Mismatch: ArrayCell(Id(matrix),[FloatLiteral(1.5),IntLiteral(2)])\n"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_multidimensional_array_cell_access_with_boolean_index(self):
        input = """
        func main() {
            var matrix [3][3]int = [3][3]int {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
            var x = matrix[1][true];
        }
        """
        expect = "Type Mismatch: ArrayCell(Id(matrix),[IntLiteral(1),BooleanLiteral(true)])\n"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_array_cell_assignment(self):
        input = """
        func main() {
            var arr [5]int = [5]int {1, 2, 3, 4, 5};
            arr[2] := 10;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 500))