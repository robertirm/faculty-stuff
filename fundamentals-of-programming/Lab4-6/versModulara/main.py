from ui import run
from ui2 import meniu_batch

def func():
    print("M1.Normal M2.Batch ")
    x=input("M=")
    if x=='1':
        run()
    elif x=='2':
        meniu_batch()

func()