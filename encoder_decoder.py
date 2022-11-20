from matplotlib import pyplot as plt
import numpy as np
import collections


def encoder_unipolar(input):
    input_signal = list(input)
    input_signal.insert(0, 0)
    return input_signal

def decoderUnipolar(input):
    ans_list = []
    for i in range(1, len(input)):
        if input[i] == 1:
            ans_list.append(1)
        else:
            ans_list.append(0)
    return ans_list

def encoder_polar_nrz_l(input):
    input_signal = list(input)
    input_signal.insert(0, 0)
    input_signal = [-1 if i == 0 else 1 for i in input_signal]
    return input_signal

def decoderNRZL(input):
    ans_list = []
    for i in range(1, len(input)):
        if input[i] == -1:
            ans_list.append(0)
        elif input[i] == 1:
            ans_list.append(1)
    return ans_list

def encoder_polar_nrz_i(input):
    input_signal = list(input)
    lock = False
    for i in range(len(input_signal)):
        if input_signal[i] == 1 and not lock:
            lock = True
            continue
        if lock and input_signal[i] == 1:
            if input_signal[i - 1] == 0:
                input_signal[i] = 1
                continue
            else:
                input_signal[i] = 0
                continue
        if lock:
            input_signal[i] = input_signal[i - 1]
    input_signal = [-1 if i == 0 else 1 for i in input_signal]
    return input_signal

def decoderNRZI(input):
    ans_list = []
    if input[1] == 1:
        ans_list.append(1)
    else:
        ans_list.append(0)
    for i in range(2, len(li)):
        if input[i] == input[i-1]:
            ans_list.append(0)
        else:
            ans_list.append(1)
    return ans_list

def encoder_polar_rz(input):
    input_signal = list(input)
    input_signal = [-1 if i == 0 else 1 for i in input_signal]
    list = []
    for i in range(len(input_signal)):
        list.append(input_signal[i])
        list.append(0)
    return list

def decoderRZ(input):
    list = []
    for i in range(0, len(input), 2):
        if (input[i] == 1 and input[i+1] == 0):
            list.append(1)
        elif (input[i] == -1 and input[i+1] == 0):
            list.append(0)
    return list


def encoder_Biphase_manchester(input):
    input_signal = list(input)
    ans_list_= []
    for i in range(len(input_signal)):
        if input_signal[i] == 0:
            ans_list_.append(-1)
            ans_list_.append(1)
        elif input_signal[i] == 1:
            ans_list_.append(1)
            ans_list_.append(-1)
    return ans_list_

def decoderBiphaseManchester(list):
    ans_list = []
    print(list)
    for i in range(0, len(list), 2):
        if (list[i] == 1 and list[i+1] == -1):
            ans_list.append(1)
        elif (list[i] == -1 and list[i+1] == 1):
            ans_list.append(0)
    return ans_list

def encoder_Differential_manchester(input):
    input_signal = list(input)
    ans_list, lock, pre = [], False, ''
    for i in range(len(input_signal)):
        if input_signal[i] == 0 and not lock:
            ans_list.append(-1)
            ans_list.append(-1)
            ans_list.append(1)
            lock = True
            pre = 'S'
        elif input_signal[i] == 1 and not lock:
            ans_list.append(1)
            ans_list.append(1)
            ans_list.append(-1)
            lock = True
            pre = 'Z'
        else:
            if input_signal[i] == 0:
                if pre == 'S':
                    ans_list.append(-1);
                    ans_list.append(1)
                else:
                    ans_list.append(1);
                    ans_list.append(-1)
            else:
                if pre == 'Z':
                    pre = 'S'
                    ans_list.append(-1);
                    ans_list.append(1)
                else:
                    pre = 'Z'
                    ans_list.append(1);
                    ans_list.append(-1)

    return ans_list

def decoderDiffManchester(input):
    ans_list = []
    if input[1] == 1:
        ans_list.append(1)
    else:
        ans_list.append(0)
    for i in range(3, len(input), 2):
        if input[i] == input[i-2]:
            ans_list.append(0)
        else:
            ans_list.append(1)
    return ans_list


def encoder_AMI(input):
    input_signal = list(input)
    input_signal.insert(0, 0)
    lock = False
    for i in range(len(input_signal)):
        if input_signal[i] == 1 and not lock:
            lock = True
            continue
        elif lock and input_signal[i] == 1:
            input_signal[i] = -1
            lock = False
    return input_signal

