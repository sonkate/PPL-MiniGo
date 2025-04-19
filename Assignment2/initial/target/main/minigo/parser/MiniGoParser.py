# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u0281\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\5\2\u0082\n\2\3\2")
        buf.write("\6\2\u0085\n\2\r\2\16\2\u0086\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3\u0093\n\3\3\4\3\4\3\4\3\4\5\4\u0099")
        buf.write("\n\4\3\4\3\4\5\4\u009d\n\4\3\5\3\5\3\5\5\5\u00a2\n\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6\u00ac\n\6\3\6\3\6\5")
        buf.write("\6\u00b0\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5")
        buf.write("\7\u00bc\n\7\3\7\3\7\5\7\u00c0\n\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u00c9\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\5\n")
        buf.write("\u00d2\n\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f")
        buf.write("\u00dd\n\f\f\f\16\f\u00e0\13\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\5\r\u00e8\n\r\3\r\3\r\5\r\u00ec\n\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\7\16\u00f6\n\16\f\16\16\16\u00f9")
        buf.write("\13\16\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u0101\n\17\f")
        buf.write("\17\16\17\u0104\13\17\3\20\3\20\3\20\3\20\3\20\3\20\7")
        buf.write("\20\u010c\n\20\f\20\16\20\u010f\13\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\7\21\u0117\n\21\f\21\16\21\u011a\13\21\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\7\22\u0122\n\22\f\22\16\22")
        buf.write("\u0125\13\22\3\23\3\23\3\23\5\23\u012a\n\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0134\n\24\5\24\u0136")
        buf.write("\n\24\7\24\u0138\n\24\f\24\16\24\u013b\13\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\5\25\u0144\n\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0150\n\26")
        buf.write("\3\27\3\27\3\27\3\27\5\27\u0156\n\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u0168\n\30\3\31\3\31\3\31\3\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\5\32\u0175\n\32\7\32\u0177")
        buf.write("\n\32\f\32\16\32\u017a\13\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u0183\n\34\3\34\3\34\5\34\u0187\n\34\3")
        buf.write("\34\3\34\5\34\u018b\n\34\3\34\5\34\u018e\n\34\3\35\3\35")
        buf.write("\3\35\3\35\5\35\u0194\n\35\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\5\36\u019c\n\36\3\36\3\36\3\37\3\37\3\37\5\37\u01a3")
        buf.write("\n\37\3\37\5\37\u01a6\n\37\3\37\3\37\3 \3 \3 \3!\3!\3")
        buf.write("!\5!\u01b0\n!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3#\3#\5#\u01c1\n#\3$\3$\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3(\5(\u01d3\n(\3(\3(\3(\3(\5(\u01d9")
        buf.write("\n(\3(\3(\3(\3)\3)\3)\5)\u01e1\n)\3)\3)\3*\3*\3*\5*\u01e8")
        buf.write("\n*\3+\3+\3+\3+\3+\7+\u01ef\n+\f+\16+\u01f2\13+\3+\3+")
        buf.write("\5+\u01f6\n+\3,\3,\3,\3,\3-\3-\5-\u01fe\n-\3-\3-\7-\u0202")
        buf.write("\n-\f-\16-\u0205\13-\3.\3.\3.\3.\5.\u020b\n.\3.\3.\3/")
        buf.write("\3/\3/\3/\5/\u0213\n/\3\60\3\60\3\60\3\60\3\60\5\60\u021a")
        buf.write("\n\60\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u0222\n\61\3")
        buf.write("\62\3\62\3\63\3\63\3\63\3\63\5\63\u022a\n\63\3\64\3\64")
        buf.write("\3\64\3\64\3\65\3\65\6\65\u0232\n\65\r\65\16\65\u0233")
        buf.write("\5\65\u0236\n\65\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\5\67\u0243\n\67\38\38\38\38\58\u0249")
        buf.write("\n8\38\38\39\39\39\39\39\59\u0252\n9\3:\3:\3:\3:\3:\5")
        buf.write(":\u0259\n:\3;\3;\3;\3;\3;\5;\u0260\n;\3<\3<\3<\3<\3<\3")
        buf.write("<\5<\u0268\n<\3=\3=\3=\5=\u026d\n=\3=\3=\3>\3>\3>\3>\3")
        buf.write(">\5>\u0276\n>\3?\3?\3?\3?\3@\6@\u027d\n@\r@\16@\u027e")
        buf.write("\3@\2\t\32\34\36 \"&\62A\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhjlnprtvxz|~\2\n\3\2\34!\3\2\27\30\3\2\31\33\4\2\30")
        buf.write("\30$$\3\2%*\4\2\67\67AA\3\2\13\16\3\2\25\26\2\u02a8\2")
        buf.write("\u0081\3\2\2\2\4\u0092\3\2\2\2\6\u0094\3\2\2\2\b\u009e")
        buf.write("\3\2\2\2\n\u00a7\3\2\2\2\f\u00b3\3\2\2\2\16\u00c8\3\2")
        buf.write("\2\2\20\u00ca\3\2\2\2\22\u00d1\3\2\2\2\24\u00d3\3\2\2")
        buf.write("\2\26\u00d6\3\2\2\2\30\u00e4\3\2\2\2\32\u00ef\3\2\2\2")
        buf.write("\34\u00fa\3\2\2\2\36\u0105\3\2\2\2 \u0110\3\2\2\2\"\u011b")
        buf.write("\3\2\2\2$\u0129\3\2\2\2&\u012b\3\2\2\2(\u0143\3\2\2\2")
        buf.write("*\u014f\3\2\2\2,\u0155\3\2\2\2.\u0167\3\2\2\2\60\u0169")
        buf.write("\3\2\2\2\62\u016d\3\2\2\2\64\u017b\3\2\2\2\66\u017d\3")
        buf.write("\2\2\28\u0193\3\2\2\2:\u0195\3\2\2\2<\u01a2\3\2\2\2>\u01a9")
        buf.write("\3\2\2\2@\u01ac\3\2\2\2B\u01b6\3\2\2\2D\u01c0\3\2\2\2")
        buf.write("F\u01c2\3\2\2\2H\u01c4\3\2\2\2J\u01c8\3\2\2\2L\u01cb\3")
        buf.write("\2\2\2N\u01d2\3\2\2\2P\u01dd\3\2\2\2R\u01e4\3\2\2\2T\u01e9")
        buf.write("\3\2\2\2V\u01f7\3\2\2\2X\u01fb\3\2\2\2Z\u0206\3\2\2\2")
        buf.write("\\\u0212\3\2\2\2^\u0219\3\2\2\2`\u0221\3\2\2\2b\u0223")
        buf.write("\3\2\2\2d\u0229\3\2\2\2f\u022b\3\2\2\2h\u0235\3\2\2\2")
        buf.write("j\u0237\3\2\2\2l\u0242\3\2\2\2n\u0244\3\2\2\2p\u0251\3")
        buf.write("\2\2\2r\u0258\3\2\2\2t\u025f\3\2\2\2v\u0267\3\2\2\2x\u0269")
        buf.write("\3\2\2\2z\u0275\3\2\2\2|\u0277\3\2\2\2~\u027c\3\2\2\2")
        buf.write("\u0080\u0082\5~@\2\u0081\u0080\3\2\2\2\u0081\u0082\3\2")
        buf.write("\2\2\u0082\u0084\3\2\2\2\u0083\u0085\5\4\3\2\u0084\u0083")
        buf.write("\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0084\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\7\2\2\3")
        buf.write("\u0089\3\3\2\2\2\u008a\u008b\5\6\4\2\u008b\u008c\5h\65")
        buf.write("\2\u008c\u0093\3\2\2\2\u008d\u0093\5\b\5\2\u008e\u0093")
        buf.write("\5\n\6\2\u008f\u0093\5\f\7\2\u0090\u0093\5\24\13\2\u0091")
        buf.write("\u0093\5\26\f\2\u0092\u008a\3\2\2\2\u0092\u008d\3\2\2")
        buf.write("\2\u0092\u008e\3\2\2\2\u0092\u008f\3\2\2\2\u0092\u0090")
        buf.write("\3\2\2\2\u0092\u0091\3\2\2\2\u0093\5\3\2\2\2\u0094\u0095")
        buf.write("\7\20\2\2\u0095\u009c\7A\2\2\u0096\u009d\5`\61\2\u0097")
        buf.write("\u0099\5`\61\2\u0098\u0097\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\u009a\3\2\2\2\u009a\u009b\7+\2\2\u009b\u009d\5")
        buf.write("\32\16\2\u009c\u0096\3\2\2\2\u009c\u0098\3\2\2\2\u009d")
        buf.write("\7\3\2\2\2\u009e\u009f\7\17\2\2\u009f\u00a1\7A\2\2\u00a0")
        buf.write("\u00a2\5`\61\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\u00a3\3\2\2\2\u00a3\u00a4\7+\2\2\u00a4\u00a5\5")
        buf.write("\32\16\2\u00a5\u00a6\5h\65\2\u00a6\t\3\2\2\2\u00a7\u00a8")
        buf.write("\7\7\2\2\u00a8\u00a9\7A\2\2\u00a9\u00ab\7/\2\2\u00aa\u00ac")
        buf.write("\5\16\b\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac")
        buf.write("\u00ad\3\2\2\2\u00ad\u00af\7\60\2\2\u00ae\u00b0\5`\61")
        buf.write("\2\u00af\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1")
        buf.write("\3\2\2\2\u00b1\u00b2\5X-\2\u00b2\13\3\2\2\2\u00b3\u00b4")
        buf.write("\7\7\2\2\u00b4\u00b5\7/\2\2\u00b5\u00b6\7A\2\2\u00b6\u00b7")
        buf.write("\7A\2\2\u00b7\u00b8\7\60\2\2\u00b8\u00b9\7A\2\2\u00b9")
        buf.write("\u00bb\7/\2\2\u00ba\u00bc\5\16\b\2\u00bb\u00ba\3\2\2\2")
        buf.write("\u00bb\u00bc\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00bf\7")
        buf.write("\60\2\2\u00be\u00c0\5`\61\2\u00bf\u00be\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c2\5X-\2\u00c2")
        buf.write("\r\3\2\2\2\u00c3\u00c4\5\20\t\2\u00c4\u00c5\7\63\2\2\u00c5")
        buf.write("\u00c6\5\16\b\2\u00c6\u00c9\3\2\2\2\u00c7\u00c9\5\20\t")
        buf.write("\2\u00c8\u00c3\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9\17\3")
        buf.write("\2\2\2\u00ca\u00cb\5\22\n\2\u00cb\u00cc\5`\61\2\u00cc")
        buf.write("\21\3\2\2\2\u00cd\u00ce\7A\2\2\u00ce\u00cf\7\63\2\2\u00cf")
        buf.write("\u00d2\5\22\n\2\u00d0\u00d2\7A\2\2\u00d1\u00cd\3\2\2\2")
        buf.write("\u00d1\u00d0\3\2\2\2\u00d2\23\3\2\2\2\u00d3\u00d4\7\b")
        buf.write("\2\2\u00d4\u00d5\5T+\2\u00d5\25\3\2\2\2\u00d6\u00d7\7")
        buf.write("\b\2\2\u00d7\u00d8\7A\2\2\u00d8\u00d9\7\n\2\2\u00d9\u00de")
        buf.write("\7\61\2\2\u00da\u00dd\7B\2\2\u00db\u00dd\5\30\r\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\u00e0\3\2\2\2")
        buf.write("\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e1\3")
        buf.write("\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e2\7\62\2\2\u00e2")
        buf.write("\u00e3\5h\65\2\u00e3\27\3\2\2\2\u00e4\u00e5\7A\2\2\u00e5")
        buf.write("\u00e7\7/\2\2\u00e6\u00e8\5\16\b\2\u00e7\u00e6\3\2\2\2")
        buf.write("\u00e7\u00e8\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00eb\7")
        buf.write("\60\2\2\u00ea\u00ec\5`\61\2\u00eb\u00ea\3\2\2\2\u00eb")
        buf.write("\u00ec\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee\5h\65\2")
        buf.write("\u00ee\31\3\2\2\2\u00ef\u00f0\b\16\1\2\u00f0\u00f1\5\34")
        buf.write("\17\2\u00f1\u00f7\3\2\2\2\u00f2\u00f3\f\4\2\2\u00f3\u00f4")
        buf.write("\7#\2\2\u00f4\u00f6\5\34\17\2\u00f5\u00f2\3\2\2\2\u00f6")
        buf.write("\u00f9\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2")
        buf.write("\u00f8\33\3\2\2\2\u00f9\u00f7\3\2\2\2\u00fa\u00fb\b\17")
        buf.write("\1\2\u00fb\u00fc\5\36\20\2\u00fc\u0102\3\2\2\2\u00fd\u00fe")
        buf.write("\f\4\2\2\u00fe\u00ff\7\"\2\2\u00ff\u0101\5\36\20\2\u0100")
        buf.write("\u00fd\3\2\2\2\u0101\u0104\3\2\2\2\u0102\u0100\3\2\2\2")
        buf.write("\u0102\u0103\3\2\2\2\u0103\35\3\2\2\2\u0104\u0102\3\2")
        buf.write("\2\2\u0105\u0106\b\20\1\2\u0106\u0107\5 \21\2\u0107\u010d")
        buf.write("\3\2\2\2\u0108\u0109\f\4\2\2\u0109\u010a\t\2\2\2\u010a")
        buf.write("\u010c\5 \21\2\u010b\u0108\3\2\2\2\u010c\u010f\3\2\2\2")
        buf.write("\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\37\3\2")
        buf.write("\2\2\u010f\u010d\3\2\2\2\u0110\u0111\b\21\1\2\u0111\u0112")
        buf.write("\5\"\22\2\u0112\u0118\3\2\2\2\u0113\u0114\f\4\2\2\u0114")
        buf.write("\u0115\t\3\2\2\u0115\u0117\5\"\22\2\u0116\u0113\3\2\2")
        buf.write("\2\u0117\u011a\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0119")
        buf.write("\3\2\2\2\u0119!\3\2\2\2\u011a\u0118\3\2\2\2\u011b\u011c")
        buf.write("\b\22\1\2\u011c\u011d\5$\23\2\u011d\u0123\3\2\2\2\u011e")
        buf.write("\u011f\f\4\2\2\u011f\u0120\t\4\2\2\u0120\u0122\5$\23\2")
        buf.write("\u0121\u011e\3\2\2\2\u0122\u0125\3\2\2\2\u0123\u0121\3")
        buf.write("\2\2\2\u0123\u0124\3\2\2\2\u0124#\3\2\2\2\u0125\u0123")
        buf.write("\3\2\2\2\u0126\u0127\t\5\2\2\u0127\u012a\5$\23\2\u0128")
        buf.write("\u012a\5&\24\2\u0129\u0126\3\2\2\2\u0129\u0128\3\2\2\2")
        buf.write("\u012a%\3\2\2\2\u012b\u012c\b\24\1\2\u012c\u012d\5(\25")
        buf.write("\2\u012d\u0139\3\2\2\2\u012e\u0135\f\4\2\2\u012f\u0136")
        buf.write("\5d\63\2\u0130\u0133\7,\2\2\u0131\u0134\7A\2\2\u0132\u0134")
        buf.write("\5Z.\2\u0133\u0131\3\2\2\2\u0133\u0132\3\2\2\2\u0134\u0136")
        buf.write("\3\2\2\2\u0135\u012f\3\2\2\2\u0135\u0130\3\2\2\2\u0136")
        buf.write("\u0138\3\2\2\2\u0137\u012e\3\2\2\2\u0138\u013b\3\2\2\2")
        buf.write("\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a\'\3\2\2")
        buf.write("\2\u013b\u0139\3\2\2\2\u013c\u0144\5*\26\2\u013d\u013e")
        buf.write("\7/\2\2\u013e\u013f\5\32\16\2\u013f\u0140\7\60\2\2\u0140")
        buf.write("\u0144\3\2\2\2\u0141\u0144\7A\2\2\u0142\u0144\5Z.\2\u0143")
        buf.write("\u013c\3\2\2\2\u0143\u013d\3\2\2\2\u0143\u0141\3\2\2\2")
        buf.write("\u0143\u0142\3\2\2\2\u0144)\3\2\2\2\u0145\u0150\7=\2\2")
        buf.write("\u0146\u0150\7:\2\2\u0147\u0150\7;\2\2\u0148\u0150\7<")
        buf.write("\2\2\u0149\u0150\7>\2\2\u014a\u0150\7?\2\2\u014b\u0150")
        buf.write("\5j\66\2\u014c\u0150\7\24\2\2\u014d\u0150\5n8\2\u014e")
        buf.write("\u0150\5x=\2\u014f\u0145\3\2\2\2\u014f\u0146\3\2\2\2\u014f")
        buf.write("\u0147\3\2\2\2\u014f\u0148\3\2\2\2\u014f\u0149\3\2\2\2")
        buf.write("\u014f\u014a\3\2\2\2\u014f\u014b\3\2\2\2\u014f\u014c\3")
        buf.write("\2\2\2\u014f\u014d\3\2\2\2\u014f\u014e\3\2\2\2\u0150+")
        buf.write("\3\2\2\2\u0151\u0152\5.\30\2\u0152\u0153\5,\27\2\u0153")
        buf.write("\u0156\3\2\2\2\u0154\u0156\5.\30\2\u0155\u0151\3\2\2\2")
        buf.write("\u0155\u0154\3\2\2\2\u0156-\3\2\2\2\u0157\u0158\5\6\4")
        buf.write("\2\u0158\u0159\5h\65\2\u0159\u0168\3\2\2\2\u015a\u0168")
        buf.write("\5\b\5\2\u015b\u0168\5\24\13\2\u015c\u0168\5\f\7\2\u015d")
        buf.write("\u015e\5\60\31\2\u015e\u015f\5h\65\2\u015f\u0168\3\2\2")
        buf.write("\2\u0160\u0168\5\66\34\2\u0161\u0168\5<\37\2\u0162\u0168")
        buf.write("\5J&\2\u0163\u0168\5L\'\2\u0164\u0168\5N(\2\u0165\u0168")
        buf.write("\5P)\2\u0166\u0168\5X-\2\u0167\u0157\3\2\2\2\u0167\u015a")
        buf.write("\3\2\2\2\u0167\u015b\3\2\2\2\u0167\u015c\3\2\2\2\u0167")
        buf.write("\u015d\3\2\2\2\u0167\u0160\3\2\2\2\u0167\u0161\3\2\2\2")
        buf.write("\u0167\u0162\3\2\2\2\u0167\u0163\3\2\2\2\u0167\u0164\3")
        buf.write("\2\2\2\u0167\u0165\3\2\2\2\u0167\u0166\3\2\2\2\u0168/")
        buf.write("\3\2\2\2\u0169\u016a\5\62\32\2\u016a\u016b\5\64\33\2\u016b")
        buf.write("\u016c\5\32\16\2\u016c\61\3\2\2\2\u016d\u016e\b\32\1\2")
        buf.write("\u016e\u016f\7A\2\2\u016f\u0178\3\2\2\2\u0170\u0174\f")
        buf.write("\4\2\2\u0171\u0175\5d\63\2\u0172\u0173\7,\2\2\u0173\u0175")
        buf.write("\7A\2\2\u0174\u0171\3\2\2\2\u0174\u0172\3\2\2\2\u0175")
        buf.write("\u0177\3\2\2\2\u0176\u0170\3\2\2\2\u0177\u017a\3\2\2\2")
        buf.write("\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\63\3\2")
        buf.write("\2\2\u017a\u0178\3\2\2\2\u017b\u017c\t\6\2\2\u017c\65")
        buf.write("\3\2\2\2\u017d\u017e\7\3\2\2\u017e\u017f\7/\2\2\u017f")
        buf.write("\u0180\5\32\16\2\u0180\u0182\7\60\2\2\u0181\u0183\5~@")
        buf.write("\2\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184")
        buf.write("\3\2\2\2\u0184\u0186\5X-\2\u0185\u0187\58\35\2\u0186\u0185")
        buf.write("\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u018d\3\2\2\2\u0188")
        buf.write("\u018a\7\4\2\2\u0189\u018b\5~@\2\u018a\u0189\3\2\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018e\5X-\2\u018d")
        buf.write("\u0188\3\2\2\2\u018d\u018e\3\2\2\2\u018e\67\3\2\2\2\u018f")
        buf.write("\u0190\5:\36\2\u0190\u0191\58\35\2\u0191\u0194\3\2\2\2")
        buf.write("\u0192\u0194\5:\36\2\u0193\u018f\3\2\2\2\u0193\u0192\3")
        buf.write("\2\2\2\u01949\3\2\2\2\u0195\u0196\7\4\2\2\u0196\u0197")
        buf.write("\7\3\2\2\u0197\u0198\7/\2\2\u0198\u0199\5\32\16\2\u0199")
        buf.write("\u019b\7\60\2\2\u019a\u019c\5~@\2\u019b\u019a\3\2\2\2")
        buf.write("\u019b\u019c\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019e\5")
        buf.write("X-\2\u019e;\3\2\2\2\u019f\u01a3\5> \2\u01a0\u01a3\5@!")
        buf.write("\2\u01a1\u01a3\5B\"\2\u01a2\u019f\3\2\2\2\u01a2\u01a0")
        buf.write("\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3\u01a5\3\2\2\2\u01a4")
        buf.write("\u01a6\5~@\2\u01a5\u01a4\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("\u01a7\3\2\2\2\u01a7\u01a8\5X-\2\u01a8=\3\2\2\2\u01a9")
        buf.write("\u01aa\7\5\2\2\u01aa\u01ab\5\32\16\2\u01ab?\3\2\2\2\u01ac")
        buf.write("\u01af\7\5\2\2\u01ad\u01b0\5\60\31\2\u01ae\u01b0\5\6\4")
        buf.write("\2\u01af\u01ad\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0\u01b1")
        buf.write("\3\2\2\2\u01b1\u01b2\7\66\2\2\u01b2\u01b3\5\32\16\2\u01b3")
        buf.write("\u01b4\7\66\2\2\u01b4\u01b5\5\60\31\2\u01b5A\3\2\2\2\u01b6")
        buf.write("\u01b7\7\5\2\2\u01b7\u01b8\5D#\2\u01b8\u01b9\7\63\2\2")
        buf.write("\u01b9\u01ba\7A\2\2\u01ba\u01bb\7%\2\2\u01bb\u01bc\7\23")
        buf.write("\2\2\u01bc\u01bd\5\32\16\2\u01bdC\3\2\2\2\u01be\u01c1")
        buf.write("\5F$\2\u01bf\u01c1\5H%\2\u01c0\u01be\3\2\2\2\u01c0\u01bf")
        buf.write("\3\2\2\2\u01c1E\3\2\2\2\u01c2\u01c3\t\7\2\2\u01c3G\3\2")
        buf.write("\2\2\u01c4\u01c5\t\7\2\2\u01c5\u01c6\7\63\2\2\u01c6\u01c7")
        buf.write("\t\7\2\2\u01c7I\3\2\2\2\u01c8\u01c9\7\22\2\2\u01c9\u01ca")
        buf.write("\5h\65\2\u01caK\3\2\2\2\u01cb\u01cc\7\21\2\2\u01cc\u01cd")
        buf.write("\5h\65\2\u01cdM\3\2\2\2\u01ce\u01cf\5\62\32\2\u01cf\u01d0")
        buf.write("\7,\2\2\u01d0\u01d3\3\2\2\2\u01d1\u01d3\3\2\2\2\u01d2")
        buf.write("\u01ce\3\2\2\2\u01d2\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2")
        buf.write("\u01d4\u01d5\7A\2\2\u01d5\u01d8\7/\2\2\u01d6\u01d9\5\\")
        buf.write("/\2\u01d7\u01d9\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d7")
        buf.write("\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01db\7\60\2\2\u01db")
        buf.write("\u01dc\5h\65\2\u01dcO\3\2\2\2\u01dd\u01e0\7\6\2\2\u01de")
        buf.write("\u01e1\5\32\16\2\u01df\u01e1\3\2\2\2\u01e0\u01de\3\2\2")
        buf.write("\2\u01e0\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3")
        buf.write("\5h\65\2\u01e3Q\3\2\2\2\u01e4\u01e7\5d\63\2\u01e5\u01e8")
        buf.write("\5b\62\2\u01e6\u01e8\7A\2\2\u01e7\u01e5\3\2\2\2\u01e7")
        buf.write("\u01e6\3\2\2\2\u01e8S\3\2\2\2\u01e9\u01ea\7A\2\2\u01ea")
        buf.write("\u01eb\7\t\2\2\u01eb\u01f0\7\61\2\2\u01ec\u01ef\7B\2\2")
        buf.write("\u01ed\u01ef\5V,\2\u01ee\u01ec\3\2\2\2\u01ee\u01ed\3\2")
        buf.write("\2\2\u01ef\u01f2\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01f1")
        buf.write("\3\2\2\2\u01f1\u01f3\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f3")
        buf.write("\u01f5\7\62\2\2\u01f4\u01f6\5h\65\2\u01f5\u01f4\3\2\2")
        buf.write("\2\u01f5\u01f6\3\2\2\2\u01f6U\3\2\2\2\u01f7\u01f8\7A\2")
        buf.write("\2\u01f8\u01f9\5`\61\2\u01f9\u01fa\5h\65\2\u01faW\3\2")
        buf.write("\2\2\u01fb\u01fd\7\61\2\2\u01fc\u01fe\5,\27\2\u01fd\u01fc")
        buf.write("\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write("\u0203\7\62\2\2\u0200\u0202\5h\65\2\u0201\u0200\3\2\2")
        buf.write("\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2\u0203\u0204")
        buf.write("\3\2\2\2\u0204Y\3\2\2\2\u0205\u0203\3\2\2\2\u0206\u0207")
        buf.write("\7A\2\2\u0207\u020a\7/\2\2\u0208\u020b\5\\/\2\u0209\u020b")
        buf.write("\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u0209\3\2\2\2\u020b")
        buf.write("\u020c\3\2\2\2\u020c\u020d\7\60\2\2\u020d[\3\2\2\2\u020e")
        buf.write("\u020f\5\32\16\2\u020f\u0210\5^\60\2\u0210\u0213\3\2\2")
        buf.write("\2\u0211\u0213\5\32\16\2\u0212\u020e\3\2\2\2\u0212\u0211")
        buf.write("\3\2\2\2\u0213]\3\2\2\2\u0214\u0215\7\63\2\2\u0215\u0216")
        buf.write("\5\32\16\2\u0216\u0217\5^\60\2\u0217\u021a\3\2\2\2\u0218")
        buf.write("\u021a\3\2\2\2\u0219\u0214\3\2\2\2\u0219\u0218\3\2\2\2")
        buf.write("\u021a_\3\2\2\2\u021b\u0222\7\f\2\2\u021c\u0222\7\r\2")
        buf.write("\2\u021d\u0222\7\16\2\2\u021e\u0222\7\13\2\2\u021f\u0222")
        buf.write("\5R*\2\u0220\u0222\7A\2\2\u0221\u021b\3\2\2\2\u0221\u021c")
        buf.write("\3\2\2\2\u0221\u021d\3\2\2\2\u0221\u021e\3\2\2\2\u0221")
        buf.write("\u021f\3\2\2\2\u0221\u0220\3\2\2\2\u0222a\3\2\2\2\u0223")
        buf.write("\u0224\t\b\2\2\u0224c\3\2\2\2\u0225\u0226\5f\64\2\u0226")
        buf.write("\u0227\5d\63\2\u0227\u022a\3\2\2\2\u0228\u022a\5f\64\2")
        buf.write("\u0229\u0225\3\2\2\2\u0229\u0228\3\2\2\2\u022ae\3\2\2")
        buf.write("\2\u022b\u022c\7-\2\2\u022c\u022d\5\32\16\2\u022d\u022e")
        buf.write("\7.\2\2\u022eg\3\2\2\2\u022f\u0236\7\66\2\2\u0230\u0232")
        buf.write("\7B\2\2\u0231\u0230\3\2\2\2\u0232\u0233\3\2\2\2\u0233")
        buf.write("\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0236\3\2\2\2")
        buf.write("\u0235\u022f\3\2\2\2\u0235\u0231\3\2\2\2\u0236i\3\2\2")
        buf.write("\2\u0237\u0238\t\t\2\2\u0238k\3\2\2\2\u0239\u0243\7=\2")
        buf.write("\2\u023a\u0243\7:\2\2\u023b\u0243\7;\2\2\u023c\u0243\7")
        buf.write("<\2\2\u023d\u0243\7>\2\2\u023e\u0243\7?\2\2\u023f\u0243")
        buf.write("\5j\66\2\u0240\u0243\7\24\2\2\u0241\u0243\5x=\2\u0242")
        buf.write("\u0239\3\2\2\2\u0242\u023a\3\2\2\2\u0242\u023b\3\2\2\2")
        buf.write("\u0242\u023c\3\2\2\2\u0242\u023d\3\2\2\2\u0242\u023e\3")
        buf.write("\2\2\2\u0242\u023f\3\2\2\2\u0242\u0240\3\2\2\2\u0242\u0241")
        buf.write("\3\2\2\2\u0243m\3\2\2\2\u0244\u0245\5d\63\2\u0245\u0246")
        buf.write("\5`\61\2\u0246\u0248\7\61\2\2\u0247\u0249\5p9\2\u0248")
        buf.write("\u0247\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u024a\3\2\2\2")
        buf.write("\u024a\u024b\7\62\2\2\u024bo\3\2\2\2\u024c\u024d\5r:\2")
        buf.write("\u024d\u024e\7\63\2\2\u024e\u024f\5p9\2\u024f\u0252\3")
        buf.write("\2\2\2\u0250\u0252\5r:\2\u0251\u024c\3\2\2\2\u0251\u0250")
        buf.write("\3\2\2\2\u0252q\3\2\2\2\u0253\u0259\5t;\2\u0254\u0255")
        buf.write("\7\61\2\2\u0255\u0256\5r:\2\u0256\u0257\7\62\2\2\u0257")
        buf.write("\u0259\3\2\2\2\u0258\u0253\3\2\2\2\u0258\u0254\3\2\2\2")
        buf.write("\u0259s\3\2\2\2\u025a\u025b\5v<\2\u025b\u025c\7\63\2\2")
        buf.write("\u025c\u025d\5t;\2\u025d\u0260\3\2\2\2\u025e\u0260\5v")
        buf.write("<\2\u025f\u025a\3\2\2\2\u025f\u025e\3\2\2\2\u0260u\3\2")
        buf.write("\2\2\u0261\u0268\5l\67\2\u0262\u0268\5\32\16\2\u0263\u0264")
        buf.write("\7\61\2\2\u0264\u0265\5r:\2\u0265\u0266\7\62\2\2\u0266")
        buf.write("\u0268\3\2\2\2\u0267\u0261\3\2\2\2\u0267\u0262\3\2\2\2")
        buf.write("\u0267\u0263\3\2\2\2\u0268w\3\2\2\2\u0269\u026a\7A\2\2")
        buf.write("\u026a\u026c\7\61\2\2\u026b\u026d\5z>\2\u026c\u026b\3")
        buf.write("\2\2\2\u026c\u026d\3\2\2\2\u026d\u026e\3\2\2\2\u026e\u026f")
        buf.write("\7\62\2\2\u026fy\3\2\2\2\u0270\u0271\5|?\2\u0271\u0272")
        buf.write("\7\63\2\2\u0272\u0273\5z>\2\u0273\u0276\3\2\2\2\u0274")
        buf.write("\u0276\5|?\2\u0275\u0270\3\2\2\2\u0275\u0274\3\2\2\2\u0276")
        buf.write("{\3\2\2\2\u0277\u0278\7A\2\2\u0278\u0279\7\64\2\2\u0279")
        buf.write("\u027a\5\32\16\2\u027a}\3\2\2\2\u027b\u027d\7B\2\2\u027c")
        buf.write("\u027b\3\2\2\2\u027d\u027e\3\2\2\2\u027e\u027c\3\2\2\2")
        buf.write("\u027e\u027f\3\2\2\2\u027f\177\3\2\2\2D\u0081\u0086\u0092")
        buf.write("\u0098\u009c\u00a1\u00ab\u00af\u00bb\u00bf\u00c8\u00d1")
        buf.write("\u00dc\u00de\u00e7\u00eb\u00f7\u0102\u010d\u0118\u0123")
        buf.write("\u0129\u0133\u0135\u0139\u0143\u014f\u0155\u0167\u0174")
        buf.write("\u0178\u0182\u0186\u018a\u018d\u0193\u019b\u01a2\u01a5")
        buf.write("\u01af\u01c0\u01d2\u01d8\u01e0\u01e7\u01ee\u01f0\u01f5")
        buf.write("\u01fd\u0203\u020a\u0212\u0219\u0221\u0229\u0233\u0235")
        buf.write("\u0242\u0248\u0251\u0258\u025f\u0267\u026c\u0275\u027e")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'='", "'.'", "'['", "']'", "'('", "')'", "'{'", "'}'", 
                     "','", "':'", "'\"'", "';'", "'_'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD_OP", "SUB_OP", "MUL_OP", 
                      "DIV_OP", "MOD_OP", "EQ_OP", "NEQ_OP", "LT_OP", "LEQ_OP", 
                      "GT_OP", "GEQ_OP", "AND_OP", "OR_OP", "NOT_OP", "EQ_ASSIGN_OP", 
                      "ADD_ASSIGN_OP", "SUB_ASSIGN_OP", "MUL_ASSIGN_OP", 
                      "DIV_ASSIGN_OP", "MOD_ASSIGN_OP", "EQ", "DOT_OP", 
                      "LSB", "RSB", "LRB", "RRB", "LCB", "RCB", "CM", "COL", 
                      "QUOTES", "SM", "UNDERSCORE", "LINE_CMT", "COMMENT", 
                      "BINLIT", "OCTLIT", "HEXLIT", "INTLIT", "FLOATLIT", 
                      "STRINGLIT", "NILLIT", "ID", "NL", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_var_decl = 2
    RULE_const_decl = 3
    RULE_func_decl = 4
    RULE_method_decl = 5
    RULE_parameter_list = 6
    RULE_parameter = 7
    RULE_list_ID = 8
    RULE_struct_decl = 9
    RULE_interface_decl = 10
    RULE_interface_method = 11
    RULE_expr = 12
    RULE_expr1 = 13
    RULE_expr2 = 14
    RULE_expr3 = 15
    RULE_expr4 = 16
    RULE_expr5 = 17
    RULE_expr6 = 18
    RULE_factor = 19
    RULE_literal = 20
    RULE_stmt_list = 21
    RULE_statement = 22
    RULE_assign_stmt = 23
    RULE_assignment_lhs = 24
    RULE_assign_op = 25
    RULE_if_stmt = 26
    RULE_list_elif = 27
    RULE_elif_one = 28
    RULE_for_stmt = 29
    RULE_basic_for = 30
    RULE_init_for = 31
    RULE_range_for = 32
    RULE_range_vars = 33
    RULE_single_var = 34
    RULE_dual_var = 35
    RULE_break_stmt = 36
    RULE_continue_stmt = 37
    RULE_call_stmt = 38
    RULE_return_stmt = 39
    RULE_array_type = 40
    RULE_struct_type = 41
    RULE_struct_field = 42
    RULE_body = 43
    RULE_func_call = 44
    RULE_expr_list = 45
    RULE_expr_tail = 46
    RULE_all_type = 47
    RULE_prim_types = 48
    RULE_list_array_index = 49
    RULE_array_index = 50
    RULE_sm_nl = 51
    RULE_boollit = 52
    RULE_array_item = 53
    RULE_arraylit = 54
    RULE_list_array_element = 55
    RULE_array_element = 56
    RULE_itemlist = 57
    RULE_item = 58
    RULE_structlit = 59
    RULE_list_struct_element = 60
    RULE_structlit_element = 61
    RULE_list_newline = 62

    ruleNames =  [ "program", "decl", "var_decl", "const_decl", "func_decl", 
                   "method_decl", "parameter_list", "parameter", "list_ID", 
                   "struct_decl", "interface_decl", "interface_method", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "factor", "literal", "stmt_list", "statement", 
                   "assign_stmt", "assignment_lhs", "assign_op", "if_stmt", 
                   "list_elif", "elif_one", "for_stmt", "basic_for", "init_for", 
                   "range_for", "range_vars", "single_var", "dual_var", 
                   "break_stmt", "continue_stmt", "call_stmt", "return_stmt", 
                   "array_type", "struct_type", "struct_field", "body", 
                   "func_call", "expr_list", "expr_tail", "all_type", "prim_types", 
                   "list_array_index", "array_index", "sm_nl", "boollit", 
                   "array_item", "arraylit", "list_array_element", "array_element", 
                   "itemlist", "item", "structlit", "list_struct_element", 
                   "structlit_element", "list_newline" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD_OP=21
    SUB_OP=22
    MUL_OP=23
    DIV_OP=24
    MOD_OP=25
    EQ_OP=26
    NEQ_OP=27
    LT_OP=28
    LEQ_OP=29
    GT_OP=30
    GEQ_OP=31
    AND_OP=32
    OR_OP=33
    NOT_OP=34
    EQ_ASSIGN_OP=35
    ADD_ASSIGN_OP=36
    SUB_ASSIGN_OP=37
    MUL_ASSIGN_OP=38
    DIV_ASSIGN_OP=39
    MOD_ASSIGN_OP=40
    EQ=41
    DOT_OP=42
    LSB=43
    RSB=44
    LRB=45
    RRB=46
    LCB=47
    RCB=48
    CM=49
    COL=50
    QUOTES=51
    SM=52
    UNDERSCORE=53
    LINE_CMT=54
    COMMENT=55
    BINLIT=56
    OCTLIT=57
    HEXLIT=58
    INTLIT=59
    FLOATLIT=60
    STRINGLIT=61
    NILLIT=62
    ID=63
    NL=64
    WS=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67
    ERROR_CHAR=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def list_newline(self):
            return self.getTypedRuleContext(MiniGoParser.List_newlineContext,0)


        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NL:
                self.state = 126
                self.list_newline()


            self.state = 130 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 129
                self.decl()
                self.state = 132 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 134
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def sm_nl(self):
            return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 136
                self.var_decl()
                self.state = 137
                self.sm_nl()
                pass

            elif la_ == 2:
                self.state = 139
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 140
                self.func_decl()
                pass

            elif la_ == 4:
                self.state = 141
                self.method_decl()
                pass

            elif la_ == 5:
                self.state = 142
                self.struct_decl()
                pass

            elif la_ == 6:
                self.state = 143
                self.interface_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(MiniGoParser.VAR)
            self.state = 147
            self.match(MiniGoParser.ID)
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 148
                self.all_type()
                pass

            elif la_ == 2:
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 149
                    self.all_type()


                self.state = 152
                self.match(MiniGoParser.EQ)
                self.state = 153
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def sm_nl(self):
            return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_const_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(MiniGoParser.CONST)
            self.state = 157
            self.match(MiniGoParser.ID)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 158
                self.all_type()


            self.state = 161
            self.match(MiniGoParser.EQ)
            self.state = 162
            self.expr(0)
            self.state = 163
            self.sm_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LRB(self):
            return self.getToken(MiniGoParser.LRB, 0)

        def RRB(self):
            return self.getToken(MiniGoParser.RRB, 0)

        def body(self):
            return self.getTypedRuleContext(MiniGoParser.BodyContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_listContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(MiniGoParser.FUNC)
            self.state = 166
            self.match(MiniGoParser.ID)
            self.state = 167
            self.match(MiniGoParser.LRB)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 168
                self.parameter_list()


            self.state = 171
            self.match(MiniGoParser.RRB)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 172
                self.all_type()


            self.state = 175
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LRB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LRB)
            else:
                return self.getToken(MiniGoParser.LRB, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RRB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RRB)
            else:
                return self.getToken(MiniGoParser.RRB, i)

        def body(self):
            return self.getTypedRuleContext(MiniGoParser.BodyContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_listContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(MiniGoParser.FUNC)
            self.state = 178
            self.match(MiniGoParser.LRB)
            self.state = 179
            self.match(MiniGoParser.ID)
            self.state = 180
            self.match(MiniGoParser.ID)
            self.state = 181
            self.match(MiniGoParser.RRB)
            self.state = 182
            self.match(MiniGoParser.ID)
            self.state = 183
            self.match(MiniGoParser.LRB)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 184
                self.parameter_list()


            self.state = 187
            self.match(MiniGoParser.RRB)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 188
                self.all_type()


            self.state = 191
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterContext,0)


        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = MiniGoParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameter_list)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.parameter()
                self.state = 194
                self.match(MiniGoParser.CM)
                self.state = 195
                self.parameter_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MiniGoParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.list_ID()
            self.state = 201
            self.all_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_IDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_ID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_ID" ):
                return visitor.visitList_ID(self)
            else:
                return visitor.visitChildren(self)




    def list_ID(self):

        localctx = MiniGoParser.List_IDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_ID)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(MiniGoParser.ID)
                self.state = 204
                self.match(MiniGoParser.CM)
                self.state = 205
                self.list_ID()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MiniGoParser.TYPE)
            self.state = 210
            self.struct_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def sm_nl(self):
            return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

        def interface_method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Interface_methodContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_interface_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(MiniGoParser.TYPE)
            self.state = 213
            self.match(MiniGoParser.ID)
            self.state = 214
            self.match(MiniGoParser.INTERFACE)
            self.state = 215
            self.match(MiniGoParser.LCB)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID or _la==MiniGoParser.NL:
                self.state = 218
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NL]:
                    self.state = 216
                    self.match(MiniGoParser.NL)
                    pass
                elif token in [MiniGoParser.ID]:
                    self.state = 217
                    self.interface_method()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
            self.match(MiniGoParser.RCB)
            self.state = 224
            self.sm_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LRB(self):
            return self.getToken(MiniGoParser.LRB, 0)

        def RRB(self):
            return self.getToken(MiniGoParser.RRB, 0)

        def sm_nl(self):
            return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_listContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method" ):
                return visitor.visitInterface_method(self)
            else:
                return visitor.visitChildren(self)




    def interface_method(self):

        localctx = MiniGoParser.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_interface_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(MiniGoParser.ID)
            self.state = 227
            self.match(MiniGoParser.LRB)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 228
                self.parameter_list()


            self.state = 231
            self.match(MiniGoParser.RRB)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 232
                self.all_type()


            self.state = 235
            self.sm_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR_OP(self):
            return self.getToken(MiniGoParser.OR_OP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 245
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 240
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 241
                    self.match(MiniGoParser.OR_OP)
                    self.state = 242
                    self.expr1(0) 
                self.state = 247
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND_OP(self):
            return self.getToken(MiniGoParser.AND_OP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 256
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 251
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 252
                    self.match(MiniGoParser.AND_OP)
                    self.state = 253
                    self.expr2(0) 
                self.state = 258
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def EQ_OP(self):
            return self.getToken(MiniGoParser.EQ_OP, 0)

        def NEQ_OP(self):
            return self.getToken(MiniGoParser.NEQ_OP, 0)

        def LT_OP(self):
            return self.getToken(MiniGoParser.LT_OP, 0)

        def LEQ_OP(self):
            return self.getToken(MiniGoParser.LEQ_OP, 0)

        def GT_OP(self):
            return self.getToken(MiniGoParser.GT_OP, 0)

        def GEQ_OP(self):
            return self.getToken(MiniGoParser.GEQ_OP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 262
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 263
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ_OP) | (1 << MiniGoParser.NEQ_OP) | (1 << MiniGoParser.LT_OP) | (1 << MiniGoParser.LEQ_OP) | (1 << MiniGoParser.GT_OP) | (1 << MiniGoParser.GEQ_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 264
                    self.expr3(0) 
                self.state = 269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def ADD_OP(self):
            return self.getToken(MiniGoParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(MiniGoParser.SUB_OP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 273
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 274
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD_OP or _la==MiniGoParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 275
                    self.expr4(0) 
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def MUL_OP(self):
            return self.getToken(MiniGoParser.MUL_OP, 0)

        def DIV_OP(self):
            return self.getToken(MiniGoParser.DIV_OP, 0)

        def MOD_OP(self):
            return self.getToken(MiniGoParser.MOD_OP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 289
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 284
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 285
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL_OP) | (1 << MiniGoParser.DIV_OP) | (1 << MiniGoParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 286
                    self.expr5() 
                self.state = 291
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def NOT_OP(self):
            return self.getToken(MiniGoParser.NOT_OP, 0)

        def SUB_OP(self):
            return self.getToken(MiniGoParser.SUB_OP, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB_OP, MiniGoParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB_OP or _la==MiniGoParser.NOT_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 293
                self.expr5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LSB, MiniGoParser.LRB, MiniGoParser.BINLIT, MiniGoParser.OCTLIT, MiniGoParser.HEXLIT, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.expr6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(MiniGoParser.FactorContext,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def list_array_index(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_indexContext,0)


        def DOT_OP(self):
            return self.getToken(MiniGoParser.DOT_OP, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 300
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 307
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LSB]:
                        self.state = 301
                        self.list_array_index()
                        pass
                    elif token in [MiniGoParser.DOT_OP]:
                        self.state = 302
                        self.match(MiniGoParser.DOT_OP)
                        self.state = 305
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                        if la_ == 1:
                            self.state = 303
                            self.match(MiniGoParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 304
                            self.func_call()
                            pass


                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def LRB(self):
            return self.getToken(MiniGoParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RRB(self):
            return self.getToken(MiniGoParser.RRB, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = MiniGoParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_factor)
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.match(MiniGoParser.LRB)
                self.state = 316
                self.expr(0)
                self.state = 317
                self.match(MiniGoParser.RRB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 319
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 320
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def BINLIT(self):
            return self.getToken(MiniGoParser.BINLIT, 0)

        def OCTLIT(self):
            return self.getToken(MiniGoParser.OCTLIT, 0)

        def HEXLIT(self):
            return self.getToken(MiniGoParser.HEXLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MiniGoParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def boollit(self):
            return self.getTypedRuleContext(MiniGoParser.BoollitContext,0)


        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def arraylit(self):
            return self.getTypedRuleContext(MiniGoParser.ArraylitContext,0)


        def structlit(self):
            return self.getTypedRuleContext(MiniGoParser.StructlitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_literal)
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(MiniGoParser.INTLIT)
                pass
            elif token in [MiniGoParser.BINLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.match(MiniGoParser.BINLIT)
                pass
            elif token in [MiniGoParser.OCTLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 325
                self.match(MiniGoParser.OCTLIT)
                pass
            elif token in [MiniGoParser.HEXLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 326
                self.match(MiniGoParser.HEXLIT)
                pass
            elif token in [MiniGoParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 327
                self.match(MiniGoParser.FLOATLIT)
                pass
            elif token in [MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 328
                self.match(MiniGoParser.STRINGLIT)
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 329
                self.boollit()
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 330
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 9)
                self.state = 331
                self.arraylit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 10)
                self.state = 332
                self.structlit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = MiniGoParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stmt_list)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.statement()
                self.state = 336
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def sm_nl(self):
            return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def body(self):
            return self.getTypedRuleContext(MiniGoParser.BodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 341
                self.var_decl()
                self.state = 342
                self.sm_nl()
                pass

            elif la_ == 2:
                self.state = 344
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 345
                self.struct_decl()
                pass

            elif la_ == 4:
                self.state = 346
                self.method_decl()
                pass

            elif la_ == 5:
                self.state = 347
                self.assign_stmt()
                self.state = 348
                self.sm_nl()
                pass

            elif la_ == 6:
                self.state = 350
                self.if_stmt()
                pass

            elif la_ == 7:
                self.state = 351
                self.for_stmt()
                pass

            elif la_ == 8:
                self.state = 352
                self.break_stmt()
                pass

            elif la_ == 9:
                self.state = 353
                self.continue_stmt()
                pass

            elif la_ == 10:
                self.state = 354
                self.call_stmt()
                pass

            elif la_ == 11:
                self.state = 355
                self.return_stmt()
                pass

            elif la_ == 12:
                self.state = 356
                self.body()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhsContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = MiniGoParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.assignment_lhs(0)
            self.state = 360
            self.assign_op()
            self.state = 361
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhsContext,0)


        def list_array_index(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_indexContext,0)


        def DOT_OP(self):
            return self.getToken(MiniGoParser.DOT_OP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_lhs" ):
                return visitor.visitAssignment_lhs(self)
            else:
                return visitor.visitChildren(self)



    def assignment_lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Assignment_lhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_assignment_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Assignment_lhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignment_lhs)
                    self.state = 366
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 370
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LSB]:
                        self.state = 367
                        self.list_array_index()
                        pass
                    elif token in [MiniGoParser.DOT_OP]:
                        self.state = 368
                        self.match(MiniGoParser.DOT_OP)
                        self.state = 369
                        self.match(MiniGoParser.ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 376
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Assign_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ_ASSIGN_OP(self):
            return self.getToken(MiniGoParser.EQ_ASSIGN_OP, 0)

        def ADD_ASSIGN_OP(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN_OP, 0)

        def SUB_ASSIGN_OP(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN_OP, 0)

        def MUL_ASSIGN_OP(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN_OP, 0)

        def DIV_ASSIGN_OP(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN_OP, 0)

        def MOD_ASSIGN_OP(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN_OP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_op" ):
                return visitor.visitAssign_op(self)
            else:
                return visitor.visitChildren(self)




    def assign_op(self):

        localctx = MiniGoParser.Assign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ_ASSIGN_OP) | (1 << MiniGoParser.ADD_ASSIGN_OP) | (1 << MiniGoParser.SUB_ASSIGN_OP) | (1 << MiniGoParser.MUL_ASSIGN_OP) | (1 << MiniGoParser.DIV_ASSIGN_OP) | (1 << MiniGoParser.MOD_ASSIGN_OP))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LRB(self):
            return self.getToken(MiniGoParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RRB(self):
            return self.getToken(MiniGoParser.RRB, 0)

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BodyContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BodyContext,i)


        def list_newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.List_newlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.List_newlineContext,i)


        def list_elif(self):
            return self.getTypedRuleContext(MiniGoParser.List_elifContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(MiniGoParser.IF)
            self.state = 380
            self.match(MiniGoParser.LRB)
            self.state = 381
            self.expr(0)
            self.state = 382
            self.match(MiniGoParser.RRB)
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NL:
                self.state = 383
                self.list_newline()


            self.state = 386
            self.body()
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 387
                self.list_elif()


            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 390
                self.match(MiniGoParser.ELSE)
                self.state = 392
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.NL:
                    self.state = 391
                    self.list_newline()


                self.state = 394
                self.body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_one(self):
            return self.getTypedRuleContext(MiniGoParser.Elif_oneContext,0)


        def list_elif(self):
            return self.getTypedRuleContext(MiniGoParser.List_elifContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elif" ):
                return visitor.visitList_elif(self)
            else:
                return visitor.visitChildren(self)




    def list_elif(self):

        localctx = MiniGoParser.List_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_list_elif)
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.elif_one()
                self.state = 398
                self.list_elif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.elif_one()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_oneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LRB(self):
            return self.getToken(MiniGoParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RRB(self):
            return self.getToken(MiniGoParser.RRB, 0)

        def body(self):
            return self.getTypedRuleContext(MiniGoParser.BodyContext,0)


        def list_newline(self):
            return self.getTypedRuleContext(MiniGoParser.List_newlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elif_one

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_one" ):
                return visitor.visitElif_one(self)
            else:
                return visitor.visitChildren(self)




    def elif_one(self):

        localctx = MiniGoParser.Elif_oneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_elif_one)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(MiniGoParser.ELSE)
            self.state = 404
            self.match(MiniGoParser.IF)
            self.state = 405
            self.match(MiniGoParser.LRB)
            self.state = 406
            self.expr(0)
            self.state = 407
            self.match(MiniGoParser.RRB)
            self.state = 409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NL:
                self.state = 408
                self.list_newline()


            self.state = 411
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(MiniGoParser.BodyContext,0)


        def basic_for(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_forContext,0)


        def init_for(self):
            return self.getTypedRuleContext(MiniGoParser.Init_forContext,0)


        def range_for(self):
            return self.getTypedRuleContext(MiniGoParser.Range_forContext,0)


        def list_newline(self):
            return self.getTypedRuleContext(MiniGoParser.List_newlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 413
                self.basic_for()
                pass

            elif la_ == 2:
                self.state = 414
                self.init_for()
                pass

            elif la_ == 3:
                self.state = 415
                self.range_for()
                pass


            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NL:
                self.state = 418
                self.list_newline()


            self.state = 421
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_for" ):
                return visitor.visitBasic_for(self)
            else:
                return visitor.visitChildren(self)




    def basic_for(self):

        localctx = MiniGoParser.Basic_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_basic_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(MiniGoParser.FOR)
            self.state = 424
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SM)
            else:
                return self.getToken(MiniGoParser.SM, i)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def assign_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assign_stmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assign_stmtContext,i)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_for" ):
                return visitor.visitInit_for(self)
            else:
                return visitor.visitChildren(self)




    def init_for(self):

        localctx = MiniGoParser.Init_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_init_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(MiniGoParser.FOR)
            self.state = 429
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 427
                self.assign_stmt()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 428
                self.var_decl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 431
            self.match(MiniGoParser.SM)
            self.state = 432
            self.expr(0)
            self.state = 433
            self.match(MiniGoParser.SM)
            self.state = 434
            self.assign_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def range_vars(self):
            return self.getTypedRuleContext(MiniGoParser.Range_varsContext,0)


        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def EQ_ASSIGN_OP(self):
            return self.getToken(MiniGoParser.EQ_ASSIGN_OP, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_range_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_for" ):
                return visitor.visitRange_for(self)
            else:
                return visitor.visitChildren(self)




    def range_for(self):

        localctx = MiniGoParser.Range_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_range_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(MiniGoParser.FOR)
            self.state = 437
            self.range_vars()
            self.state = 438
            self.match(MiniGoParser.CM)
            self.state = 439
            self.match(MiniGoParser.ID)
            self.state = 440
            self.match(MiniGoParser.EQ_ASSIGN_OP)
            self.state = 441
            self.match(MiniGoParser.RANGE)
            self.state = 442
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_varsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_var(self):
            return self.getTypedRuleContext(MiniGoParser.Single_varContext,0)


        def dual_var(self):
            return self.getTypedRuleContext(MiniGoParser.Dual_varContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_range_vars

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_vars" ):
                return visitor.visitRange_vars(self)
            else:
                return visitor.visitChildren(self)




    def range_vars(self):

        localctx = MiniGoParser.Range_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_range_vars)
        try:
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.single_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.dual_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def UNDERSCORE(self):
            return self.getToken(MiniGoParser.UNDERSCORE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_single_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_var" ):
                return visitor.visitSingle_var(self)
            else:
                return visitor.visitChildren(self)




    def single_var(self):

        localctx = MiniGoParser.Single_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_single_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dual_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def UNDERSCORE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.UNDERSCORE)
            else:
                return self.getToken(MiniGoParser.UNDERSCORE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dual_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDual_var" ):
                return visitor.visitDual_var(self)
            else:
                return visitor.visitChildren(self)




    def dual_var(self):

        localctx = MiniGoParser.Dual_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_dual_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 451
            self.match(MiniGoParser.CM)
            self.state = 452
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def sm_nl(self):
            return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(MiniGoParser.BREAK)
            self.state = 455
            self.sm_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def sm_nl(self):
            return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(MiniGoParser.CONTINUE)
            self.state = 458
            self.sm_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LRB(self):
            return self.getToken(MiniGoParser.LRB, 0)

        def RRB(self):
            return self.getToken(MiniGoParser.RRB, 0)

        def sm_nl(self):
            return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,0)


        def assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhsContext,0)


        def DOT_OP(self):
            return self.getToken(MiniGoParser.DOT_OP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MiniGoParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 460
                self.assignment_lhs(0)
                self.state = 461
                self.match(MiniGoParser.DOT_OP)
                pass

            elif la_ == 2:
                pass


            self.state = 466
            self.match(MiniGoParser.ID)
            self.state = 467
            self.match(MiniGoParser.LRB)
            self.state = 470
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB_OP, MiniGoParser.NOT_OP, MiniGoParser.LSB, MiniGoParser.LRB, MiniGoParser.BINLIT, MiniGoParser.OCTLIT, MiniGoParser.HEXLIT, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT, MiniGoParser.ID]:
                self.state = 468
                self.expr_list()
                pass
            elif token in [MiniGoParser.RRB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 472
            self.match(MiniGoParser.RRB)
            self.state = 473
            self.sm_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def sm_nl(self):
            return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(MiniGoParser.RETURN)
            self.state = 478
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB_OP, MiniGoParser.NOT_OP, MiniGoParser.LSB, MiniGoParser.LRB, MiniGoParser.BINLIT, MiniGoParser.OCTLIT, MiniGoParser.HEXLIT, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT, MiniGoParser.ID]:
                self.state = 476
                self.expr(0)
                pass
            elif token in [MiniGoParser.SM, MiniGoParser.NL]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 480
            self.sm_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_array_index(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_indexContext,0)


        def prim_types(self):
            return self.getTypedRuleContext(MiniGoParser.Prim_typesContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.list_array_index()
            self.state = 485
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 483
                self.prim_types()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 484
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

        def struct_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_fieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,i)


        def sm_nl(self):
            return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_struct_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(MiniGoParser.ID)
            self.state = 488
            self.match(MiniGoParser.STRUCT)
            self.state = 489
            self.match(MiniGoParser.LCB)
            self.state = 494
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID or _la==MiniGoParser.NL:
                self.state = 492
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NL]:
                    self.state = 490
                    self.match(MiniGoParser.NL)
                    pass
                elif token in [MiniGoParser.ID]:
                    self.state = 491
                    self.struct_field()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 496
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 497
            self.match(MiniGoParser.RCB)
            self.state = 499
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SM or _la==MiniGoParser.NL:
                self.state = 498
                self.sm_nl()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def sm_nl(self):
            return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field" ):
                return visitor.visitStruct_field(self)
            else:
                return visitor.visitChildren(self)




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_struct_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(MiniGoParser.ID)
            self.state = 502
            self.all_type()
            self.state = 503
            self.sm_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_listContext,0)


        def sm_nl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Sm_nlContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MiniGoParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(MiniGoParser.LCB)
            self.state = 507
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.LCB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 506
                self.stmt_list()


            self.state = 509
            self.match(MiniGoParser.RCB)
            self.state = 513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SM or _la==MiniGoParser.NL:
                self.state = 510
                self.sm_nl()
                self.state = 515
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LRB(self):
            return self.getToken(MiniGoParser.LRB, 0)

        def RRB(self):
            return self.getToken(MiniGoParser.RRB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.match(MiniGoParser.ID)
            self.state = 517
            self.match(MiniGoParser.LRB)
            self.state = 520
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB_OP, MiniGoParser.NOT_OP, MiniGoParser.LSB, MiniGoParser.LRB, MiniGoParser.BINLIT, MiniGoParser.OCTLIT, MiniGoParser.HEXLIT, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT, MiniGoParser.ID]:
                self.state = 518
                self.expr_list()
                pass
            elif token in [MiniGoParser.RRB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 522
            self.match(MiniGoParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def expr_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = MiniGoParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr_list)
        try:
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.expr(0)
                self.state = 525
                self.expr_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def expr_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_tail" ):
                return visitor.visitExpr_tail(self)
            else:
                return visitor.visitChildren(self)




    def expr_tail(self):

        localctx = MiniGoParser.Expr_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr_tail)
        try:
            self.state = 535
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.match(MiniGoParser.CM)
                self.state = 531
                self.expr(0)
                self.state = 532
                self.expr_tail()
                pass
            elif token in [MiniGoParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_all_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_type" ):
                return visitor.visitAll_type(self)
            else:
                return visitor.visitChildren(self)




    def all_type(self):

        localctx = MiniGoParser.All_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_all_type)
        try:
            self.state = 543
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 538
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 539
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 540
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 541
                self.array_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 542
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prim_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_prim_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrim_types" ):
                return visitor.visitPrim_types(self)
            else:
                return visitor.visitChildren(self)




    def prim_types(self):

        localctx = MiniGoParser.Prim_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_prim_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_array_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_index(self):
            return self.getTypedRuleContext(MiniGoParser.Array_indexContext,0)


        def list_array_index(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_indexContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_index" ):
                return visitor.visitList_array_index(self)
            else:
                return visitor.visitChildren(self)




    def list_array_index(self):

        localctx = MiniGoParser.List_array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_list_array_index)
        try:
            self.state = 551
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                self.array_index()
                self.state = 548
                self.list_array_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 550
                self.array_index()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_index" ):
                return visitor.visitArray_index(self)
            else:
                return visitor.visitChildren(self)




    def array_index(self):

        localctx = MiniGoParser.Array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_array_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(MiniGoParser.LSB)
            self.state = 554
            self.expr(0)
            self.state = 555
            self.match(MiniGoParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sm_nlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(MiniGoParser.SM, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_sm_nl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSm_nl" ):
                return visitor.visitSm_nl(self)
            else:
                return visitor.visitChildren(self)




    def sm_nl(self):

        localctx = MiniGoParser.Sm_nlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_sm_nl)
        try:
            self.state = 563
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 557
                self.match(MiniGoParser.SM)
                pass
            elif token in [MiniGoParser.NL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 559 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 558
                        self.match(MiniGoParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 561 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoollitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_boollit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoollit" ):
                return visitor.visitBoollit(self)
            else:
                return visitor.visitChildren(self)




    def boollit(self):

        localctx = MiniGoParser.BoollitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.TRUE or _la==MiniGoParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def BINLIT(self):
            return self.getToken(MiniGoParser.BINLIT, 0)

        def OCTLIT(self):
            return self.getToken(MiniGoParser.OCTLIT, 0)

        def HEXLIT(self):
            return self.getToken(MiniGoParser.HEXLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MiniGoParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def boollit(self):
            return self.getTypedRuleContext(MiniGoParser.BoollitContext,0)


        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def structlit(self):
            return self.getTypedRuleContext(MiniGoParser.StructlitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_item" ):
                return visitor.visitArray_item(self)
            else:
                return visitor.visitChildren(self)




    def array_item(self):

        localctx = MiniGoParser.Array_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_array_item)
        try:
            self.state = 576
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 567
                self.match(MiniGoParser.INTLIT)
                pass
            elif token in [MiniGoParser.BINLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 568
                self.match(MiniGoParser.BINLIT)
                pass
            elif token in [MiniGoParser.OCTLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 569
                self.match(MiniGoParser.OCTLIT)
                pass
            elif token in [MiniGoParser.HEXLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 570
                self.match(MiniGoParser.HEXLIT)
                pass
            elif token in [MiniGoParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 571
                self.match(MiniGoParser.FLOATLIT)
                pass
            elif token in [MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 572
                self.match(MiniGoParser.STRINGLIT)
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 573
                self.boollit()
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 574
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 9)
                self.state = 575
                self.structlit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_array_index(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_indexContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def list_array_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = MiniGoParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_arraylit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
            self.list_array_index()
            self.state = 579
            self.all_type()
            self.state = 580
            self.match(MiniGoParser.LCB)
            self.state = 582
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB_OP) | (1 << MiniGoParser.NOT_OP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.LRB) | (1 << MiniGoParser.LCB) | (1 << MiniGoParser.BINLIT) | (1 << MiniGoParser.OCTLIT) | (1 << MiniGoParser.HEXLIT) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT) | (1 << MiniGoParser.ID))) != 0):
                self.state = 581
                self.list_array_element()


            self.state = 584
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def list_array_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_element" ):
                return visitor.visitList_array_element(self)
            else:
                return visitor.visitChildren(self)




    def list_array_element(self):

        localctx = MiniGoParser.List_array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_list_array_element)
        try:
            self.state = 591
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 586
                self.array_element()
                self.state = 587
                self.match(MiniGoParser.CM)
                self.state = 588
                self.list_array_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 590
                self.array_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def itemlist(self):
            return self.getTypedRuleContext(MiniGoParser.ItemlistContext,0)


        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = MiniGoParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_array_element)
        try:
            self.state = 598
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 593
                self.itemlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 594
                self.match(MiniGoParser.LCB)
                self.state = 595
                self.array_element()
                self.state = 596
                self.match(MiniGoParser.RCB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item(self):
            return self.getTypedRuleContext(MiniGoParser.ItemContext,0)


        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def itemlist(self):
            return self.getTypedRuleContext(MiniGoParser.ItemlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_itemlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItemlist" ):
                return visitor.visitItemlist(self)
            else:
                return visitor.visitChildren(self)




    def itemlist(self):

        localctx = MiniGoParser.ItemlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_itemlist)
        try:
            self.state = 605
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 600
                self.item()
                self.state = 601
                self.match(MiniGoParser.CM)
                self.state = 602
                self.itemlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 604
                self.item()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_item(self):
            return self.getTypedRuleContext(MiniGoParser.Array_itemContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = MiniGoParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_item)
        try:
            self.state = 613
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 607
                self.array_item()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 608
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 609
                self.match(MiniGoParser.LCB)
                self.state = 610
                self.array_element()
                self.state = 611
                self.match(MiniGoParser.RCB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def list_struct_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructlit" ):
                return visitor.visitStructlit(self)
            else:
                return visitor.visitChildren(self)




    def structlit(self):

        localctx = MiniGoParser.StructlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_structlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.match(MiniGoParser.ID)
            self.state = 616
            self.match(MiniGoParser.LCB)
            self.state = 618
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 617
                self.list_struct_element()


            self.state = 620
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_struct_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structlit_element(self):
            return self.getTypedRuleContext(MiniGoParser.Structlit_elementContext,0)


        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def list_struct_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_struct_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_struct_element" ):
                return visitor.visitList_struct_element(self)
            else:
                return visitor.visitChildren(self)




    def list_struct_element(self):

        localctx = MiniGoParser.List_struct_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_list_struct_element)
        try:
            self.state = 627
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 622
                self.structlit_element()
                self.state = 623
                self.match(MiniGoParser.CM)
                self.state = 624
                self.list_struct_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 626
                self.structlit_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structlit_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COL(self):
            return self.getToken(MiniGoParser.COL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structlit_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructlit_element" ):
                return visitor.visitStructlit_element(self)
            else:
                return visitor.visitChildren(self)




    def structlit_element(self):

        localctx = MiniGoParser.Structlit_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_structlit_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.match(MiniGoParser.ID)
            self.state = 630
            self.match(MiniGoParser.COL)
            self.state = 631
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_newlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_newline" ):
                return visitor.visitList_newline(self)
            else:
                return visitor.visitChildren(self)




    def list_newline(self):

        localctx = MiniGoParser.List_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_list_newline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 633
                self.match(MiniGoParser.NL)
                self.state = 636 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.NL):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expr_sempred
        self._predicates[13] = self.expr1_sempred
        self._predicates[14] = self.expr2_sempred
        self._predicates[15] = self.expr3_sempred
        self._predicates[16] = self.expr4_sempred
        self._predicates[18] = self.expr6_sempred
        self._predicates[24] = self.assignment_lhs_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def assignment_lhs_sempred(self, localctx:Assignment_lhsContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




