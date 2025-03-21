# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u01ef\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\7\66\u0155\n\66\f\66\16\66\u0158\13\66\3\66\3\66\5\66")
        buf.write("\u015c\n\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\7\67\u0165")
        buf.write("\n\67\f\67\16\67\u0168\13\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\38\38\39\39\59\u0173\n9\39\69\u0176\n9\r9\169\u0177\3")
        buf.write(":\3:\3:\3:\3:\5:\u017f\n:\3;\3;\3;\6;\u0184\n;\r;\16;")
        buf.write("\u0185\3<\3<\3<\6<\u018b\n<\r<\16<\u018c\3=\3=\3=\6=\u0192")
        buf.write("\n=\r=\16=\u0193\3>\3>\3>\7>\u0199\n>\f>\16>\u019c\13")
        buf.write(">\5>\u019e\n>\3?\6?\u01a1\n?\r?\16?\u01a2\3?\3?\7?\u01a7")
        buf.write("\n?\f?\16?\u01aa\13?\3?\5?\u01ad\n?\3?\6?\u01b0\n?\r?")
        buf.write("\16?\u01b1\3?\3?\5?\u01b6\n?\3@\3@\7@\u01ba\n@\f@\16@")
        buf.write("\u01bd\13@\3@\3@\3@\3A\3A\3B\3B\7B\u01c6\nB\fB\16B\u01c9")
        buf.write("\13B\3C\3C\3C\3D\6D\u01cf\nD\rD\16D\u01d0\3D\3D\3E\3E")
        buf.write("\7E\u01d7\nE\fE\16E\u01da\13E\3E\5E\u01dd\nE\3E\3E\3F")
        buf.write("\3F\7F\u01e3\nF\fF\16F\u01e6\13F\3F\3F\3F\3F\3F\3G\3G")
        buf.write("\3G\4\u0156\u0166\2H\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m8o\2q\2s\2u9w:y;{<}=\177>\u0081?\u0083@\u0085")
        buf.write("A\u0087B\u0089C\u008bD\u008dE\3\2\22\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\7\2$$^^ppttvv\5\2\f\f$$^^\4\2DDdd\3\2\62\63\4\2")
        buf.write("QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\3\2\63;\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\5\2\13\13\17\17\"\"\3\3\f\f\2\u0202\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2u\3\2\2\2\2w")
        buf.write("\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\3\u008f\3\2\2\2\5\u0092\3\2\2\2\7\u0097\3\2\2\2\t\u009b")
        buf.write("\3\2\2\2\13\u00a2\3\2\2\2\r\u00a7\3\2\2\2\17\u00ac\3\2")
        buf.write("\2\2\21\u00b3\3\2\2\2\23\u00bd\3\2\2\2\25\u00c4\3\2\2")
        buf.write("\2\27\u00c8\3\2\2\2\31\u00ce\3\2\2\2\33\u00d6\3\2\2\2")
        buf.write("\35\u00dc\3\2\2\2\37\u00e0\3\2\2\2!\u00e9\3\2\2\2#\u00ef")
        buf.write("\3\2\2\2%\u00f5\3\2\2\2\'\u00f9\3\2\2\2)\u00fe\3\2\2\2")
        buf.write("+\u0104\3\2\2\2-\u0106\3\2\2\2/\u0108\3\2\2\2\61\u010a")
        buf.write("\3\2\2\2\63\u010c\3\2\2\2\65\u010e\3\2\2\2\67\u0111\3")
        buf.write("\2\2\29\u0114\3\2\2\2;\u0116\3\2\2\2=\u0119\3\2\2\2?\u011b")
        buf.write("\3\2\2\2A\u011e\3\2\2\2C\u0121\3\2\2\2E\u0124\3\2\2\2")
        buf.write("G\u0126\3\2\2\2I\u0129\3\2\2\2K\u012c\3\2\2\2M\u012f\3")
        buf.write("\2\2\2O\u0132\3\2\2\2Q\u0135\3\2\2\2S\u0138\3\2\2\2U\u013a")
        buf.write("\3\2\2\2W\u013c\3\2\2\2Y\u013e\3\2\2\2[\u0140\3\2\2\2")
        buf.write("]\u0142\3\2\2\2_\u0144\3\2\2\2a\u0146\3\2\2\2c\u0148\3")
        buf.write("\2\2\2e\u014a\3\2\2\2g\u014c\3\2\2\2i\u014e\3\2\2\2k\u0150")
        buf.write("\3\2\2\2m\u015f\3\2\2\2o\u016e\3\2\2\2q\u0170\3\2\2\2")
        buf.write("s\u017e\3\2\2\2u\u0180\3\2\2\2w\u0187\3\2\2\2y\u018e\3")
        buf.write("\2\2\2{\u019d\3\2\2\2}\u01b5\3\2\2\2\177\u01b7\3\2\2\2")
        buf.write("\u0081\u01c1\3\2\2\2\u0083\u01c3\3\2\2\2\u0085\u01ca\3")
        buf.write("\2\2\2\u0087\u01ce\3\2\2\2\u0089\u01d4\3\2\2\2\u008b\u01e0")
        buf.write("\3\2\2\2\u008d\u01ec\3\2\2\2\u008f\u0090\7k\2\2\u0090")
        buf.write("\u0091\7h\2\2\u0091\4\3\2\2\2\u0092\u0093\7g\2\2\u0093")
        buf.write("\u0094\7n\2\2\u0094\u0095\7u\2\2\u0095\u0096\7g\2\2\u0096")
        buf.write("\6\3\2\2\2\u0097\u0098\7h\2\2\u0098\u0099\7q\2\2\u0099")
        buf.write("\u009a\7t\2\2\u009a\b\3\2\2\2\u009b\u009c\7t\2\2\u009c")
        buf.write("\u009d\7g\2\2\u009d\u009e\7v\2\2\u009e\u009f\7w\2\2\u009f")
        buf.write("\u00a0\7t\2\2\u00a0\u00a1\7p\2\2\u00a1\n\3\2\2\2\u00a2")
        buf.write("\u00a3\7h\2\2\u00a3\u00a4\7w\2\2\u00a4\u00a5\7p\2\2\u00a5")
        buf.write("\u00a6\7e\2\2\u00a6\f\3\2\2\2\u00a7\u00a8\7v\2\2\u00a8")
        buf.write("\u00a9\7{\2\2\u00a9\u00aa\7r\2\2\u00aa\u00ab\7g\2\2\u00ab")
        buf.write("\16\3\2\2\2\u00ac\u00ad\7u\2\2\u00ad\u00ae\7v\2\2\u00ae")
        buf.write("\u00af\7t\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1\7e\2\2\u00b1")
        buf.write("\u00b2\7v\2\2\u00b2\20\3\2\2\2\u00b3\u00b4\7k\2\2\u00b4")
        buf.write("\u00b5\7p\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7\7g\2\2\u00b7")
        buf.write("\u00b8\7t\2\2\u00b8\u00b9\7h\2\2\u00b9\u00ba\7c\2\2\u00ba")
        buf.write("\u00bb\7e\2\2\u00bb\u00bc\7g\2\2\u00bc\22\3\2\2\2\u00bd")
        buf.write("\u00be\7u\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0\7t\2\2\u00c0")
        buf.write("\u00c1\7k\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3\7i\2\2\u00c3")
        buf.write("\24\3\2\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7p\2\2\u00c6")
        buf.write("\u00c7\7v\2\2\u00c7\26\3\2\2\2\u00c8\u00c9\7h\2\2\u00c9")
        buf.write("\u00ca\7n\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc\7c\2\2\u00cc")
        buf.write("\u00cd\7v\2\2\u00cd\30\3\2\2\2\u00ce\u00cf\7d\2\2\u00cf")
        buf.write("\u00d0\7q\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7n\2\2\u00d2")
        buf.write("\u00d3\7g\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7p\2\2\u00d5")
        buf.write("\32\3\2\2\2\u00d6\u00d7\7e\2\2\u00d7\u00d8\7q\2\2\u00d8")
        buf.write("\u00d9\7p\2\2\u00d9\u00da\7u\2\2\u00da\u00db\7v\2\2\u00db")
        buf.write("\34\3\2\2\2\u00dc\u00dd\7x\2\2\u00dd\u00de\7c\2\2\u00de")
        buf.write("\u00df\7t\2\2\u00df\36\3\2\2\2\u00e0\u00e1\7e\2\2\u00e1")
        buf.write("\u00e2\7q\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7v\2\2\u00e4")
        buf.write("\u00e5\7k\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7w\2\2\u00e7")
        buf.write("\u00e8\7g\2\2\u00e8 \3\2\2\2\u00e9\u00ea\7d\2\2\u00ea")
        buf.write("\u00eb\7t\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed\7c\2\2\u00ed")
        buf.write("\u00ee\7m\2\2\u00ee\"\3\2\2\2\u00ef\u00f0\7t\2\2\u00f0")
        buf.write("\u00f1\7c\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3\7i\2\2\u00f3")
        buf.write("\u00f4\7g\2\2\u00f4$\3\2\2\2\u00f5\u00f6\7p\2\2\u00f6")
        buf.write("\u00f7\7k\2\2\u00f7\u00f8\7n\2\2\u00f8&\3\2\2\2\u00f9")
        buf.write("\u00fa\7v\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc\7w\2\2\u00fc")
        buf.write("\u00fd\7g\2\2\u00fd(\3\2\2\2\u00fe\u00ff\7h\2\2\u00ff")
        buf.write("\u0100\7c\2\2\u0100\u0101\7n\2\2\u0101\u0102\7u\2\2\u0102")
        buf.write("\u0103\7g\2\2\u0103*\3\2\2\2\u0104\u0105\7-\2\2\u0105")
        buf.write(",\3\2\2\2\u0106\u0107\7/\2\2\u0107.\3\2\2\2\u0108\u0109")
        buf.write("\7,\2\2\u0109\60\3\2\2\2\u010a\u010b\7\61\2\2\u010b\62")
        buf.write("\3\2\2\2\u010c\u010d\7\'\2\2\u010d\64\3\2\2\2\u010e\u010f")
        buf.write("\7?\2\2\u010f\u0110\7?\2\2\u0110\66\3\2\2\2\u0111\u0112")
        buf.write("\7#\2\2\u0112\u0113\7?\2\2\u01138\3\2\2\2\u0114\u0115")
        buf.write("\7>\2\2\u0115:\3\2\2\2\u0116\u0117\7>\2\2\u0117\u0118")
        buf.write("\7?\2\2\u0118<\3\2\2\2\u0119\u011a\7@\2\2\u011a>\3\2\2")
        buf.write("\2\u011b\u011c\7@\2\2\u011c\u011d\7?\2\2\u011d@\3\2\2")
        buf.write("\2\u011e\u011f\7(\2\2\u011f\u0120\7(\2\2\u0120B\3\2\2")
        buf.write("\2\u0121\u0122\7~\2\2\u0122\u0123\7~\2\2\u0123D\3\2\2")
        buf.write("\2\u0124\u0125\7#\2\2\u0125F\3\2\2\2\u0126\u0127\7<\2")
        buf.write("\2\u0127\u0128\7?\2\2\u0128H\3\2\2\2\u0129\u012a\7-\2")
        buf.write("\2\u012a\u012b\7?\2\2\u012bJ\3\2\2\2\u012c\u012d\7/\2")
        buf.write("\2\u012d\u012e\7?\2\2\u012eL\3\2\2\2\u012f\u0130\7,\2")
        buf.write("\2\u0130\u0131\7?\2\2\u0131N\3\2\2\2\u0132\u0133\7\61")
        buf.write("\2\2\u0133\u0134\7?\2\2\u0134P\3\2\2\2\u0135\u0136\7\'")
        buf.write("\2\2\u0136\u0137\7?\2\2\u0137R\3\2\2\2\u0138\u0139\7?")
        buf.write("\2\2\u0139T\3\2\2\2\u013a\u013b\7\60\2\2\u013bV\3\2\2")
        buf.write("\2\u013c\u013d\7]\2\2\u013dX\3\2\2\2\u013e\u013f\7_\2")
        buf.write("\2\u013fZ\3\2\2\2\u0140\u0141\7*\2\2\u0141\\\3\2\2\2\u0142")
        buf.write("\u0143\7+\2\2\u0143^\3\2\2\2\u0144\u0145\7}\2\2\u0145")
        buf.write("`\3\2\2\2\u0146\u0147\7\177\2\2\u0147b\3\2\2\2\u0148\u0149")
        buf.write("\7.\2\2\u0149d\3\2\2\2\u014a\u014b\7<\2\2\u014bf\3\2\2")
        buf.write("\2\u014c\u014d\7$\2\2\u014dh\3\2\2\2\u014e\u014f\7=\2")
        buf.write("\2\u014fj\3\2\2\2\u0150\u0151\7\61\2\2\u0151\u0152\7\61")
        buf.write("\2\2\u0152\u0156\3\2\2\2\u0153\u0155\13\2\2\2\u0154\u0153")
        buf.write("\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0157\3\2\2\2\u0156")
        buf.write("\u0154\3\2\2\2\u0157\u015b\3\2\2\2\u0158\u0156\3\2\2\2")
        buf.write("\u0159\u015c\5\u0085C\2\u015a\u015c\7\2\2\3\u015b\u0159")
        buf.write("\3\2\2\2\u015b\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d")
        buf.write("\u015e\b\66\2\2\u015el\3\2\2\2\u015f\u0160\7\61\2\2\u0160")
        buf.write("\u0161\7,\2\2\u0161\u0166\3\2\2\2\u0162\u0165\5m\67\2")
        buf.write("\u0163\u0165\13\2\2\2\u0164\u0162\3\2\2\2\u0164\u0163")
        buf.write("\3\2\2\2\u0165\u0168\3\2\2\2\u0166\u0167\3\2\2\2\u0166")
        buf.write("\u0164\3\2\2\2\u0167\u0169\3\2\2\2\u0168\u0166\3\2\2\2")
        buf.write("\u0169\u016a\7,\2\2\u016a\u016b\7\61\2\2\u016b\u016c\3")
        buf.write("\2\2\2\u016c\u016d\b\67\2\2\u016dn\3\2\2\2\u016e\u016f")
        buf.write("\t\2\2\2\u016fp\3\2\2\2\u0170\u0172\t\3\2\2\u0171\u0173")
        buf.write("\t\4\2\2\u0172\u0171\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("\u0175\3\2\2\2\u0174\u0176\5o8\2\u0175\u0174\3\2\2\2\u0176")
        buf.write("\u0177\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178r\3\2\2\2\u0179\u017a\7^\2\2\u017a\u017f\t\5\2\2")
        buf.write("\u017b\u017c\7)\2\2\u017c\u017f\7$\2\2\u017d\u017f\n\6")
        buf.write("\2\2\u017e\u0179\3\2\2\2\u017e\u017b\3\2\2\2\u017e\u017d")
        buf.write("\3\2\2\2\u017ft\3\2\2\2\u0180\u0181\7\62\2\2\u0181\u0183")
        buf.write("\t\7\2\2\u0182\u0184\t\b\2\2\u0183\u0182\3\2\2\2\u0184")
        buf.write("\u0185\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2")
        buf.write("\u0186v\3\2\2\2\u0187\u0188\7\62\2\2\u0188\u018a\t\t\2")
        buf.write("\2\u0189\u018b\t\n\2\2\u018a\u0189\3\2\2\2\u018b\u018c")
        buf.write("\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d")
        buf.write("x\3\2\2\2\u018e\u018f\7\62\2\2\u018f\u0191\t\13\2\2\u0190")
        buf.write("\u0192\t\f\2\2\u0191\u0190\3\2\2\2\u0192\u0193\3\2\2\2")
        buf.write("\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194z\3\2\2")
        buf.write("\2\u0195\u019e\7\62\2\2\u0196\u019a\t\r\2\2\u0197\u0199")
        buf.write("\t\2\2\2\u0198\u0197\3\2\2\2\u0199\u019c\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019e\3\2\2\2")
        buf.write("\u019c\u019a\3\2\2\2\u019d\u0195\3\2\2\2\u019d\u0196\3")
        buf.write("\2\2\2\u019e|\3\2\2\2\u019f\u01a1\5o8\2\u01a0\u019f\3")
        buf.write("\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a8\7\60\2\2\u01a5")
        buf.write("\u01a7\5o8\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8")
        buf.write("\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ac\3\2\2\2")
        buf.write("\u01aa\u01a8\3\2\2\2\u01ab\u01ad\5q9\2\u01ac\u01ab\3\2")
        buf.write("\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01b6\3\2\2\2\u01ae\u01b0")
        buf.write("\5o8\2\u01af\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01af")
        buf.write("\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("\u01b4\5q9\2\u01b4\u01b6\3\2\2\2\u01b5\u01a0\3\2\2\2\u01b5")
        buf.write("\u01af\3\2\2\2\u01b6~\3\2\2\2\u01b7\u01bb\5g\64\2\u01b8")
        buf.write("\u01ba\5s:\2\u01b9\u01b8\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb")
        buf.write("\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2")
        buf.write("\u01bd\u01bb\3\2\2\2\u01be\u01bf\5g\64\2\u01bf\u01c0\b")
        buf.write("@\3\2\u01c0\u0080\3\2\2\2\u01c1\u01c2\5%\23\2\u01c2\u0082")
        buf.write("\3\2\2\2\u01c3\u01c7\t\16\2\2\u01c4\u01c6\t\17\2\2\u01c5")
        buf.write("\u01c4\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2")
        buf.write("\u01c7\u01c8\3\2\2\2\u01c8\u0084\3\2\2\2\u01c9\u01c7\3")
        buf.write("\2\2\2\u01ca\u01cb\7\f\2\2\u01cb\u01cc\bC\4\2\u01cc\u0086")
        buf.write("\3\2\2\2\u01cd\u01cf\t\20\2\2\u01ce\u01cd\3\2\2\2\u01cf")
        buf.write("\u01d0\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2")
        buf.write("\u01d1\u01d2\3\2\2\2\u01d2\u01d3\bD\2\2\u01d3\u0088\3")
        buf.write("\2\2\2\u01d4\u01d8\5g\64\2\u01d5\u01d7\5s:\2\u01d6\u01d5")
        buf.write("\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8")
        buf.write("\u01d9\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2")
        buf.write("\u01db\u01dd\t\21\2\2\u01dc\u01db\3\2\2\2\u01dd\u01de")
        buf.write("\3\2\2\2\u01de\u01df\bE\5\2\u01df\u008a\3\2\2\2\u01e0")
        buf.write("\u01e4\5g\64\2\u01e1\u01e3\5s:\2\u01e2\u01e1\3\2\2\2\u01e3")
        buf.write("\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2")
        buf.write("\u01e5\u01e7\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01e8\7")
        buf.write("^\2\2\u01e8\u01e9\n\5\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb")
        buf.write("\bF\6\2\u01eb\u008c\3\2\2\2\u01ec\u01ed\13\2\2\2\u01ed")
        buf.write("\u01ee\bG\7\2\u01ee\u008e\3\2\2\2\32\2\u0156\u015b\u0164")
        buf.write("\u0166\u0172\u0177\u017e\u0185\u018c\u0193\u019a\u019d")
        buf.write("\u01a2\u01a8\u01ac\u01b1\u01b5\u01bb\u01c7\u01d0\u01d8")
        buf.write("\u01dc\u01e4\b\b\2\2\3@\2\3C\3\3E\4\3F\5\3G\6")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    ADD_OP = 21
    SUB_OP = 22
    MUL_OP = 23
    DIV_OP = 24
    MOD_OP = 25
    EQ_OP = 26
    NEQ_OP = 27
    LT_OP = 28
    LEQ_OP = 29
    GT_OP = 30
    GEQ_OP = 31
    AND_OP = 32
    OR_OP = 33
    NOT_OP = 34
    EQ_ASSIGN_OP = 35
    ADD_ASSIGN_OP = 36
    SUB_ASSIGN_OP = 37
    MUL_ASSIGN_OP = 38
    DIV_ASSIGN_OP = 39
    MOD_ASSIGN_OP = 40
    EQ = 41
    DOT_OP = 42
    LSB = 43
    RSB = 44
    LRB = 45
    RRB = 46
    LCB = 47
    RCB = 48
    CM = 49
    COL = 50
    QUOTES = 51
    SM = 52
    LINE_CMT = 53
    COMMENT = 54
    BINLIT = 55
    OCTLIT = 56
    HEXLIT = 57
    INTLIT = 58
    FLOATLIT = 59
    STRINGLIT = 60
    NILLIT = 61
    ID = 62
    NL = 63
    WS = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66
    ERROR_CHAR = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'='", "'.'", 
            "'['", "']'", "'('", "')'", "'{'", "'}'", "','", "':'", "'\"'", 
            "';'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD_OP", "SUB_OP", 
            "MUL_OP", "DIV_OP", "MOD_OP", "EQ_OP", "NEQ_OP", "LT_OP", "LEQ_OP", 
            "GT_OP", "GEQ_OP", "AND_OP", "OR_OP", "NOT_OP", "EQ_ASSIGN_OP", 
            "ADD_ASSIGN_OP", "SUB_ASSIGN_OP", "MUL_ASSIGN_OP", "DIV_ASSIGN_OP", 
            "MOD_ASSIGN_OP", "EQ", "DOT_OP", "LSB", "RSB", "LRB", "RRB", 
            "LCB", "RCB", "CM", "COL", "QUOTES", "SM", "LINE_CMT", "COMMENT", 
            "BINLIT", "OCTLIT", "HEXLIT", "INTLIT", "FLOATLIT", "STRINGLIT", 
            "NILLIT", "ID", "NL", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "MOD_OP", "EQ_OP", 
                  "NEQ_OP", "LT_OP", "LEQ_OP", "GT_OP", "GEQ_OP", "AND_OP", 
                  "OR_OP", "NOT_OP", "EQ_ASSIGN_OP", "ADD_ASSIGN_OP", "SUB_ASSIGN_OP", 
                  "MUL_ASSIGN_OP", "DIV_ASSIGN_OP", "MOD_ASSIGN_OP", "EQ", 
                  "DOT_OP", "LSB", "RSB", "LRB", "RRB", "LCB", "RCB", "CM", 
                  "COL", "QUOTES", "SM", "LINE_CMT", "COMMENT", "DIGIT", 
                  "EXPONENT", "CHAR", "BINLIT", "OCTLIT", "HEXLIT", "INTLIT", 
                  "FLOATLIT", "STRINGLIT", "NILLIT", "ID", "NL", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    preType = None

    def emit(self):
    	tk = self.type
    	self.preType = tk;
    	if tk == self.UNCLOSE_STRING:       
    		result = super().emit();
    		raise UncloseString(result.text);
    	elif tk == self.ILLEGAL_ESCAPE:
    		result = super().emit();
    		raise IllegalEscape(result.text);
    	elif tk == self.ERROR_CHAR:
    		result = super().emit();
    		raise ErrorToken(result.text); 
    	else:
    		return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[62] = self.STRINGLIT_action 
            actions[65] = self.NL_action 
            actions[67] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[69] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                if self.preType in [self.ID, self.INTLIT, self.BINLIT, self.OCTLIT, self.HEXLIT, self.STRINGLIT, self.FLOATLIT,
                                    self.TRUE, self.FALSE, self.INT, self.FLOAT, self.STRING, self.BOOLEAN, self.NIL,
                                    self.RETURN, self.CONTINUE, self.BREAK,
                                    self.RRB, self.RCB, self.RSB]:
                    self.text = ";"
                    self.type = self.SM
                else:
                    self.skip()

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    if(self.text[-1]=='\n'):
                        raise UncloseString(self.text[:-1])
                    raise UncloseString(self.text)
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text)
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


