# -*- encoding: utf8 -*-
import struct

# testNumbers = [1, 2, 3, 4, 9, 13, 24, 511, 1025, 1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025,1, 2, 3, 4, 9, 13, 24, 511, 1025]
# jianju = []
#
# for i in range(0, len(testNumbers)):
#     if i == 0:
#         jianju.append(testNumbers[i])
#     else:
#         jianju.append(testNumbers[i]-testNumbers[i-1])
#
#
# binfile = open('jianju.txt','wb')
# for i in jianju:
#     bytes = struct.pack('i',i)
#     binfile.write(bytes)
# binfile.close()
#
#
# file = open('bin.txt', 'rb')
# byte = file.read()
# a = struct.unpack(len(testNumbers)*'i',byte)
# file.close()
# print a[7]
#
#
# jianjufile = open('jianju.txt','w')
# for i in jianju:
#     jianjufile.write(str(i))
# jianjufile.close()
#
# #
# def VBencode(num):
#     binary = bin(num)[2:]
#     zheng = len(binary)/8
#     yu = len(binary)%8
#     bulen = (zheng + 1) * 8 - len(binary)
#     print str(000)+ str(binary)
#     print binary
#
# if __name__ == '__main__':
#     VBencode(1000)

def VB(num_str):
    jianju = []
    VBbytes = []
    for i in range(0, len(num_str)):
        if i == 0:
            jianju.append(num_str[i])
        else:
            jianju.append(num_str[i] - num_str[i - 1])
    for i in jianju:
        VBbytes.append(struct.pack('i',i))

    return VBbytes