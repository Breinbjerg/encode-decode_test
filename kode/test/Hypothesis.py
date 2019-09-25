'''
Created on 20 Sep 2019

@author: Steffen
'''





from hypothesis import given
from hypothesis.strategies import text, characters
from kode.RLE import rle, rle_decode


@given(text(characters('L',('P','S','C'),('ª','µ')),1,3))
def hypo_rle(mess):
    assert(rle_decode(rle(mess)))
    
    
if __name__ == '__main__':
    hypo_rle()