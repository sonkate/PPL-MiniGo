"""
* @author nhphung
"""

from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return (
            "MType(["
            + ",".join(str(x) for x in self.partype)
            + "],"
            + str(self.rettype)
            + ")"
        )

    def __eq__(self, other):
        if not isinstance(other, MType):
            return False
        return self.partype == other.partype and type(self.rettype) == type(other.rettype)

class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return (
            "Symbol("
            + str(self.name)
            + ","
            + str(self.mtype)
            + ("" if self.value is None else "," + str(self.value))
            + ")"
        )


class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast
        self.current_func = None
        # self.global_envi = [[]]
        self.global_envi = [[
            Symbol("getInt", MType([], IntType())),
            Symbol("putInt", MType([IntType()], VoidType())),
            Symbol("putIntLn", MType([IntType()], VoidType())),
            Symbol("getFloat", MType([], FloatType())),
            Symbol("putFloat", MType([FloatType()], VoidType())),
            Symbol("putFloatLn", MType([FloatType()], VoidType())),
            Symbol("getBool", MType([], BoolType())),
            Symbol("putBool", MType([BoolType()], VoidType())),
            Symbol("putBoolLn", MType([BoolType()], VoidType())),
            Symbol("getString", MType([], StringType())),
            Symbol("putString", MType([StringType()], VoidType())),
            Symbol("putStringLn", MType([StringType()], VoidType())),
            Symbol("putLn", MType([], VoidType())),
        ]]
    def printEnv(self, env):
        def stringify(syms):
            if isinstance(syms, list):
                return "[" + ", ".join(stringify(sym) for sym in syms) + "]"
            return str(syms)
        print(stringify(env))
    def compare_type(self, LHS, RHS):
        if type(LHS) is Id and type(RHS) is Id:
            if LHS.name != RHS.name:
                return False
            return True
        if ((type(LHS) is StructType and type(RHS) is Id)
            or (type(LHS) is Id and type(RHS) is StructType)
            or (type(LHS) is StructType and type(RHS) is StructType)):
            if LHS.name != RHS.name:
                return False
            return True
        if(type(LHS) != type(RHS)):
            return False
        elif(type(LHS) is ArrayType):
            if(len(LHS.dimens) != len(RHS.dimens)):
                return False
            elif type(LHS.eleType) != type(RHS.eleType):
                return False
            else:
                for i in range(len(LHS.dimens)):
                    if LHS.dimens[i] != RHS.dimens[i]:
                        return False
        return True

    def check_LHS_RHS(self, ast, lhs_type, rhs_type):
        # check VoidType
        if isinstance(lhs_type, VoidType) or isinstance(rhs_type, VoidType):
            raise TypeMismatch(ast)
        # check struct type
        if ((type(lhs_type) is StructType and type(rhs_type) is Id) 
            or (type(lhs_type) is Id and type(rhs_type) is StructType)
            or (type(lhs_type) is StructType and type(rhs_type) is StructType)):
            if lhs_type.name != rhs_type.name:
                raise TypeMismatch(ast)
            return True
        # If LHS is a scalar type
        if isinstance(lhs_type, (IntType, FloatType, BoolType, StringType)):
            if isinstance(lhs_type, FloatType) and isinstance(rhs_type, IntType):
                return True
            if type(lhs_type) != type(rhs_type):
                raise TypeMismatch(ast)
        # If LHS is an array type
        elif isinstance(lhs_type, ArrayType):
            if not isinstance(rhs_type, ArrayType):
                raise TypeMismatch(ast)
            if lhs_type.dimens != rhs_type.dimens:
                raise TypeMismatch(ast)
            if isinstance(lhs_type.eleType, FloatType) and isinstance(
                rhs_type.eleType, IntType
            ):
                return True
            if type(lhs_type.eleType) != type(rhs_type.eleType):
                check = self.compare_type(lhs_type.eleType, rhs_type.eleType)
                return check
        # If LHS is an interface type
        elif isinstance(lhs_type, InterfaceType):
            if not isinstance(rhs_type, StructType):
                raise TypeMismatch(ast)
            for method_interface in lhs_type.methods:
                found = False
                for method_struct in rhs_type.methods:
                    if (method_interface.name == method_struct.name
                    and method_interface.mtype == method_struct.mtype):
                        found = True
                        break
                if not found:
                    raise TypeMismatch(ast)
        # If LHS is undeclared, implicitly declare it with the type of RHS
        elif lhs_type is None:
            lhs_type = rhs_type
        return True
    def flatten(self, env):
        flat = []
        for x in env:
            if isinstance(x, list):
                flat.extend(self.flatten(x))
            else:
                flat.append(x)
        return flat

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast, c):
        for decl in ast.decl:
            sym = self.visit(decl, c)
            if isinstance(sym, Symbol):
                c[0].insert(0, sym)
        return c

    def visitVarDecl(self, ast: VarDecl, c):
        env = c[0].copy()
        res = self.lookup(ast.varName, env, lambda x: x.name)
        if res:
            raise Redeclared(Variable(), ast.varName)
        if ast.varInit:
            var_type = self.visit(ast.varType, c) if type(ast.varType) == Id else ast.varType
            init_type = self.visit(ast.varInit, c)
            if self.check_LHS_RHS(ast, var_type, init_type) is True:
                return Symbol(ast.varName, init_type)
            else:
                raise TypeMismatch(ast)
        return Symbol(ast.varName, ast.varType)

    def visitConstDecl(self, ast: ConstDecl, c):
        if self.lookup(ast.conName, c[0], lambda x: x.name):
            raise Redeclared(Constant(), ast.conName)
        const_type = self.visit(ast.iniExpr, c)
        self.check_LHS_RHS(ast, ast.conType, const_type)
        return Symbol(ast.conName, const_type)

    def visitFuncDecl(self, ast: FuncDecl, c):
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if res:
            raise Redeclared(Function(), ast.name)
        param_scope = []
        for param in ast.params:
            if self.lookup(param.parName, param_scope, lambda x: x.name):
                raise Redeclared(Parameter(), param.parName)
            param_scope.insert(0, Symbol(param.parName, param.parType))
        func_sym = Symbol(ast.name, MType([p.parType for p in ast.params], ast.retType))
        body_scope = [param_scope + [func_sym]] + c
        self.current_func = func_sym
        self.visit(ast.body, body_scope)
        self.current_func = None
        return func_sym

    def visitMethodDecl(self, ast: MethodDecl, c):
        env = c.copy()
        receiver_sym = Symbol(ast.receiver, self.visit(ast.recType, env), None)
        t = self.visit(ast.fun, [[]] + [[receiver_sym]] + c)

        # Tìm struct chứa receiver
        struct = self.lookup(receiver_sym.mtype.name, self.global_envi[0], lambda x: x.name)

        methods = struct.mtype.methods
        if self.lookup(ast.fun.name, methods, lambda x: x.name):
            raise Redeclared(Method(), ast.fun.name)

        new_method = Symbol(ast.fun.name, t.mtype, None)
        struct.mtype.methods.insert(0, new_method)
        return None


    def visitPrototype(self,ast: Prototype, c):
        env = c.copy()
        res = self.lookup(ast.name, env[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Prototype(), ast.name)
        params = []
        for param in ast.params:
            res = self.visit(param,env[0])
            params.append(res)
        return Symbol(ast.name, MType(params,ast.retType))

    def visitIntType(self, ast, c):
        return IntType()

    def visitFloatType(self, ast, c):
        return FloatType()

    def visitBoolType(self, ast, c):
        return BoolType()

    def visitStringType(self, ast, c):
        return StringType()

    def visitVoidType(self, ast, c):
        return VoidType()

    def visitArrayType(self, ast: ArrayType, c):
        dimen = []
        for i in ast.dimens:
            if type(i) is int:
               dimen.append(int(i))
            else:
               dim_num = self.visit(i,c)
               if type(dim_num) is not IntType:
                   raise TypeMismatch(ast)
        ele_type = self.getType(ast.eleType,c)
        return ArrayType(ast.dimens, ele_type)

    def visitStructType(self, ast: StructType, c):
        res = self.lookup(ast.name, self.global_envi[0], lambda x : x.name)
        if res is not None:
            raise Redeclared(Type(), ast.name)
        list_ele = []
        for ele in ast.elements:
            if self.lookup(ele[0], list_ele, lambda x: x[0]):
                raise Redeclared(Field(), ele[0])
            list_ele.append((ele[0], ele[1]))
        self.global_envi[0].insert(0, Symbol(ast.name, StructType(ast.name, list_ele, [])))
        return None

    def visitInterfaceType(self, ast: InterfaceType, c):
        res = self.lookup(ast.name, self.global_envi[0], lambda x : x.name)
        if res is not None:
            raise Redeclared(Type(), ast.name)
        env = [[]] +c
        for proto in ast.methods:
            env[0].append(self.visit(proto, env))
        self.global_envi[0].insert(0,Symbol(ast.name, InterfaceType(ast.name, env[0])))
        return None
    def visitBlock(self, ast: Block, c):
        new_env = [[]] + c
        for member in ast.member:
            symbol = self.visit(member, new_env)
            if isinstance(symbol, Symbol):
                new_env[0].insert(0, symbol)
        return None
    def visitAssign(self, ast: Assign, c):
        rhs_type = self.visit(ast.rhs, c)
        if type(rhs_type) is VoidType:
            raise TypeMismatch(ast)
        lhs_type = self.visit(ast.lhs,c)
        if not self.check_LHS_RHS(ast, lhs_type, rhs_type):
            raise TypeMismatch(ast)
        return None

    def visitIf(self, ast: If, c):
        cond_type = self.visit(ast.expr, c)
        if type(cond_type) is not BoolType:
            raise TypeMismatch(ast.expr)
        self.visit(ast.thenStmt, c)
        if ast.elseStmt:
            self.visit(ast.elseStmt, c)
        return None

    def visitForBasic(self, ast: ForBasic, c):
        cond_type = self.visit(ast.cond, c)
        if type(cond_type) is not BoolType:
            raise TypeMismatch(ast)
        self.visit(ast.loop, c)
        return None

    def visitForStep(self, ast: ForStep, c):
        env = [[]]+ c
        env[0].append(self.visit(ast.init, env)) if self.visit(ast.init, env) else None
        condition_type = self.visit(ast.cond, env)
        if type(condition_type) is not BoolType:
            raise TypeMismatch(ast)
        self.visit(ast.loop, c)
        return None

    def visitForEach(self, ast: ForEach, c):
        array_type = self.visit(ast.arr, c)
        if type(array_type) is Symbol:
            array_type = array_type.mtype
        if type(array_type) is MType:
            array_type = array_type.rettype
        if type(array_type) is not ArrayType:
            raise TypeMismatch(ast)
        env = [[]] + c
        if ast.idx.name != '_':
            env[0].append(Symbol(ast.idx.name, IntType()))
        if ast.value.name != '_':
            env[0].append(Symbol(ast.value.name, array_type.eleType))
        self.visit(ast.loop, env)
        return None

    def visitContinue(self, ast, c):
        return c

    def visitBreak(self, ast, c):
        return c

    def visitReturn(self, ast: Return, c):
        if ast.expr is not None:
            return_type = self.visit(ast.expr, c)
        else:
            return_type = VoidType()

        if self.current_func is not None:
            func_rettype = self.current_func.mtype.rettype
            if not self.compare_type(func_rettype, return_type):
                raise TypeMismatch(ast)
        return None

    def visitBinaryOp(self, ast:BinaryOp, c):
        left_type = self.visit(ast.left, c)
        right_type = self.visit(ast.right, c)
        # if not literal
        if isinstance(left_type, Symbol):
            left_type = left_type.mtype
        if isinstance(right_type, Symbol):
            right_type = right_type.mtype
        # function in binary expr
        if isinstance(left_type, MType):
            left_type = left_type.rettype
        if isinstance(right_type, MType):
            right_type = right_type.rettype

        if ast.op in ['+']:
            if isinstance(left_type, StringType) and isinstance(right_type, StringType):
                return StringType()
            if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
                if isinstance(left_type, FloatType) or isinstance(right_type, FloatType):
                    return FloatType()
                return IntType()
        if ast.op in ['-', '*', '/']:
            if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
                if isinstance(left_type, FloatType) or isinstance(right_type, FloatType):
                    return FloatType()
                return IntType()
        if ast.op in ['%']:
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return IntType()
        if ast.op in ['&&', '||']:
            if isinstance(left_type, BoolType) and isinstance(right_type, BoolType):
                return BoolType()
        if ast.op in ['==', '!=', '<=', '>=', '<', '>']:
            if isinstance(left_type, StringType) and isinstance(right_type, StringType):
                return BoolType()
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return BoolType()
            if isinstance(left_type, FloatType) and isinstance(right_type, FloatType):
                return BoolType()
        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast: UnaryOp, c):
        expr_type = self.visit(ast.body, c)
        if type(expr_type) is VoidType:
            raise TypeMismatch(ast.body)
        if ast.op == '!':
            if type(expr_type) is not BoolType:
                raise TypeMismatch(ast)
        if ast.op == '-':
            if type(expr_type) not in [IntType, FloatType]:
                raise TypeMismatch(ast)
        return  expr_type

    def visitFuncCall(self, ast: FuncCall, c):
        env = c.copy()
        env_flatten = self.flatten(env)
        res:Symbol = self.lookup(ast.funName, env_flatten, lambda x: x.name)
        if res is None or type(res.mtype) is not MType:
            raise Undeclared(Function(), ast.funName)
        if res and type(res.mtype) is not MType:
            raise Undeclared(Function(),ast.funName)
        # check size of args
        func_param_types = res.mtype.partype
        if len(ast.args) != len(func_param_types):
            raise TypeMismatch(ast)
        args_type = []
        args_type = [self.visit(arg, c) for arg in ast.args]
        for i in range(len(args_type)):
            if not self.compare_type(func_param_types[i], args_type[i]):
                raise TypeMismatch(ast)
        return res.mtype.rettype
    def visitMethCall(self, ast: MethCall, c):
        struct_type = self.visit(ast.receiver, c)
        while(type(struct_type) is Id):
            struct = self.lookup(struct_type.name, self.global_envi[0], lambda x: x.name)
            struct_type = struct.mtype

        if type(struct_type) is not StructType:
            raise TypeMismatch(ast)
        struct = self.lookup(struct_type.name, self.global_envi[0], lambda x: x.name)
        if type(struct.mtype) is StructType or type(struct_type) is InterfaceType:
            method = self.lookup(ast.metName, struct.mtype.methods, lambda x: x.name)
            if method is None:
                raise Undeclared(Method(), ast.metName)
            if len(ast.args) != len(method.mtype.partype):
                raise TypeMismatch(ast)
            args_type = [self.visit(arg, c) for arg in ast.args]
            for i in range(len(args_type)):
                if not self.compare_type(method.mtype.partype[i], args_type[i]):
                    raise TypeMismatch(ast)
            return method.mtype.rettype

    def visitId(self, ast: Id, c):
        for scope in c:
            res: Symbol = self.lookup(ast.name, scope, lambda x: x.name)
            if res:
                break
        if res:
            return res.mtype
        else:
            raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast: ArrayCell, c):
        arr_type = self.visit(ast.arr, c)
        if type(arr_type) is Symbol:
            arr_type = arr_type.mtype
        if type(arr_type) is MType:
            arr_type = arr_type.rettype
        if type(arr_type) is not ArrayType:
            raise TypeMismatch(ast)
        for i in ast.idx:
            idxType = self.visit(i, c)
            if type(idxType) is Symbol:
                idxType = idxType.mtype
            if type(idxType) is MType:
                idxType = idxType.rettype
            if type(idxType) is not IntType:
                raise TypeMismatch(ast)
        if isinstance(arr_type, ArrayType):
            remaining_dims = arr_type.dimens[len(ast.idx):]
            if not remaining_dims:
                return arr_type.eleType
            else:
                return ArrayType(remaining_dims, arr_type.eleType)

    def visitFieldAccess(self,ast: FieldAccess, c):
        struct_type = self.visit(ast.receiver, c)
        while(type(struct_type) is Id):
            struct = self.lookup(struct_type.name, self.global_envi[0], lambda x: x.name)
            struct_type = struct.mtype

        if type(struct_type) is not StructType:
            raise TypeMismatch(ast)
        struct = self.lookup(struct_type.name, self.global_envi[0], lambda x: x.name)
        fields = struct.mtype.elements
        res = self.lookup(ast.field, fields,lambda x: x[0])
        if res is None:
            raise Undeclared(Field(),ast.field)
        return res[1]

    def visitIntLiteral(self, ast: IntLiteral, c):
        return IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast: StringLiteral, c):
        return StringType()

    def visitArrayLiteral(self, ast: ArrayLiteral, c):
        for dimen in ast.dimens:
            dim_num  = self.visit(dimen, c)
            if type(dim_num) is not IntType:
                raise TypeMismatch(ast)
        ele_type = self.visit(ast.eleType,c)
        if not self.compare_type(ast.eleType, ele_type):
            raise TypeMismatch(ast)
        # check value of array literal
        if type(ast.value) is list:
            for i in ast.value:
                if type(i) is not list and type(i) is not List:
                    ele_type = self.visit(i,c)
                    if not self.compare_type(ele_type, ast.eleType):
                        raise TypeMismatch(ast)
        return ArrayType(ast.dimens, ele_type)

    def visitStructLiteral(self, ast: StructLiteral, c):
        res = None
        for scope in c:
            res: Symbol = self.lookup(ast.name, scope, lambda x: x.name)
            if res:
                break
        if res is None:
            raise Undeclared(Identifier(),ast.name)
        for ele in ast.elements:
            # each field in struct literal
            struct_type = self.visit(ele[1], c)
            field = self.lookup(ele[0], res.mtype.elements, lambda x: x[0])
            if field is None:
                raise Undeclared(Field(), ele[0])
            if not self.compare_type(struct_type, field[1]):
                raise TypeMismatch(ast)
        return res.mtype

    def visitNilLiteral(self, ast, c):
        return None
