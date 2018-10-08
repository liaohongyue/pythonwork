import math
def printDeltaGO(ATP,ADP,Pi):
    R=0.00831
    T=298
    deltaGO=-30.5
    value=deltaGO + R*T*math.log(ADP*Pi/ATP)
    print(value)