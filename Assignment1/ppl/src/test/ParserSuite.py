import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_var_declaration(self):
        """Test variable declaration"""
        input = """var x int
        var y float = 1.0
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_const_declaration(self):
        """Test constant declaration"""
        input = """const PI = 3.14;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_function_with_params(self):
        """Test function with parameters"""
        input = """func add(x int, y int) int {
            return x + y
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_if_statement(self):
        """Test if statement"""
        input = """
        func main() {
            if (x > 0) {
                return x;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_if_else_statement(self):
        """Test if-else statement"""
        input = """func main() {
            if (x > 0) {
                return x
            } else {
                return -x
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_for_loop(self):
        """Test for loop"""
        input = """func main() {
            for i := 0; i < 10; i += 1 {
                print(i)
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_array_declaration(self):
        """Test array declaration"""
        input = """var arr [3]int
        var matrix [2][3]float;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_struct_declaration(self):
        """Test struct declaration"""
        input = """type Person struct {
            name string
            age int
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_interface_declaration(self):
        """Test interface declaration"""
        input = """type Shape interface {
            getArea() float
            getPerimeter() float
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_nested_blocks(self):
        """Test nested blocks"""
        input = """func main() {
            {
                {
                    var x int
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_complex_expression(self):
        """Test complex expression"""
        input = """func main() {
            x := (a + b) * (c - d) / 2
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_method_declaration(self):
        """Test method declaration"""
        input = """func (r Rectangle) area() float {
            return r.length * r.width
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_multiple_statements(self):
        """Test multiple statements"""
        input = """func main() {
            var x int
            x := 5
            print(x)
            return
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_array_literal(self):
        """Test array literal"""
        input = """var arr = []int{1, 2, 3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_function_returning_array(self):
        """Test function returning array"""
        input = """func getArray() []int {
            return []int{1, 2, 3}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_function_with_return_type(self):
        """Test function with return type"""
        input = """func add(x int, y int) int {
            return x + y
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_function_call(self):
        """Test function call"""
        input = """func main() {
            add(1, 2)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_function_call_with_return(self):
        """Test function call with return"""
        input = """func main() {
            var result int = add(1, 2)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_function_call_with_expression(self):
        """Test function call with expression"""
        input = """func main() {
            var result int = add(1, 2) * 3
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_function_call_with_nested_call(self):
        """Test function call with nested call"""
        input = """func main() {
            var result int = add(add(1, 2), 3)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_function_call_with_struct(self):
        """Test function call with struct"""
        input = """func main() {
            var p Person
            p.getName()
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_function_call_with_array(self):
        """Test function call with array"""
        input = """func main() {
            var arr []int = getArray()
            print(arr[0])
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_function_call_with_method(self):
        """Test function call with method"""
        input = """func main() {
            var r Rectangle
            r.area()
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_function_call_with_method_and_params(self):
        """Test function call with method and parameters"""
        input = """func main() {
            var r Rectangle
            r.setDimensions(5, 10)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_function_call_with_method_and_return(self):
        """Test function call with method and return"""
        input = """func main() {
            var r Rectangle
            var area float = r.area()
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_function_call_with_method_and_expression(self):
        """Test function call with method and expression"""
        input = """func main() {
            var r Rectangle
            var area float = r.area() * 2
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_function_call_with_method_and_nested_call(self):
        """Test function call with method and nested call"""
        input = """func main() {
            var r Rectangle
            var area float = r.area() + r.perimeter()
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_function_call_with_method_and_struct(self):
        """Test function call with method and struct"""
        input = """func main() {
            var p Person
            var name string = p.getName()
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_function_call_with_method_and_array(self):
        """Test function call with method and array"""
        input = """func main() {
            var arr []int = getArray()
            var first int = arr[0]
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_function_call_with_method_and_array_assignment(self):
        """Test function call with method and array assignment"""
        input = """func main() {
            var arr []int = getArray()
            arr[0] = 10
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_function_call_with_method_and_array_access(self):
        """Test function call with method and array access"""
        input = """func main() {
            var arr []int = getArray()
            var value int = arr[1]
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_function_call_with_method_and_array_length(self):
        """Test function call with method and array length"""
        input = """func main() {
            var arr []int = getArray()
            var length int = len(arr)
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_function_call_with_method_and_array_iteration(self):
        """Test function call with method and array iteration"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                print(arr[i])
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_function_call_with_method_and_array_sum(self):
        """Test function call with method and array sum"""
        input = """func main() {
            var arr []int = getArray()
            var sum int = 0
            for i := 0; i < len(arr); i += 1 {
                sum += arr[i]
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_function_call_with_method_and_array_reverse(self):
        """Test function call with method and array reverse"""
        input = """func main() {
            var arr []int = getArray()
            var n int = len(arr)
            for i := 0; i < n/2; i += 1 {
                var temp int = arr[i]
                arr[i] = arr[n-i-1]
                arr[n-i-1] = temp
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_function_call_with_method_and_array_sort(self):
        """Test function call with method and array sort"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                for j := i + 1; j < len(arr); j += 1 {
                    if arr[i] > arr[j] {
                        var temp int = arr[i]
                        arr[i] = arr[j]
                        arr[j] = temp
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_function_call_with_method_and_array_find(self):
        """Test function call with method and array find"""
        input = """func main() {
            var arr []int = getArray()
            var target int = 5
            var found bool = false
            for i := 0; i < len(arr); i += 1 {
                if arr[i] == target {
                    found = true
                    break
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_function_call_with_method_and_array_min(self):
        """Test function call with method and array min"""
        input = """func main() {
            var arr []int = getArray()
            var min int = arr[0]
            for i := 1; i < len(arr); i += 1 {
                if arr[i] < min {
                    min = arr[i]
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_function_call_with_method_and_array_max(self):
        """Test function call with method and array max"""
        input = """func main() {
            var arr []int = getArray()
            var max int = arr[0]
            for i := 1; i < len(arr); i += 1 {
                if arr[i] > max {
                    max = arr[i]
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_function_call_with_method_and_array_average(self):
        """Test function call with method and array average"""
        input = """func main() {
            var arr []int = getArray()
            var sum int = 0
            for i := 0; i < len(arr); i += 1 {
                sum += arr[i]
            }
            var average float = float(sum) / float(len(arr))
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_function_call_with_method_and_array_median(self):
        """Test function call with method and array median"""
        input = """func main() {
            var arr []int = getArray()
            var n int = len(arr)
            for i := 0; i < n; i += 1 {
                for j := i + 1; j < n; j += 1 {
                    if arr[i] > arr[j] {
                        var temp int = arr[i]
                        arr[i] = arr[j]
                        arr[j] = temp
                    }
                }
            }
            var median float
            if n % 2 == 0 {
                median = float(arr[n/2-1] + arr[n/2]) / 2
            } else {
                median = float(arr[n/2])
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_function_call_with_method_and_array_mode(self):
        """Test function call with method and array mode"""
        input = """func main() {
            var arr []int = getArray()
            var frequency map[int]int
            for i := 0; i < len(arr); i += 1 {
                if frequency[arr[i]] == 0 {
                    frequency[arr[i]] = 1
                } else {
                    frequency[arr[i]] += 1
                }
            }
            var mode int = arr[0]
            var maxCount int = frequency[arr[0]]
            for key, value := range frequency {
                if value > maxCount {
                    maxCount = value
                    mode = key
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_function_call_with_method_and_array_unique(self):
        """Test function call with method and array unique"""
        input = """func main() {
            var arr []int = getArray()
            var unique []int
            var seen map[int]bool
            for i := 0; i < len(arr); i += 1 {
                if !seen[arr[i]] {
                    unique = append(unique, arr[i])
                    seen[arr[i]] = true
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_function_call_with_method_and_array_concat(self):
        """Test function call with method and array concat"""
        input = """func main() {
            var arr1 []int = getArray()
            var arr2 []int = getArray()
            var result []int = append(arr1, arr2...)
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))


    def test_function_call_with_method_and_array_copy(self):
        """Test function call with method and array copy"""
        input = """func main() {
            var arr []int = getArray()
            var copyArr []int = make([]int, len(arr))
            copy(copyArr, arr)
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_function_call_with_method_and_array_clear(self):
        """Test function call with method and array clear"""
        input = """func main() {
            var arr []int = getArray()
            arr = arr[:0]
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_function_call_with_method_and_array_resize(self):
        """Test function call with method and array resize"""
        input = """func main() {
            var arr []int = getArray()
            arr = append(arr, make([]int, 5)...)
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_function_call_with_method_and_array_fill(self):
        """Test function call with method and array fill"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] = 1
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_function_call_with_method_and_array_double(self):
        """Test function call with method and array double"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] *= 2
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_function_call_with_method_and_array_half(self):
        """Test function call with method and array half"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] /= 2
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_function_call_with_method_and_array_square(self):
        """Test function call with method and array square"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] *= arr[i]
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_function_call_with_method_and_array_cube(self):
        """Test function call with method and array cube"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] = arr[i] * arr[i] * arr[i]
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_function_call_with_method_and_array_sqrt(self):
        """Test function call with method and array sqrt"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] = int(math.Sqrt(float64(arr[i])))
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_function_call_with_method_and_array_pow(self):
        """Test function call with method and array pow"""
        input = """func main() {
            var arr []int = getArray()
            var exponent int = 3
            for i := 0; i < len(arr); i += 1 {
                arr[i] = int(math.Pow(float64(arr[i]), float64(exponent)))
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_function_call_with_method_and_array_log(self):
        """Test function call with method and array log"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] = int(math.Log(float64(arr[i])))
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_function_call_with_method_and_array_exp(self):
        """Test function call with method and array exp"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] = int(math.Exp(float64(arr[i])))
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_function_call_with_method_and_array_abs(self):
        """Test function call with method and array abs"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] = int(math.Abs(float64(arr[i])))
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_function_call_with_method_and_array_sign(self):
        """Test function call with method and array sign"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                if arr[i] > 0 {
                    arr[i] = 1
                } else if arr[i] < 0 {
                    arr[i] = -1
                } else {
                    arr[i] = 0
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_function_call_with_method_and_array_sign(self):
        """Test function call with method and array sign"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                if (arr[i] > 0) {
                    arr[i] := 1
                } else if (arr[i] < 0) {
                    arr[i] := -1
                } else {
                    arr[i] := 0
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_function_call_with_method_and_array_abs(self):
        """Test function call with method and array abs"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] := foo(math.Abs(float64(arr[i])))
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_function_call_with_method_and_array_exp(self):
        """Test function call with method and array exp"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] := foo(math.Exp(float64(arr[i])))
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_function_call_with_method_and_array_log(self):
        """Test function call with method and array log"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] := foo(math.Log(float64(arr[i])))
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_function_call_with_method_and_array_pow(self):
        """Test function call with method and array pow"""
        input = """func main() {
            var arr []int = getArray()
            var exponent int = 3
            for i := 0; i < len(arr); i += 1 {
                arr[i] := foo(math.Pow(float64(arr[i]), float64(exponent)))
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_function_call_with_method_and_array_sqrt(self):
        """Test function call with method and array sqrt"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] := foo(math.Sqrt(float64(arr[i])))
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_function_call_with_method_and_array_cube(self):
        """Test function call with method and array cube"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] := arr[i] * arr[i] * arr[i]
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_function_call_with_method_and_array_square(self):
        """Test function call with method and array square"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] *= arr[i]
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_function_call_with_method_and_array_half(self):
        """Test function call with method and array half"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] /= 2
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_function_call_with_method_and_array_double(self):
        """Test function call with method and array double"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] *= 2
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_function_call_with_method_and_array_fill(self):
        """Test function call with method and array fill"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
                arr[i] := 1
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_function_call_with_method_and_array_resize(self):
        """Test function call with method and array resize"""
        input = """func main() {
            var arr []int = getArray()
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_function_call_with_method_and_array_clear(self):
        """Test function call with method and array clear"""
        input = """func main() {
            var arr []int = getArray()
            arr := arr[0]
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_function_call_with_method_and_array_copy(self):
        """Test function call with method and array copy"""
        input = """func main() {
            var arr []int = getArray()
            copy(copyArr, arr)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))


    def test_function_call_with_method_and_array_concat(self):
        """Test function call with method and array concat"""
        input = """func main() {
            var arr1 []int = getArray()
            var arr2 []int = getArray()
            var result []int = append(arr1, arr2)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_function_call_with_method_and_array_unique(self):
        """Test function call with method and array unique"""
        input = """func main() {
            var arr []int = getArray()
            var unique []int
            for i := 0; i < len(arr); i += 1 {
                if (!seen[arr[i]]) {
                    unique := append(unique, arr[i])
                    seen[arr[i]] := true
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_function_call_with_method_and_array_mode(self):
        """Test function call with method and array mode"""
        input = """func main() {
            var arr []int = getArray()
            var frequency []int
            for i := 0; i < len(arr); i += 1 {
                if (frequency[arr[i]] == 0) {
                    frequency[arr[i]] := 1
                } else {
                    frequency[arr[i]] += 1
                }
            }
            var mode int = arr[0]
            var maxCount int = frequency[arr[0]]
            for key, value := range frequency {
                if (value > maxCount) {
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_function_call_with_method_and_array_median(self):
        """Test function call with method and array median"""
        input = """func main() {
            var arr []int = getArray()
            var n int = len(arr)
            for i := 0; i < n; i += 1 {
            for j := i + 1; j < n; j += 1 {
                if (arr[i] > arr[j]) {
                var temp int = arr[i]
                arr[i] := arr[j]
                arr[j] := temp
                }
            }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_function_call_with_method_and_array_average(self):
        """Test function call with method and array average"""
        input = """func main() {
            var arr []int = getArray()
            var sum int = 0
            for i := 0; i < len(arr); i += 1 {
            sum += arr[i]
            }
            var average_float = Float(sum) / Float(len(arr))
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_function_call_with_method_and_array_max(self):
        """Test function call with method and array max"""
        input = """func main() {
            var arr []int = getArray()
            var max int := arr[0]
            for i := 1; i < len(arr); i += 1 {
            if (arr[i] > max) {
                max := arr[i]
            }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_function_call_with_method_and_array_min(self):
        """Test function call with method and array min"""
        input = """func main() {
            var arr []int = getArray()
            var min int := arr[0]
            for i := 1; i < len(arr); i += 1 {
            if (arr[i] < min) {
                min := arr[i]
            }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_function_call_with_method_and_array_find(self):
        """Test function call with method and array find"""
        input = """func main() {
            var arr []int = getArray()
            var target int := 5
            var found bool := false
            for i := 0; i < len(arr); i += 1 {
            if (arr[i] == target) {
                found := true
                break
            }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_function_call_with_method_and_array_sort(self):
        """Test function call with method and array sort"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
            for j := i + 1; j < len(arr); j += 1 {
                if (arr[i] > arr[j]) {
                var temp int := arr[i]
                arr[i] := arr[j]
                arr[j] := temp
                }
            }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_function_call_with_method_and_array_reverse(self):
        """Test function call with method and array reverse"""
        input = """func main() {
            var arr []int = getArray()
            var n int = len(arr)
            for i := 0; i < n/2; i += 1 {
            var temp int := arr[i]
            arr[i] := arr[n-i-1]
            arr[n-i-1] := temp
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_function_call_with_method_and_array_sum(self):
        """Test function call with method and array sum"""
        input = """func main() {
            var arr []int = getArray()
            var sum int := 0
            for i := 0; i < len(arr); i += 1 {
            sum += arr[i]
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_function_call_with_method_and_array_iteration(self):
        """Test function call with method and array iteration"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
            print(arr[i])
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_function_call_with_method_and_array_length(self):
        """Test function call with method and array length"""
        input = """func main() {
            var arr []int = getArray()
            var length int = len(arr)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_function_call_with_method_and_array_access(self):
        """Test function call with method and array access"""
        input = """func main() {
            var arr []int = getArray()
            var value int := arr[1]
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_function_call_with_method_and_array_assignment(self):
        """Test function call with method and array assignment"""
        input = """func main() {
            var arr []int = getArray()
            arr[0] := 10
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_function_call_with_method_and_array(self):
        """Test function call with method and array"""
        input = """func main() {
            var arr []int = getArray()
            var first int := arr[0]
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_function_call_with_method_and_array(self):
        """Test function call with method and array"""
        input = """func main() {
            var arr []int = getArray()
            var first int = arr[0]
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_function_call_with_method_and_array_assignment(self):
        """Test function call with method and array assignment"""
        input = """func main() {
            var arr []int = getArray()
            arr[0] := 10
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_function_call_with_method_and_array_access(self):
        """Test function call with method and array access"""
        input = """func main() {
            var arr []int = getArray()
            var value int = arr[1]
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_function_call_with_method_and_array_length(self):
        """Test function call with method and array length"""
        input = """func main() {
            var arr []int = getArray()
            var length int = len(arr)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_function_call_with_method_and_array_iteration(self):
        """Test function call with method and array iteration"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
            print(arr[i])
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_function_call_with_method_and_array_sum(self):
        """Test function call with method and array sum"""
        input = """func main() {
            var arr []int = getArray()
            var sum int = 0
            for i := 0; i < len(arr); i += 1 {
            sum += arr[i]
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_function_call_with_method_and_array_reverse(self):
        """Test function call with method and array reverse"""
        input = """func main() {
            var arr []int = getArray()
            var n int = len(arr)
            for i := 0; i < n/2; i += 1 {
            var temp int = arr[i]
            arr[i] := arr[n-i-1]
            arr[n-i-1] := temp
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_function_call_with_method_and_array_sort(self):
        """Test function call with method and array sort"""
        input = """func main() {
            var arr []int = getArray()
            for i := 0; i < len(arr); i += 1 {
            for j := i + 1; j < len(arr); j += 1 {
                if (arr[i] > arr[j]) {
                var temp int = arr[i]
                arr[i] := arr[j]
                arr[j] := temp
                }
            }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_function_call_with_method_and_array_find(self):
        """Test function call with method and array find"""
        input = """func main() {
            var arr []int = getArray()
            var target int = 5
            var found bool = false
            for i := 0; i < len(arr); i += 1 {
            if (arr[i] == target) {
                found := true
                break
            }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_function_call_with_method_and_array_min(self):
        """Test function call with method and array min"""
        input = """func main() {
            var arr []int = getArray()
            var min int = arr[0]
            for i := 1; i < len(arr); i += 1 {
            if (arr[i] < min) {
                min := arr[i]
            }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_function_call_with_method_and_array_max(self):
        """Test function call with method and array max"""
        input = """func main() {
            var arr []int = getArray()
            var max int = arr[0]
            for i := 1; i < len(arr); i += 1 {
            if (arr[i] > max) {
                max := arr[i]
            }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))
