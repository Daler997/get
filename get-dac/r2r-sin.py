import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 1
sampling_frequency = 1000

if __name__ == "__main__":
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.2871, True)

    try:
        while True:
            dac.set_voltage(sg.get_sin_wave_amplitude(signal_frequency, time.time()))
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        dac.deinit()