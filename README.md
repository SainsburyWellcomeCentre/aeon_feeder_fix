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

The IR beam break processing code is implemented in the `main.py` file, [here](https://github.com/SainsburyWellcomeCentre/aeon_feeder_fix/blob/main/Code/main.py). This should be transferred to the root of the pico file system so it can be executed on reset. One way to do this is via the [Thonny IDE](https://thonny.org/): if the firmware has been correctly installed, then when plugging the pico back into the computer, and opening the Thonny IDE, in the bottom-right corner of the IDE you should be able to select devices, and the Pico should show up here; if you click the Pico device listed here, and then in the main menu bar in Thonny click "View -> Files", you should see both the filesystem of the computer, and the filesystem of the Pico, and you should then be able to click and upload files from the computer to the Pico.
