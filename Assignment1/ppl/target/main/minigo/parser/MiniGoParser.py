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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u0268\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\5\2~\n\2\3\2\6\2\u0081\n\2\r\2")
        buf.write("\16\2\u0082\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u008d")
        buf.write("\n\3\3\3\6\3\u0090\n\3\r\3\16\3\u0091\3\4\3\4\3\4\3\4")
        buf.write("\5\4\u0098\n\4\3\4\3\4\5\4\u009c\n\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\5\6\u00a7\n\6\3\6\3\6\5\6\u00ab\n\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00b7\n\7")
        buf.write("\3\7\3\7\5\7\u00bb\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\b")
        buf.write("\u00c4\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\5\n\u00cd\n\n\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00d8\n\f\f")
        buf.write("\f\16\f\u00db\13\f\3\f\3\f\3\r\3\r\3\r\5\r\u00e2\n\r\3")
        buf.write("\r\3\r\5\r\u00e6\n\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\7\16\u00f0\n\16\f\16\16\16\u00f3\13\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\7\17\u00fb\n\17\f\17\16\17\u00fe")
        buf.write("\13\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u0106\n\20\f")
        buf.write("\20\16\20\u0109\13\20\3\21\3\21\3\21\3\21\3\21\3\21\7")
        buf.write("\21\u0111\n\21\f\21\16\21\u0114\13\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\7\22\u011c\n\22\f\22\16\22\u011f\13\22\3")
        buf.write("\23\3\23\3\23\5\23\u0124\n\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0131\n\24\5\24\u0133")
        buf.write("\n\24\7\24\u0135\n\24\f\24\16\24\u0138\13\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\5\25\u0141\n\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u014d\n\26")
        buf.write("\3\27\3\27\3\27\3\27\5\27\u0153\n\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0161")
        buf.write("\n\30\3\30\6\30\u0164\n\30\r\30\16\30\u0165\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\5\32\u0176\n\32\7\32\u0178\n\32\f\32\16\32\u017b")
        buf.write("\13\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34\5\34\u0184\n")
        buf.write("\34\3\34\3\34\3\34\3\34\5\34\u018a\n\34\3\34\5\34\u018d")
        buf.write("\n\34\3\35\3\35\3\35\3\35\5\35\u0193\n\35\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\5\36\u019b\n\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\5\37\u01a2\n\37\3\37\5\37\u01a5\n\37\3\37\3\37\3")
        buf.write(" \3 \3 \3!\3!\3!\5!\u01af\n!\3!\3!\3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3%\5%\u01c6")
        buf.write("\n%\3%\3%\3%\3%\5%\u01cc\n%\3%\3%\3&\3&\3&\5&\u01d3\n")
        buf.write("&\3\'\3\'\3\'\3(\3(\3(\3(\3(\7(\u01dd\n(\f(\16(\u01e0")
        buf.write("\13(\3(\3(\3)\3)\3)\3)\5)\u01e8\n)\3*\3*\3*\6*\u01ed\n")
        buf.write("*\r*\16*\u01ee\3+\3+\5+\u01f3\n+\3+\3+\3,\3,\3,\3,\5,")
        buf.write("\u01fb\n,\3,\3,\3-\3-\3-\3-\5-\u0203\n-\3.\3.\3.\3.\3")
        buf.write(".\5.\u020a\n.\3/\3/\3/\3/\3/\3/\5/\u0212\n/\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\5\61\u021a\n\61\3\62\3\62\3\62\5")
        buf.write("\62\u021f\n\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\5\65\u022c\n\65\3\66\3\66\5\66\u0230\n")
        buf.write("\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67")
        buf.write("\u023b\n\67\38\38\38\38\38\38\39\39\39\39\39\59\u0248")
        buf.write("\n9\3:\3:\3:\3:\3:\5:\u024f\n:\3;\3;\3;\5;\u0254\n;\3")
        buf.write(";\3;\3<\3<\3<\3<\3<\5<\u025d\n<\3=\3=\3=\3=\3>\6>\u0264")
        buf.write("\n>\r>\16>\u0265\3>\2\t\32\34\36 \"&\62?\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnprtvxz\2\n\3\2\34!\3\2\27\30\3\2")
        buf.write("\31\33\4\2\30\30$$\3\2%*\3\2\13\16\4\2\66\66AA\3\2\25")
        buf.write("\26\2\u028c\2}\3\2\2\2\4\u008c\3\2\2\2\6\u0093\3\2\2\2")
        buf.write("\b\u009d\3\2\2\2\n\u00a2\3\2\2\2\f\u00ae\3\2\2\2\16\u00c3")
        buf.write("\3\2\2\2\20\u00c5\3\2\2\2\22\u00cc\3\2\2\2\24\u00ce\3")
        buf.write("\2\2\2\26\u00d1\3\2\2\2\30\u00de\3\2\2\2\32\u00e9\3\2")
        buf.write("\2\2\34\u00f4\3\2\2\2\36\u00ff\3\2\2\2 \u010a\3\2\2\2")
        buf.write("\"\u0115\3\2\2\2$\u0123\3\2\2\2&\u0125\3\2\2\2(\u0140")
        buf.write("\3\2\2\2*\u014c\3\2\2\2,\u0152\3\2\2\2.\u0160\3\2\2\2")
        buf.write("\60\u0167\3\2\2\2\62\u016b\3\2\2\2\64\u017c\3\2\2\2\66")
        buf.write("\u017e\3\2\2\28\u0192\3\2\2\2:\u0194\3\2\2\2<\u01a1\3")
        buf.write("\2\2\2>\u01a8\3\2\2\2@\u01ab\3\2\2\2B\u01b5\3\2\2\2D\u01bd")
        buf.write("\3\2\2\2F\u01bf\3\2\2\2H\u01c5\3\2\2\2J\u01cf\3\2\2\2")
        buf.write("L\u01d4\3\2\2\2N\u01d7\3\2\2\2P\u01e7\3\2\2\2R\u01e9\3")
        buf.write("\2\2\2T\u01f0\3\2\2\2V\u01f6\3\2\2\2X\u0202\3\2\2\2Z\u0209")
        buf.write("\3\2\2\2\\\u0211\3\2\2\2^\u0213\3\2\2\2`\u0219\3\2\2\2")
        buf.write("b\u021b\3\2\2\2d\u0222\3\2\2\2f\u0224\3\2\2\2h\u022b\3")
        buf.write("\2\2\2j\u022f\3\2\2\2l\u023a\3\2\2\2n\u023c\3\2\2\2p\u0247")
        buf.write("\3\2\2\2r\u024e\3\2\2\2t\u0250\3\2\2\2v\u025c\3\2\2\2")
        buf.write("x\u025e\3\2\2\2z\u0263\3\2\2\2|~\5z>\2}|\3\2\2\2}~\3\2")
        buf.write("\2\2~\u0080\3\2\2\2\177\u0081\5\4\3\2\u0080\177\3\2\2")
        buf.write("\2\u0081\u0082\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083")
        buf.write("\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085\7\2\2\3\u0085")
        buf.write("\3\3\2\2\2\u0086\u008d\5\6\4\2\u0087\u008d\5\b\5\2\u0088")
        buf.write("\u008d\5\n\6\2\u0089\u008d\5\f\7\2\u008a\u008d\5\24\13")
        buf.write("\2\u008b\u008d\5\26\f\2\u008c\u0086\3\2\2\2\u008c\u0087")
        buf.write("\3\2\2\2\u008c\u0088\3\2\2\2\u008c\u0089\3\2\2\2\u008c")
        buf.write("\u008a\3\2\2\2\u008c\u008b\3\2\2\2\u008d\u008f\3\2\2\2")
        buf.write("\u008e\u0090\5d\63\2\u008f\u008e\3\2\2\2\u0090\u0091\3")
        buf.write("\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\5")
        buf.write("\3\2\2\2\u0093\u0094\7\20\2\2\u0094\u009b\7@\2\2\u0095")
        buf.write("\u009c\5\\/\2\u0096\u0098\5\\/\2\u0097\u0096\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\7+\2\2")
        buf.write("\u009a\u009c\5\32\16\2\u009b\u0095\3\2\2\2\u009b\u0097")
        buf.write("\3\2\2\2\u009c\7\3\2\2\2\u009d\u009e\7\17\2\2\u009e\u009f")
        buf.write("\7@\2\2\u009f\u00a0\7+\2\2\u00a0\u00a1\5\32\16\2\u00a1")
        buf.write("\t\3\2\2\2\u00a2\u00a3\7\7\2\2\u00a3\u00a4\7@\2\2\u00a4")
        buf.write("\u00a6\7/\2\2\u00a5\u00a7\5\16\b\2\u00a6\u00a5\3\2\2\2")
        buf.write("\u00a6\u00a7\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00aa\7")
        buf.write("\60\2\2\u00a9\u00ab\5\\/\2\u00aa\u00a9\3\2\2\2\u00aa\u00ab")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\5T+\2\u00ad\13")
        buf.write("\3\2\2\2\u00ae\u00af\7\7\2\2\u00af\u00b0\7/\2\2\u00b0")
        buf.write("\u00b1\7@\2\2\u00b1\u00b2\7@\2\2\u00b2\u00b3\7\60\2\2")
        buf.write("\u00b3\u00b4\7@\2\2\u00b4\u00b6\7/\2\2\u00b5\u00b7\5\16")
        buf.write("\b\2\u00b6\u00b5\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8")
        buf.write("\3\2\2\2\u00b8\u00ba\7\60\2\2\u00b9\u00bb\5\\/\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\3\2\2\2")
        buf.write("\u00bc\u00bd\5T+\2\u00bd\r\3\2\2\2\u00be\u00bf\5\20\t")
        buf.write("\2\u00bf\u00c0\7\63\2\2\u00c0\u00c1\5\16\b\2\u00c1\u00c4")
        buf.write("\3\2\2\2\u00c2\u00c4\5\20\t\2\u00c3\u00be\3\2\2\2\u00c3")
        buf.write("\u00c2\3\2\2\2\u00c4\17\3\2\2\2\u00c5\u00c6\5\22\n\2\u00c6")
        buf.write("\u00c7\5\\/\2\u00c7\21\3\2\2\2\u00c8\u00c9\7@\2\2\u00c9")
        buf.write("\u00ca\7\63\2\2\u00ca\u00cd\5\22\n\2\u00cb\u00cd\7@\2")
        buf.write("\2\u00cc\u00c8\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd\23\3")
        buf.write("\2\2\2\u00ce\u00cf\7\b\2\2\u00cf\u00d0\5N(\2\u00d0\25")
        buf.write("\3\2\2\2\u00d1\u00d2\7\b\2\2\u00d2\u00d3\7@\2\2\u00d3")
        buf.write("\u00d4\7\n\2\2\u00d4\u00d9\7\61\2\2\u00d5\u00d8\7A\2\2")
        buf.write("\u00d6\u00d8\5\30\r\2\u00d7\u00d5\3\2\2\2\u00d7\u00d6")
        buf.write("\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9")
        buf.write("\u00da\3\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00d9\3\2\2\2")
        buf.write("\u00dc\u00dd\7\62\2\2\u00dd\27\3\2\2\2\u00de\u00df\7@")
        buf.write("\2\2\u00df\u00e1\7/\2\2\u00e0\u00e2\5\16\b\2\u00e1\u00e0")
        buf.write("\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write("\u00e5\7\60\2\2\u00e4\u00e6\5\\/\2\u00e5\u00e4\3\2\2\2")
        buf.write("\u00e5\u00e6\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\5")
        buf.write("d\63\2\u00e8\31\3\2\2\2\u00e9\u00ea\b\16\1\2\u00ea\u00eb")
        buf.write("\5\34\17\2\u00eb\u00f1\3\2\2\2\u00ec\u00ed\f\4\2\2\u00ed")
        buf.write("\u00ee\7#\2\2\u00ee\u00f0\5\34\17\2\u00ef\u00ec\3\2\2")
        buf.write("\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2")
        buf.write("\3\2\2\2\u00f2\33\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f5")
        buf.write("\b\17\1\2\u00f5\u00f6\5\36\20\2\u00f6\u00fc\3\2\2\2\u00f7")
        buf.write("\u00f8\f\4\2\2\u00f8\u00f9\7\"\2\2\u00f9\u00fb\5\36\20")
        buf.write("\2\u00fa\u00f7\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa")
        buf.write("\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\35\3\2\2\2\u00fe\u00fc")
        buf.write("\3\2\2\2\u00ff\u0100\b\20\1\2\u0100\u0101\5 \21\2\u0101")
        buf.write("\u0107\3\2\2\2\u0102\u0103\f\4\2\2\u0103\u0104\t\2\2\2")
        buf.write("\u0104\u0106\5 \21\2\u0105\u0102\3\2\2\2\u0106\u0109\3")
        buf.write("\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\37")
        buf.write("\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u010b\b\21\1\2\u010b")
        buf.write("\u010c\5\"\22\2\u010c\u0112\3\2\2\2\u010d\u010e\f\4\2")
        buf.write("\2\u010e\u010f\t\3\2\2\u010f\u0111\5\"\22\2\u0110\u010d")
        buf.write("\3\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113!\3\2\2\2\u0114\u0112\3\2\2\2\u0115")
        buf.write("\u0116\b\22\1\2\u0116\u0117\5$\23\2\u0117\u011d\3\2\2")
        buf.write("\2\u0118\u0119\f\4\2\2\u0119\u011a\t\4\2\2\u011a\u011c")
        buf.write("\5$\23\2\u011b\u0118\3\2\2\2\u011c\u011f\3\2\2\2\u011d")
        buf.write("\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e#\3\2\2\2\u011f")
        buf.write("\u011d\3\2\2\2\u0120\u0121\t\5\2\2\u0121\u0124\5$\23\2")
        buf.write("\u0122\u0124\5&\24\2\u0123\u0120\3\2\2\2\u0123\u0122\3")
        buf.write("\2\2\2\u0124%\3\2\2\2\u0125\u0126\b\24\1\2\u0126\u0127")
        buf.write("\5(\25\2\u0127\u0136\3\2\2\2\u0128\u0132\f\4\2\2\u0129")
        buf.write("\u012a\7-\2\2\u012a\u012b\5\32\16\2\u012b\u012c\7.\2\2")
        buf.write("\u012c\u0133\3\2\2\2\u012d\u0130\7,\2\2\u012e\u0131\7")
        buf.write("@\2\2\u012f\u0131\5V,\2\u0130\u012e\3\2\2\2\u0130\u012f")
        buf.write("\3\2\2\2\u0131\u0133\3\2\2\2\u0132\u0129\3\2\2\2\u0132")
        buf.write("\u012d\3\2\2\2\u0133\u0135\3\2\2\2\u0134\u0128\3\2\2\2")
        buf.write("\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3")
        buf.write("\2\2\2\u0137\'\3\2\2\2\u0138\u0136\3\2\2\2\u0139\u0141")
        buf.write("\5*\26\2\u013a\u013b\7/\2\2\u013b\u013c\5\32\16\2\u013c")
        buf.write("\u013d\7\60\2\2\u013d\u0141\3\2\2\2\u013e\u0141\7@\2\2")
        buf.write("\u013f\u0141\5V,\2\u0140\u0139\3\2\2\2\u0140\u013a\3\2")
        buf.write("\2\2\u0140\u013e\3\2\2\2\u0140\u013f\3\2\2\2\u0141)\3")
        buf.write("\2\2\2\u0142\u014d\7<\2\2\u0143\u014d\79\2\2\u0144\u014d")
        buf.write("\7:\2\2\u0145\u014d\7;\2\2\u0146\u014d\7=\2\2\u0147\u014d")
        buf.write("\7>\2\2\u0148\u014d\5f\64\2\u0149\u014d\7\24\2\2\u014a")
        buf.write("\u014d\5n8\2\u014b\u014d\5t;\2\u014c\u0142\3\2\2\2\u014c")
        buf.write("\u0143\3\2\2\2\u014c\u0144\3\2\2\2\u014c\u0145\3\2\2\2")
        buf.write("\u014c\u0146\3\2\2\2\u014c\u0147\3\2\2\2\u014c\u0148\3")
        buf.write("\2\2\2\u014c\u0149\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014b")
        buf.write("\3\2\2\2\u014d+\3\2\2\2\u014e\u014f\5.\30\2\u014f\u0150")
        buf.write("\5,\27\2\u0150\u0153\3\2\2\2\u0151\u0153\5.\30\2\u0152")
        buf.write("\u014e\3\2\2\2\u0152\u0151\3\2\2\2\u0153-\3\2\2\2\u0154")
        buf.write("\u0161\5\6\4\2\u0155\u0161\5\b\5\2\u0156\u0161\5\24\13")
        buf.write("\2\u0157\u0161\5\f\7\2\u0158\u0161\5\60\31\2\u0159\u0161")
        buf.write("\5\66\34\2\u015a\u0161\5<\37\2\u015b\u0161\5D#\2\u015c")
        buf.write("\u0161\5F$\2\u015d\u0161\5H%\2\u015e\u0161\5J&\2\u015f")
        buf.write("\u0161\5T+\2\u0160\u0154\3\2\2\2\u0160\u0155\3\2\2\2\u0160")
        buf.write("\u0156\3\2\2\2\u0160\u0157\3\2\2\2\u0160\u0158\3\2\2\2")
        buf.write("\u0160\u0159\3\2\2\2\u0160\u015a\3\2\2\2\u0160\u015b\3")
        buf.write("\2\2\2\u0160\u015c\3\2\2\2\u0160\u015d\3\2\2\2\u0160\u015e")
        buf.write("\3\2\2\2\u0160\u015f\3\2\2\2\u0161\u0163\3\2\2\2\u0162")
        buf.write("\u0164\5d\63\2\u0163\u0162\3\2\2\2\u0164\u0165\3\2\2\2")
        buf.write("\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166/\3\2\2")
        buf.write("\2\u0167\u0168\5\62\32\2\u0168\u0169\5\64\33\2\u0169\u016a")
        buf.write("\5\32\16\2\u016a\61\3\2\2\2\u016b\u016c\b\32\1\2\u016c")
        buf.write("\u016d\7@\2\2\u016d\u0179\3\2\2\2\u016e\u0175\f\4\2\2")
        buf.write("\u016f\u0170\7-\2\2\u0170\u0171\5\32\16\2\u0171\u0172")
        buf.write("\7.\2\2\u0172\u0176\3\2\2\2\u0173\u0174\7,\2\2\u0174\u0176")
        buf.write("\7@\2\2\u0175\u016f\3\2\2\2\u0175\u0173\3\2\2\2\u0176")
        buf.write("\u0178\3\2\2\2\u0177\u016e\3\2\2\2\u0178\u017b\3\2\2\2")
        buf.write("\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\63\3\2")
        buf.write("\2\2\u017b\u0179\3\2\2\2\u017c\u017d\t\6\2\2\u017d\65")
        buf.write("\3\2\2\2\u017e\u017f\7\3\2\2\u017f\u0180\7/\2\2\u0180")
        buf.write("\u0181\5\32\16\2\u0181\u0183\7\60\2\2\u0182\u0184\5z>")
        buf.write("\2\u0183\u0182\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185")
        buf.write("\3\2\2\2\u0185\u0186\5T+\2\u0186\u018c\58\35\2\u0187\u0189")
        buf.write("\7\4\2\2\u0188\u018a\5z>\2\u0189\u0188\3\2\2\2\u0189\u018a")
        buf.write("\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018d\5T+\2\u018c\u0187")
        buf.write("\3\2\2\2\u018c\u018d\3\2\2\2\u018d\67\3\2\2\2\u018e\u018f")
        buf.write("\5:\36\2\u018f\u0190\58\35\2\u0190\u0193\3\2\2\2\u0191")
        buf.write("\u0193\3\2\2\2\u0192\u018e\3\2\2\2\u0192\u0191\3\2\2\2")
        buf.write("\u01939\3\2\2\2\u0194\u0195\7\4\2\2\u0195\u0196\7\3\2")
        buf.write("\2\u0196\u0197\7/\2\2\u0197\u0198\5\32\16\2\u0198\u019a")
        buf.write("\7\60\2\2\u0199\u019b\5z>\2\u019a\u0199\3\2\2\2\u019a")
        buf.write("\u019b\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019d\5T+\2\u019d")
        buf.write(";\3\2\2\2\u019e\u01a2\5> \2\u019f\u01a2\5@!\2\u01a0\u01a2")
        buf.write("\5B\"\2\u01a1\u019e\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3\u01a5\5z>\2\u01a4")
        buf.write("\u01a3\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6\3\2\2\2")
        buf.write("\u01a6\u01a7\5T+\2\u01a7=\3\2\2\2\u01a8\u01a9\7\5\2\2")
        buf.write("\u01a9\u01aa\5\32\16\2\u01aa?\3\2\2\2\u01ab\u01ae\7\5")
        buf.write("\2\2\u01ac\u01af\5\60\31\2\u01ad\u01af\5\6\4\2\u01ae\u01ac")
        buf.write("\3\2\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0")
        buf.write("\u01b1\7\66\2\2\u01b1\u01b2\5\32\16\2\u01b2\u01b3\7\66")
        buf.write("\2\2\u01b3\u01b4\5\60\31\2\u01b4A\3\2\2\2\u01b5\u01b6")
        buf.write("\7\5\2\2\u01b6\u01b7\7@\2\2\u01b7\u01b8\7\63\2\2\u01b8")
        buf.write("\u01b9\7@\2\2\u01b9\u01ba\7%\2\2\u01ba\u01bb\7\23\2\2")
        buf.write("\u01bb\u01bc\5\32\16\2\u01bcC\3\2\2\2\u01bd\u01be\7\22")
        buf.write("\2\2\u01beE\3\2\2\2\u01bf\u01c0\7\21\2\2\u01c0G\3\2\2")
        buf.write("\2\u01c1\u01c2\5\62\32\2\u01c2\u01c3\7,\2\2\u01c3\u01c6")
        buf.write("\3\2\2\2\u01c4\u01c6\3\2\2\2\u01c5\u01c1\3\2\2\2\u01c5")
        buf.write("\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8\7@\2\2")
        buf.write("\u01c8\u01cb\7/\2\2\u01c9\u01cc\5X-\2\u01ca\u01cc\3\2")
        buf.write("\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01ca\3\2\2\2\u01cc\u01cd")
        buf.write("\3\2\2\2\u01cd\u01ce\7\60\2\2\u01ceI\3\2\2\2\u01cf\u01d2")
        buf.write("\7\6\2\2\u01d0\u01d3\5\32\16\2\u01d1\u01d3\3\2\2\2\u01d2")
        buf.write("\u01d0\3\2\2\2\u01d2\u01d1\3\2\2\2\u01d3K\3\2\2\2\u01d4")
        buf.write("\u01d5\5`\61\2\u01d5\u01d6\5^\60\2\u01d6M\3\2\2\2\u01d7")
        buf.write("\u01d8\7@\2\2\u01d8\u01d9\7\t\2\2\u01d9\u01de\7\61\2\2")
        buf.write("\u01da\u01dd\7A\2\2\u01db\u01dd\5P)\2\u01dc\u01da\3\2")
        buf.write("\2\2\u01dc\u01db\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc")
        buf.write("\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e1\3\2\2\2\u01e0")
        buf.write("\u01de\3\2\2\2\u01e1\u01e2\7\62\2\2\u01e2O\3\2\2\2\u01e3")
        buf.write("\u01e4\5R*\2\u01e4\u01e5\5P)\2\u01e5\u01e8\3\2\2\2\u01e6")
        buf.write("\u01e8\5R*\2\u01e7\u01e3\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8")
        buf.write("Q\3\2\2\2\u01e9\u01ea\7@\2\2\u01ea\u01ec\5\\/\2\u01eb")
        buf.write("\u01ed\5d\63\2\u01ec\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2")
        buf.write("\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01efS\3\2\2")
        buf.write("\2\u01f0\u01f2\7\61\2\2\u01f1\u01f3\5,\27\2\u01f2\u01f1")
        buf.write("\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4")
        buf.write("\u01f5\7\62\2\2\u01f5U\3\2\2\2\u01f6\u01f7\7@\2\2\u01f7")
        buf.write("\u01fa\7/\2\2\u01f8\u01fb\5X-\2\u01f9\u01fb\3\2\2\2\u01fa")
        buf.write("\u01f8\3\2\2\2\u01fa\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2")
        buf.write("\u01fc\u01fd\7\60\2\2\u01fdW\3\2\2\2\u01fe\u01ff\5\32")
        buf.write("\16\2\u01ff\u0200\5Z.\2\u0200\u0203\3\2\2\2\u0201\u0203")
        buf.write("\5\32\16\2\u0202\u01fe\3\2\2\2\u0202\u0201\3\2\2\2\u0203")
        buf.write("Y\3\2\2\2\u0204\u0205\7\63\2\2\u0205\u0206\5\32\16\2\u0206")
        buf.write("\u0207\5Z.\2\u0207\u020a\3\2\2\2\u0208\u020a\3\2\2\2\u0209")
        buf.write("\u0204\3\2\2\2\u0209\u0208\3\2\2\2\u020a[\3\2\2\2\u020b")
        buf.write("\u0212\7\f\2\2\u020c\u0212\7\r\2\2\u020d\u0212\7\16\2")
        buf.write("\2\u020e\u0212\7\13\2\2\u020f\u0212\5L\'\2\u0210\u0212")
        buf.write("\7@\2\2\u0211\u020b\3\2\2\2\u0211\u020c\3\2\2\2\u0211")
        buf.write("\u020d\3\2\2\2\u0211\u020e\3\2\2\2\u0211\u020f\3\2\2\2")
        buf.write("\u0211\u0210\3\2\2\2\u0212]\3\2\2\2\u0213\u0214\t\7\2")
        buf.write("\2\u0214_\3\2\2\2\u0215\u0216\5b\62\2\u0216\u0217\5`\61")
        buf.write("\2\u0217\u021a\3\2\2\2\u0218\u021a\5b\62\2\u0219\u0215")
        buf.write("\3\2\2\2\u0219\u0218\3\2\2\2\u021aa\3\2\2\2\u021b\u021e")
        buf.write("\7-\2\2\u021c\u021f\5\32\16\2\u021d\u021f\3\2\2\2\u021e")
        buf.write("\u021c\3\2\2\2\u021e\u021d\3\2\2\2\u021f\u0220\3\2\2\2")
        buf.write("\u0220\u0221\7.\2\2\u0221c\3\2\2\2\u0222\u0223\t\b\2\2")
        buf.write("\u0223e\3\2\2\2\u0224\u0225\t\t\2\2\u0225g\3\2\2\2\u0226")
        buf.write("\u0227\5j\66\2\u0227\u0228\7\63\2\2\u0228\u0229\5h\65")
        buf.write("\2\u0229\u022c\3\2\2\2\u022a\u022c\5j\66\2\u022b\u0226")
        buf.write("\3\2\2\2\u022b\u022a\3\2\2\2\u022ci\3\2\2\2\u022d\u0230")
        buf.write("\5l\67\2\u022e\u0230\5\32\16\2\u022f\u022d\3\2\2\2\u022f")
        buf.write("\u022e\3\2\2\2\u0230k\3\2\2\2\u0231\u023b\7<\2\2\u0232")
        buf.write("\u023b\79\2\2\u0233\u023b\7:\2\2\u0234\u023b\7;\2\2\u0235")
        buf.write("\u023b\7=\2\2\u0236\u023b\7>\2\2\u0237\u023b\5f\64\2\u0238")
        buf.write("\u023b\7\24\2\2\u0239\u023b\5t;\2\u023a\u0231\3\2\2\2")
        buf.write("\u023a\u0232\3\2\2\2\u023a\u0233\3\2\2\2\u023a\u0234\3")
        buf.write("\2\2\2\u023a\u0235\3\2\2\2\u023a\u0236\3\2\2\2\u023a\u0237")
        buf.write("\3\2\2\2\u023a\u0238\3\2\2\2\u023a\u0239\3\2\2\2\u023b")
        buf.write("m\3\2\2\2\u023c\u023d\5`\61\2\u023d\u023e\5\\/\2\u023e")
        buf.write("\u023f\7\61\2\2\u023f\u0240\5p9\2\u0240\u0241\7\62\2\2")
        buf.write("\u0241o\3\2\2\2\u0242\u0243\5r:\2\u0243\u0244\7\63\2\2")
        buf.write("\u0244\u0245\5p9\2\u0245\u0248\3\2\2\2\u0246\u0248\5r")
        buf.write(":\2\u0247\u0242\3\2\2\2\u0247\u0246\3\2\2\2\u0248q\3\2")
        buf.write("\2\2\u0249\u024f\5h\65\2\u024a\u024b\7\61\2\2\u024b\u024c")
        buf.write("\5r:\2\u024c\u024d\7\62\2\2\u024d\u024f\3\2\2\2\u024e")
        buf.write("\u0249\3\2\2\2\u024e\u024a\3\2\2\2\u024fs\3\2\2\2\u0250")
        buf.write("\u0251\7@\2\2\u0251\u0253\7\61\2\2\u0252\u0254\5v<\2\u0253")
        buf.write("\u0252\3\2\2\2\u0253\u0254\3\2\2\2\u0254\u0255\3\2\2\2")
        buf.write("\u0255\u0256\7\61\2\2\u0256u\3\2\2\2\u0257\u0258\5x=\2")
        buf.write("\u0258\u0259\7\63\2\2\u0259\u025a\5v<\2\u025a\u025d\3")
        buf.write("\2\2\2\u025b\u025d\5x=\2\u025c\u0257\3\2\2\2\u025c\u025b")
        buf.write("\3\2\2\2\u025dw\3\2\2\2\u025e\u025f\7@\2\2\u025f\u0260")
        buf.write("\7\64\2\2\u0260\u0261\5\32\16\2\u0261y\3\2\2\2\u0262\u0264")
        buf.write("\7A\2\2\u0263\u0262\3\2\2\2\u0264\u0265\3\2\2\2\u0265")
        buf.write("\u0263\3\2\2\2\u0265\u0266\3\2\2\2\u0266{\3\2\2\2@}\u0082")
        buf.write("\u008c\u0091\u0097\u009b\u00a6\u00aa\u00b6\u00ba\u00c3")
        buf.write("\u00cc\u00d7\u00d9\u00e1\u00e5\u00f1\u00fc\u0107\u0112")
        buf.write("\u011d\u0123\u0130\u0132\u0136\u0140\u014c\u0152\u0160")
        buf.write("\u0165\u0175\u0179\u0183\u0189\u018c\u0192\u019a\u01a1")
        buf.write("\u01a4\u01ae\u01c5\u01cb\u01d2\u01dc\u01de\u01e7\u01ee")
        buf.write("\u01f2\u01fa\u0202\u0209\u0211\u0219\u021e\u022b\u022f")
        buf.write("\u023a\u0247\u024e\u0253\u025c\u0265")
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
                     "','", "':'", "'\"'", "';'", "<INVALID>", "<INVALID>", 
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
                      "QUOTES", "SM", "LINE_CMT", "COMMENT", "BINLIT", "OCTLIT", 
                      "HEXLIT", "INTLIT", "FLOATLIT", "STRINGLIT", "NILLIT", 
                      "ID", "NL", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

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
    RULE_break_stmt = 33
    RULE_continue_stmt = 34
    RULE_call_stmt = 35
    RULE_return_stmt = 36
    RULE_array_type = 37
    RULE_struct_type = 38
    RULE_struct_field_list = 39
    RULE_struct_field = 40
    RULE_body = 41
    RULE_func_call = 42
    RULE_expr_list = 43
    RULE_expr_tail = 44
    RULE_all_type = 45
    RULE_prim_types = 46
    RULE_list_array_index = 47
    RULE_array_index = 48
    RULE_sm_nl = 49
    RULE_boollit = 50
    RULE_itemlist = 51
    RULE_item = 52
    RULE_array_item = 53
    RULE_arraylit = 54
    RULE_list_array_element = 55
    RULE_array_element = 56
    RULE_structlit = 57
    RULE_list_struct_element = 58
    RULE_list_element = 59
    RULE_list_newline = 60

    ruleNames =  [ "program", "decl", "var_decl", "const_decl", "func_decl", 
                   "method_decl", "parameter_list", "parameter", "list_ID", 
                   "struct_decl", "interface_decl", "interface_method", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "factor", "literal", "stmt_list", "statement", 
                   "assign_stmt", "assignment_lhs", "assign_op", "if_stmt", 
                   "list_elif", "elif_one", "for_stmt", "basic_for", "init_for", 
                   "range_for", "break_stmt", "continue_stmt", "call_stmt", 
                   "return_stmt", "array_type", "struct_type", "struct_field_list", 
                   "struct_field", "body", "func_call", "expr_list", "expr_tail", 
                   "all_type", "prim_types", "list_array_index", "array_index", 
                   "sm_nl", "boollit", "itemlist", "item", "array_item", 
                   "arraylit", "list_array_element", "array_element", "structlit", 
                   "list_struct_element", "list_element", "list_newline" ]

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
    LINE_CMT=53
    COMMENT=54
    BINLIT=55
    OCTLIT=56
    HEXLIT=57
    INTLIT=58
    FLOATLIT=59
    STRINGLIT=60
    NILLIT=61
    ID=62
    NL=63
    WS=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66
    ERROR_CHAR=67

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
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NL:
                self.state = 122
                self.list_newline()


            self.state = 126 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 125
                self.decl()
                self.state = 128 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 130
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


        def sm_nl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Sm_nlContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 132
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 133
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 134
                self.func_decl()
                pass

            elif la_ == 4:
                self.state = 135
                self.method_decl()
                pass

            elif la_ == 5:
                self.state = 136
                self.struct_decl()
                pass

            elif la_ == 6:
                self.state = 137
                self.interface_decl()
                pass


            self.state = 141 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 140
                self.sm_nl()
                self.state = 143 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.SM or _la==MiniGoParser.NL):
                    break

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
            self.state = 145
            self.match(MiniGoParser.VAR)
            self.state = 146
            self.match(MiniGoParser.ID)
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 147
                self.all_type()
                pass

            elif la_ == 2:
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 148
                    self.all_type()


                self.state = 151
                self.match(MiniGoParser.EQ)
                self.state = 152
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(MiniGoParser.CONST)
            self.state = 156
            self.match(MiniGoParser.ID)
            self.state = 157
            self.match(MiniGoParser.EQ)
            self.state = 158
            self.expr(0)
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
            self.state = 160
            self.match(MiniGoParser.FUNC)
            self.state = 161
            self.match(MiniGoParser.ID)
            self.state = 162
            self.match(MiniGoParser.LRB)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 163
                self.parameter_list()


            self.state = 166
            self.match(MiniGoParser.RRB)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 167
                self.all_type()


            self.state = 170
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
            self.state = 172
            self.match(MiniGoParser.FUNC)
            self.state = 173
            self.match(MiniGoParser.LRB)
            self.state = 174
            self.match(MiniGoParser.ID)
            self.state = 175
            self.match(MiniGoParser.ID)
            self.state = 176
            self.match(MiniGoParser.RRB)
            self.state = 177
            self.match(MiniGoParser.ID)
            self.state = 178
            self.match(MiniGoParser.LRB)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 179
                self.parameter_list()


            self.state = 182
            self.match(MiniGoParser.RRB)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 183
                self.all_type()


            self.state = 186
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
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.parameter()
                self.state = 189
                self.match(MiniGoParser.CM)
                self.state = 190
                self.parameter_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
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
            self.state = 195
            self.list_ID()
            self.state = 196
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
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(MiniGoParser.ID)
                self.state = 199
                self.match(MiniGoParser.CM)
                self.state = 200
                self.list_ID()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
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
            self.state = 204
            self.match(MiniGoParser.TYPE)
            self.state = 205
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
            self.state = 207
            self.match(MiniGoParser.TYPE)
            self.state = 208
            self.match(MiniGoParser.ID)
            self.state = 209
            self.match(MiniGoParser.INTERFACE)
            self.state = 210
            self.match(MiniGoParser.LCB)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID or _la==MiniGoParser.NL:
                self.state = 213
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NL]:
                    self.state = 211
                    self.match(MiniGoParser.NL)
                    pass
                elif token in [MiniGoParser.ID]:
                    self.state = 212
                    self.interface_method()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 218
            self.match(MiniGoParser.RCB)
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
            self.state = 220
            self.match(MiniGoParser.ID)
            self.state = 221
            self.match(MiniGoParser.LRB)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 222
                self.parameter_list()


            self.state = 225
            self.match(MiniGoParser.RRB)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 226
                self.all_type()


            self.state = 229
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
            self.state = 232
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 234
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 235
                    self.match(MiniGoParser.OR_OP)
                    self.state = 236
                    self.expr1(0) 
                self.state = 241
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
            self.state = 243
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 245
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 246
                    self.match(MiniGoParser.AND_OP)
                    self.state = 247
                    self.expr2(0) 
                self.state = 252
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
            self.state = 254
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 261
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 256
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 257
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ_OP) | (1 << MiniGoParser.NEQ_OP) | (1 << MiniGoParser.LT_OP) | (1 << MiniGoParser.LEQ_OP) | (1 << MiniGoParser.GT_OP) | (1 << MiniGoParser.GEQ_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 258
                    self.expr3(0) 
                self.state = 263
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
            self.state = 265
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 267
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 268
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD_OP or _la==MiniGoParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 269
                    self.expr4(0) 
                self.state = 274
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
            self.state = 276
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 278
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 279
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL_OP) | (1 << MiniGoParser.DIV_OP) | (1 << MiniGoParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 280
                    self.expr5() 
                self.state = 285
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
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB_OP, MiniGoParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB_OP or _la==MiniGoParser.NOT_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 287
                self.expr5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LSB, MiniGoParser.LRB, MiniGoParser.BINLIT, MiniGoParser.OCTLIT, MiniGoParser.HEXLIT, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
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


        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

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
            self.state = 292
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 294
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 304
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LSB]:
                        self.state = 295
                        self.match(MiniGoParser.LSB)
                        self.state = 296
                        self.expr(0)
                        self.state = 297
                        self.match(MiniGoParser.RSB)
                        pass
                    elif token in [MiniGoParser.DOT_OP]:
                        self.state = 299
                        self.match(MiniGoParser.DOT_OP)
                        self.state = 302
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                        if la_ == 1:
                            self.state = 300
                            self.match(MiniGoParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 301
                            self.func_call()
                            pass


                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 310
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
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.match(MiniGoParser.LRB)
                self.state = 313
                self.expr(0)
                self.state = 314
                self.match(MiniGoParser.RRB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 316
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 317
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
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.match(MiniGoParser.INTLIT)
                pass
            elif token in [MiniGoParser.BINLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.match(MiniGoParser.BINLIT)
                pass
            elif token in [MiniGoParser.OCTLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.match(MiniGoParser.OCTLIT)
                pass
            elif token in [MiniGoParser.HEXLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 323
                self.match(MiniGoParser.HEXLIT)
                pass
            elif token in [MiniGoParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 324
                self.match(MiniGoParser.FLOATLIT)
                pass
            elif token in [MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 325
                self.match(MiniGoParser.STRINGLIT)
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 326
                self.boollit()
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 327
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 9)
                self.state = 328
                self.arraylit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 10)
                self.state = 329
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
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.statement()
                self.state = 333
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
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


        def sm_nl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Sm_nlContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 338
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 339
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 340
                self.struct_decl()
                pass

            elif la_ == 4:
                self.state = 341
                self.method_decl()
                pass

            elif la_ == 5:
                self.state = 342
                self.assign_stmt()
                pass

            elif la_ == 6:
                self.state = 343
                self.if_stmt()
                pass

            elif la_ == 7:
                self.state = 344
                self.for_stmt()
                pass

            elif la_ == 8:
                self.state = 345
                self.break_stmt()
                pass

            elif la_ == 9:
                self.state = 346
                self.continue_stmt()
                pass

            elif la_ == 10:
                self.state = 347
                self.call_stmt()
                pass

            elif la_ == 11:
                self.state = 348
                self.return_stmt()
                pass

            elif la_ == 12:
                self.state = 349
                self.body()
                pass


            self.state = 353 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 352
                self.sm_nl()
                self.state = 355 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.SM or _la==MiniGoParser.NL):
                    break

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
            self.state = 357
            self.assignment_lhs(0)
            self.state = 358
            self.assign_op()
            self.state = 359
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


        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

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
            self.state = 362
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 375
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Assignment_lhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignment_lhs)
                    self.state = 364
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 371
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LSB]:
                        self.state = 365
                        self.match(MiniGoParser.LSB)
                        self.state = 366
                        self.expr(0)
                        self.state = 367
                        self.match(MiniGoParser.RSB)
                        pass
                    elif token in [MiniGoParser.DOT_OP]:
                        self.state = 369
                        self.match(MiniGoParser.DOT_OP)
                        self.state = 370
                        self.match(MiniGoParser.ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 377
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
            self.state = 378
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


        def list_elif(self):
            return self.getTypedRuleContext(MiniGoParser.List_elifContext,0)


        def list_newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.List_newlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.List_newlineContext,i)


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
            self.state = 380
            self.match(MiniGoParser.IF)
            self.state = 381
            self.match(MiniGoParser.LRB)
            self.state = 382
            self.expr(0)
            self.state = 383
            self.match(MiniGoParser.RRB)
            self.state = 385
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NL:
                self.state = 384
                self.list_newline()


            self.state = 387
            self.body()
            self.state = 388
            self.list_elif()
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 389
                self.match(MiniGoParser.ELSE)
                self.state = 391
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.NL:
                    self.state = 390
                    self.list_newline()


                self.state = 393
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
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.elif_one()
                self.state = 397
                self.list_elif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

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
            self.state = 402
            self.match(MiniGoParser.ELSE)
            self.state = 403
            self.match(MiniGoParser.IF)
            self.state = 404
            self.match(MiniGoParser.LRB)
            self.state = 405
            self.expr(0)
            self.state = 406
            self.match(MiniGoParser.RRB)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NL:
                self.state = 407
                self.list_newline()


            self.state = 410
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
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 412
                self.basic_for()
                pass

            elif la_ == 2:
                self.state = 413
                self.init_for()
                pass

            elif la_ == 3:
                self.state = 414
                self.range_for()
                pass


            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NL:
                self.state = 417
                self.list_newline()


            self.state = 420
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
            self.state = 422
            self.match(MiniGoParser.FOR)
            self.state = 423
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
            self.state = 425
            self.match(MiniGoParser.FOR)
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 426
                self.assign_stmt()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 427
                self.var_decl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 430
            self.match(MiniGoParser.SM)
            self.state = 431
            self.expr(0)
            self.state = 432
            self.match(MiniGoParser.SM)
            self.state = 433
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

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
            self.state = 435
            self.match(MiniGoParser.FOR)
            self.state = 436
            self.match(MiniGoParser.ID)
            self.state = 437
            self.match(MiniGoParser.CM)
            self.state = 438
            self.match(MiniGoParser.ID)
            self.state = 439
            self.match(MiniGoParser.EQ_ASSIGN_OP)
            self.state = 440
            self.match(MiniGoParser.RANGE)
            self.state = 441
            self.expr(0)
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(MiniGoParser.BREAK)
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(MiniGoParser.CONTINUE)
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
        self.enterRule(localctx, 70, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 447
                self.assignment_lhs(0)
                self.state = 448
                self.match(MiniGoParser.DOT_OP)
                pass

            elif la_ == 2:
                pass


            self.state = 453
            self.match(MiniGoParser.ID)
            self.state = 454
            self.match(MiniGoParser.LRB)
            self.state = 457
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB_OP, MiniGoParser.NOT_OP, MiniGoParser.LSB, MiniGoParser.LRB, MiniGoParser.BINLIT, MiniGoParser.OCTLIT, MiniGoParser.HEXLIT, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT, MiniGoParser.ID]:
                self.state = 455
                self.expr_list()
                pass
            elif token in [MiniGoParser.RRB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 459
            self.match(MiniGoParser.RRB)
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
        self.enterRule(localctx, 72, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(MiniGoParser.RETURN)
            self.state = 464
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB_OP, MiniGoParser.NOT_OP, MiniGoParser.LSB, MiniGoParser.LRB, MiniGoParser.BINLIT, MiniGoParser.OCTLIT, MiniGoParser.HEXLIT, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT, MiniGoParser.ID]:
                self.state = 462
                self.expr(0)
                pass
            elif token in [MiniGoParser.SM, MiniGoParser.NL]:
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


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_array_index(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_indexContext,0)


        def prim_types(self):
            return self.getTypedRuleContext(MiniGoParser.Prim_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.list_array_index()
            self.state = 467
            self.prim_types()
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

        def struct_field_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_field_listContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_field_listContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_struct_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(MiniGoParser.ID)
            self.state = 470
            self.match(MiniGoParser.STRUCT)
            self.state = 471
            self.match(MiniGoParser.LCB)
            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID or _la==MiniGoParser.NL:
                self.state = 474
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NL]:
                    self.state = 472
                    self.match(MiniGoParser.NL)
                    pass
                elif token in [MiniGoParser.ID]:
                    self.state = 473
                    self.struct_field_list()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 478
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 479
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_field_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_field(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,0)


        def struct_field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field_list" ):
                return visitor.visitStruct_field_list(self)
            else:
                return visitor.visitChildren(self)




    def struct_field_list(self):

        localctx = MiniGoParser.Struct_field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_struct_field_list)
        try:
            self.state = 485
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                self.struct_field()
                self.state = 482
                self.struct_field_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 484
                self.struct_field()
                pass


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


        def sm_nl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Sm_nlContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field" ):
                return visitor.visitStruct_field(self)
            else:
                return visitor.visitChildren(self)




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_struct_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(MiniGoParser.ID)
            self.state = 488
            self.all_type()
            self.state = 490 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 489
                    self.sm_nl()

                else:
                    raise NoViableAltException(self)
                self.state = 492 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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


        def getRuleIndex(self):
            return MiniGoParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MiniGoParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(MiniGoParser.LCB)
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.LCB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 495
                self.stmt_list()


            self.state = 498
            self.match(MiniGoParser.RCB)
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
        self.enterRule(localctx, 84, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(MiniGoParser.ID)
            self.state = 501
            self.match(MiniGoParser.LRB)
            self.state = 504
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB_OP, MiniGoParser.NOT_OP, MiniGoParser.LSB, MiniGoParser.LRB, MiniGoParser.BINLIT, MiniGoParser.OCTLIT, MiniGoParser.HEXLIT, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT, MiniGoParser.ID]:
                self.state = 502
                self.expr_list()
                pass
            elif token in [MiniGoParser.RRB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 506
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
        self.enterRule(localctx, 86, self.RULE_expr_list)
        try:
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.expr(0)
                self.state = 509
                self.expr_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 511
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
        self.enterRule(localctx, 88, self.RULE_expr_tail)
        try:
            self.state = 519
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.match(MiniGoParser.CM)
                self.state = 515
                self.expr(0)
                self.state = 516
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
        self.enterRule(localctx, 90, self.RULE_all_type)
        try:
            self.state = 527
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 523
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 524
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 525
                self.array_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 526
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
        self.enterRule(localctx, 92, self.RULE_prim_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
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
        self.enterRule(localctx, 94, self.RULE_list_array_index)
        try:
            self.state = 535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.array_index()
                self.state = 532
                self.list_array_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 534
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

        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_index" ):
                return visitor.visitArray_index(self)
            else:
                return visitor.visitChildren(self)




    def array_index(self):

        localctx = MiniGoParser.Array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_array_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(MiniGoParser.LSB)
            self.state = 540
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB_OP, MiniGoParser.NOT_OP, MiniGoParser.LSB, MiniGoParser.LRB, MiniGoParser.BINLIT, MiniGoParser.OCTLIT, MiniGoParser.HEXLIT, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT, MiniGoParser.ID]:
                self.state = 538
                self.expr(0)
                pass
            elif token in [MiniGoParser.RSB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 542
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

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_sm_nl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSm_nl" ):
                return visitor.visitSm_nl(self)
            else:
                return visitor.visitChildren(self)




    def sm_nl(self):

        localctx = MiniGoParser.Sm_nlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_sm_nl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SM or _la==MiniGoParser.NL):
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
        self.enterRule(localctx, 100, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
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
        self.enterRule(localctx, 102, self.RULE_itemlist)
        try:
            self.state = 553
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
                self.item()
                self.state = 549
                self.match(MiniGoParser.CM)
                self.state = 550
                self.itemlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = MiniGoParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_item)
        try:
            self.state = 557
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self.array_item()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 556
                self.expr(0)
                pass


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
            self.state = 568
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 559
                self.match(MiniGoParser.INTLIT)
                pass
            elif token in [MiniGoParser.BINLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 560
                self.match(MiniGoParser.BINLIT)
                pass
            elif token in [MiniGoParser.OCTLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 561
                self.match(MiniGoParser.OCTLIT)
                pass
            elif token in [MiniGoParser.HEXLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 562
                self.match(MiniGoParser.HEXLIT)
                pass
            elif token in [MiniGoParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 563
                self.match(MiniGoParser.FLOATLIT)
                pass
            elif token in [MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 564
                self.match(MiniGoParser.STRINGLIT)
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 565
                self.boollit()
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 566
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 9)
                self.state = 567
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

        def list_array_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.list_array_index()
            self.state = 571
            self.all_type()
            self.state = 572
            self.match(MiniGoParser.LCB)
            self.state = 573
            self.list_array_element()
            self.state = 574
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
            self.state = 581
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.array_element()
                self.state = 577
                self.match(MiniGoParser.CM)
                self.state = 578
                self.list_array_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 580
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
            self.state = 588
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB_OP, MiniGoParser.NOT_OP, MiniGoParser.LSB, MiniGoParser.LRB, MiniGoParser.BINLIT, MiniGoParser.OCTLIT, MiniGoParser.HEXLIT, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 583
                self.itemlist()
                pass
            elif token in [MiniGoParser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 584
                self.match(MiniGoParser.LCB)
                self.state = 585
                self.array_element()
                self.state = 586
                self.match(MiniGoParser.RCB)
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


    class StructlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LCB)
            else:
                return self.getToken(MiniGoParser.LCB, i)

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
        self.enterRule(localctx, 114, self.RULE_structlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            self.match(MiniGoParser.ID)
            self.state = 591
            self.match(MiniGoParser.LCB)
            self.state = 593
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 592
                self.list_struct_element()


            self.state = 595
            self.match(MiniGoParser.LCB)
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

        def list_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_elementContext,0)


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
        self.enterRule(localctx, 116, self.RULE_list_struct_element)
        try:
            self.state = 602
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 597
                self.list_element()
                self.state = 598
                self.match(MiniGoParser.CM)
                self.state = 599
                self.list_struct_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 601
                self.list_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elementContext(ParserRuleContext):
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
            return MiniGoParser.RULE_list_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_element" ):
                return visitor.visitList_element(self)
            else:
                return visitor.visitChildren(self)




    def list_element(self):

        localctx = MiniGoParser.List_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_list_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(MiniGoParser.ID)
            self.state = 605
            self.match(MiniGoParser.COL)
            self.state = 606
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
        self.enterRule(localctx, 120, self.RULE_list_newline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 608
                self.match(MiniGoParser.NL)
                self.state = 611 
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
         