def decoderAMI(li):
    ans = []
    for i in range(1, len(li)):
        if li[i] == 0:
            ans.append(0)
        else:
            ans.append(1)
    return ans


def scrambler_HDB3(a):
    p = -1
    cnt = 0
    even = 0
    i = 1
    j = 1
    n = len(a)
    b = [0]
    while i <= n and j <= n:
        if a[j-1] == 0:
            b.append(0)
            cnt = cnt+1
            if cnt == 4:
                if even == 0:
                    b[i] = -p
                    b[j] = -p
                    p = -p
                    cnt = 0
                    i = j+1
                else:
                    b[j] = p
                    even = 0
                cnt = 0
                i = j+1
        else:
            p = -p
            if even == 0:
                even = 1
            else:
                even = 0
            b.append(p)
            i = j+1
            cnt = 0
        j = j+1
    return b

def dec_HDB3(data_hdb3) :
   data=[]
   prev=-1
   i=1
   while i in range(len(data_hdb3)):
        if data_hdb3[i] == 0  :
            data.append(0)
        elif data_hdb3[i] == -prev :
            data.append(1)
            prev=-prev
        else:
             data.append(0)
             data[i-4]=0
        i=i+1
   return data

def scrambler_B8ZS(data):
    p = -1
    cnt = 0
    i = 1
    j = 1
    n = len(data)
    data_b8zs = [0]
    while i <= n and j <= n:
        if data[j-1] == 0:
            data_b8zs.append(0)
            cnt = cnt+1
            if cnt == 8:
                data_b8zs[i+3] = p
                data_b8zs[i+4] = -p
                data_b8zs[i+6] = -p
                data_b8zs[i+7] = p
                cnt = 0
                i = j+1

        else:
            p = -p
            data_b8zs.append(p)
            i = j+1
            cnt = 0
        j = j+1
    return data_b8zs

def dec_B8ZS(data_b8zs) :
   data=[]
   prev=-1
   i=1
   while i in range(len(data_b8zs)):
        if data_b8zs[i] == 0  :
            data.append(0)
        elif data_b8zs[i] == -prev :
            data.append(1)
            prev=-prev
        else:
            for x in range(5):
             data.append(0)
            i=i+4
        i=i+1
   return data

