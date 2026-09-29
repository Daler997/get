import pwm_dac as PWM
import time
import signal_generator as sg

amplitude = 3.2
signal_frequency = 1
sampling_frequency = 1000

if __name__ == "__main__":
    pwm = PWM.PWM_DAC(12, 1000, 3.2871)

    try:
        while True:
            pwm.set_voltage(amplitude * sg.get_sin_wave_amplitude(signal_frequency, time.time()))
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        pwm.deinit()