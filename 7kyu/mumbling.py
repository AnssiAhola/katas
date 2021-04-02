# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def accum(s):
    output = ''
    for i, c in enumerate(s):
        if i != 0:
            output += '-'
        output += c.upper() + c.lower()*i
    return output


# From Kata Solutions
def accum(s):
    return '-'.join(c.upper() + c.lower()*i for i, c in enumerate(s))


print(accum("ZpglnRxqenU") ==
      "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
print(accum("NyffsGeyylB") ==
      "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
print(accum("MjtkuBovqrU") ==
      "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
print(accum("EvidjUnokmM") ==
      "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
print(accum("HbideVbxncC") ==
      "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")
