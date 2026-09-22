import smbus

class MCP4725:
    def __init__(self, dynamic_range, address = 0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("Нужно целое число")
        
        if not (0 <= number <= 4095):
            print("Число выходит за 12 бит")
        
        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число {number}, отправлено: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02x}]\n")

    def set_voltage(self, U):
        try:
            if self.dynamic_range >= U >= 0:
                a = int(4095 * U / self.dynamic_range)
            else:
                print(f"Не попадает в диапазон [0.00 B; {self.dynamic_range} B]")
                a = 0
        except ValueError:
            print("Not-a-Number")
            a = 0
        
        self.set_number(a)
        
if __name__ == "__main__":
    mcp = MCP4725(5)

    try:
        while True:
            print("Введите напряжение: ")
            mcp.set_voltage(float(input()))

    finally:
        mcp.deinit()