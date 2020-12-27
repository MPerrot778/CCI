import time
import numpy as np

def hello_w0rld():
    current_time = time.time_ns()
    while(True):
        if(np.ceil(current_time%100) == 0):
            print('Hello world')
        else:
            pass
    return None


if __name__ == "__main__":
    hello_w0rld()
    pass
    
