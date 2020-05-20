# M-ary-ASK-Simulation
Simulation and analysis of the Amplitude Shift Keying (ASK) and its Bit Error Rate (BER) for 8-ary case.

## Prerequisites
1. Python
2. numpy, matplotlib and scipy

## Run
Run the following command for Windows or Linux in this directory. where 1000000 is the number of random decoded bits
```sh
$ python main.py 1000000
```

## Expected output
<img align="center" src="output.png">

## Important Equations
1. Eb = E0 * summation(ai^2)/N , where N is the total number of bits. In this example assume Eb = 1 to get E0.
2. SNR = Eb/N0.
3. Variance = N0/2.
4. Standard Deviation = sqrt(Variance).