def plot(li):
    choice = int(input("\n[+] Choose a Encoding Technique :\n 1) Unipolar-NRZ\n 2) Polar-NRZ-L\n 3) Polar-NRZ-I\n 4) Polar-RZ\n 5) Biphase Manchester\n 6) Differential Manchestor\n 7) Bipolar AMI\n>>> "))
    if (choice == 1):
        plt.subplot(7, 1, 1)
        plt.ylabel("Unipolar-NRZ")
        plt.plot(encoder_unipolar(li), color='blue', drawstyle='steps-pre', marker='o')
        option = input("\n[+] Do You Want to decode the Digital Signal to Binary (Y/N)\n>>> ")
        if (option== "Y" or option=="y"):
            li2=list(encoder_unipolar(li))
            li3=list(decoderUnipolar(li2))
            print("Decoded Signal : {0}".format(str(li3)))

    elif  (choice == 2):
        plt.subplot(7, 1, 2)
        plt.ylabel("P-NRZ-L")
        plt.plot(encoder_polar_nrz_l(li), color='blue', drawstyle='steps-pre', marker='o')

        option = input("\n[+] Do You Want to decode the Digital Signal to Binary (Y/N)\n>>> ")
        if (option== "Y" or option=="y"):
            li2=list(encoder_polar_nrz_l(li))
            li3=list(decoderNRZL(li2))
            print("Decoded Signal : {0}".format(str(li3)))
    
    elif  (choice == 3):    
        plt.subplot(7, 1, 3)
        plt.ylabel("P-NRZ-I")
        plt.plot(encoder_polar_nrz_i(li), color='blue', drawstyle='steps-pre', marker='o')

        option = input("\n[+] Do You Want to decode the Digital Signal to Binary (Y/N)\n>>> ")
        if (option== "Y" or option=="y"):
            li2=list(encoder_polar_nrz_i(li))
            li3=list(decoderNRZI(li2))
            print("Decoded Signal : {0}".format(str(li3)))

    elif  (choice == 4):        
        plt.subplot(7, 1, 4)
        plt.ylabel("Polar-RZ")
        plt.plot(encoder_polar_rz(li), color='blue', drawstyle='steps-pre', marker='o')

        option = input("\n[+] Do You Want to decode the Digital Signal to Binary (Y/N)\n>>> ")
        if (option== "Y" or option=="y"):
            li2=list(encoder_polar_rz(li))
            li3=list(decoderRZ(li2))
            print("Decoded Signal : {0}".format(str(li3)))

    elif  (choice == 5):        
        plt.subplot(7, 1, 5)
        plt.ylabel("B_Man")
        plt.plot(encoder_Biphase_manchester(li), color='blue', drawstyle='steps-pre', marker='o')

        option = input("\n[+] Do You Want to decode the Digital Signal to Binary (Y/N)\n>>> ")
        if (option== "Y" or option=="y"):
            li2=list(encoder_Biphase_manchester(li))
            li3=str(list(decoderBiphaseManchester(li2)))
            print("Decoded Signal : {0}".format(str(li3)))

    elif  (choice == 6):        
        plt.subplot(7, 1, 6)
        plt.ylabel("Dif_Man")
        plt.plot(encoder_Differential_manchester(li), color='blue', drawstyle='steps-pre', marker='o')

        option = input("\n[+] Do You Want to decode the Digital Signal to Binary (Y/N)\n>>> ")
        if (option== "Y" or option=="y"):
            li2=list(encoder_Differential_manchester(li))
            li3=str(list(decoderDiffManchester(li2)))
            print("Decoded Signal : {0}".format(str(li3)))


    elif  (choice == 7):
        if (len(li) >= 8):
          x=li
          zeros=[0,0,0,0,0,0,0,0]
          for i in range(0,len(li)-7):
            each = list(x[i:i+8])
            # print(each)
            if (each==zeros):
                choice2 = int(input("\n[+] Please choose a Scrambling Method\n 1) HDB3\n 2) B8ZS\n >>> "))
                if (choice2 == 1):
                    plt.subplot(7, 1, 7)
                    plt.ylabel("HDB3")
                    plt.plot(scrambler_HDB3(li), color='blue', drawstyle='steps-pre', marker='o')
                    option = input("\n[+] Do You Want to decode the Digital Signal to Binary (Y/N)\n>>> ")
                    if (option== "Y" or option=="y"):
                        li2=list(scrambler_HDB3(li))
                        li3=str(list(dec_HDB3(li2)))
                        print("Decoded Signal : {0}".format(str(li3)))
                    break
                elif (choice2 == 2):
                    plt.subplot(7, 1, 7)
                    plt.ylabel("B8ZS")
                    plt.plot(scrambler_B8ZS(li), color='blue', drawstyle='steps-pre', marker='o')
                    option = input("\n[+] Do You Want to decode the Digital Signal to Binary (Y/N)\n>>> ")
                    if (option== "Y" or option=="y"):
                        li2=list(scrambler_B8ZS(li))
                        li3=str(list(dec_B8ZS(li2)))
                        print("Decoded Signal : {0}".format(str(li3)))
                    break
                break
            elif (i == len(li)-8):
                plt.subplot(7, 1, 7)
                plt.ylabel("A-M-I")
                plt.plot(encoder_AMI(li), color='blue', drawstyle='steps-pre', marker='o')
                option = input("\n\n[+] Do You Want to decode the Digital Signal to Binary (Y/N)\n>>> ")
                if (option== "Y" or option=="y"):
                    li2=list(encoder_AMI(li))
                    li3=str(list(decoderAMI(li2)))
                    print("Decoded Signal : {0}".format(str(li3)))
        else:
          plt.subplot(7, 1, 7)
          plt.ylabel("A-M-I")
          plt.plot(encoder_AMI(li), color='blue', drawstyle='steps-pre', marker='o')

          option = input("\n\n[+] Do You Want to decode the Digital Signal to Binary (Y/N)\n>>> ")
          if (option== "Y" or option=="y"):
            li2=list(encoder_AMI(li))
            li3=str(list(decoderAMI(li2)))
            print("Decoded Signal : {0}".format(str(li3)))

    else:
        plot(li)
    plt.draw()
    plt.show()


if __name__ == '__main__':
    print('\n[+] Enter binary bits of any length : \n')
    binary_bits=input(">>> ")
    li = list(binary_bits)
    li = np.array(li,dtype=int)
    plot(li)