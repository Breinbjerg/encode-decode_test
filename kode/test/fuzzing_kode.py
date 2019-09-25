'''
Created on 18 Sep 2019

@author: Steffen
'''

from fuzzing.fuzzer import FuzzExecutor



file_list = ["/media/sf_Centos_Pythontest/first_test/kode/encode.txt"]

apps_under_test = ["python & /media/sf_Centos_Pythontest/first_test/kode/RLE.py -e"]

number_of_runs = 5


def test():
    fuzz_executor = FuzzExecutor(apps_under_test,file_list)
    fuzz_executor.run_test(number_of_runs)
    return  fuzz_executor.stats



def main():
    stats = test()
    print(stats)
    
if __name__ == '__main__':
    main()