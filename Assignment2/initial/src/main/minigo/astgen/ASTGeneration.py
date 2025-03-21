#  Tran Thanh Son - 2053405
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce

class ASTGeneration(MiniGoVisitor):
    def visitProgram(self, ctx: MiniGoParser.ProgramContext):
        return Program([self.visit(decl) for decl in ctx.decl()])

    def visitDecl(self, ctx: MiniGoParser.DeclContext):
        return self.visit(ctx.getChild(0))

    def visitVar_decl(self, ctx: MiniGoParser.Var_declContext):
        var_type = self.visit(ctx.all_type()) if ctx.all_type() else None
        var_init = self.visit(ctx.expr()) if ctx.expr() else None
        return VarDecl(ctx.ID().getText(), var_type, var_init)

    def visitConst_decl(self, ctx: MiniGoParser.Const_declContext):
        const_type = self.visit(ctx.all_type()) if ctx.all_type() else None
        ini_expr = self.visit(ctx.expr())
        return ConstDecl(ctx.ID().getText(), const_type, ini_expr)

    def visitFunc_decl(self, ctx: MiniGoParser.Func_declContext):
        param_list = self.visit(ctx.parameter_list()) if ctx.parameter_list() else []
        ret_type = self.visit(ctx.all_type()) if ctx.all_type() else VoidType()
        body = self.visit(ctx.body())
        return FuncDecl(ctx.ID().getText(), param_list, ret_type, body)

    def visitMethod_decl(self, ctx: MiniGoParser.Method_declContext):
        receiver = ctx.ID(0).getText()
        rec_type = Id(ctx.ID(1).getText())
        fun = FuncDecl(
            ctx.ID(2).getText(),
            self.visit(ctx.parameter_list()) if ctx.parameter_list() else [],
            self.visit(ctx.all_type()) if ctx.all_type() else VoidType(),
            self.visit(ctx.body()),
        )
        return MethodDecl(receiver, rec_type, fun)

    def visitParameter_list(self, ctx: MiniGoParser.Parameter_listContext):
        return self.visit(ctx.parameter()) + self.visit(ctx.parameter_list()) if ctx.parameter_list() else self.visit(ctx.parameter())

    def visitParameter(self, ctx: MiniGoParser.ParameterContext):
        list_id = self.visit(ctx.list_ID())
        return [ParamDecl(id, self.visit(ctx.all_type())) for id in list_id]

    def visitList_ID(self, ctx: MiniGoParser.List_IDContext):
        return [ctx.ID().getText()] + self.visit(ctx.list_ID()) if ctx.list_ID() else [ctx.ID().getText()]

    def visitStruct_decl(self, ctx: MiniGoParser.Struct_declContext):
        return self.visit(ctx.struct_type())

    def visitInterface_decl(self, ctx: MiniGoParser.Interface_declContext):
        name = ctx.ID().getText()
        methods = [self.visit(method) for method in ctx.interface_method()] if ctx.interface_method() else []
        return InterfaceType(name, methods)

    def visitInterface_method(self, ctx: MiniGoParser.Interface_methodContext):
        name = ctx.ID().getText()
        params: list[ParamDecl] = self.visit(ctx.parameter_list()) if ctx.parameter_list() else []
        params_type = [param.parType for param in params]
        ret_type = self.visit(ctx.all_type()) if ctx.all_type() else VoidType()
        return Prototype(name, params_type, ret_type)

    def visitExpr(self, ctx: MiniGoParser.ExprContext):
        if ctx.OR_OP():
            left = self.visit(ctx.expr())
            right = self.visit(ctx.expr1())
            return BinaryOp(ctx.OR_OP().getText(), left, right)
        else:
            return self.visit(ctx.expr1())

    def visitExpr1(self, ctx: MiniGoParser.Expr1Context):
        if ctx.AND_OP():
            left = self.visit(ctx.expr1())
            right = self.visit(ctx.expr2())
            return BinaryOp(ctx.AND_OP().getText(), left, right)
        else:
            return self.visit(ctx.expr2())

    def visitExpr2(self, ctx: MiniGoParser.Expr2Context):
        if (ctx.getChildCount() == 3):
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr3())

    def visitExpr3(self, ctx: MiniGoParser.Expr3Context):
        if ctx.ADD_OP() or ctx.SUB_OP():
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr4())

    def visitExpr4(self, ctx: MiniGoParser.Expr4Context):
        if ctx.MUL_OP() or ctx.DIV_OP() or ctx.MOD_OP():
            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr5())

    def visitExpr5(self, ctx: MiniGoParser.Expr5Context):
        if ctx.NOT_OP() or ctx.SUB_OP():
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.expr5())
            return UnaryOp(op, body)
        else:
            return self.visit(ctx.expr6())

    def visitExpr6(self, ctx: MiniGoParser.Expr6Context):
        if ctx.list_array_index():
            arr = self.visit(ctx.expr6())
            idx = self.visit(ctx.list_array_index())
            return ArrayCell(arr, idx)
        elif ctx.DOT_OP():
            receiver = self.visit(ctx.expr6())
            if ctx.ID():
                field = ctx.ID().getText()
                return FieldAccess(receiver, field)
            elif ctx.func_call():
                func_call: FuncCall =  self.visit(ctx.func_call())
                return MethCall(receiver, func_call.funName, func_call.args)
        else:
            return self.visit(ctx.factor())

    def visitFactor(self, ctx: MiniGoParser.FactorContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        return None

    def visitLiteral(self, ctx: MiniGoParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BINLIT():
            return IntLiteral(ctx.BINLIT().getText())
        elif ctx.OCTLIT():
            return IntLiteral(ctx.OCTLIT().getText())
        elif ctx.HEXLIT():
            return IntLiteral(ctx.HEXLIT().getText())
        elif ctx.FLOATLIT():
            return FloatLiteral(ctx.FLOATLIT().getText())
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.boollit():
            return BooleanLiteral(ctx.boollit().getText() == "true")
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        elif ctx.structlit():
            return self.visit(ctx.structlit())
        return None

    # statement
    def visitStmt_list(self, ctx: MiniGoParser.Stmt_listContext):
        return [self.visit(ctx.statement())] + self.visit(ctx.stmt_list()) if ctx.stmt_list() else [self.visit(ctx.statement())]

    def visitStatement(self, ctx: MiniGoParser.StatementContext):
        return self.visit(ctx.getChild(0))

    def visitAssign_stmt(self, ctx: MiniGoParser.Assign_stmtContext):
        assign_op = self.visit(ctx.assign_op())
        assignment_lhs = self.visit(ctx.assignment_lhs())
        expr = self.visit(ctx.expr())
        if assign_op == ":":
            return Assign(assignment_lhs, expr)
        return Assign(assignment_lhs, BinaryOp(assign_op, assignment_lhs, expr))

    def visitAssignment_lhs(self, ctx: MiniGoParser.Assignment_lhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        elif ctx.assignment_lhs():
            lhs = self.visit(ctx.assignment_lhs())
            if ctx.list_array_index():
                idx = self.visit(ctx.list_array_index())
                return ArrayCell(lhs, idx)
            elif ctx.DOT_OP():
                field = ctx.ID().getText()
                return FieldAccess(lhs, field)
        return None

    def visitAssign_op(self, ctx: MiniGoParser.Assign_opContext):
        return ctx.getChild(0).getText()[0]
    # if_stmt:
	# IF LRB expr RRB list_newline? body list_elif? (
	# 	ELSE list_newline? body
	# )?;
    # list_elif: elif_one list_elif | elif_one;
    # elif_one: ELSE IF LRB expr RRB list_newline? body;
    def visitIf_stmt(self, ctx: MiniGoParser.If_stmtContext):
        expr = self.visit(ctx.expr())
        then_stmt = self.visit(ctx.body(0))
        else_stmt = self.visit(ctx.body(1)) if ctx.body(1) else None

        if ctx.list_elif():
            list_elif = self.visit(ctx.list_elif())
            combined_elif = reduce(lambda acc, elif_stmt: If(elif_stmt[0], elif_stmt[1], acc), reversed(list_elif), else_stmt)
            return If(expr, then_stmt, combined_elif)
        else:
            return If(expr, then_stmt, else_stmt)

    def visitList_elif(self, ctx: MiniGoParser.List_elifContext):
        return [self.visit(ctx.elif_one())] + self.visit(ctx.list_elif()) if ctx.list_elif() else [self.visit(ctx.elif_one())]

    def visitElif_one(self, ctx: MiniGoParser.Elif_oneContext):
        return (self.visit(ctx.expr()), self.visit(ctx.body()))

    def visitFor_stmt(self, ctx: MiniGoParser.For_stmtContext):
        loop = self.visit(ctx.body())
        if ctx.basic_for():
            cond = self.visit(ctx.basic_for().expr())
            return ForBasic(cond, loop)
        elif ctx.init_for():
            if ctx.init_for().var_decl():
                init = self.visit(ctx.init_for().var_decl())
                cond = self.visit(ctx.init_for().expr())
                upda = self.visit(ctx.init_for().assign_stmt(0))
            else:
                init = self.visit(ctx.init_for().assign_stmt(0))
                cond = self.visit(ctx.init_for().expr())
                upda = self.visit(ctx.init_for().assign_stmt(1))
            return ForStep(init, cond, upda, loop)
        elif ctx.range_for():
            # range_for: FOR (ID|UNDERSCORE) CM ID EQ_ASSIGN_OP RANGE expr;
            if ctx.range_for().UNDERSCORE():
                idx = ctx.UNDERSCORE().getText()
                value = Id(ctx.range_for().ID(0).getText())
            else:
                idx = Id(ctx.range_for().ID(0).getText())
                value = Id(ctx.range_for().ID(1).getText())
            arr = self.visit(ctx.range_for().expr())
            return ForEach(idx, value, arr, loop)

    def visitBreak_stmt(self, ctx: MiniGoParser.Break_stmtContext):
        return Break()

    def visitContinue_stmt(self, ctx: MiniGoParser.Continue_stmtContext):
        return Continue()

    def visitCall_stmt(self, ctx: MiniGoParser.Call_stmtContext):
        
        if ctx.DOT_OP():
            receiver = self.visit(ctx.assignment_lhs())
            met_name = ctx.ID().getText()
            args = self.visit(ctx.expr_list()) if ctx.expr_list() else []
            return MethCall(receiver, met_name, args)
        else:
            fun_name = ctx.ID().getText()
            args = self.visit(ctx.expr_list()) if ctx.expr_list() else []
            return FuncCall(fun_name, args)

    def visitReturn_stmt(self, ctx: MiniGoParser.Return_stmtContext):
        expr = self.visit(ctx.expr()) if ctx.expr() else None
        return Return(expr)
    # array struct interface type
    # array_type: list_array_index (prim_types | ID);
    def visitArray_type(self, ctx: MiniGoParser.Array_typeContext):
        dimens = self.visit(ctx.list_array_index())
        ele_type = self.visit(ctx.prim_types()) if ctx.prim_types() else Id(ctx.ID().getText())
        return ArrayType(dimens, ele_type)

    def visitStruct_type(self, ctx: MiniGoParser.Struct_typeContext):
        name = ctx.ID().getText()
        fields = [self.visit(field) for field in ctx.struct_field()] if ctx.struct_field() else []
        return StructType(name, fields, [])

    def visitStruct_field(self, ctx: MiniGoParser.Struct_fieldContext):
        return (ctx.ID().getText(), self.visit(ctx.all_type()))

    # Support
    def visitBody(self, ctx: MiniGoParser.BodyContext):
        return Block(
            self.visit(ctx.stmt_list()) if ctx.stmt_list() else []
        )

    def visitFunc_call(self, ctx: MiniGoParser.Func_callContext):
        fun_name = ctx.ID().getText()
        args = (
            self.visit(ctx.expr_list())
            if ctx.expr_list()
            else []
        )
        return FuncCall(fun_name, args)

    def visitExpr_list(self, ctx: MiniGoParser.Expr_listContext):
        return [self.visit(ctx.expr())] + self.visit(ctx.expr_tail()) if ctx.expr_tail() else [self.visit(ctx.expr())]

    def visitExpr_tail(self, ctx: MiniGoParser.Expr_tailContext):
        return [self.visit(ctx.expr())] + self.visit(ctx.expr_tail()) if ctx.expr_tail() else []

    def visitPrim_types(self, ctx: MiniGoParser.Prim_typesContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()

    def visitAll_type(self, ctx: MiniGoParser.All_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        else:
            return Id(ctx.ID().getText())

    def visitList_array_index(self, ctx: MiniGoParser.List_array_indexContext):
        return [self.visit(ctx.array_index())] + self.visit(ctx.list_array_index()) if ctx.list_array_index() else [self.visit(ctx.array_index())]

    def visitArray_index(self, ctx: MiniGoParser.Array_indexContext):
        return self.visit(ctx.expr())
    # Array and Struct Literals
    def visitArraylit(self, ctx: MiniGoParser.ArraylitContext):
        dimens = self.visit(ctx.list_array_index())
        ele_type = self.visit(ctx.all_type())
        value = self.visit(ctx.list_array_element()) if ctx.list_array_element() else []
        return ArrayLiteral(dimens, ele_type, value)

    def visitList_array_element(self, ctx: MiniGoParser.List_array_elementContext):
        array_elements =  self.visit(ctx.array_element()) + self.visit(ctx.list_array_element()) if ctx.list_array_element() else self.visit(ctx.array_element())
        return array_elements
    def visitArray_element(self, ctx: MiniGoParser.Array_elementContext):
        if ctx.itemlist():
            return self.visit(ctx.itemlist())
        elif ctx.array_element():
            return [self.visit(ctx.array_element())]

    def visitItemlist(self, ctx: MiniGoParser.ItemlistContext):
        return [self.visit(ctx.item())] + self.visit(ctx.itemlist()) if ctx.itemlist() else [self.visit(ctx.item())]
    def visitItem(self, ctx: MiniGoParser.ItemContext):
        if ctx.array_element():
            return self.visit(ctx.array_element())
        return self.visit(ctx.getChild(0))

    def visitArray_item(self, ctx: MiniGoParser.Array_itemContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(ctx.FLOATLIT().getText())
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.boollit():
            return BooleanLiteral(ctx.boollit().getText() == "true")
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.structlit():
            return self.visit(ctx.structlit())
    # structlit: ID LCB list_struct_element? LCB;
    # list_struct_element:
    #     structlit_element CM list_struct_element
    #     | structlit_element;
    # structlit_element: ID COL expr;
    def visitStructlit(self, ctx: MiniGoParser.StructlitContext):
        name = ctx.ID().getText()
        elements = self.visit(ctx.list_struct_element()) if ctx.list_struct_element() else []
        return StructLiteral(name, elements)
    def visitList_struct_element(self, ctx: MiniGoParser.List_struct_elementContext):
        return [self.visit(ctx.structlit_element())] + self.visit(ctx.list_struct_element()) if ctx.list_struct_element() else [self.visit(ctx.structlit_element())]
    def visitStructlit_element(self, ctx: MiniGoParser.Structlit_elementContext):
        return (ctx.ID().getText(), self.visit(ctx.expr()))

