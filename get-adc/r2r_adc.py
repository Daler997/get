import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.compare_time = compare_time
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    
    def number_to_dac(self, n):
        GPIO.output(self.bits_gpio, [int(i) for i in bin(n)[2:].zfill(8)])

    def sequential_counting_adc(self):
        for i in range(0, 2 ** 8):
            self.number_to_dac(i)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio):
                return i
        
        return 2 ** 8 - 1

    def get_sc_voltage(self):
        return self.dynamic_range * self.sequential_counting_adc() / 255

    def successive_approximation_adc(self):
        min = 0
        max = 2**8 - 1
        while max >= min:
            middle = min + (max-min) // 2
            self.number_to_dac(middle)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio):
                max = middle - 1                                        
            else:
                min =  middle + 1
        return middle
    
    def get_sar_voltage(self):
        return self.dynamic_range * self.successive_approximation_adc() / 255

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

if __name__ == "__main__":
    adc = R2R_ADC(3.291)

    try:
        while True:
#            print(adc.sequential_counting_adc(), end = "\t")
            print(adc.successive_approximation_adc(), end = "\t")
            print(f"{adc.get_sar_voltage():.3f}")

    finally:
        adc.deinit()