# aeon_feeder_fix

The IR beam break processing code runs on top of [MicroPython](https://github.com/micropython/micropython), an implementation of a Python interpreter for microcontrollers.

## How to install

### Prerequisites

* [Visual Studio Code](https://code.visualstudio.com/)
* [Raspberry Pi Pico SDK](https://www.raspberrypi.com/news/raspberry-pi-pico-windows-installer/)

### Firmware

Before running the actual Python code, we need to install the MicroPython firmware in the Pico. To do this, boot the Pico into firmware uploading mode by holding BOOTSEL while plugging the USB cable into the computer, then release. A storage drive should now be mounted on the computer, e.g. RPI-RP2.

To install the firmware, drag the file `RPI_PICO-20231005-v1.21.0.uf2` into the storage drive. The drive should be automatically unmounted and the Pico will then boot straight into MicroPython.

### MicroPython code

The IR beam break processing code is implemented in the `main.py` file. This should be transferred to the root of the pico file system so it can be executed on reset. A simple way to test and manipulate MicroPython code is to use the [Thonny IDE](https://thonny.org/).
