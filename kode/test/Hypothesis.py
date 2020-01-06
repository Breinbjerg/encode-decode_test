'''
Created on 20 Sep 2019

@author: Steffen
'''
import sys
sys.path.append('/home/Steffen/rle_encode/encode-decode_test/kode/')

import pytest 
from RLE import rle_decode, rle
from hypothesis import given
from hypothesis.strategies import text, characters






@given(text(characters(whitelist_categories=['Ll','Lu'],blacklist_categories=['So','Sk','Sm','Sc'],min_codepoint=65,max_codepoint=122),0,10))
def hypo_rle(mess):
    assert(rle_decode(rle(mess)))
    
    
if __name__ == '__main__':
    hypo_rle()