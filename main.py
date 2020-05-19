import random

##### Generate Random binary bits with size n #####
def randomBits(n):
    bits = []
    for i in range(n):
        bits.append(random.randrange(2))
    return bits

##### The Mapper takes bits and return the signal to be transmitted #####
def mapper(bits):
    signal = []

    return signal

##### The Channel takes the transmitted signal to add AWGN to it #####
def channel(transmitted_signal):
    distorted_signal = []

    return distorted_signal

##### The DeMapper takes the received signal to retrieve the original bits #####
def demapper(distorted_signal):
    received_bits = []

    return received_bits

def main():

    ##### The bits to be transmitted #####
    bits = randomBits(10)
    print(bits)

    ##### The transmitted signal for bits #####
    transmitted_signal = mapper(bits)
    print(transmitted_signal)

    ##### The signal after AWGN distortion #####
    distorted_signal = channel(transmitted_signal)
    print(distorted_signal)

    ##### The received bits #####
    received_bits = demapper(distorted_signal)
    print(received_bits)

##### Calling the main function #####
main()