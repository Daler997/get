import smbus
import time

class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Принятые данные: {data}, старший байт: {upper_data_byte:x}, младший байт: {lower_data_byte:x}, число: {number}")

        return number

    def get_voltage(self):
        return self.dynamic_range * self.get_number() / 1023


if __name__ == "__main__":
    mcp3021 = MCP3021(5)

    try:
        while True:
            print(mcp3021.get_number(), end = "\t")
            print(f"{mcp3021.get_voltage():.3f}")

            time.sleep(0.5)

    finally:
        mcp3021.deinit()
        