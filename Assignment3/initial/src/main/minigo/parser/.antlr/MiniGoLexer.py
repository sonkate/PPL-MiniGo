# Generated from /home/son/Downloads/PPL-MiniGo/Assignment3/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,68,496,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,
        1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,
        1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,
        1,25,1,26,1,26,1,26,1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,30,1,30,
        1,30,1,31,1,31,1,31,1,32,1,32,1,32,1,33,1,33,1,34,1,34,1,34,1,35,
        1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,38,1,38,1,38,1,39,1,39,
        1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,43,1,43,1,44,1,44,1,45,1,45,
        1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,51,1,51,1,52,
        1,52,1,53,1,53,1,53,1,53,5,53,343,8,53,10,53,12,53,346,9,53,1,53,
        1,53,3,53,350,8,53,1,53,1,53,1,54,1,54,1,54,1,54,1,54,5,54,359,8,
        54,10,54,12,54,362,9,54,1,54,1,54,1,54,1,54,1,54,1,55,1,55,1,56,
        1,56,3,56,373,8,56,1,56,4,56,376,8,56,11,56,12,56,377,1,57,1,57,
        1,57,1,57,1,57,3,57,385,8,57,1,58,1,58,1,58,4,58,390,8,58,11,58,
        12,58,391,1,59,1,59,1,59,4,59,397,8,59,11,59,12,59,398,1,60,1,60,
        1,60,4,60,404,8,60,11,60,12,60,405,1,61,1,61,1,61,5,61,411,8,61,
        10,61,12,61,414,9,61,3,61,416,8,61,1,62,4,62,419,8,62,11,62,12,62,
        420,1,62,1,62,5,62,425,8,62,10,62,12,62,428,9,62,1,62,3,62,431,8,
        62,1,62,4,62,434,8,62,11,62,12,62,435,1,62,1,62,3,62,440,8,62,1,
        63,1,63,5,63,444,8,63,10,63,12,63,447,9,63,1,63,1,63,1,64,1,64,1,
        65,1,65,5,65,455,8,65,10,65,12,65,458,9,65,1,66,1,66,1,66,1,67,4,
        67,464,8,67,11,67,12,67,465,1,67,1,67,1,68,1,68,5,68,472,8,68,10,
        68,12,68,475,9,68,1,68,3,68,478,8,68,1,68,1,68,1,69,1,69,5,69,484,
        8,69,10,69,12,69,487,9,69,1,69,1,69,1,69,1,69,1,69,1,70,1,70,1,70,
        2,344,360,0,71,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,
        11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,
        22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,
        33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,
        44,89,45,91,46,93,47,95,48,97,49,99,50,101,51,103,52,105,53,107,
        54,109,55,111,0,113,0,115,0,117,56,119,57,121,58,123,59,125,60,127,
        61,129,62,131,63,133,64,135,65,137,66,139,67,141,68,1,0,16,1,0,48,
        57,2,0,69,69,101,101,2,0,43,43,45,45,5,0,34,34,92,92,110,110,114,
        114,116,116,3,0,10,10,34,34,92,92,2,0,66,66,98,98,1,0,48,49,2,0,
        79,79,111,111,1,0,48,55,2,0,88,88,120,120,3,0,48,57,65,70,97,102,
        1,0,49,57,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,3,
        0,9,9,13,13,32,32,1,1,10,10,515,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,
        0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,
        0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,
        0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,
        0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,
        0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,
        0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,
        0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,
        0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,
        0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,
        0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,
        121,1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,
        0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,0,139,
        1,0,0,0,0,141,1,0,0,0,1,143,1,0,0,0,3,146,1,0,0,0,5,151,1,0,0,0,
        7,155,1,0,0,0,9,162,1,0,0,0,11,167,1,0,0,0,13,172,1,0,0,0,15,179,
        1,0,0,0,17,189,1,0,0,0,19,196,1,0,0,0,21,200,1,0,0,0,23,206,1,0,
        0,0,25,214,1,0,0,0,27,220,1,0,0,0,29,224,1,0,0,0,31,233,1,0,0,0,
        33,239,1,0,0,0,35,245,1,0,0,0,37,249,1,0,0,0,39,254,1,0,0,0,41,260,
        1,0,0,0,43,262,1,0,0,0,45,264,1,0,0,0,47,266,1,0,0,0,49,268,1,0,
        0,0,51,270,1,0,0,0,53,273,1,0,0,0,55,276,1,0,0,0,57,278,1,0,0,0,
        59,281,1,0,0,0,61,283,1,0,0,0,63,286,1,0,0,0,65,289,1,0,0,0,67,292,
        1,0,0,0,69,294,1,0,0,0,71,297,1,0,0,0,73,300,1,0,0,0,75,303,1,0,
        0,0,77,306,1,0,0,0,79,309,1,0,0,0,81,312,1,0,0,0,83,314,1,0,0,0,
        85,316,1,0,0,0,87,318,1,0,0,0,89,320,1,0,0,0,91,322,1,0,0,0,93,324,
        1,0,0,0,95,326,1,0,0,0,97,328,1,0,0,0,99,330,1,0,0,0,101,332,1,0,
        0,0,103,334,1,0,0,0,105,336,1,0,0,0,107,338,1,0,0,0,109,353,1,0,
        0,0,111,368,1,0,0,0,113,370,1,0,0,0,115,384,1,0,0,0,117,386,1,0,
        0,0,119,393,1,0,0,0,121,400,1,0,0,0,123,415,1,0,0,0,125,439,1,0,
        0,0,127,441,1,0,0,0,129,450,1,0,0,0,131,452,1,0,0,0,133,459,1,0,
        0,0,135,463,1,0,0,0,137,469,1,0,0,0,139,481,1,0,0,0,141,493,1,0,
        0,0,143,144,5,105,0,0,144,145,5,102,0,0,145,2,1,0,0,0,146,147,5,
        101,0,0,147,148,5,108,0,0,148,149,5,115,0,0,149,150,5,101,0,0,150,
        4,1,0,0,0,151,152,5,102,0,0,152,153,5,111,0,0,153,154,5,114,0,0,
        154,6,1,0,0,0,155,156,5,114,0,0,156,157,5,101,0,0,157,158,5,116,
        0,0,158,159,5,117,0,0,159,160,5,114,0,0,160,161,5,110,0,0,161,8,
        1,0,0,0,162,163,5,102,0,0,163,164,5,117,0,0,164,165,5,110,0,0,165,
        166,5,99,0,0,166,10,1,0,0,0,167,168,5,116,0,0,168,169,5,121,0,0,
        169,170,5,112,0,0,170,171,5,101,0,0,171,12,1,0,0,0,172,173,5,115,
        0,0,173,174,5,116,0,0,174,175,5,114,0,0,175,176,5,117,0,0,176,177,
        5,99,0,0,177,178,5,116,0,0,178,14,1,0,0,0,179,180,5,105,0,0,180,
        181,5,110,0,0,181,182,5,116,0,0,182,183,5,101,0,0,183,184,5,114,
        0,0,184,185,5,102,0,0,185,186,5,97,0,0,186,187,5,99,0,0,187,188,
        5,101,0,0,188,16,1,0,0,0,189,190,5,115,0,0,190,191,5,116,0,0,191,
        192,5,114,0,0,192,193,5,105,0,0,193,194,5,110,0,0,194,195,5,103,
        0,0,195,18,1,0,0,0,196,197,5,105,0,0,197,198,5,110,0,0,198,199,5,
        116,0,0,199,20,1,0,0,0,200,201,5,102,0,0,201,202,5,108,0,0,202,203,
        5,111,0,0,203,204,5,97,0,0,204,205,5,116,0,0,205,22,1,0,0,0,206,
        207,5,98,0,0,207,208,5,111,0,0,208,209,5,111,0,0,209,210,5,108,0,
        0,210,211,5,101,0,0,211,212,5,97,0,0,212,213,5,110,0,0,213,24,1,
        0,0,0,214,215,5,99,0,0,215,216,5,111,0,0,216,217,5,110,0,0,217,218,
        5,115,0,0,218,219,5,116,0,0,219,26,1,0,0,0,220,221,5,118,0,0,221,
        222,5,97,0,0,222,223,5,114,0,0,223,28,1,0,0,0,224,225,5,99,0,0,225,
        226,5,111,0,0,226,227,5,110,0,0,227,228,5,116,0,0,228,229,5,105,
        0,0,229,230,5,110,0,0,230,231,5,117,0,0,231,232,5,101,0,0,232,30,
        1,0,0,0,233,234,5,98,0,0,234,235,5,114,0,0,235,236,5,101,0,0,236,
        237,5,97,0,0,237,238,5,107,0,0,238,32,1,0,0,0,239,240,5,114,0,0,
        240,241,5,97,0,0,241,242,5,110,0,0,242,243,5,103,0,0,243,244,5,101,
        0,0,244,34,1,0,0,0,245,246,5,110,0,0,246,247,5,105,0,0,247,248,5,
        108,0,0,248,36,1,0,0,0,249,250,5,116,0,0,250,251,5,114,0,0,251,252,
        5,117,0,0,252,253,5,101,0,0,253,38,1,0,0,0,254,255,5,102,0,0,255,
        256,5,97,0,0,256,257,5,108,0,0,257,258,5,115,0,0,258,259,5,101,0,
        0,259,40,1,0,0,0,260,261,5,43,0,0,261,42,1,0,0,0,262,263,5,45,0,
        0,263,44,1,0,0,0,264,265,5,42,0,0,265,46,1,0,0,0,266,267,5,47,0,
        0,267,48,1,0,0,0,268,269,5,37,0,0,269,50,1,0,0,0,270,271,5,61,0,
        0,271,272,5,61,0,0,272,52,1,0,0,0,273,274,5,33,0,0,274,275,5,61,
        0,0,275,54,1,0,0,0,276,277,5,60,0,0,277,56,1,0,0,0,278,279,5,60,
        0,0,279,280,5,61,0,0,280,58,1,0,0,0,281,282,5,62,0,0,282,60,1,0,
        0,0,283,284,5,62,0,0,284,285,5,61,0,0,285,62,1,0,0,0,286,287,5,38,
        0,0,287,288,5,38,0,0,288,64,1,0,0,0,289,290,5,124,0,0,290,291,5,
        124,0,0,291,66,1,0,0,0,292,293,5,33,0,0,293,68,1,0,0,0,294,295,5,
        58,0,0,295,296,5,61,0,0,296,70,1,0,0,0,297,298,5,43,0,0,298,299,
        5,61,0,0,299,72,1,0,0,0,300,301,5,45,0,0,301,302,5,61,0,0,302,74,
        1,0,0,0,303,304,5,42,0,0,304,305,5,61,0,0,305,76,1,0,0,0,306,307,
        5,47,0,0,307,308,5,61,0,0,308,78,1,0,0,0,309,310,5,37,0,0,310,311,
        5,61,0,0,311,80,1,0,0,0,312,313,5,61,0,0,313,82,1,0,0,0,314,315,
        5,46,0,0,315,84,1,0,0,0,316,317,5,91,0,0,317,86,1,0,0,0,318,319,
        5,93,0,0,319,88,1,0,0,0,320,321,5,40,0,0,321,90,1,0,0,0,322,323,
        5,41,0,0,323,92,1,0,0,0,324,325,5,123,0,0,325,94,1,0,0,0,326,327,
        5,125,0,0,327,96,1,0,0,0,328,329,5,44,0,0,329,98,1,0,0,0,330,331,
        5,58,0,0,331,100,1,0,0,0,332,333,5,34,0,0,333,102,1,0,0,0,334,335,
        5,59,0,0,335,104,1,0,0,0,336,337,5,95,0,0,337,106,1,0,0,0,338,339,
        5,47,0,0,339,340,5,47,0,0,340,344,1,0,0,0,341,343,9,0,0,0,342,341,
        1,0,0,0,343,346,1,0,0,0,344,345,1,0,0,0,344,342,1,0,0,0,345,349,
        1,0,0,0,346,344,1,0,0,0,347,350,3,133,66,0,348,350,5,0,0,1,349,347,
        1,0,0,0,349,348,1,0,0,0,350,351,1,0,0,0,351,352,6,53,0,0,352,108,
        1,0,0,0,353,354,5,47,0,0,354,355,5,42,0,0,355,360,1,0,0,0,356,359,
        3,109,54,0,357,359,9,0,0,0,358,356,1,0,0,0,358,357,1,0,0,0,359,362,
        1,0,0,0,360,361,1,0,0,0,360,358,1,0,0,0,361,363,1,0,0,0,362,360,
        1,0,0,0,363,364,5,42,0,0,364,365,5,47,0,0,365,366,1,0,0,0,366,367,
        6,54,0,0,367,110,1,0,0,0,368,369,7,0,0,0,369,112,1,0,0,0,370,372,
        7,1,0,0,371,373,7,2,0,0,372,371,1,0,0,0,372,373,1,0,0,0,373,375,
        1,0,0,0,374,376,3,111,55,0,375,374,1,0,0,0,376,377,1,0,0,0,377,375,
        1,0,0,0,377,378,1,0,0,0,378,114,1,0,0,0,379,380,5,92,0,0,380,385,
        7,3,0,0,381,382,5,39,0,0,382,385,5,34,0,0,383,385,8,4,0,0,384,379,
        1,0,0,0,384,381,1,0,0,0,384,383,1,0,0,0,385,116,1,0,0,0,386,387,
        5,48,0,0,387,389,7,5,0,0,388,390,7,6,0,0,389,388,1,0,0,0,390,391,
        1,0,0,0,391,389,1,0,0,0,391,392,1,0,0,0,392,118,1,0,0,0,393,394,
        5,48,0,0,394,396,7,7,0,0,395,397,7,8,0,0,396,395,1,0,0,0,397,398,
        1,0,0,0,398,396,1,0,0,0,398,399,1,0,0,0,399,120,1,0,0,0,400,401,
        5,48,0,0,401,403,7,9,0,0,402,404,7,10,0,0,403,402,1,0,0,0,404,405,
        1,0,0,0,405,403,1,0,0,0,405,406,1,0,0,0,406,122,1,0,0,0,407,416,
        5,48,0,0,408,412,7,11,0,0,409,411,7,0,0,0,410,409,1,0,0,0,411,414,
        1,0,0,0,412,410,1,0,0,0,412,413,1,0,0,0,413,416,1,0,0,0,414,412,
        1,0,0,0,415,407,1,0,0,0,415,408,1,0,0,0,416,124,1,0,0,0,417,419,
        3,111,55,0,418,417,1,0,0,0,419,420,1,0,0,0,420,418,1,0,0,0,420,421,
        1,0,0,0,421,422,1,0,0,0,422,426,5,46,0,0,423,425,3,111,55,0,424,
        423,1,0,0,0,425,428,1,0,0,0,426,424,1,0,0,0,426,427,1,0,0,0,427,
        430,1,0,0,0,428,426,1,0,0,0,429,431,3,113,56,0,430,429,1,0,0,0,430,
        431,1,0,0,0,431,440,1,0,0,0,432,434,3,111,55,0,433,432,1,0,0,0,434,
        435,1,0,0,0,435,433,1,0,0,0,435,436,1,0,0,0,436,437,1,0,0,0,437,
        438,3,113,56,0,438,440,1,0,0,0,439,418,1,0,0,0,439,433,1,0,0,0,440,
        126,1,0,0,0,441,445,3,101,50,0,442,444,3,115,57,0,443,442,1,0,0,
        0,444,447,1,0,0,0,445,443,1,0,0,0,445,446,1,0,0,0,446,448,1,0,0,
        0,447,445,1,0,0,0,448,449,3,101,50,0,449,128,1,0,0,0,450,451,3,35,
        17,0,451,130,1,0,0,0,452,456,7,12,0,0,453,455,7,13,0,0,454,453,1,
        0,0,0,455,458,1,0,0,0,456,454,1,0,0,0,456,457,1,0,0,0,457,132,1,
        0,0,0,458,456,1,0,0,0,459,460,5,10,0,0,460,461,6,66,1,0,461,134,
        1,0,0,0,462,464,7,14,0,0,463,462,1,0,0,0,464,465,1,0,0,0,465,463,
        1,0,0,0,465,466,1,0,0,0,466,467,1,0,0,0,467,468,6,67,0,0,468,136,
        1,0,0,0,469,473,3,101,50,0,470,472,3,115,57,0,471,470,1,0,0,0,472,
        475,1,0,0,0,473,471,1,0,0,0,473,474,1,0,0,0,474,477,1,0,0,0,475,
        473,1,0,0,0,476,478,7,15,0,0,477,476,1,0,0,0,478,479,1,0,0,0,479,
        480,6,68,2,0,480,138,1,0,0,0,481,485,3,101,50,0,482,484,3,115,57,
        0,483,482,1,0,0,0,484,487,1,0,0,0,485,483,1,0,0,0,485,486,1,0,0,
        0,486,488,1,0,0,0,487,485,1,0,0,0,488,489,5,92,0,0,489,490,8,3,0,
        0,490,491,1,0,0,0,491,492,6,69,3,0,492,140,1,0,0,0,493,494,9,0,0,
        0,494,495,6,70,4,0,495,142,1,0,0,0,24,0,344,349,358,360,372,377,
        384,391,398,405,412,415,420,426,430,435,439,445,456,465,473,477,
        485,5,6,0,0,1,66,0,1,68,1,1,69,2,1,70,3
    ]

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
            "';'", "'_'", "'\\n'" ]

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
        self.checkVersion("4.13.1")
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
     


