# Generated from /home/son/Downloads/PPL-MiniGo/Assignment2/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,68,639,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,1,0,3,0,128,8,0,1,0,4,0,131,8,
        0,11,0,12,0,132,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,145,
        8,1,1,2,1,2,1,2,1,2,3,2,151,8,2,1,2,1,2,3,2,155,8,2,1,3,1,3,1,3,
        3,3,160,8,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,170,8,4,1,4,1,4,
        3,4,174,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,186,8,5,
        1,5,1,5,3,5,190,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,199,8,6,1,7,
        1,7,1,7,1,8,1,8,1,8,1,8,3,8,208,8,8,1,9,1,9,1,9,1,10,1,10,1,10,1,
        10,1,10,1,10,5,10,219,8,10,10,10,12,10,222,9,10,1,10,1,10,1,10,1,
        11,1,11,1,11,3,11,230,8,11,1,11,1,11,3,11,234,8,11,1,11,1,11,1,12,
        1,12,1,12,1,12,1,12,1,12,5,12,244,8,12,10,12,12,12,247,9,12,1,13,
        1,13,1,13,1,13,1,13,1,13,5,13,255,8,13,10,13,12,13,258,9,13,1,14,
        1,14,1,14,1,14,1,14,1,14,5,14,266,8,14,10,14,12,14,269,9,14,1,15,
        1,15,1,15,1,15,1,15,1,15,5,15,277,8,15,10,15,12,15,280,9,15,1,16,
        1,16,1,16,1,16,1,16,1,16,5,16,288,8,16,10,16,12,16,291,9,16,1,17,
        1,17,1,17,3,17,296,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        3,18,306,8,18,3,18,308,8,18,5,18,310,8,18,10,18,12,18,313,9,18,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,322,8,19,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,334,8,20,1,21,1,21,1,21,1,
        21,3,21,340,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,358,8,22,1,23,1,23,1,23,1,
        23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,371,8,24,5,24,373,8,24,
        10,24,12,24,376,9,24,1,25,1,25,1,26,1,26,1,26,1,26,1,26,3,26,385,
        8,26,1,26,1,26,3,26,389,8,26,1,26,1,26,3,26,393,8,26,1,26,3,26,396,
        8,26,1,27,1,27,1,27,1,27,3,27,402,8,27,1,28,1,28,1,28,1,28,1,28,
        1,28,3,28,410,8,28,1,28,1,28,1,29,1,29,1,29,3,29,417,8,29,1,29,3,
        29,420,8,29,1,29,1,29,1,30,1,30,1,30,1,31,1,31,1,31,3,31,430,8,31,
        1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,33,1,33,3,33,447,8,33,1,34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,
        1,36,1,37,1,37,1,37,1,38,1,38,1,38,1,38,3,38,465,8,38,1,38,1,38,
        1,38,1,38,3,38,471,8,38,1,38,1,38,1,38,1,39,1,39,1,39,3,39,479,8,
        39,1,39,1,39,1,40,1,40,1,40,3,40,486,8,40,1,41,1,41,1,41,1,41,1,
        41,5,41,493,8,41,10,41,12,41,496,9,41,1,41,1,41,3,41,500,8,41,1,
        42,1,42,1,42,1,42,1,43,1,43,3,43,508,8,43,1,43,1,43,5,43,512,8,43,
        10,43,12,43,515,9,43,1,44,1,44,1,44,1,44,3,44,521,8,44,1,44,1,44,
        1,45,1,45,1,45,1,45,3,45,529,8,45,1,46,1,46,1,46,1,46,1,46,3,46,
        536,8,46,1,47,1,47,1,47,1,47,1,47,1,47,3,47,544,8,47,1,48,1,48,1,
        49,1,49,1,49,1,49,3,49,552,8,49,1,50,1,50,1,50,1,50,1,51,1,51,4,
        51,560,8,51,11,51,12,51,561,3,51,564,8,51,1,52,1,52,1,53,1,53,1,
        53,1,53,1,53,1,53,1,53,1,53,1,53,3,53,577,8,53,1,54,1,54,1,54,1,
        54,3,54,583,8,54,1,54,1,54,1,55,1,55,1,55,1,55,1,55,3,55,592,8,55,
        1,56,1,56,1,56,1,56,1,56,3,56,599,8,56,1,57,1,57,1,57,1,57,1,57,
        3,57,606,8,57,1,58,1,58,1,58,1,58,1,58,1,58,3,58,614,8,58,1,59,1,
        59,1,59,3,59,619,8,59,1,59,1,59,1,60,1,60,1,60,1,60,1,60,3,60,628,
        8,60,1,61,1,61,1,61,1,61,1,62,4,62,635,8,62,11,62,12,62,636,1,62,
        0,7,24,26,28,30,32,36,48,63,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,
        72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,
        112,114,116,118,120,122,124,0,8,1,0,26,31,1,0,21,22,1,0,23,25,2,
        0,22,22,34,34,1,0,35,40,2,0,53,53,63,63,1,0,9,12,1,0,19,20,678,0,
        127,1,0,0,0,2,144,1,0,0,0,4,146,1,0,0,0,6,156,1,0,0,0,8,165,1,0,
        0,0,10,177,1,0,0,0,12,198,1,0,0,0,14,200,1,0,0,0,16,207,1,0,0,0,
        18,209,1,0,0,0,20,212,1,0,0,0,22,226,1,0,0,0,24,237,1,0,0,0,26,248,
        1,0,0,0,28,259,1,0,0,0,30,270,1,0,0,0,32,281,1,0,0,0,34,295,1,0,
        0,0,36,297,1,0,0,0,38,321,1,0,0,0,40,333,1,0,0,0,42,339,1,0,0,0,
        44,357,1,0,0,0,46,359,1,0,0,0,48,363,1,0,0,0,50,377,1,0,0,0,52,379,
        1,0,0,0,54,401,1,0,0,0,56,403,1,0,0,0,58,416,1,0,0,0,60,423,1,0,
        0,0,62,426,1,0,0,0,64,436,1,0,0,0,66,446,1,0,0,0,68,448,1,0,0,0,
        70,450,1,0,0,0,72,454,1,0,0,0,74,457,1,0,0,0,76,464,1,0,0,0,78,475,
        1,0,0,0,80,482,1,0,0,0,82,487,1,0,0,0,84,501,1,0,0,0,86,505,1,0,
        0,0,88,516,1,0,0,0,90,528,1,0,0,0,92,535,1,0,0,0,94,543,1,0,0,0,
        96,545,1,0,0,0,98,551,1,0,0,0,100,553,1,0,0,0,102,563,1,0,0,0,104,
        565,1,0,0,0,106,576,1,0,0,0,108,578,1,0,0,0,110,591,1,0,0,0,112,
        598,1,0,0,0,114,605,1,0,0,0,116,613,1,0,0,0,118,615,1,0,0,0,120,
        627,1,0,0,0,122,629,1,0,0,0,124,634,1,0,0,0,126,128,3,124,62,0,127,
        126,1,0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,131,3,2,1,0,130,
        129,1,0,0,0,131,132,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,
        134,1,0,0,0,134,135,5,0,0,1,135,1,1,0,0,0,136,137,3,4,2,0,137,138,
        3,102,51,0,138,145,1,0,0,0,139,145,3,6,3,0,140,145,3,8,4,0,141,145,
        3,10,5,0,142,145,3,18,9,0,143,145,3,20,10,0,144,136,1,0,0,0,144,
        139,1,0,0,0,144,140,1,0,0,0,144,141,1,0,0,0,144,142,1,0,0,0,144,
        143,1,0,0,0,145,3,1,0,0,0,146,147,5,14,0,0,147,154,5,63,0,0,148,
        155,3,94,47,0,149,151,3,94,47,0,150,149,1,0,0,0,150,151,1,0,0,0,
        151,152,1,0,0,0,152,153,5,41,0,0,153,155,3,24,12,0,154,148,1,0,0,
        0,154,150,1,0,0,0,155,5,1,0,0,0,156,157,5,13,0,0,157,159,5,63,0,
        0,158,160,3,94,47,0,159,158,1,0,0,0,159,160,1,0,0,0,160,161,1,0,
        0,0,161,162,5,41,0,0,162,163,3,24,12,0,163,164,3,102,51,0,164,7,
        1,0,0,0,165,166,5,5,0,0,166,167,5,63,0,0,167,169,5,45,0,0,168,170,
        3,12,6,0,169,168,1,0,0,0,169,170,1,0,0,0,170,171,1,0,0,0,171,173,
        5,46,0,0,172,174,3,94,47,0,173,172,1,0,0,0,173,174,1,0,0,0,174,175,
        1,0,0,0,175,176,3,86,43,0,176,9,1,0,0,0,177,178,5,5,0,0,178,179,
        5,45,0,0,179,180,5,63,0,0,180,181,5,63,0,0,181,182,5,46,0,0,182,
        183,5,63,0,0,183,185,5,45,0,0,184,186,3,12,6,0,185,184,1,0,0,0,185,
        186,1,0,0,0,186,187,1,0,0,0,187,189,5,46,0,0,188,190,3,94,47,0,189,
        188,1,0,0,0,189,190,1,0,0,0,190,191,1,0,0,0,191,192,3,86,43,0,192,
        11,1,0,0,0,193,194,3,14,7,0,194,195,5,49,0,0,195,196,3,12,6,0,196,
        199,1,0,0,0,197,199,3,14,7,0,198,193,1,0,0,0,198,197,1,0,0,0,199,
        13,1,0,0,0,200,201,3,16,8,0,201,202,3,94,47,0,202,15,1,0,0,0,203,
        204,5,63,0,0,204,205,5,49,0,0,205,208,3,16,8,0,206,208,5,63,0,0,
        207,203,1,0,0,0,207,206,1,0,0,0,208,17,1,0,0,0,209,210,5,6,0,0,210,
        211,3,82,41,0,211,19,1,0,0,0,212,213,5,6,0,0,213,214,5,63,0,0,214,
        215,5,8,0,0,215,220,5,47,0,0,216,219,5,64,0,0,217,219,3,22,11,0,
        218,216,1,0,0,0,218,217,1,0,0,0,219,222,1,0,0,0,220,218,1,0,0,0,
        220,221,1,0,0,0,221,223,1,0,0,0,222,220,1,0,0,0,223,224,5,48,0,0,
        224,225,3,102,51,0,225,21,1,0,0,0,226,227,5,63,0,0,227,229,5,45,
        0,0,228,230,3,12,6,0,229,228,1,0,0,0,229,230,1,0,0,0,230,231,1,0,
        0,0,231,233,5,46,0,0,232,234,3,94,47,0,233,232,1,0,0,0,233,234,1,
        0,0,0,234,235,1,0,0,0,235,236,3,102,51,0,236,23,1,0,0,0,237,238,
        6,12,-1,0,238,239,3,26,13,0,239,245,1,0,0,0,240,241,10,2,0,0,241,
        242,5,33,0,0,242,244,3,26,13,0,243,240,1,0,0,0,244,247,1,0,0,0,245,
        243,1,0,0,0,245,246,1,0,0,0,246,25,1,0,0,0,247,245,1,0,0,0,248,249,
        6,13,-1,0,249,250,3,28,14,0,250,256,1,0,0,0,251,252,10,2,0,0,252,
        253,5,32,0,0,253,255,3,28,14,0,254,251,1,0,0,0,255,258,1,0,0,0,256,
        254,1,0,0,0,256,257,1,0,0,0,257,27,1,0,0,0,258,256,1,0,0,0,259,260,
        6,14,-1,0,260,261,3,30,15,0,261,267,1,0,0,0,262,263,10,2,0,0,263,
        264,7,0,0,0,264,266,3,30,15,0,265,262,1,0,0,0,266,269,1,0,0,0,267,
        265,1,0,0,0,267,268,1,0,0,0,268,29,1,0,0,0,269,267,1,0,0,0,270,271,
        6,15,-1,0,271,272,3,32,16,0,272,278,1,0,0,0,273,274,10,2,0,0,274,
        275,7,1,0,0,275,277,3,32,16,0,276,273,1,0,0,0,277,280,1,0,0,0,278,
        276,1,0,0,0,278,279,1,0,0,0,279,31,1,0,0,0,280,278,1,0,0,0,281,282,
        6,16,-1,0,282,283,3,34,17,0,283,289,1,0,0,0,284,285,10,2,0,0,285,
        286,7,2,0,0,286,288,3,34,17,0,287,284,1,0,0,0,288,291,1,0,0,0,289,
        287,1,0,0,0,289,290,1,0,0,0,290,33,1,0,0,0,291,289,1,0,0,0,292,293,
        7,3,0,0,293,296,3,34,17,0,294,296,3,36,18,0,295,292,1,0,0,0,295,
        294,1,0,0,0,296,35,1,0,0,0,297,298,6,18,-1,0,298,299,3,38,19,0,299,
        311,1,0,0,0,300,307,10,2,0,0,301,308,3,98,49,0,302,305,5,42,0,0,
        303,306,5,63,0,0,304,306,3,88,44,0,305,303,1,0,0,0,305,304,1,0,0,
        0,306,308,1,0,0,0,307,301,1,0,0,0,307,302,1,0,0,0,308,310,1,0,0,
        0,309,300,1,0,0,0,310,313,1,0,0,0,311,309,1,0,0,0,311,312,1,0,0,
        0,312,37,1,0,0,0,313,311,1,0,0,0,314,322,3,40,20,0,315,316,5,45,
        0,0,316,317,3,24,12,0,317,318,5,46,0,0,318,322,1,0,0,0,319,322,5,
        63,0,0,320,322,3,88,44,0,321,314,1,0,0,0,321,315,1,0,0,0,321,319,
        1,0,0,0,321,320,1,0,0,0,322,39,1,0,0,0,323,334,5,59,0,0,324,334,
        5,56,0,0,325,334,5,57,0,0,326,334,5,58,0,0,327,334,5,60,0,0,328,
        334,5,61,0,0,329,334,3,104,52,0,330,334,5,18,0,0,331,334,3,108,54,
        0,332,334,3,118,59,0,333,323,1,0,0,0,333,324,1,0,0,0,333,325,1,0,
        0,0,333,326,1,0,0,0,333,327,1,0,0,0,333,328,1,0,0,0,333,329,1,0,
        0,0,333,330,1,0,0,0,333,331,1,0,0,0,333,332,1,0,0,0,334,41,1,0,0,
        0,335,336,3,44,22,0,336,337,3,42,21,0,337,340,1,0,0,0,338,340,3,
        44,22,0,339,335,1,0,0,0,339,338,1,0,0,0,340,43,1,0,0,0,341,342,3,
        4,2,0,342,343,3,102,51,0,343,358,1,0,0,0,344,358,3,6,3,0,345,358,
        3,18,9,0,346,358,3,10,5,0,347,348,3,46,23,0,348,349,3,102,51,0,349,
        358,1,0,0,0,350,358,3,52,26,0,351,358,3,58,29,0,352,358,3,72,36,
        0,353,358,3,74,37,0,354,358,3,76,38,0,355,358,3,78,39,0,356,358,
        3,86,43,0,357,341,1,0,0,0,357,344,1,0,0,0,357,345,1,0,0,0,357,346,
        1,0,0,0,357,347,1,0,0,0,357,350,1,0,0,0,357,351,1,0,0,0,357,352,
        1,0,0,0,357,353,1,0,0,0,357,354,1,0,0,0,357,355,1,0,0,0,357,356,
        1,0,0,0,358,45,1,0,0,0,359,360,3,48,24,0,360,361,3,50,25,0,361,362,
        3,24,12,0,362,47,1,0,0,0,363,364,6,24,-1,0,364,365,5,63,0,0,365,
        374,1,0,0,0,366,370,10,2,0,0,367,371,3,98,49,0,368,369,5,42,0,0,
        369,371,5,63,0,0,370,367,1,0,0,0,370,368,1,0,0,0,371,373,1,0,0,0,
        372,366,1,0,0,0,373,376,1,0,0,0,374,372,1,0,0,0,374,375,1,0,0,0,
        375,49,1,0,0,0,376,374,1,0,0,0,377,378,7,4,0,0,378,51,1,0,0,0,379,
        380,5,1,0,0,380,381,5,45,0,0,381,382,3,24,12,0,382,384,5,46,0,0,
        383,385,3,124,62,0,384,383,1,0,0,0,384,385,1,0,0,0,385,386,1,0,0,
        0,386,388,3,86,43,0,387,389,3,54,27,0,388,387,1,0,0,0,388,389,1,
        0,0,0,389,395,1,0,0,0,390,392,5,2,0,0,391,393,3,124,62,0,392,391,
        1,0,0,0,392,393,1,0,0,0,393,394,1,0,0,0,394,396,3,86,43,0,395,390,
        1,0,0,0,395,396,1,0,0,0,396,53,1,0,0,0,397,398,3,56,28,0,398,399,
        3,54,27,0,399,402,1,0,0,0,400,402,3,56,28,0,401,397,1,0,0,0,401,
        400,1,0,0,0,402,55,1,0,0,0,403,404,5,2,0,0,404,405,5,1,0,0,405,406,
        5,45,0,0,406,407,3,24,12,0,407,409,5,46,0,0,408,410,3,124,62,0,409,
        408,1,0,0,0,409,410,1,0,0,0,410,411,1,0,0,0,411,412,3,86,43,0,412,
        57,1,0,0,0,413,417,3,60,30,0,414,417,3,62,31,0,415,417,3,64,32,0,
        416,413,1,0,0,0,416,414,1,0,0,0,416,415,1,0,0,0,417,419,1,0,0,0,
        418,420,3,124,62,0,419,418,1,0,0,0,419,420,1,0,0,0,420,421,1,0,0,
        0,421,422,3,86,43,0,422,59,1,0,0,0,423,424,5,3,0,0,424,425,3,24,
        12,0,425,61,1,0,0,0,426,429,5,3,0,0,427,430,3,46,23,0,428,430,3,
        4,2,0,429,427,1,0,0,0,429,428,1,0,0,0,430,431,1,0,0,0,431,432,5,
        52,0,0,432,433,3,24,12,0,433,434,5,52,0,0,434,435,3,46,23,0,435,
        63,1,0,0,0,436,437,5,3,0,0,437,438,3,66,33,0,438,439,5,49,0,0,439,
        440,5,63,0,0,440,441,5,35,0,0,441,442,5,17,0,0,442,443,3,24,12,0,
        443,65,1,0,0,0,444,447,3,68,34,0,445,447,3,70,35,0,446,444,1,0,0,
        0,446,445,1,0,0,0,447,67,1,0,0,0,448,449,7,5,0,0,449,69,1,0,0,0,
        450,451,7,5,0,0,451,452,5,49,0,0,452,453,7,5,0,0,453,71,1,0,0,0,
        454,455,5,16,0,0,455,456,3,102,51,0,456,73,1,0,0,0,457,458,5,15,
        0,0,458,459,3,102,51,0,459,75,1,0,0,0,460,461,3,48,24,0,461,462,
        5,42,0,0,462,465,1,0,0,0,463,465,1,0,0,0,464,460,1,0,0,0,464,463,
        1,0,0,0,465,466,1,0,0,0,466,467,5,63,0,0,467,470,5,45,0,0,468,471,
        3,90,45,0,469,471,1,0,0,0,470,468,1,0,0,0,470,469,1,0,0,0,471,472,
        1,0,0,0,472,473,5,46,0,0,473,474,3,102,51,0,474,77,1,0,0,0,475,478,
        5,4,0,0,476,479,3,24,12,0,477,479,1,0,0,0,478,476,1,0,0,0,478,477,
        1,0,0,0,479,480,1,0,0,0,480,481,3,102,51,0,481,79,1,0,0,0,482,485,
        3,98,49,0,483,486,3,96,48,0,484,486,5,63,0,0,485,483,1,0,0,0,485,
        484,1,0,0,0,486,81,1,0,0,0,487,488,5,63,0,0,488,489,5,7,0,0,489,
        494,5,47,0,0,490,493,5,64,0,0,491,493,3,84,42,0,492,490,1,0,0,0,
        492,491,1,0,0,0,493,496,1,0,0,0,494,492,1,0,0,0,494,495,1,0,0,0,
        495,497,1,0,0,0,496,494,1,0,0,0,497,499,5,48,0,0,498,500,3,102,51,
        0,499,498,1,0,0,0,499,500,1,0,0,0,500,83,1,0,0,0,501,502,5,63,0,
        0,502,503,3,94,47,0,503,504,3,102,51,0,504,85,1,0,0,0,505,507,5,
        47,0,0,506,508,3,42,21,0,507,506,1,0,0,0,507,508,1,0,0,0,508,509,
        1,0,0,0,509,513,5,48,0,0,510,512,3,102,51,0,511,510,1,0,0,0,512,
        515,1,0,0,0,513,511,1,0,0,0,513,514,1,0,0,0,514,87,1,0,0,0,515,513,
        1,0,0,0,516,517,5,63,0,0,517,520,5,45,0,0,518,521,3,90,45,0,519,
        521,1,0,0,0,520,518,1,0,0,0,520,519,1,0,0,0,521,522,1,0,0,0,522,
        523,5,46,0,0,523,89,1,0,0,0,524,525,3,24,12,0,525,526,3,92,46,0,
        526,529,1,0,0,0,527,529,3,24,12,0,528,524,1,0,0,0,528,527,1,0,0,
        0,529,91,1,0,0,0,530,531,5,49,0,0,531,532,3,24,12,0,532,533,3,92,
        46,0,533,536,1,0,0,0,534,536,1,0,0,0,535,530,1,0,0,0,535,534,1,0,
        0,0,536,93,1,0,0,0,537,544,5,10,0,0,538,544,5,11,0,0,539,544,5,12,
        0,0,540,544,5,9,0,0,541,544,3,80,40,0,542,544,5,63,0,0,543,537,1,
        0,0,0,543,538,1,0,0,0,543,539,1,0,0,0,543,540,1,0,0,0,543,541,1,
        0,0,0,543,542,1,0,0,0,544,95,1,0,0,0,545,546,7,6,0,0,546,97,1,0,
        0,0,547,548,3,100,50,0,548,549,3,98,49,0,549,552,1,0,0,0,550,552,
        3,100,50,0,551,547,1,0,0,0,551,550,1,0,0,0,552,99,1,0,0,0,553,554,
        5,43,0,0,554,555,3,24,12,0,555,556,5,44,0,0,556,101,1,0,0,0,557,
        564,5,52,0,0,558,560,5,64,0,0,559,558,1,0,0,0,560,561,1,0,0,0,561,
        559,1,0,0,0,561,562,1,0,0,0,562,564,1,0,0,0,563,557,1,0,0,0,563,
        559,1,0,0,0,564,103,1,0,0,0,565,566,7,7,0,0,566,105,1,0,0,0,567,
        577,5,59,0,0,568,577,5,56,0,0,569,577,5,57,0,0,570,577,5,58,0,0,
        571,577,5,60,0,0,572,577,5,61,0,0,573,577,3,104,52,0,574,577,5,18,
        0,0,575,577,3,118,59,0,576,567,1,0,0,0,576,568,1,0,0,0,576,569,1,
        0,0,0,576,570,1,0,0,0,576,571,1,0,0,0,576,572,1,0,0,0,576,573,1,
        0,0,0,576,574,1,0,0,0,576,575,1,0,0,0,577,107,1,0,0,0,578,579,3,
        98,49,0,579,580,3,94,47,0,580,582,5,47,0,0,581,583,3,110,55,0,582,
        581,1,0,0,0,582,583,1,0,0,0,583,584,1,0,0,0,584,585,5,48,0,0,585,
        109,1,0,0,0,586,587,3,112,56,0,587,588,5,49,0,0,588,589,3,110,55,
        0,589,592,1,0,0,0,590,592,3,112,56,0,591,586,1,0,0,0,591,590,1,0,
        0,0,592,111,1,0,0,0,593,599,3,114,57,0,594,595,5,47,0,0,595,596,
        3,112,56,0,596,597,5,48,0,0,597,599,1,0,0,0,598,593,1,0,0,0,598,
        594,1,0,0,0,599,113,1,0,0,0,600,601,3,116,58,0,601,602,5,49,0,0,
        602,603,3,114,57,0,603,606,1,0,0,0,604,606,3,116,58,0,605,600,1,
        0,0,0,605,604,1,0,0,0,606,115,1,0,0,0,607,614,3,106,53,0,608,614,
        3,24,12,0,609,610,5,47,0,0,610,611,3,112,56,0,611,612,5,48,0,0,612,
        614,1,0,0,0,613,607,1,0,0,0,613,608,1,0,0,0,613,609,1,0,0,0,614,
        117,1,0,0,0,615,616,5,63,0,0,616,618,5,47,0,0,617,619,3,120,60,0,
        618,617,1,0,0,0,618,619,1,0,0,0,619,620,1,0,0,0,620,621,5,48,0,0,
        621,119,1,0,0,0,622,623,3,122,61,0,623,624,5,49,0,0,624,625,3,120,
        60,0,625,628,1,0,0,0,626,628,3,122,61,0,627,622,1,0,0,0,627,626,
        1,0,0,0,628,121,1,0,0,0,629,630,5,63,0,0,630,631,5,50,0,0,631,632,
        3,24,12,0,632,123,1,0,0,0,633,635,5,64,0,0,634,633,1,0,0,0,635,636,
        1,0,0,0,636,634,1,0,0,0,636,637,1,0,0,0,637,125,1,0,0,0,66,127,132,
        144,150,154,159,169,173,185,189,198,207,218,220,229,233,245,256,
        267,278,289,295,305,307,311,321,333,339,357,370,374,384,388,392,
        395,401,409,416,419,429,446,464,470,478,485,492,494,499,507,513,
        520,528,535,543,551,561,563,576,582,591,598,605,613,618,627,636
    ]

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
                     "'\\n'" ]

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
        self.checkVersion("4.13.1")
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




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 24672) != 0)):
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223363240761745920) != 0):
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223363240761745920) != 0):
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
            if _la==63:
                self.state = 168
                self.parameter_list()


            self.state = 171
            self.match(MiniGoParser.RRB)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223363240761745920) != 0):
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
            if _la==63:
                self.state = 184
                self.parameter_list()


            self.state = 187
            self.match(MiniGoParser.RRB)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223363240761745920) != 0):
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
            while _la==63 or _la==64:
                self.state = 218
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [64]:
                    self.state = 216
                    self.match(MiniGoParser.NL)
                    pass
                elif token in [63]:
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
            if _la==63:
                self.state = 228
                self.parameter_list()


            self.state = 231
            self.match(MiniGoParser.RRB)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223363240761745920) != 0):
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0)):
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
                    if not(_la==21 or _la==22):
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
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




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                _la = self._input.LA(1)
                if not(_la==22 or _la==34):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 293
                self.expr5()
                pass
            elif token in [18, 19, 20, 43, 45, 56, 57, 58, 59, 60, 61, 63]:
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
                    if token in [43]:
                        self.state = 301
                        self.list_array_index()
                        pass
                    elif token in [42]:
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




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_literal)
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(MiniGoParser.INTLIT)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.match(MiniGoParser.BINLIT)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 3)
                self.state = 325
                self.match(MiniGoParser.OCTLIT)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 4)
                self.state = 326
                self.match(MiniGoParser.HEXLIT)
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 5)
                self.state = 327
                self.match(MiniGoParser.FLOATLIT)
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 6)
                self.state = 328
                self.match(MiniGoParser.STRINGLIT)
                pass
            elif token in [19, 20]:
                self.enterOuterAlt(localctx, 7)
                self.state = 329
                self.boollit()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 8)
                self.state = 330
                self.match(MiniGoParser.NIL)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 9)
                self.state = 331
                self.arraylit()
                pass
            elif token in [63]:
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
                    if token in [43]:
                        self.state = 367
                        self.list_array_index()
                        pass
                    elif token in [42]:
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




    def assign_op(self):

        localctx = MiniGoParser.Assign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2164663517184) != 0)):
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
            if _la==64:
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
            if _la==2:
                self.state = 390
                self.match(MiniGoParser.ELSE)
                self.state = 392
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==64:
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
            if _la==64:
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
            if _la==64:
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
            if token in [63]:
                self.state = 427
                self.assign_stmt()
                pass
            elif token in [14]:
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




    def single_var(self):

        localctx = MiniGoParser.Single_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_single_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            _la = self._input.LA(1)
            if not(_la==53 or _la==63):
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




    def dual_var(self):

        localctx = MiniGoParser.Dual_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_dual_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            _la = self._input.LA(1)
            if not(_la==53 or _la==63):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 451
            self.match(MiniGoParser.CM)
            self.state = 452
            _la = self._input.LA(1)
            if not(_la==53 or _la==63):
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
            if token in [18, 19, 20, 22, 34, 43, 45, 56, 57, 58, 59, 60, 61, 63]:
                self.state = 468
                self.expr_list()
                pass
            elif token in [46]:
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
            if token in [18, 19, 20, 22, 34, 43, 45, 56, 57, 58, 59, 60, 61, 63]:
                self.state = 476
                self.expr(0)
                pass
            elif token in [52, 64]:
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
            if token in [9, 10, 11, 12]:
                self.state = 483
                self.prim_types()
                pass
            elif token in [63]:
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
            while _la==63 or _la==64:
                self.state = 492
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [64]:
                    self.state = 490
                    self.match(MiniGoParser.NL)
                    pass
                elif token in [63]:
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
            if _la==52 or _la==64:
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223231299366297478) != 0):
                self.state = 506
                self.stmt_list()


            self.state = 509
            self.match(MiniGoParser.RCB)
            self.state = 513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52 or _la==64:
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
            if token in [18, 19, 20, 22, 34, 43, 45, 56, 57, 58, 59, 60, 61, 63]:
                self.state = 518
                self.expr_list()
                pass
            elif token in [46]:
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




    def expr_tail(self):

        localctx = MiniGoParser.Expr_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr_tail)
        try:
            self.state = 535
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.match(MiniGoParser.CM)
                self.state = 531
                self.expr(0)
                self.state = 532
                self.expr_tail()
                pass
            elif token in [46]:
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




    def all_type(self):

        localctx = MiniGoParser.All_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_all_type)
        try:
            self.state = 543
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.match(MiniGoParser.INT)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 538
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 539
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 540
                self.match(MiniGoParser.STRING)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 5)
                self.state = 541
                self.array_type()
                pass
            elif token in [63]:
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




    def prim_types(self):

        localctx = MiniGoParser.Prim_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_prim_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
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




    def sm_nl(self):

        localctx = MiniGoParser.Sm_nlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_sm_nl)
        try:
            self.state = 563
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 557
                self.match(MiniGoParser.SM)
                pass
            elif token in [64]:
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




    def boollit(self):

        localctx = MiniGoParser.BoollitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            _la = self._input.LA(1)
            if not(_la==19 or _la==20):
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




    def array_item(self):

        localctx = MiniGoParser.Array_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_array_item)
        try:
            self.state = 576
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 567
                self.match(MiniGoParser.INTLIT)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 568
                self.match(MiniGoParser.BINLIT)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 3)
                self.state = 569
                self.match(MiniGoParser.OCTLIT)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 4)
                self.state = 570
                self.match(MiniGoParser.HEXLIT)
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 5)
                self.state = 571
                self.match(MiniGoParser.FLOATLIT)
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 6)
                self.state = 572
                self.match(MiniGoParser.STRINGLIT)
                pass
            elif token in [19, 20]:
                self.enterOuterAlt(localctx, 7)
                self.state = 573
                self.boollit()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 8)
                self.state = 574
                self.match(MiniGoParser.NIL)
                pass
            elif token in [63]:
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -4683558877325950976) != 0):
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
            if _la==63:
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
                if not (_la==64):
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
         




