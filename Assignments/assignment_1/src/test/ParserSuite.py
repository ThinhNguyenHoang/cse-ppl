import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):


    def test_1(self):
        """ Test Var Declare 1 line 1 var """
        input = """
var a: integer;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
        

    def test_2(self):
        """ Test Var Declare 1 line n var """
        input = """
var a, b, c: integer;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
        

    def test_3(self):
        """ Test Var Declare n line """
        input = """
var a, b, c: integer;
var x, y: real;
var z: string;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
        

    def test_4(self):
        """ Test Var Declare array """
        input = """
var a: array[1 .. 3] of integer;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
        

    def test_5(self):
        """ Test Var Declare """
        input = """
Var a, B, c: array [5 .. 1000] of Boolean ;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
        

    def test_6(self):
        input = """
Var a, B, c: InTeGer;
    x, Y, Z: Boolean ;
    g: Array [4 .. 6] of REAL;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
        

    def test_7(self):
        input = """
procedure foo();
var a: real;
begin

end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
        

    def test_8(self):
        input = """
procedure foo(x: integer);
var a, b, c: real;
begin

end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
        

    def test_9(self):
        input = """
procedure foo(x: integer; y, z: real; g, h: string);
var 
    a, b, c: real;
    p: boolean;
    q: string;
    i, j: integer;

begin


end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
        

    def test_10(self):
        input = """
procedure foo(
    x: integer;
    y, z: real;
    g, h: string;
    arr_nodes: Array[0 .. 1000] of real
);

var 
    a, b, c: real;
    p: boolean;
    q: string;
    i, j: integer;
    dd: array[0..1000005] of boolean;

begin


end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
        

    def test_11(self):
        input = """
procedure foo();

var 
    a: real;

begin
    a := 5;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
        

    def test_12(self):
        input = """
procedure foo();

var 
    a: real;

begin
    a := b := c := 5;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
        

    def test_13(self):
        input = """
procedure foo();

var 
    a: real;

begin
    a := b [10] := foo() [3 ] := x := 1 ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
        

    def test_14(self):
        input = """
procedure foo();

var 
    a: real;

begin
    foo(2)[3+x] := a[b[f+y[2]]] + 3;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
        

    def test_15(self):
        input = """
procedure foo();

var 
    a: real;

begin
    foo(2)[3+x] := a[b[f+y[2]-h[t[5+j]] * 4]] + 3;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
        

    def test_16(self):
        input = """
// Test Assoc + -

procedure foo();

var 
    a: real;

begin
    a := b + 2 + n + 5 - g - 9;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
        

    def test_17(self):
        input = """
// Test Assoc + - or

procedure foo();

var 
    a: real;

begin
    a := b + 2 + n or 4 + 5 - g or 2 - 9;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
        

    def test_18(self):
        input = """
// Test Assoc / * div mod and

procedure foo();

var 
    a: real;

begin
    a := b / 2 * n / 4 div 5 mod g and 2 * 9 / 4 mod 2;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
        

    def test_19(self):
        input = """
// Test Precedence, Assoc "- not" with "( + -)"

procedure foo();

var 
    a: real;

begin
    a := -5 - 6 + not 5 - 9 - not -(3 + not -5);
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
        

    def test_20(self):
        input = """
// Test Precedence, Assoc - not * / div mod + - and or (  )

procedure foo();

var 
    a: real;

begin
    a := not - F * G div 5 + (I or L and N + Y or Q * not -P) and 6 * 5 + O div not (5 mod T) ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
        

    def test_21(self):
        input = """
// Test Assoc = <> < <= > >=

procedure foo();

var 
    a: real;

begin
    a := b = c ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
        

    def test_22(self):
        input = """
// Test Assoc = <> < <= > >=

procedure foo();

var 
    a: real;

begin
    a := (((5 <> 6) < (6 = 5)) >= (4 + 5 > 1)) <= 1 ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
        

    def test_23(self):
        input = """
// Test Assoc and then, or else

procedure foo();

var 
    a: real;

begin
    a := TRUE and then 2 ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
        

    def test_24(self):
        input = """
// Test Assoc and then, or else

procedure foo();

var 
    a: real;

