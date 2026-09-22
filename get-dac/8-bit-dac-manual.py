try:
    import RPi.GPIO as GPIO

    def voltage_to_number(U):
        try:
            if 3.2871 >= float(U.replace(",", ".")) > 0:
                return int(256 * float(U) / 3.3)
            else:
                print("Не попадает в диапазон ЦАП [0.00 B; 3.2871 B]")
                return 0
        except ValueError:
            print("Not-a-Number")
            return 0

    def to_bin(n):
        return [int(i) for i in bin(n)[2:].zfill(8)]

    GPIO.setmode(GPIO.BCM)
    dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]

    GPIO.setup(dac_bits, GPIO.OUT)

    while True:
        print("Введите напряжение: ")
        a = to_bin(voltage_to_number(input()))
        GPIO.output(dac_bits, a)

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()