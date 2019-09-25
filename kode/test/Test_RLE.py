'''
Created on 11 Sep 2019

@author: Steffen
'''
from kode.RLE import rle_decode, rle



def test_rl4():
    assert rle_decode('3a4b') == 'aaabbbb'
    
# fail input - There must always be a number before character.
def test_rl5():
    assert  rle_decode('a5b6c') == ''
    
def test_rl6():
    assert rle_decode('15a3b') == 'aaaaaaaaaaaaaaabbb'

def test_rl7():
    assert rle_decode('110a30b') == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
    
def test_rl9():
    assert rle_decode('') == ''

def test_rl10():
    assert rle('aaaaaccccccbbbbbbggggggg') == '5a6c6b7g'
    
def test_rl11():
    assert rle_decode('5a6c6b7g') == 'aaaaaccccccbbbbbbggggggg'
    
    
    

        