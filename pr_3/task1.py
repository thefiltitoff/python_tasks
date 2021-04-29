import struct


def create_d_structures(data, address):
    result = []
    dsize = struct.unpack('<H', data[address:address+2])[0]
    # print(dsize)
    d_address = struct.unpack('<I', data[address+2:address+ 6])[0]

    k = 0
    for i in range(dsize):


        d1 = struct.unpack('<H', data[d_address+k:d_address+k+2])[0]
        # print(d1)
        d2 = struct.unpack('<b', data[d_address+k+2:d_address+k+3])[0]
        # print(d2)
        d3 = struct.unpack('<H', data[d_address+k+3:d_address+k+5 ])[0]
        # print(d3)

        k = k + 5

        result.append({
            'D1': d1,
            'D2': d2,
            'D3': d3
        })

    return result


def f31(data):
    a1 = struct.unpack('<f', data[4:8])[0]
    # print(a1)
    a2 = struct.unpack('<i', data[8:12])[0]
    # print(a2)
    a3 = struct.unpack('<q', data[12:20])[0]
    # print(a3)
    a4 = struct.unpack('<I', data[20:24])[0]
    # print(a4)
    rsize = struct.unpack('<H', data[24:26])[0]
    d_address = struct.unpack('<I', data[26:30])[0]
    a5 = list(struct.unpack('<'+str(rsize)+'q', data[d_address:d_address + (rsize*8)]))
    # print(a5)
    a6 = struct.unpack('<h', data[30:32])[0]
    # print(a6)

    b1 = struct.unpack('B', data[a4:a4+1])[0]
    # print(b1)
    b3 = list(struct.unpack('<7b',data[a4+57:a4+64]))
    # print(b3)
    b4 = struct.unpack('<i',data[a4+64:a4+68])[0]
    # print(b4)
    b5 = struct.unpack('<q', data[a4 + 68:a4 + 76])[0]
    # print(b5)
    b6 = struct.unpack('<h', data[a4 + 76:a4 + 78])[0]
    # print(b6)
    b7 = struct.unpack('<h', data[a4 + 78:a4 + 80])[0]
    # print(b7)


    c1 = create_d_structures(data, a4+1)
    # print(c1)
    c2 = struct.unpack('<q', data[a4+7:a4+15])[0]
    # print(c2)
    c3 = struct.unpack('<q', data[a4 + 15:a4 + 23])[0]
    # print(c3)
    c4 = struct.unpack('<d', data[a4 + 23:a4 + 31])[0]
    # print(c4)
    c5 = struct.unpack('<f', data[a4 + 31:a4 + 35])[0]
    # print(c5)
    c6 = struct.unpack('<q', data[a4 + 35:a4 + 43])[0]
    # print(c6)
    c7 = struct.unpack('<q', data[a4 + 43:a4 + 51])[0]
    # print(c7)
    rsize = struct.unpack('<I',data[a4+51:a4+55])[0]
    d_address = struct.unpack('<H', data[a4+55:a4+57])[0]
    # print(adress)
    # print(rsize)
    c8 = list(struct.unpack('<'+str(rsize)+'b', data[d_address:d_address+3]))
    # print(c8)






    out_dict = {

        'A1': a1,
        'A2': a2,
        'A3': a3,
        'A4': {
            'B1': b1,
            'B2': {
                'C1': c1,
                'C2': c2,
                'C3': c3,
                'C4': c4,
                'C5': c5,
                'C6': c6,
                'C7': c7,
                'C8': c8
            },
            'B3' : b3,
            'B4' : b4,
            'B5' : b5,
            'B6' : b6,
            'B7' : b7
        },
        'A5': a5,
        'A6': a6
    }

    # print(out_dict)
    return out_dict


# f31((b'FQDC\xb9aaooog\xa68\x00\x00\x00E\x00\x00\x00R\x00\x00\x00\xa0\xfaxQ'
#      b'3\xcc\x8f,\r\x90$<\x08\xe3\x84\xdd_\x004\xdda\x17\xb6\x1c\xaa\xf4\x1a\xb8'
#      b'\xc5\x0f\xbf)\x04\xecN\xd2\x7fq\xf6\xc2]\xb23\x83\xd3\xe1<\xc7\x1d\xf3\xb13'
#      b"\x02\xc0\xc48O.@\xc2\x0f\xa1\xb4d\n'a\xb3y\xa2\xa0\x98\xe9\xe8F\xc9"
#      b'\xbe\xc4?c\x97z\xe1"\xbfY\x8d\x90\x8a\xbc=\x168\x8a\xffw<sxO\xe4\x18\x7f\xa5'
#      b'6\x8f#\xd4\xfe\xdb7\xf9p'))

# f31((b'FQDC\xb9vjthja\xe58\x00\x00\x00E\x00\x00\x00R\x00\x00\x00\x91\xa8\xdd\x1c'
# b'\xc5\xeb\x10W\xe3|?\xe1\xab[\xaf\xd4_\x00L\x81\xf8\x80R\x17\xe3T\xfb\xc3'
# b'\x17!jX\xc2K\xd2\xf9/\x8e\xd7:\xa6\xc2^l\x81\xa4R\xdb\xe9\xf6\r\x98'
# b'\x18\x1e-\xa0\x8c\xceDH\x9e\xcb\x84\x9d^\x80\xdfJm\x02X\xc0\xc6\xb1\x81\xb0'
# b'\x8f\x9f\xbfA\x94R S?\x05\x9f^\\!\x94\xc9\xcbg\xce\xb8-\xe7\xa9\x03'
# b'<\xec\x890\xeaK\x92%u}I\xb6%'))

# f31((b'LVKJJ)s\xbf\t\xacQ\x10\x13\x86_\x8aeYXJ-\x00\x00\x00\x02\x00}\x00'
# b'\x00\x00\xd1\xcef\xe5t\xc2\xd9\xe5$\xc3;\x95\x8b\xb1\x04I\x02\x00'
# b" \x00\x00\x00'\xce\x97\xc7\xee\xbc\xbd\x80\xc6 \xff\x9ch\xeaI\x84\x00Kw^"
# b'\xc4\x16\xe7\xbf\x9e\xf0a\xbfE\xd6\x96~E\xc3\x94\xeaeQp\x90\xc0j\xe4\xf2'
# b'\x03\x00\x00\x00*\x00L\x15\xe2\xbek\x8d\xd1R\x04\xd4\xdf8\xf7\xbb'
# b'\x1e\x04\x90\x879}\xad\x87\x8f\xc1`\xb7,\xd0\xd5\xb5\x8dW\x85p\xcd`)\xf1'
# b'\xf2')
# )
#
# f31((b'LVKJ\x96\r\xf8\xbe\x1fQ:\x18\x00h\x97\x02\x8f\xbb1\xbb-\x00\x00\x00'
# b'\x02\x00}\x00\x00\x00\x8a\xd6\xa3\x9b^\r\x066]a#\xdd\xf3ja\xe1\x02\x00'
# b' \x00\x00\x00\xb1\xa0\xd0^o\x9c\x83\x18\x95\x81[`x\x1c\x06c\xb6\xe0\x85p'
# b'\xeby\xe3?Fz\x11?5?~F\xcc\xe0\xbc\xcb\x1a}S\xb1\xf6C\xc5\xec\x03\x00\x00\x00'
# b'*\x00\xd4\x9a1\xf7\xb3q\xf6\xd6\x97_\xfe\xd0\xd7\\,\xe9\xba\x0e}.\xc8\x9c'
# b',L\xdf\xbf\x08P\x9d\x99i\xa9\x91\xa4\x08\x10\xe2\x1c\xda'))