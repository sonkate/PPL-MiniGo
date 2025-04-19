# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl.
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_decl.
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameter_list.
    def visitParameter_list(self, ctx:MiniGoParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameter.
    def visitParameter(self, ctx:MiniGoParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_ID.
    def visitList_ID(self, ctx:MiniGoParser.List_IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method.
    def visitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#factor.
    def visitFactor(self, ctx:MiniGoParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt_list.
    def visitStmt_list(self, ctx:MiniGoParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_stmt.
    def visitAssign_stmt(self, ctx:MiniGoParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_lhs.
    def visitAssignment_lhs(self, ctx:MiniGoParser.Assignment_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_op.
    def visitAssign_op(self, ctx:MiniGoParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt.
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_elif.
    def visitList_elif(self, ctx:MiniGoParser.List_elifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elif_one.
    def visitElif_one(self, ctx:MiniGoParser.Elif_oneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt.
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basic_for.
    def visitBasic_for(self, ctx:MiniGoParser.Basic_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init_for.
    def visitInit_for(self, ctx:MiniGoParser.Init_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#range_for.
    def visitRange_for(self, ctx:MiniGoParser.Range_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#range_vars.
    def visitRange_vars(self, ctx:MiniGoParser.Range_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#single_var.
    def visitSingle_var(self, ctx:MiniGoParser.Single_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dual_var.
    def visitDual_var(self, ctx:MiniGoParser.Dual_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_stmt.
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_stmt.
    def visitCall_stmt(self, ctx:MiniGoParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_stmt.
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_type.
    def visitStruct_type(self, ctx:MiniGoParser.Struct_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_field.
    def visitStruct_field(self, ctx:MiniGoParser.Struct_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#body.
    def visitBody(self, ctx:MiniGoParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr_list.
    def visitExpr_list(self, ctx:MiniGoParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr_tail.
    def visitExpr_tail(self, ctx:MiniGoParser.Expr_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#all_type.
    def visitAll_type(self, ctx:MiniGoParser.All_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#prim_types.
    def visitPrim_types(self, ctx:MiniGoParser.Prim_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_array_index.
    def visitList_array_index(self, ctx:MiniGoParser.List_array_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_index.
    def visitArray_index(self, ctx:MiniGoParser.Array_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#sm_nl.
    def visitSm_nl(self, ctx:MiniGoParser.Sm_nlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#boollit.
    def visitBoollit(self, ctx:MiniGoParser.BoollitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_item.
    def visitArray_item(self, ctx:MiniGoParser.Array_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arraylit.
    def visitArraylit(self, ctx:MiniGoParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_array_element.
    def visitList_array_element(self, ctx:MiniGoParser.List_array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_element.
    def visitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#itemlist.
    def visitItemlist(self, ctx:MiniGoParser.ItemlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#item.
    def visitItem(self, ctx:MiniGoParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structlit.
    def visitStructlit(self, ctx:MiniGoParser.StructlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_struct_element.
    def visitList_struct_element(self, ctx:MiniGoParser.List_struct_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structlit_element.
    def visitStructlit_element(self, ctx:MiniGoParser.Structlit_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_newline.
    def visitList_newline(self, ctx:MiniGoParser.List_newlineContext):
        return self.visitChildren(ctx)



del MiniGoParser