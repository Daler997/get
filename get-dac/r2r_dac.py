import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)
    
    def set_number(self, n):
        GPIO.output(self.gpio_bits, [int(i) for i in bin(n)[2:].zfill(8)])

    def set_voltage(self, U):
        try:
            if self.dynamic_range >= U >= 0:
                a = int(256 * U / self.dynamic_range)
            else:
                print(f"Не попадает в диапазон ЦАП [0.00 B; {self.dynamic_range} B]")
                a = 0
        except ValueError:
            print("Not-a-Number")
            a = 0
        
        self.set_number(a)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
        

if __name__ == "__main__":
    dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.2871, True)

    try:
        while True:
            print("Введите напряжение: ")
            dac.set_voltage(float(input()))

    finally:
        dac.deinit()