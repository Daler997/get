import RPi.GPIO as GPIO


class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.gpio_pin = gpio_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_pin, GPIO.OUT, initial=0)
        self.pwm = GPIO.PWM(gpio_pin, pwm_frequency)

    def set_voltage(self, U):
        try:
            if 3.2871 >= U > 0:
                duty = U / self.dynamic_range * 100
                self.pwm.start(duty)
            else:
                print("Не попадает в диапазон ЦАП [0.00 B; 3.2871 B]")
                return 0
        except ValueError:
            print("Not-a-Number")
            self.pwm.stop()

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

if __name__ == "__main__":
    pwm = PWM_DAC(12, 200, 3.2871)

    try:
        while True:
            print("Введите напряжение: ")
            pwm.set_voltage(float(input()))

    finally:
        pwm.deinit()