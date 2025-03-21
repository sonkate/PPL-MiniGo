# Generated from /home/son/Downloads/PPL/Assignment2/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
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
        4,1,68,623,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,1,0,3,0,122,8,0,1,0,4,0,125,8,0,11,0,12,0,126,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,139,8,1,1,2,1,2,1,2,1,2,3,2,145,8,
        2,1,2,1,2,3,2,149,8,2,1,3,1,3,1,3,3,3,154,8,3,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,3,4,164,8,4,1,4,1,4,3,4,168,8,4,1,4,1,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,3,5,180,8,5,1,5,1,5,3,5,184,8,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,3,6,193,8,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,202,
        8,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,213,8,10,10,10,
        12,10,216,9,10,1,10,1,10,1,10,1,11,1,11,1,11,3,11,224,8,11,1,11,
        1,11,3,11,228,8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,5,12,
        238,8,12,10,12,12,12,241,9,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,
        249,8,13,10,13,12,13,252,9,13,1,14,1,14,1,14,1,14,1,14,1,14,5,14,
        260,8,14,10,14,12,14,263,9,14,1,15,1,15,1,15,1,15,1,15,1,15,5,15,
        271,8,15,10,15,12,15,274,9,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,
        282,8,16,10,16,12,16,285,9,16,1,17,1,17,1,17,3,17,290,8,17,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,300,8,18,3,18,302,8,18,5,
        18,304,8,18,10,18,12,18,307,9,18,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,3,19,316,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,3,20,328,8,20,1,21,1,21,1,21,1,21,3,21,334,8,21,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        3,22,352,8,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,3,24,365,8,24,5,24,367,8,24,10,24,12,24,370,9,24,1,25,1,25,
        1,26,1,26,1,26,1,26,1,26,3,26,379,8,26,1,26,1,26,3,26,383,8,26,1,
        26,1,26,3,26,387,8,26,1,26,3,26,390,8,26,1,27,1,27,1,27,1,27,3,27,
        396,8,27,1,28,1,28,1,28,1,28,1,28,1,28,3,28,404,8,28,1,28,1,28,1,
        29,1,29,1,29,3,29,411,8,29,1,29,3,29,414,8,29,1,29,1,29,1,30,1,30,
        1,30,1,31,1,31,1,31,3,31,424,8,31,1,31,1,31,1,31,1,31,1,31,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,34,1,34,1,34,
        1,35,1,35,1,35,1,35,3,35,449,8,35,1,35,1,35,1,35,1,35,3,35,455,8,
        35,1,35,1,35,1,35,1,36,1,36,1,36,3,36,463,8,36,1,36,1,36,1,37,1,
        37,1,37,3,37,470,8,37,1,38,1,38,1,38,1,38,1,38,5,38,477,8,38,10,
        38,12,38,480,9,38,1,38,1,38,3,38,484,8,38,1,39,1,39,1,39,1,39,1,
        40,1,40,3,40,492,8,40,1,40,1,40,5,40,496,8,40,10,40,12,40,499,9,
        40,1,41,1,41,1,41,1,41,3,41,505,8,41,1,41,1,41,1,42,1,42,1,42,1,
        42,3,42,513,8,42,1,43,1,43,1,43,1,43,1,43,3,43,520,8,43,1,44,1,44,
        1,44,1,44,1,44,1,44,3,44,528,8,44,1,45,1,45,1,46,1,46,1,46,1,46,
        3,46,536,8,46,1,47,1,47,1,47,1,47,1,48,1,48,4,48,544,8,48,11,48,
        12,48,545,3,48,548,8,48,1,49,1,49,1,50,1,50,1,50,1,50,1,50,1,50,
        1,50,1,50,1,50,3,50,561,8,50,1,51,1,51,1,51,1,51,3,51,567,8,51,1,
        51,1,51,1,52,1,52,1,52,1,52,1,52,3,52,576,8,52,1,53,1,53,1,53,1,
        53,1,53,3,53,583,8,53,1,54,1,54,1,54,1,54,1,54,3,54,590,8,54,1,55,
        1,55,1,55,1,55,1,55,1,55,3,55,598,8,55,1,56,1,56,1,56,3,56,603,8,
        56,1,56,1,56,1,57,1,57,1,57,1,57,1,57,3,57,612,8,57,1,58,1,58,1,
        58,1,58,1,59,4,59,619,8,59,11,59,12,59,620,1,59,0,7,24,26,28,30,
        32,36,48,60,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,
        82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,
        0,8,1,0,26,31,1,0,21,22,1,0,23,25,2,0,22,22,34,34,1,0,35,40,2,0,
        53,53,63,63,1,0,9,12,1,0,19,20,664,0,121,1,0,0,0,2,138,1,0,0,0,4,
        140,1,0,0,0,6,150,1,0,0,0,8,159,1,0,0,0,10,171,1,0,0,0,12,192,1,
        0,0,0,14,194,1,0,0,0,16,201,1,0,0,0,18,203,1,0,0,0,20,206,1,0,0,
        0,22,220,1,0,0,0,24,231,1,0,0,0,26,242,1,0,0,0,28,253,1,0,0,0,30,
        264,1,0,0,0,32,275,1,0,0,0,34,289,1,0,0,0,36,291,1,0,0,0,38,315,
        1,0,0,0,40,327,1,0,0,0,42,333,1,0,0,0,44,351,1,0,0,0,46,353,1,0,
        0,0,48,357,1,0,0,0,50,371,1,0,0,0,52,373,1,0,0,0,54,395,1,0,0,0,
        56,397,1,0,0,0,58,410,1,0,0,0,60,417,1,0,0,0,62,420,1,0,0,0,64,430,
        1,0,0,0,66,438,1,0,0,0,68,441,1,0,0,0,70,448,1,0,0,0,72,459,1,0,
        0,0,74,466,1,0,0,0,76,471,1,0,0,0,78,485,1,0,0,0,80,489,1,0,0,0,
        82,500,1,0,0,0,84,512,1,0,0,0,86,519,1,0,0,0,88,527,1,0,0,0,90,529,
        1,0,0,0,92,535,1,0,0,0,94,537,1,0,0,0,96,547,1,0,0,0,98,549,1,0,
        0,0,100,560,1,0,0,0,102,562,1,0,0,0,104,575,1,0,0,0,106,582,1,0,
        0,0,108,589,1,0,0,0,110,597,1,0,0,0,112,599,1,0,0,0,114,611,1,0,
        0,0,116,613,1,0,0,0,118,618,1,0,0,0,120,122,3,118,59,0,121,120,1,
        0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,125,3,2,1,0,124,123,1,
        0,0,0,125,126,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,128,1,
        0,0,0,128,129,5,0,0,1,129,1,1,0,0,0,130,131,3,4,2,0,131,132,3,96,
        48,0,132,139,1,0,0,0,133,139,3,6,3,0,134,139,3,8,4,0,135,139,3,10,
        5,0,136,139,3,18,9,0,137,139,3,20,10,0,138,130,1,0,0,0,138,133,1,
        0,0,0,138,134,1,0,0,0,138,135,1,0,0,0,138,136,1,0,0,0,138,137,1,
        0,0,0,139,3,1,0,0,0,140,141,5,14,0,0,141,148,5,63,0,0,142,149,3,
        88,44,0,143,145,3,88,44,0,144,143,1,0,0,0,144,145,1,0,0,0,145,146,
        1,0,0,0,146,147,5,41,0,0,147,149,3,24,12,0,148,142,1,0,0,0,148,144,
        1,0,0,0,149,5,1,0,0,0,150,151,5,13,0,0,151,153,5,63,0,0,152,154,
        3,88,44,0,153,152,1,0,0,0,153,154,1,0,0,0,154,155,1,0,0,0,155,156,
        5,41,0,0,156,157,3,24,12,0,157,158,3,96,48,0,158,7,1,0,0,0,159,160,
        5,5,0,0,160,161,5,63,0,0,161,163,5,45,0,0,162,164,3,12,6,0,163,162,
        1,0,0,0,163,164,1,0,0,0,164,165,1,0,0,0,165,167,5,46,0,0,166,168,
        3,88,44,0,167,166,1,0,0,0,167,168,1,0,0,0,168,169,1,0,0,0,169,170,
        3,80,40,0,170,9,1,0,0,0,171,172,5,5,0,0,172,173,5,45,0,0,173,174,
        5,63,0,0,174,175,5,63,0,0,175,176,5,46,0,0,176,177,5,63,0,0,177,
        179,5,45,0,0,178,180,3,12,6,0,179,178,1,0,0,0,179,180,1,0,0,0,180,
        181,1,0,0,0,181,183,5,46,0,0,182,184,3,88,44,0,183,182,1,0,0,0,183,
        184,1,0,0,0,184,185,1,0,0,0,185,186,3,80,40,0,186,11,1,0,0,0,187,
        188,3,14,7,0,188,189,5,49,0,0,189,190,3,12,6,0,190,193,1,0,0,0,191,
        193,3,14,7,0,192,187,1,0,0,0,192,191,1,0,0,0,193,13,1,0,0,0,194,
        195,3,16,8,0,195,196,3,88,44,0,196,15,1,0,0,0,197,198,5,63,0,0,198,
        199,5,49,0,0,199,202,3,16,8,0,200,202,5,63,0,0,201,197,1,0,0,0,201,
        200,1,0,0,0,202,17,1,0,0,0,203,204,5,6,0,0,204,205,3,76,38,0,205,
        19,1,0,0,0,206,207,5,6,0,0,207,208,5,63,0,0,208,209,5,8,0,0,209,
        214,5,47,0,0,210,213,5,64,0,0,211,213,3,22,11,0,212,210,1,0,0,0,
        212,211,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,214,215,1,0,0,0,
        215,217,1,0,0,0,216,214,1,0,0,0,217,218,5,48,0,0,218,219,3,96,48,
        0,219,21,1,0,0,0,220,221,5,63,0,0,221,223,5,45,0,0,222,224,3,12,
        6,0,223,222,1,0,0,0,223,224,1,0,0,0,224,225,1,0,0,0,225,227,5,46,
        0,0,226,228,3,88,44,0,227,226,1,0,0,0,227,228,1,0,0,0,228,229,1,
        0,0,0,229,230,3,96,48,0,230,23,1,0,0,0,231,232,6,12,-1,0,232,233,
        3,26,13,0,233,239,1,0,0,0,234,235,10,2,0,0,235,236,5,33,0,0,236,
        238,3,26,13,0,237,234,1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,
        240,1,0,0,0,240,25,1,0,0,0,241,239,1,0,0,0,242,243,6,13,-1,0,243,
        244,3,28,14,0,244,250,1,0,0,0,245,246,10,2,0,0,246,247,5,32,0,0,
        247,249,3,28,14,0,248,245,1,0,0,0,249,252,1,0,0,0,250,248,1,0,0,
        0,250,251,1,0,0,0,251,27,1,0,0,0,252,250,1,0,0,0,253,254,6,14,-1,
        0,254,255,3,30,15,0,255,261,1,0,0,0,256,257,10,2,0,0,257,258,7,0,
        0,0,258,260,3,30,15,0,259,256,1,0,0,0,260,263,1,0,0,0,261,259,1,
        0,0,0,261,262,1,0,0,0,262,29,1,0,0,0,263,261,1,0,0,0,264,265,6,15,
        -1,0,265,266,3,32,16,0,266,272,1,0,0,0,267,268,10,2,0,0,268,269,
        7,1,0,0,269,271,3,32,16,0,270,267,1,0,0,0,271,274,1,0,0,0,272,270,
        1,0,0,0,272,273,1,0,0,0,273,31,1,0,0,0,274,272,1,0,0,0,275,276,6,
        16,-1,0,276,277,3,34,17,0,277,283,1,0,0,0,278,279,10,2,0,0,279,280,
        7,2,0,0,280,282,3,34,17,0,281,278,1,0,0,0,282,285,1,0,0,0,283,281,
        1,0,0,0,283,284,1,0,0,0,284,33,1,0,0,0,285,283,1,0,0,0,286,287,7,
        3,0,0,287,290,3,34,17,0,288,290,3,36,18,0,289,286,1,0,0,0,289,288,
        1,0,0,0,290,35,1,0,0,0,291,292,6,18,-1,0,292,293,3,38,19,0,293,305,
        1,0,0,0,294,301,10,2,0,0,295,302,3,92,46,0,296,299,5,42,0,0,297,
        300,5,63,0,0,298,300,3,82,41,0,299,297,1,0,0,0,299,298,1,0,0,0,300,
        302,1,0,0,0,301,295,1,0,0,0,301,296,1,0,0,0,302,304,1,0,0,0,303,
        294,1,0,0,0,304,307,1,0,0,0,305,303,1,0,0,0,305,306,1,0,0,0,306,
        37,1,0,0,0,307,305,1,0,0,0,308,316,3,40,20,0,309,310,5,45,0,0,310,
        311,3,24,12,0,311,312,5,46,0,0,312,316,1,0,0,0,313,316,5,63,0,0,
        314,316,3,82,41,0,315,308,1,0,0,0,315,309,1,0,0,0,315,313,1,0,0,
        0,315,314,1,0,0,0,316,39,1,0,0,0,317,328,5,59,0,0,318,328,5,56,0,
        0,319,328,5,57,0,0,320,328,5,58,0,0,321,328,5,60,0,0,322,328,5,61,
        0,0,323,328,3,98,49,0,324,328,5,18,0,0,325,328,3,102,51,0,326,328,
        3,112,56,0,327,317,1,0,0,0,327,318,1,0,0,0,327,319,1,0,0,0,327,320,
        1,0,0,0,327,321,1,0,0,0,327,322,1,0,0,0,327,323,1,0,0,0,327,324,
        1,0,0,0,327,325,1,0,0,0,327,326,1,0,0,0,328,41,1,0,0,0,329,330,3,
        44,22,0,330,331,3,42,21,0,331,334,1,0,0,0,332,334,3,44,22,0,333,
        329,1,0,0,0,333,332,1,0,0,0,334,43,1,0,0,0,335,336,3,4,2,0,336,337,
        3,96,48,0,337,352,1,0,0,0,338,352,3,6,3,0,339,352,3,18,9,0,340,352,
        3,10,5,0,341,342,3,46,23,0,342,343,3,96,48,0,343,352,1,0,0,0,344,
        352,3,52,26,0,345,352,3,58,29,0,346,352,3,66,33,0,347,352,3,68,34,
        0,348,352,3,70,35,0,349,352,3,72,36,0,350,352,3,80,40,0,351,335,
        1,0,0,0,351,338,1,0,0,0,351,339,1,0,0,0,351,340,1,0,0,0,351,341,
        1,0,0,0,351,344,1,0,0,0,351,345,1,0,0,0,351,346,1,0,0,0,351,347,
        1,0,0,0,351,348,1,0,0,0,351,349,1,0,0,0,351,350,1,0,0,0,352,45,1,
        0,0,0,353,354,3,48,24,0,354,355,3,50,25,0,355,356,3,24,12,0,356,
        47,1,0,0,0,357,358,6,24,-1,0,358,359,5,63,0,0,359,368,1,0,0,0,360,
        364,10,2,0,0,361,365,3,92,46,0,362,363,5,42,0,0,363,365,5,63,0,0,
        364,361,1,0,0,0,364,362,1,0,0,0,365,367,1,0,0,0,366,360,1,0,0,0,
        367,370,1,0,0,0,368,366,1,0,0,0,368,369,1,0,0,0,369,49,1,0,0,0,370,
        368,1,0,0,0,371,372,7,4,0,0,372,51,1,0,0,0,373,374,5,1,0,0,374,375,
        5,45,0,0,375,376,3,24,12,0,376,378,5,46,0,0,377,379,3,118,59,0,378,
        377,1,0,0,0,378,379,1,0,0,0,379,380,1,0,0,0,380,382,3,80,40,0,381,
        383,3,54,27,0,382,381,1,0,0,0,382,383,1,0,0,0,383,389,1,0,0,0,384,
        386,5,2,0,0,385,387,3,118,59,0,386,385,1,0,0,0,386,387,1,0,0,0,387,
        388,1,0,0,0,388,390,3,80,40,0,389,384,1,0,0,0,389,390,1,0,0,0,390,
        53,1,0,0,0,391,392,3,56,28,0,392,393,3,54,27,0,393,396,1,0,0,0,394,
        396,3,56,28,0,395,391,1,0,0,0,395,394,1,0,0,0,396,55,1,0,0,0,397,
        398,5,2,0,0,398,399,5,1,0,0,399,400,5,45,0,0,400,401,3,24,12,0,401,
        403,5,46,0,0,402,404,3,118,59,0,403,402,1,0,0,0,403,404,1,0,0,0,
        404,405,1,0,0,0,405,406,3,80,40,0,406,57,1,0,0,0,407,411,3,60,30,
        0,408,411,3,62,31,0,409,411,3,64,32,0,410,407,1,0,0,0,410,408,1,
        0,0,0,410,409,1,0,0,0,411,413,1,0,0,0,412,414,3,118,59,0,413,412,
        1,0,0,0,413,414,1,0,0,0,414,415,1,0,0,0,415,416,3,80,40,0,416,59,
        1,0,0,0,417,418,5,3,0,0,418,419,3,24,12,0,419,61,1,0,0,0,420,423,
        5,3,0,0,421,424,3,46,23,0,422,424,3,4,2,0,423,421,1,0,0,0,423,422,
        1,0,0,0,424,425,1,0,0,0,425,426,5,52,0,0,426,427,3,24,12,0,427,428,
        5,52,0,0,428,429,3,46,23,0,429,63,1,0,0,0,430,431,5,3,0,0,431,432,
        7,5,0,0,432,433,5,49,0,0,433,434,5,63,0,0,434,435,5,35,0,0,435,436,
        5,17,0,0,436,437,3,24,12,0,437,65,1,0,0,0,438,439,5,16,0,0,439,440,
        3,96,48,0,440,67,1,0,0,0,441,442,5,15,0,0,442,443,3,96,48,0,443,
        69,1,0,0,0,444,445,3,48,24,0,445,446,5,42,0,0,446,449,1,0,0,0,447,
        449,1,0,0,0,448,444,1,0,0,0,448,447,1,0,0,0,449,450,1,0,0,0,450,
        451,5,63,0,0,451,454,5,45,0,0,452,455,3,84,42,0,453,455,1,0,0,0,
        454,452,1,0,0,0,454,453,1,0,0,0,455,456,1,0,0,0,456,457,5,46,0,0,
        457,458,3,96,48,0,458,71,1,0,0,0,459,462,5,4,0,0,460,463,3,24,12,
        0,461,463,1,0,0,0,462,460,1,0,0,0,462,461,1,0,0,0,463,464,1,0,0,
        0,464,465,3,96,48,0,465,73,1,0,0,0,466,469,3,92,46,0,467,470,3,90,
        45,0,468,470,5,63,0,0,469,467,1,0,0,0,469,468,1,0,0,0,470,75,1,0,
        0,0,471,472,5,63,0,0,472,473,5,7,0,0,473,478,5,47,0,0,474,477,5,
        64,0,0,475,477,3,78,39,0,476,474,1,0,0,0,476,475,1,0,0,0,477,480,
        1,0,0,0,478,476,1,0,0,0,478,479,1,0,0,0,479,481,1,0,0,0,480,478,
        1,0,0,0,481,483,5,48,0,0,482,484,3,96,48,0,483,482,1,0,0,0,483,484,
        1,0,0,0,484,77,1,0,0,0,485,486,5,63,0,0,486,487,3,88,44,0,487,488,
        3,96,48,0,488,79,1,0,0,0,489,491,5,47,0,0,490,492,3,42,21,0,491,
        490,1,0,0,0,491,492,1,0,0,0,492,493,1,0,0,0,493,497,5,48,0,0,494,
        496,3,96,48,0,495,494,1,0,0,0,496,499,1,0,0,0,497,495,1,0,0,0,497,
        498,1,0,0,0,498,81,1,0,0,0,499,497,1,0,0,0,500,501,5,63,0,0,501,
        504,5,45,0,0,502,505,3,84,42,0,503,505,1,0,0,0,504,502,1,0,0,0,504,
        503,1,0,0,0,505,506,1,0,0,0,506,507,5,46,0,0,507,83,1,0,0,0,508,
        509,3,24,12,0,509,510,3,86,43,0,510,513,1,0,0,0,511,513,3,24,12,
        0,512,508,1,0,0,0,512,511,1,0,0,0,513,85,1,0,0,0,514,515,5,49,0,
        0,515,516,3,24,12,0,516,517,3,86,43,0,517,520,1,0,0,0,518,520,1,
        0,0,0,519,514,1,0,0,0,519,518,1,0,0,0,520,87,1,0,0,0,521,528,5,10,
        0,0,522,528,5,11,0,0,523,528,5,12,0,0,524,528,5,9,0,0,525,528,3,
        74,37,0,526,528,5,63,0,0,527,521,1,0,0,0,527,522,1,0,0,0,527,523,
        1,0,0,0,527,524,1,0,0,0,527,525,1,0,0,0,527,526,1,0,0,0,528,89,1,
        0,0,0,529,530,7,6,0,0,530,91,1,0,0,0,531,532,3,94,47,0,532,533,3,
        92,46,0,533,536,1,0,0,0,534,536,3,94,47,0,535,531,1,0,0,0,535,534,
        1,0,0,0,536,93,1,0,0,0,537,538,5,43,0,0,538,539,3,24,12,0,539,540,
        5,44,0,0,540,95,1,0,0,0,541,548,5,52,0,0,542,544,5,64,0,0,543,542,
        1,0,0,0,544,545,1,0,0,0,545,543,1,0,0,0,545,546,1,0,0,0,546,548,
        1,0,0,0,547,541,1,0,0,0,547,543,1,0,0,0,548,97,1,0,0,0,549,550,7,
        7,0,0,550,99,1,0,0,0,551,561,5,59,0,0,552,561,5,56,0,0,553,561,5,
        57,0,0,554,561,5,58,0,0,555,561,5,60,0,0,556,561,5,61,0,0,557,561,
        3,98,49,0,558,561,5,18,0,0,559,561,3,112,56,0,560,551,1,0,0,0,560,
        552,1,0,0,0,560,553,1,0,0,0,560,554,1,0,0,0,560,555,1,0,0,0,560,
        556,1,0,0,0,560,557,1,0,0,0,560,558,1,0,0,0,560,559,1,0,0,0,561,
        101,1,0,0,0,562,563,3,92,46,0,563,564,3,88,44,0,564,566,5,47,0,0,
        565,567,3,104,52,0,566,565,1,0,0,0,566,567,1,0,0,0,567,568,1,0,0,
        0,568,569,5,48,0,0,569,103,1,0,0,0,570,571,3,106,53,0,571,572,5,
        49,0,0,572,573,3,104,52,0,573,576,1,0,0,0,574,576,3,106,53,0,575,
        570,1,0,0,0,575,574,1,0,0,0,576,105,1,0,0,0,577,583,3,108,54,0,578,
        579,5,47,0,0,579,580,3,106,53,0,580,581,5,48,0,0,581,583,1,0,0,0,
        582,577,1,0,0,0,582,578,1,0,0,0,583,107,1,0,0,0,584,585,3,110,55,
        0,585,586,5,49,0,0,586,587,3,108,54,0,587,590,1,0,0,0,588,590,3,
        110,55,0,589,584,1,0,0,0,589,588,1,0,0,0,590,109,1,0,0,0,591,598,
        3,100,50,0,592,598,3,24,12,0,593,594,5,47,0,0,594,595,3,106,53,0,
        595,596,5,48,0,0,596,598,1,0,0,0,597,591,1,0,0,0,597,592,1,0,0,0,
        597,593,1,0,0,0,598,111,1,0,0,0,599,600,5,63,0,0,600,602,5,47,0,
        0,601,603,3,114,57,0,602,601,1,0,0,0,602,603,1,0,0,0,603,604,1,0,
        0,0,604,605,5,48,0,0,605,113,1,0,0,0,606,607,3,116,58,0,607,608,
        5,49,0,0,608,609,3,114,57,0,609,612,1,0,0,0,610,612,3,116,58,0,611,
        606,1,0,0,0,611,610,1,0,0,0,612,115,1,0,0,0,613,614,5,63,0,0,614,
        615,5,50,0,0,615,616,3,24,12,0,616,117,1,0,0,0,617,619,5,64,0,0,
        618,617,1,0,0,0,619,620,1,0,0,0,620,618,1,0,0,0,620,621,1,0,0,0,
        621,119,1,0,0,0,65,121,126,138,144,148,153,163,167,179,183,192,201,
        212,214,223,227,239,250,261,272,283,289,299,301,305,315,327,333,
        351,364,368,378,382,386,389,395,403,410,413,423,448,454,462,469,
        476,478,483,491,497,504,512,519,527,535,545,547,560,566,575,582,
        589,597,602,611,620
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
    RULE_break_stmt = 33
    RULE_continue_stmt = 34
    RULE_call_stmt = 35
    RULE_return_stmt = 36
    RULE_array_type = 37
    RULE_struct_type = 38
    RULE_struct_field = 39
    RULE_body = 40
    RULE_func_call = 41
    RULE_expr_list = 42
    RULE_expr_tail = 43
    RULE_all_type = 44
    RULE_prim_types = 45
    RULE_list_array_index = 46
    RULE_array_index = 47
    RULE_sm_nl = 48
    RULE_boollit = 49
    RULE_array_item = 50
    RULE_arraylit = 51
    RULE_list_array_element = 52
    RULE_array_element = 53
    RULE_itemlist = 54
    RULE_item = 55
    RULE_structlit = 56
    RULE_list_struct_element = 57
    RULE_structlit_element = 58
    RULE_list_newline = 59

    ruleNames =  [ "program", "decl", "var_decl", "const_decl", "func_decl", 
                   "method_decl", "parameter_list", "parameter", "list_ID", 
                   "struct_decl", "interface_decl", "interface_method", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "factor", "literal", "stmt_list", "statement", 
                   "assign_stmt", "assignment_lhs", "assign_op", "if_stmt", 
                   "list_elif", "elif_one", "for_stmt", "basic_for", "init_for", 
                   "range_for", "break_stmt", "continue_stmt", "call_stmt", 
                   "return_stmt", "array_type", "struct_type", "struct_field", 
                   "body", "func_call", "expr_list", "expr_tail", "all_type", 
                   "prim_types", "list_array_index", "array_index", "sm_nl", 
                   "boollit", "array_item", "arraylit", "list_array_element", 
                   "array_element", "itemlist", "item", "structlit", "list_struct_element", 
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
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 120
                self.list_newline()


            self.state = 124 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 123
                self.decl()
                self.state = 126 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 24672) != 0)):
                    break

            self.state = 128
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
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 130
                self.var_decl()
                self.state = 131
                self.sm_nl()
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
            self.state = 140
            self.match(MiniGoParser.VAR)
            self.state = 141
            self.match(MiniGoParser.ID)
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 142
                self.all_type()
                pass

            elif la_ == 2:
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223363240761745920) != 0):
                    self.state = 143
                    self.all_type()


                self.state = 146
                self.match(MiniGoParser.EQ)
                self.state = 147
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
            self.state = 150
            self.match(MiniGoParser.CONST)
            self.state = 151
            self.match(MiniGoParser.ID)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223363240761745920) != 0):
                self.state = 152
                self.all_type()


            self.state = 155
            self.match(MiniGoParser.EQ)
            self.state = 156
            self.expr(0)
            self.state = 157
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
            self.state = 159
            self.match(MiniGoParser.FUNC)
            self.state = 160
            self.match(MiniGoParser.ID)
            self.state = 161
            self.match(MiniGoParser.LRB)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==63:
                self.state = 162
                self.parameter_list()


            self.state = 165
            self.match(MiniGoParser.RRB)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223363240761745920) != 0):
                self.state = 166
                self.all_type()


            self.state = 169
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
            self.state = 171
            self.match(MiniGoParser.FUNC)
            self.state = 172
            self.match(MiniGoParser.LRB)
            self.state = 173
            self.match(MiniGoParser.ID)
            self.state = 174
            self.match(MiniGoParser.ID)
            self.state = 175
            self.match(MiniGoParser.RRB)
            self.state = 176
            self.match(MiniGoParser.ID)
            self.state = 177
            self.match(MiniGoParser.LRB)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==63:
                self.state = 178
                self.parameter_list()


            self.state = 181
            self.match(MiniGoParser.RRB)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223363240761745920) != 0):
                self.state = 182
                self.all_type()


            self.state = 185
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
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.parameter()
                self.state = 188
                self.match(MiniGoParser.CM)
                self.state = 189
                self.parameter_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
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
            self.state = 194
            self.list_ID()
            self.state = 195
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
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(MiniGoParser.ID)
                self.state = 198
                self.match(MiniGoParser.CM)
                self.state = 199
                self.list_ID()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
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
            self.state = 203
            self.match(MiniGoParser.TYPE)
            self.state = 204
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
            self.state = 206
            self.match(MiniGoParser.TYPE)
            self.state = 207
            self.match(MiniGoParser.ID)
            self.state = 208
            self.match(MiniGoParser.INTERFACE)
            self.state = 209
            self.match(MiniGoParser.LCB)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==63 or _la==64:
                self.state = 212
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [64]:
                    self.state = 210
                    self.match(MiniGoParser.NL)
                    pass
                elif token in [63]:
                    self.state = 211
                    self.interface_method()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 217
            self.match(MiniGoParser.RCB)
            self.state = 218
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
            self.state = 220
            self.match(MiniGoParser.ID)
            self.state = 221
            self.match(MiniGoParser.LRB)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==63:
                self.state = 222
                self.parameter_list()


            self.state = 225
            self.match(MiniGoParser.RRB)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223363240761745920) != 0):
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0)):
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
                    if not(_la==21 or _la==22):
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
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




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                _la = self._input.LA(1)
                if not(_la==22 or _la==34):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 287
                self.expr5()
                pass
            elif token in [18, 19, 20, 43, 45, 56, 57, 58, 59, 60, 61, 63]:
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
            self.state = 292
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 305
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
                    self.state = 301
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [43]:
                        self.state = 295
                        self.list_array_index()
                        pass
                    elif token in [42]:
                        self.state = 296
                        self.match(MiniGoParser.DOT_OP)
                        self.state = 299
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                        if la_ == 1:
                            self.state = 297
                            self.match(MiniGoParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 298
                            self.func_call()
                            pass


                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 307
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
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.match(MiniGoParser.LRB)
                self.state = 310
                self.expr(0)
                self.state = 311
                self.match(MiniGoParser.RRB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 313
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 314
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
            self.state = 327
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(MiniGoParser.INTLIT)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.match(MiniGoParser.BINLIT)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 3)
                self.state = 319
                self.match(MiniGoParser.OCTLIT)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 4)
                self.state = 320
                self.match(MiniGoParser.HEXLIT)
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 5)
                self.state = 321
                self.match(MiniGoParser.FLOATLIT)
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 6)
                self.state = 322
                self.match(MiniGoParser.STRINGLIT)
                pass
            elif token in [19, 20]:
                self.enterOuterAlt(localctx, 7)
                self.state = 323
                self.boollit()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 8)
                self.state = 324
                self.match(MiniGoParser.NIL)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 9)
                self.state = 325
                self.arraylit()
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 10)
                self.state = 326
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
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.statement()
                self.state = 330
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
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
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 335
                self.var_decl()
                self.state = 336
                self.sm_nl()
                pass

            elif la_ == 2:
                self.state = 338
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 339
                self.struct_decl()
                pass

            elif la_ == 4:
                self.state = 340
                self.method_decl()
                pass

            elif la_ == 5:
                self.state = 341
                self.assign_stmt()
                self.state = 342
                self.sm_nl()
                pass

            elif la_ == 6:
                self.state = 344
                self.if_stmt()
                pass

            elif la_ == 7:
                self.state = 345
                self.for_stmt()
                pass

            elif la_ == 8:
                self.state = 346
                self.break_stmt()
                pass

            elif la_ == 9:
                self.state = 347
                self.continue_stmt()
                pass

            elif la_ == 10:
                self.state = 348
                self.call_stmt()
                pass

            elif la_ == 11:
                self.state = 349
                self.return_stmt()
                pass

            elif la_ == 12:
                self.state = 350
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
            self.state = 353
            self.assignment_lhs(0)
            self.state = 354
            self.assign_op()
            self.state = 355
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
            self.state = 358
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Assignment_lhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignment_lhs)
                    self.state = 360
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 364
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [43]:
                        self.state = 361
                        self.list_array_index()
                        pass
                    elif token in [42]:
                        self.state = 362
                        self.match(MiniGoParser.DOT_OP)
                        self.state = 363
                        self.match(MiniGoParser.ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 370
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
            self.state = 371
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
            self.state = 373
            self.match(MiniGoParser.IF)
            self.state = 374
            self.match(MiniGoParser.LRB)
            self.state = 375
            self.expr(0)
            self.state = 376
            self.match(MiniGoParser.RRB)
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 377
                self.list_newline()


            self.state = 380
            self.body()
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 381
                self.list_elif()


            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 384
                self.match(MiniGoParser.ELSE)
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==64:
                    self.state = 385
                    self.list_newline()


                self.state = 388
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
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.elif_one()
                self.state = 392
                self.list_elif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
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
            self.state = 397
            self.match(MiniGoParser.ELSE)
            self.state = 398
            self.match(MiniGoParser.IF)
            self.state = 399
            self.match(MiniGoParser.LRB)
            self.state = 400
            self.expr(0)
            self.state = 401
            self.match(MiniGoParser.RRB)
            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 402
                self.list_newline()


            self.state = 405
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
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 407
                self.basic_for()
                pass

            elif la_ == 2:
                self.state = 408
                self.init_for()
                pass

            elif la_ == 3:
                self.state = 409
                self.range_for()
                pass


            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 412
                self.list_newline()


            self.state = 415
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
            self.state = 417
            self.match(MiniGoParser.FOR)
            self.state = 418
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
            self.state = 420
            self.match(MiniGoParser.FOR)
            self.state = 423
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [63]:
                self.state = 421
                self.assign_stmt()
                pass
            elif token in [14]:
                self.state = 422
                self.var_decl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 425
            self.match(MiniGoParser.SM)
            self.state = 426
            self.expr(0)
            self.state = 427
            self.match(MiniGoParser.SM)
            self.state = 428
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

        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def EQ_ASSIGN_OP(self):
            return self.getToken(MiniGoParser.EQ_ASSIGN_OP, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def UNDERSCORE(self):
            return self.getToken(MiniGoParser.UNDERSCORE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_range_for




    def range_for(self):

        localctx = MiniGoParser.Range_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_range_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(MiniGoParser.FOR)
            self.state = 431
            _la = self._input.LA(1)
            if not(_la==53 or _la==63):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 432
            self.match(MiniGoParser.CM)
            self.state = 433
            self.match(MiniGoParser.ID)
            self.state = 434
            self.match(MiniGoParser.EQ_ASSIGN_OP)
            self.state = 435
            self.match(MiniGoParser.RANGE)
            self.state = 436
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

        def sm_nl(self):
            return self.getTypedRuleContext(MiniGoParser.Sm_nlContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(MiniGoParser.BREAK)
            self.state = 439
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
        self.enterRule(localctx, 68, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(MiniGoParser.CONTINUE)
            self.state = 442
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
        self.enterRule(localctx, 70, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 444
                self.assignment_lhs(0)
                self.state = 445
                self.match(MiniGoParser.DOT_OP)
                pass

            elif la_ == 2:
                pass


            self.state = 450
            self.match(MiniGoParser.ID)
            self.state = 451
            self.match(MiniGoParser.LRB)
            self.state = 454
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 22, 34, 43, 45, 56, 57, 58, 59, 60, 61, 63]:
                self.state = 452
                self.expr_list()
                pass
            elif token in [46]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 456
            self.match(MiniGoParser.RRB)
            self.state = 457
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
        self.enterRule(localctx, 72, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(MiniGoParser.RETURN)
            self.state = 462
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 22, 34, 43, 45, 56, 57, 58, 59, 60, 61, 63]:
                self.state = 460
                self.expr(0)
                pass
            elif token in [52, 64]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 464
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
        self.enterRule(localctx, 74, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.list_array_index()
            self.state = 469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12]:
                self.state = 467
                self.prim_types()
                pass
            elif token in [63]:
                self.state = 468
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
        self.enterRule(localctx, 76, self.RULE_struct_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(MiniGoParser.ID)
            self.state = 472
            self.match(MiniGoParser.STRUCT)
            self.state = 473
            self.match(MiniGoParser.LCB)
            self.state = 478
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==63 or _la==64:
                self.state = 476
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [64]:
                    self.state = 474
                    self.match(MiniGoParser.NL)
                    pass
                elif token in [63]:
                    self.state = 475
                    self.struct_field()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 480
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 481
            self.match(MiniGoParser.RCB)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52 or _la==64:
                self.state = 482
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
        self.enterRule(localctx, 78, self.RULE_struct_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(MiniGoParser.ID)
            self.state = 486
            self.all_type()
            self.state = 487
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
        self.enterRule(localctx, 80, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(MiniGoParser.LCB)
            self.state = 491
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223231299366297478) != 0):
                self.state = 490
                self.stmt_list()


            self.state = 493
            self.match(MiniGoParser.RCB)
            self.state = 497
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52 or _la==64:
                self.state = 494
                self.sm_nl()
                self.state = 499
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
        self.enterRule(localctx, 82, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(MiniGoParser.ID)
            self.state = 501
            self.match(MiniGoParser.LRB)
            self.state = 504
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 22, 34, 43, 45, 56, 57, 58, 59, 60, 61, 63]:
                self.state = 502
                self.expr_list()
                pass
            elif token in [46]:
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




    def expr_list(self):

        localctx = MiniGoParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr_list)
        try:
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
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




    def expr_tail(self):

        localctx = MiniGoParser.Expr_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr_tail)
        try:
            self.state = 519
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.match(MiniGoParser.CM)
                self.state = 515
                self.expr(0)
                self.state = 516
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
        self.enterRule(localctx, 88, self.RULE_all_type)
        try:
            self.state = 527
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.match(MiniGoParser.INT)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 523
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 524
                self.match(MiniGoParser.STRING)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 5)
                self.state = 525
                self.array_type()
                pass
            elif token in [63]:
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




    def prim_types(self):

        localctx = MiniGoParser.Prim_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_prim_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
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
        self.enterRule(localctx, 92, self.RULE_list_array_index)
        try:
            self.state = 535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_index




    def array_index(self):

        localctx = MiniGoParser.Array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_array_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(MiniGoParser.LSB)
            self.state = 538
            self.expr(0)
            self.state = 539
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
        self.enterRule(localctx, 96, self.RULE_sm_nl)
        try:
            self.state = 547
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 541
                self.match(MiniGoParser.SM)
                pass
            elif token in [64]:
                self.enterOuterAlt(localctx, 2)
                self.state = 543 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 542
                        self.match(MiniGoParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 545 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

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
        self.enterRule(localctx, 98, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
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
        self.enterRule(localctx, 100, self.RULE_array_item)
        try:
            self.state = 560
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.match(MiniGoParser.INTLIT)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.match(MiniGoParser.BINLIT)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 3)
                self.state = 553
                self.match(MiniGoParser.OCTLIT)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 4)
                self.state = 554
                self.match(MiniGoParser.HEXLIT)
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 5)
                self.state = 555
                self.match(MiniGoParser.FLOATLIT)
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 6)
                self.state = 556
                self.match(MiniGoParser.STRINGLIT)
                pass
            elif token in [19, 20]:
                self.enterOuterAlt(localctx, 7)
                self.state = 557
                self.boollit()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 8)
                self.state = 558
                self.match(MiniGoParser.NIL)
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 9)
                self.state = 559
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
        self.enterRule(localctx, 102, self.RULE_arraylit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.list_array_index()
            self.state = 563
            self.all_type()
            self.state = 564
            self.match(MiniGoParser.LCB)
            self.state = 566
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -4683558877325950976) != 0):
                self.state = 565
                self.list_array_element()


            self.state = 568
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
        self.enterRule(localctx, 104, self.RULE_list_array_element)
        try:
            self.state = 575
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 570
                self.array_element()
                self.state = 571
                self.match(MiniGoParser.CM)
                self.state = 572
                self.list_array_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 574
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
        self.enterRule(localctx, 106, self.RULE_array_element)
        try:
            self.state = 582
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 577
                self.itemlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 578
                self.match(MiniGoParser.LCB)
                self.state = 579
                self.array_element()
                self.state = 580
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
        self.enterRule(localctx, 108, self.RULE_itemlist)
        try:
            self.state = 589
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 584
                self.item()
                self.state = 585
                self.match(MiniGoParser.CM)
                self.state = 586
                self.itemlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 588
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
        self.enterRule(localctx, 110, self.RULE_item)
        try:
            self.state = 597
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 591
                self.array_item()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 592
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 593
                self.match(MiniGoParser.LCB)
                self.state = 594
                self.array_element()
                self.state = 595
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
        self.enterRule(localctx, 112, self.RULE_structlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self.match(MiniGoParser.ID)
            self.state = 600
            self.match(MiniGoParser.LCB)
            self.state = 602
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==63:
                self.state = 601
                self.list_struct_element()


            self.state = 604
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
        self.enterRule(localctx, 114, self.RULE_list_struct_element)
        try:
            self.state = 611
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 606
                self.structlit_element()
                self.state = 607
                self.match(MiniGoParser.CM)
                self.state = 608
                self.list_struct_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 610
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
        self.enterRule(localctx, 116, self.RULE_structlit_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 613
            self.match(MiniGoParser.ID)
            self.state = 614
            self.match(MiniGoParser.COL)
            self.state = 615
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
        self.enterRule(localctx, 118, self.RULE_list_newline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 618 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 617
                self.match(MiniGoParser.NL)
                self.state = 620 
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
         




