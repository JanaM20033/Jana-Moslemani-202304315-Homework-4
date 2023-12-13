import time
import random
def receiveSecondSignal(delay):
    print("Waiting for the second signal...")
    time.sleep(delay)  
    print("Second signal received: Your food is ready!")

def turnOnMicrowave(delay):
    signal = {
        "action": "turn_on the microwave ",
        "delay": delay,
    }
    print(f"Signal sent: {signal}")
    time.sleep(delay)
    print("Microwave turned on after delay.")

delay = random.randint(10, 20) 
turnOnMicrowave(delay)
receiveSecondSignal(delay)
