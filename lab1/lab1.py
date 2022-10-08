import random
import matplotlib.pyplot as plt
import numpy as np



from base_1 import *
from advanced_1 import *


def main():
    #basic part
    part = input()
    if(part=='base'):
        uniform()
        chebishev()
    elif(part == 'a_tsk_1'):
        advanced_part_tsk_1()
    #elif (part == 'a_tsk_2'):
        advanced_part_tsk_2()
    #advanced part


if __name__ == '__main__':
    main()