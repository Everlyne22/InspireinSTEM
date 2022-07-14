from machine import Pi, Timer # how long you want it to blink after


led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
LED_state1= True
LED_state2= True
tim = Timer()

def tick(Timer):
    global led, LED_state1
    LED_state1 = not(LED_state1)
    led1.value(LED_state1)
    tim.init(freq=1,Mode=Timer