begin
    a := TRUE and then FALSE or     else True or      else (1 and       then 2) ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
        

    def test_25(self):
        input = """
// Test TRUE FALSE 

procedure foo();

var 
    a: real;

begin
    a := True ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
        

    def test_26(self):
        input = """
// Test If Statement

procedure foo();
var a: real;
begin
    if a = 1 then ok();
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
        

    def test_27(self):
        input = """
// Test If Statement

procedure foo();
var a: real;
begin
    if a = 1 or b = 2 and c = 3 then 
        ok();
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
        

    def test_28(self):
        input = """
// Test If Statement

procedure foo();
var a: real;
begin
    if a = 1 then
        a := 5;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
        

    def test_29(self):
        input = """
// Test If Statement

procedure foo();
var a: real;
begin
    if a = 1 then begin
        a := 5;
        b := c := e * 2;
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
        

    def test_30(self):
        input = """
// Test If Statement

procedure foo();
var a: real;
begin
    if a = 1 then ok(); else no();
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
        

    def test_31(self):
        input = """
// Test If Statement

procedure foo();
var a: real;
begin
    if a = 1 then
        if b > 3 then
            c := 5;
        else 
            d := 1;
    else
        e := 0;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
        

    def test_32(self):
        input = """
// Test If Statement

procedure foo();
var a: real;
begin
    if a = 1 then begin
        if b > 3 then c := 5;
        else d := 1;

        if e < 4 then ok();
    end else begin
        if h > 5 then nty(); else lyo();
        g := 5;
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
        

    def test_33(self):
        input = """
// Test While statement

procedure foo();
var a: real;
begin
    While (i < 1) do i := i+1;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
        

    def test_34(self):
        input = """
// Test while statement

procedure foo();
var a: real;
begin
    While i < 1 do begin
        i := i+1;
        if i = 1 then i := i - 1;
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
        

    def test_35(self):
        input = """
// Test For while with break continue return statement

procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then break;
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
        

    def test_36(self):
        input = """
// Test For while with break continue return statement

procedure foo();
var a: real;
begin
    with a: integer; do a := a + 1;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
        

    def test_37(self):
        input = """
// Test For while with break continue return statement

procedure foo();
var a: real;
begin
    with 
        a: integer;
        b, c: array [0..15] of Boolean;
        x, y, z: real;
    do begin
        a := x := y := 3;
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
        

    def test_38(self):
        input = """
// Test call statement

procedure foo();
var a: real;
begin
    foo();
    bar(1);
    nty(1, 2, 3);
    pty(hyy, dyf(), ily(123, 456, fay), jtq(gyh())) ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
        

    def test_39(self):
        input = """
// Test complex code

var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================
    *)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
        

    def test_40(self):
        input = """
// Test For while with break continue return statement

procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then break;
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
        

    def test_41(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
        

    def test_42(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))
        

    def test_43(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
        

    def test_44(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
        

    def test_45(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
        

    def test_46(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
        

    def test_47(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
        

    def test_48(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
        

    def test_49(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
        

    def test_50(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
        

    def test_51(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
        

    def test_52(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
        

    def test_53(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
        

    def test_54(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
        

    def test_55(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
        

    def test_56(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
        

    def test_57(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
        

    def test_58(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))
        

    def test_59(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
        

    def test_60(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
        

    def test_61(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
        

    def test_62(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
        

    def test_63(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
        

    def test_64(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
        

    def test_65(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))
        

    def test_66(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))
        

    def test_67(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))
        

    def test_68(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))
        

    def test_69(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))
        

    def test_70(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))
        

    def test_71(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
        

    def test_72(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
        

    def test_73(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
        

    def test_74(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
        

    def test_75(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
        

    def test_76(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
        

    def test_77(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
        

    def test_78(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
        

    def test_79(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
        

    def test_80(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
        

    def test_81(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
        

    def test_82(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
        

    def test_83(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
        

    def test_84(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
        

    def test_85(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
        

    def test_86(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
        

    def test_87(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
        

    def test_88(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))
        

    def test_89(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
        

    def test_90(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))
        

    def test_91(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
        

    def test_92(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))
        

    def test_93(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
        

    def test_94(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
        

    def test_95(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))
        

    def test_96(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
        

    def test_97(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
        

    def test_98(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))
        

    def test_99(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))
        

    def test_100(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
        
