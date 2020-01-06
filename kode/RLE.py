'''
Created on 11 Sep 2019

@author: Steffen
'''


from curses.ascii import isalpha


def rle(mess):
    #print("Running encode")
    print(mess)
    if mess == '':
        return ''
    old = mess[0]
    count = 1
    res = []
    for c in mess[1:]:
        if c == old:
            count += 1
        elif c == '\n':
            continue
        else:
            res.append(f'{count}{old}')
            count = 1
            old = c
    res.append(f'{count}{old}')
    return ''.join(res)


def rle_decode(mess):
    #print("Running decode")
    if mess == '':
        return ''
    res = ''
    count = 0
    for c in mess:
        if mess == '':
            return res
        elif isalpha(c):
            if count == 0:
                res = ''
                return res
            else:
                res+=c*count
                count = 0
        elif c == '\n':
            continue
        else:
            count = count*10 + int(c)
    return res


if __name__ =='__main__':
    import sys
    argv = sys.argv
    print(argv)
    if argv[1] == '-e':
      with open(argv[2],'r') as f:
         print(rle(f.read()))
    if argv[1] == '-d':
      print(rle_encode(argv[2]))
