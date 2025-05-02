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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u01f2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3")
        buf.write("*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\7\67\u0159\n\67\f\67\16\67\u015c\13\67")
        buf.write("\3\67\3\67\5\67\u0160\n\67\3\67\3\67\38\38\38\38\38\7")
        buf.write("8\u0169\n8\f8\168\u016c\138\38\38\38\38\38\39\39\3:\3")
        buf.write(":\5:\u0177\n:\3:\6:\u017a\n:\r:\16:\u017b\3;\3;\3;\3;")
        buf.write("\3;\5;\u0183\n;\3<\3<\3<\6<\u0188\n<\r<\16<\u0189\3=\3")
        buf.write("=\3=\6=\u018f\n=\r=\16=\u0190\3>\3>\3>\6>\u0196\n>\r>")
        buf.write("\16>\u0197\3?\3?\3?\7?\u019d\n?\f?\16?\u01a0\13?\5?\u01a2")
        buf.write("\n?\3@\6@\u01a5\n@\r@\16@\u01a6\3@\3@\7@\u01ab\n@\f@\16")
        buf.write("@\u01ae\13@\3@\5@\u01b1\n@\3@\6@\u01b4\n@\r@\16@\u01b5")
        buf.write("\3@\3@\5@\u01ba\n@\3A\3A\7A\u01be\nA\fA\16A\u01c1\13A")
        buf.write("\3A\3A\3B\3B\3C\3C\7C\u01c9\nC\fC\16C\u01cc\13C\3D\3D")
        buf.write("\3D\3E\6E\u01d2\nE\rE\16E\u01d3\3E\3E\3F\3F\7F\u01da\n")
        buf.write("F\fF\16F\u01dd\13F\3F\5F\u01e0\nF\3F\3F\3G\3G\7G\u01e6")
        buf.write("\nG\fG\16G\u01e9\13G\3G\3G\3G\3G\3G\3H\3H\3H\4\u015a\u016a")
        buf.write("\2I\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write("\2s\2u\2w:y;{<}=\177>\u0081?\u0083@\u0085A\u0087B\u0089")
        buf.write("C\u008bD\u008dE\u008fF\3\2\22\3\2\62;\4\2GGgg\4\2--//")
        buf.write("\7\2$$^^ppttvv\5\2\f\f$$^^\4\2DDdd\3\2\62\63\4\2QQqq\3")
        buf.write("\2\629\4\2ZZzz\5\2\62;CHch\3\2\63;\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\5\2\13\13\17\17\"\"\3\3\f\f\2\u0205\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\3\u0091\3\2\2\2\5\u0094\3\2\2\2\7\u0099\3\2\2")
        buf.write("\2\t\u009d\3\2\2\2\13\u00a4\3\2\2\2\r\u00a9\3\2\2\2\17")
        buf.write("\u00ae\3\2\2\2\21\u00b5\3\2\2\2\23\u00bf\3\2\2\2\25\u00c6")
        buf.write("\3\2\2\2\27\u00ca\3\2\2\2\31\u00d0\3\2\2\2\33\u00d8\3")
        buf.write("\2\2\2\35\u00de\3\2\2\2\37\u00e2\3\2\2\2!\u00eb\3\2\2")
        buf.write("\2#\u00f1\3\2\2\2%\u00f7\3\2\2\2\'\u00fb\3\2\2\2)\u0100")
        buf.write("\3\2\2\2+\u0106\3\2\2\2-\u0108\3\2\2\2/\u010a\3\2\2\2")
        buf.write("\61\u010c\3\2\2\2\63\u010e\3\2\2\2\65\u0110\3\2\2\2\67")
        buf.write("\u0113\3\2\2\29\u0116\3\2\2\2;\u0118\3\2\2\2=\u011b\3")
        buf.write("\2\2\2?\u011d\3\2\2\2A\u0120\3\2\2\2C\u0123\3\2\2\2E\u0126")
        buf.write("\3\2\2\2G\u0128\3\2\2\2I\u012b\3\2\2\2K\u012e\3\2\2\2")
        buf.write("M\u0131\3\2\2\2O\u0134\3\2\2\2Q\u0137\3\2\2\2S\u013a\3")
        buf.write("\2\2\2U\u013c\3\2\2\2W\u013e\3\2\2\2Y\u0140\3\2\2\2[\u0142")
        buf.write("\3\2\2\2]\u0144\3\2\2\2_\u0146\3\2\2\2a\u0148\3\2\2\2")
        buf.write("c\u014a\3\2\2\2e\u014c\3\2\2\2g\u014e\3\2\2\2i\u0150\3")
        buf.write("\2\2\2k\u0152\3\2\2\2m\u0154\3\2\2\2o\u0163\3\2\2\2q\u0172")
        buf.write("\3\2\2\2s\u0174\3\2\2\2u\u0182\3\2\2\2w\u0184\3\2\2\2")
        buf.write("y\u018b\3\2\2\2{\u0192\3\2\2\2}\u01a1\3\2\2\2\177\u01b9")
        buf.write("\3\2\2\2\u0081\u01bb\3\2\2\2\u0083\u01c4\3\2\2\2\u0085")
        buf.write("\u01c6\3\2\2\2\u0087\u01cd\3\2\2\2\u0089\u01d1\3\2\2\2")
        buf.write("\u008b\u01d7\3\2\2\2\u008d\u01e3\3\2\2\2\u008f\u01ef\3")
        buf.write("\2\2\2\u0091\u0092\7k\2\2\u0092\u0093\7h\2\2\u0093\4\3")
        buf.write("\2\2\2\u0094\u0095\7g\2\2\u0095\u0096\7n\2\2\u0096\u0097")
        buf.write("\7u\2\2\u0097\u0098\7g\2\2\u0098\6\3\2\2\2\u0099\u009a")
        buf.write("\7h\2\2\u009a\u009b\7q\2\2\u009b\u009c\7t\2\2\u009c\b")
        buf.write("\3\2\2\2\u009d\u009e\7t\2\2\u009e\u009f\7g\2\2\u009f\u00a0")
        buf.write("\7v\2\2\u00a0\u00a1\7w\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3")
        buf.write("\7p\2\2\u00a3\n\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6")
        buf.write("\7w\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7e\2\2\u00a8\f")
        buf.write("\3\2\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab\7{\2\2\u00ab\u00ac")
        buf.write("\7r\2\2\u00ac\u00ad\7g\2\2\u00ad\16\3\2\2\2\u00ae\u00af")
        buf.write("\7u\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2")
        buf.write("\7w\2\2\u00b2\u00b3\7e\2\2\u00b3\u00b4\7v\2\2\u00b4\20")
        buf.write("\3\2\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8")
        buf.write("\7v\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb")
        buf.write("\7h\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7e\2\2\u00bd\u00be")
        buf.write("\7g\2\2\u00be\22\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\u00c5\7i\2\2\u00c5\24\3\2\2\2\u00c6\u00c7")
        buf.write("\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9\7v\2\2\u00c9\26")
        buf.write("\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd")
        buf.write("\7q\2\2\u00cd\u00ce\7c\2\2\u00ce\u00cf\7v\2\2\u00cf\30")
        buf.write("\3\2\2\2\u00d0\u00d1\7d\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3")
        buf.write("\7q\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6")
        buf.write("\7c\2\2\u00d6\u00d7\7p\2\2\u00d7\32\3\2\2\2\u00d8\u00d9")
        buf.write("\7e\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7p\2\2\u00db\u00dc")
        buf.write("\7u\2\2\u00dc\u00dd\7v\2\2\u00dd\34\3\2\2\2\u00de\u00df")
        buf.write("\7x\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1\7t\2\2\u00e1\36")
        buf.write("\3\2\2\2\u00e2\u00e3\7e\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5")
        buf.write("\7p\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea\7g\2\2\u00ea \3")
        buf.write("\2\2\2\u00eb\u00ec\7d\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee")
        buf.write("\7g\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0\7m\2\2\u00f0\"")
        buf.write("\3\2\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\u00f5\7i\2\2\u00f5\u00f6\7g\2\2\u00f6$\3")
        buf.write("\2\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa")
        buf.write("\7n\2\2\u00fa&\3\2\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7t\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff\7g\2\2\u00ff(\3")
        buf.write("\2\2\2\u0100\u0101\7h\2\2\u0101\u0102\7c\2\2\u0102\u0103")
        buf.write("\7n\2\2\u0103\u0104\7u\2\2\u0104\u0105\7g\2\2\u0105*\3")
        buf.write("\2\2\2\u0106\u0107\7-\2\2\u0107,\3\2\2\2\u0108\u0109\7")
        buf.write("/\2\2\u0109.\3\2\2\2\u010a\u010b\7,\2\2\u010b\60\3\2\2")
        buf.write("\2\u010c\u010d\7\61\2\2\u010d\62\3\2\2\2\u010e\u010f\7")
        buf.write("\'\2\2\u010f\64\3\2\2\2\u0110\u0111\7?\2\2\u0111\u0112")
        buf.write("\7?\2\2\u0112\66\3\2\2\2\u0113\u0114\7#\2\2\u0114\u0115")
        buf.write("\7?\2\2\u01158\3\2\2\2\u0116\u0117\7>\2\2\u0117:\3\2\2")
        buf.write("\2\u0118\u0119\7>\2\2\u0119\u011a\7?\2\2\u011a<\3\2\2")
        buf.write("\2\u011b\u011c\7@\2\2\u011c>\3\2\2\2\u011d\u011e\7@\2")
        buf.write("\2\u011e\u011f\7?\2\2\u011f@\3\2\2\2\u0120\u0121\7(\2")
        buf.write("\2\u0121\u0122\7(\2\2\u0122B\3\2\2\2\u0123\u0124\7~\2")
        buf.write("\2\u0124\u0125\7~\2\2\u0125D\3\2\2\2\u0126\u0127\7#\2")
        buf.write("\2\u0127F\3\2\2\2\u0128\u0129\7<\2\2\u0129\u012a\7?\2")
        buf.write("\2\u012aH\3\2\2\2\u012b\u012c\7-\2\2\u012c\u012d\7?\2")
        buf.write("\2\u012dJ\3\2\2\2\u012e\u012f\7/\2\2\u012f\u0130\7?\2")
        buf.write("\2\u0130L\3\2\2\2\u0131\u0132\7,\2\2\u0132\u0133\7?\2")
        buf.write("\2\u0133N\3\2\2\2\u0134\u0135\7\61\2\2\u0135\u0136\7?")
        buf.write("\2\2\u0136P\3\2\2\2\u0137\u0138\7\'\2\2\u0138\u0139\7")
        buf.write("?\2\2\u0139R\3\2\2\2\u013a\u013b\7?\2\2\u013bT\3\2\2\2")
        buf.write("\u013c\u013d\7\60\2\2\u013dV\3\2\2\2\u013e\u013f\7]\2")
        buf.write("\2\u013fX\3\2\2\2\u0140\u0141\7_\2\2\u0141Z\3\2\2\2\u0142")
        buf.write("\u0143\7*\2\2\u0143\\\3\2\2\2\u0144\u0145\7+\2\2\u0145")
        buf.write("^\3\2\2\2\u0146\u0147\7}\2\2\u0147`\3\2\2\2\u0148\u0149")
        buf.write("\7\177\2\2\u0149b\3\2\2\2\u014a\u014b\7.\2\2\u014bd\3")
        buf.write("\2\2\2\u014c\u014d\7<\2\2\u014df\3\2\2\2\u014e\u014f\7")
        buf.write("$\2\2\u014fh\3\2\2\2\u0150\u0151\7=\2\2\u0151j\3\2\2\2")
        buf.write("\u0152\u0153\7a\2\2\u0153l\3\2\2\2\u0154\u0155\7\61\2")
        buf.write("\2\u0155\u0156\7\61\2\2\u0156\u015a\3\2\2\2\u0157\u0159")
        buf.write("\13\2\2\2\u0158\u0157\3\2\2\2\u0159\u015c\3\2\2\2\u015a")
        buf.write("\u015b\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u015f\3\2\2\2")
        buf.write("\u015c\u015a\3\2\2\2\u015d\u0160\5\u0087D\2\u015e\u0160")
        buf.write("\7\2\2\3\u015f\u015d\3\2\2\2\u015f\u015e\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u0162\b\67\2\2\u0162n\3\2\2\2\u0163")
        buf.write("\u0164\7\61\2\2\u0164\u0165\7,\2\2\u0165\u016a\3\2\2\2")
        buf.write("\u0166\u0169\5o8\2\u0167\u0169\13\2\2\2\u0168\u0166\3")
        buf.write("\2\2\2\u0168\u0167\3\2\2\2\u0169\u016c\3\2\2\2\u016a\u016b")
        buf.write("\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016d\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016d\u016e\7,\2\2\u016e\u016f\7\61\2\2")
        buf.write("\u016f\u0170\3\2\2\2\u0170\u0171\b8\2\2\u0171p\3\2\2\2")
        buf.write("\u0172\u0173\t\2\2\2\u0173r\3\2\2\2\u0174\u0176\t\3\2")
        buf.write("\2\u0175\u0177\t\4\2\2\u0176\u0175\3\2\2\2\u0176\u0177")
        buf.write("\3\2\2\2\u0177\u0179\3\2\2\2\u0178\u017a\5q9\2\u0179\u0178")
        buf.write("\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u0179\3\2\2\2\u017b")
        buf.write("\u017c\3\2\2\2\u017ct\3\2\2\2\u017d\u017e\7^\2\2\u017e")
        buf.write("\u0183\t\5\2\2\u017f\u0180\7)\2\2\u0180\u0183\7$\2\2\u0181")
        buf.write("\u0183\n\6\2\2\u0182\u017d\3\2\2\2\u0182\u017f\3\2\2\2")
        buf.write("\u0182\u0181\3\2\2\2\u0183v\3\2\2\2\u0184\u0185\7\62\2")
        buf.write("\2\u0185\u0187\t\7\2\2\u0186\u0188\t\b\2\2\u0187\u0186")
        buf.write("\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u0187\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018ax\3\2\2\2\u018b\u018c\7\62\2\2\u018c")
        buf.write("\u018e\t\t\2\2\u018d\u018f\t\n\2\2\u018e\u018d\3\2\2\2")
        buf.write("\u018f\u0190\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191\3")
        buf.write("\2\2\2\u0191z\3\2\2\2\u0192\u0193\7\62\2\2\u0193\u0195")
        buf.write("\t\13\2\2\u0194\u0196\t\f\2\2\u0195\u0194\3\2\2\2\u0196")
        buf.write("\u0197\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2")
        buf.write("\u0198|\3\2\2\2\u0199\u01a2\7\62\2\2\u019a\u019e\t\r\2")
        buf.write("\2\u019b\u019d\t\2\2\2\u019c\u019b\3\2\2\2\u019d\u01a0")
        buf.write("\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f")
        buf.write("\u01a2\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u0199\3\2\2\2")
        buf.write("\u01a1\u019a\3\2\2\2\u01a2~\3\2\2\2\u01a3\u01a5\5q9\2")
        buf.write("\u01a4\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a4\3")
        buf.write("\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01ac")
        buf.write("\7\60\2\2\u01a9\u01ab\5q9\2\u01aa\u01a9\3\2\2\2\u01ab")
        buf.write("\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2")
        buf.write("\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b1\5")
        buf.write("s:\2\u01b0\u01af\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01ba")
        buf.write("\3\2\2\2\u01b2\u01b4\5q9\2\u01b3\u01b2\3\2\2\2\u01b4\u01b5")
        buf.write("\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6")
        buf.write("\u01b7\3\2\2\2\u01b7\u01b8\5s:\2\u01b8\u01ba\3\2\2\2\u01b9")
        buf.write("\u01a4\3\2\2\2\u01b9\u01b3\3\2\2\2\u01ba\u0080\3\2\2\2")
        buf.write("\u01bb\u01bf\5g\64\2\u01bc\u01be\5u;\2\u01bd\u01bc\3\2")
        buf.write("\2\2\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0")
        buf.write("\3\2\2\2\u01c0\u01c2\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2")
        buf.write("\u01c3\5g\64\2\u01c3\u0082\3\2\2\2\u01c4\u01c5\5%\23\2")
        buf.write("\u01c5\u0084\3\2\2\2\u01c6\u01ca\t\16\2\2\u01c7\u01c9")
        buf.write("\t\17\2\2\u01c8\u01c7\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca")
        buf.write("\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u0086\3\2\2\2")
        buf.write("\u01cc\u01ca\3\2\2\2\u01cd\u01ce\7\f\2\2\u01ce\u01cf\b")
        buf.write("D\3\2\u01cf\u0088\3\2\2\2\u01d0\u01d2\t\20\2\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d4\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d6\bE\2\2")
        buf.write("\u01d6\u008a\3\2\2\2\u01d7\u01db\5g\64\2\u01d8\u01da\5")
        buf.write("u;\2\u01d9\u01d8\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9")
        buf.write("\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd")
        buf.write("\u01db\3\2\2\2\u01de\u01e0\t\21\2\2\u01df\u01de\3\2\2")
        buf.write("\2\u01e0\u01e1\3\2\2\2\u01e1\u01e2\bF\4\2\u01e2\u008c")
        buf.write("\3\2\2\2\u01e3\u01e7\5g\64\2\u01e4\u01e6\5u;\2\u01e5\u01e4")
        buf.write("\3\2\2\2\u01e6\u01e9\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7")
        buf.write("\u01e8\3\2\2\2\u01e8\u01ea\3\2\2\2\u01e9\u01e7\3\2\2\2")
        buf.write("\u01ea\u01eb\7^\2\2\u01eb\u01ec\n\5\2\2\u01ec\u01ed\3")
        buf.write("\2\2\2\u01ed\u01ee\bG\5\2\u01ee\u008e\3\2\2\2\u01ef\u01f0")
        buf.write("\13\2\2\2\u01f0\u01f1\bH\6\2\u01f1\u0090\3\2\2\2\32\2")
        buf.write("\u015a\u015f\u0168\u016a\u0176\u017b\u0182\u0189\u0190")
        buf.write("\u0197\u019e\u01a1\u01a6\u01ac\u01b0\u01b5\u01b9\u01bf")
        buf.write("\u01ca\u01d3\u01db\u01df\u01e7\7\b\2\2\3D\2\3F\3\3G\4")
        buf.write("\3H\5")
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
    UNDERSCORE = 53
    LINE_CMT = 54
    COMMENT = 55
    BINLIT = 56
    OCTLIT = 57
    HEXLIT = 58
    INTLIT = 59
    FLOATLIT = 60
    STRINGLIT = 61
    NILLIT = 62
    ID = 63
    NL = 64
    WS = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67
    ERROR_CHAR = 68

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
            "';'", "'_'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD_OP", "SUB_OP", 
            "MUL_OP", "DIV_OP", "MOD_OP", "EQ_OP", "NEQ_OP", "LT_OP", "LEQ_OP", 
            "GT_OP", "GEQ_OP", "AND_OP", "OR_OP", "NOT_OP", "EQ_ASSIGN_OP", 
            "ADD_ASSIGN_OP", "SUB_ASSIGN_OP", "MUL_ASSIGN_OP", "DIV_ASSIGN_OP", 
            "MOD_ASSIGN_OP", "EQ", "DOT_OP", "LSB", "RSB", "LRB", "RRB", 
            "LCB", "RCB", "CM", "COL", "QUOTES", "SM", "UNDERSCORE", "LINE_CMT", 
            "COMMENT", "BINLIT", "OCTLIT", "HEXLIT", "INTLIT", "FLOATLIT", 
            "STRINGLIT", "NILLIT", "ID", "NL", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "MOD_OP", "EQ_OP", 
                  "NEQ_OP", "LT_OP", "LEQ_OP", "GT_OP", "GEQ_OP", "AND_OP", 
                  "OR_OP", "NOT_OP", "EQ_ASSIGN_OP", "ADD_ASSIGN_OP", "SUB_ASSIGN_OP", 
                  "MUL_ASSIGN_OP", "DIV_ASSIGN_OP", "MOD_ASSIGN_OP", "EQ", 
                  "DOT_OP", "LSB", "RSB", "LRB", "RRB", "LCB", "RCB", "CM", 
                  "COL", "QUOTES", "SM", "UNDERSCORE", "LINE_CMT", "COMMENT", 
                  "DIGIT", "EXPONENT", "CHAR", "BINLIT", "OCTLIT", "HEXLIT", 
                  "INTLIT", "FLOATLIT", "STRINGLIT", "NILLIT", "ID", "NL", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[66] = self.NL_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[70] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                if self.preType in [self.ID, self.INTLIT, self.BINLIT, self.OCTLIT, self.HEXLIT, self.STRINGLIT, self.FLOATLIT,
                                    self.TRUE, self.FALSE, self.INT, self.FLOAT, self.STRING, self.BOOLEAN, self.NIL,
                                    self.RETURN, self.CONTINUE, self.BREAK,
                                    self.RRB, self.RCB, self.RSB]:
                    self.text = ";"
                    self.type = self.SM
                else:
                    self.skip()

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    if(self.text[-1]=='\n'):
                        raise UncloseString(self.text[:-1])
                    raise UncloseString(self.text)
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text)
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


