from io import StringIO
from numpy import zeros, array

def bytes_to_octal(bytestr):
    # calculate best possible number of digits
    digits = int(len(bytestr) * 8/3)
    # generate format string
    fmt = b"%%0%do" % digits
    # convert bytes to int and format as octal string
    octal = fmt % int.from_bytes(bytestr, byteorder='big')
    # return maximum "saturated" digits
    return octal[-digits:]

def movements(octal):
    # associate octal digit with movement vector
    directions = {
        ord('4'):(-1,-1), ord('5'):(-1, 0), ord('6'):(-1, 1),
        ord('3'):( 0,-1),                   ord('7'):( 0, 1),
        ord('2'):( 1,-1), ord('1'):( 1, 0), ord('0'):( 1, 1),
    }
    # return generator mapping each digit
    return (directions[c] for c in octal)

# compute randomart matrix from hash digest
def drunkenwalk(digest, size=(9, 18)):
    # initialize "drawing board" and positional vector
    matrix = zeros(size).astype(int)
    position = (array(size) / 2).astype(int)
    # perform movements and compute matrix
    for move in movements(bytes_to_octal(digest)):
        p = tuple(position)
        matrix.itemset(p, matrix.item(p) + 1)
        position = (position + move) % size
    return matrix

# character palette for drawing
PALETTE = " .*=%!~R_EWS0123456789abcdefghijklmnop"

# translation hash for ascii output
TRANSLATION = {
    ord("╭"): "/", ord("╮"): "\\", ord("╰"): "\\", ord("╯"): "/",
    ord("│"): "|", ord("─"): "-", ord("╴"): "[", ord("╶"): "]",
}

def draw_cards(matrices, palette=PALETTE):
    symbol = lambda n: PALETTE[n % len(PALETTE)]
    art = StringIO() 
    art.write("╭──────────────────╮"*3 + "\n")
    for idx in range(len(matrices[0])):
        line = ''
        for matrix in matrices:
            line += "│%s│" % "".join((symbol(el) for el in list(matrix[idx])))
        art.write(line + '\n')
    art.write("╰───────~ %s ~──────╯"*3 %(1,2,3)  + '\n')
    return art.getvalue()
