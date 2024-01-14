import os
import sys

while True:

    A = float(input("What is the number?")) # Initial Number input from user. Decimal places allowed
    D = int(input("How many decimal places do you want to display?")) #How many decimal places the user wants to display on all output values. Whole numbers only.
    ghi = 1.618033988749894 #Value for calucations later in code.
    phi = ghi - 1 #Value for calucations later in code.

    P1 = A*(phi**1)
    P2 = A*(phi**2)
    P3 = A*(phi**3)
    P4 = A*(phi**4)
    P5 = A*(phi**5)
    P6 = A*(phi**6)
    P7 = A*(phi**7)
    P8 = A*(phi**8)
    P9 = A*(phi**9)
    P10 = A*(phi**10)
    P11 = A*(phi**11)
    P12 = A*(phi**12)
    P13 = A*(phi**13)
    P14 = A*(phi**14)
    P15 = A*(phi**15)
    P16 = A*(phi**16)
    P17 = A*(phi**17)
    P18 = A*(phi**18)
    P19 = A*(phi**19)
    P20 = A*(phi**20)

    G1 = A*(ghi**1)
    G2 = A*(ghi**2)
    G3 = A*(ghi**3)
    G4 = A*(ghi**4)
    G5 = A*(ghi**5)
    G6 = A*(ghi**6)
    G7 = A*(ghi**7)
    G8 = A*(ghi**8)
    G9 = A*(ghi**9)
    G10 = A*(ghi**10)
    G11 = A*(ghi**11)
    G12 = A*(ghi**12)
    G13 = A*(ghi**13)
    G14 = A*(ghi**14)
    G15 = A*(ghi**15)
    G16 = A*(ghi**16)
    G17 = A*(ghi**17)
    G18 = A*(ghi**18)
    G19 = A*(ghi**19)
    G20 = A*(ghi**20)


    print(f"      Initial Value:{A}")
    print(f"  P1:  {P1:.{D}f}    G1:  {G1:.{D}f}")
    print(f"  P2:  {P2:.{D}f}    G2:  {G2:.{D}f}")
    print(f"  P3:  {P3:.{D}f}    G3:  {G3:.{D}f}")
    print(f"  P4:  {P4:.{D}f}    G4:  {G4:.{D}f}")
    print(f"  P5:  {P5:.{D}f}    G5:  {G5:.{D}f}")
    print(f"  P6:  {P6:.{D}f}    G6:  {G6:.{D}f}")
    print(f"  P7:  {P7:.{D}f}    G7:  {G7:.{D}f}")
    print(f"  P8:  {P8:.{D}f}    G8:  {G8:.{D}f}")
    print(f"  P9:  {P9:.{D}f}    G9:  {G9:.{D}f}")
    print(f"  P10: {P10:.{D}f}    G10: {G10:.{D}f}")
    print(f"  P11: {P11:.{D}f}    G11: {G11:.{D}f}")
    print(f"  P12: {P12:.{D}f}    G12: {G12:.{D}f}")
    print(f"  P13: {P13:.{D}f}    G13: {G13:.{D}f}")
    print(f"  P14: {P14:.{D}f}    G14: {G14:.{D}f}")
    print(f"  P15: {P15:.{D}f}    G15: {G15:.{D}f}")
    print(f"  P16: {P16:.{D}f}    G16: {G16:.{D}f}")
    print(f"  P17: {P17:.{D}f}    G17: {G17:.{D}f}")
    print(f"  P18: {P18:.{D}f}    G18: {G18:.{D}f}")
    print(f"  P19: {P19:.{D}f}    G19: {G19:.{D}f}")
    print(f"  P20: {P20:.{D}f}    G20: {G20:.{D}f}")
    print("Calculations Finished.")

    # Ask the user if they want to restart or quit
    user_input = input("Press Enter to restart or 'q' to quit: ").lower()

    if user_input == 'q':
        sys.exit()  # Exit the script if the user enters 'q'
    else:
        # Restart the script by launching a new Python process
        python = sys.executable
        os.execl(python, python, *sys.argv)




























