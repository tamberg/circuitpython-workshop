# IoT Embedded Programming with CircuitPython

## Workshop
The Internet of Things ([IoT](http://www.tamberg.org/fhnw/2021/hs/IoT01Introduction.pdf)) is the convergence of internet and real world. IoT embedded devices typically have limited resources, but they are also becoming more performant with each generation. This allows an interpreted language like Python, which is less efficient but more convenient than C, to run on a microcontroller.

### Topics
- [Introduction](#introduction)
- [Toolchain Setup](#toolchain-setup)
- [Hardware Setup](#hardware-setup)
- [GPIO & Sensors](#gpio--sensors)
- [Wi-Fi & HTTP](#wifi--http)

### Objective
This workshop teaches the basics of embedded programming on the latest IoT hardware, with CircuitPython.

### Target audience
This workshop is aimed at interested people with basic programming experience in Python.

### Prerequisites
Participants need a laptop with MacOS, Windows or Linux, and two USB/USB-C ports. IoT hardware including sensors is available on loan.

The workshop requires a Wi-Fi network that is accessible without a portal. Alternatively, a personal smartphone can be used as a hotspot.

## Introduction
### CircuitPython
> The easiest way to program microcontrollers

https://circuitpython.org/

## Toolchain setup
### Text Editor
CircuitPython works with any text editor, e.g. [Mu Editor](https://codewith.mu/), [VS Code](https://code.visualstudio.com/), or *nano*.

### Serial Monitor
To see output you'll need a serial monitor like [PuTTY](https://www.putty.org/) on Windows or *screen* on MacOS, Linux.

### CircuitPython Libraries
Download the CircuitPython library bundle ZIP file from https://circuitpython.org/libraries

You will selectively copy files from the ZIP to your microcontroller later on.

## Hardware Setup
### Boards
* [ESP32-S2](#esp32-s2)
* [ESP32-C3](#esp32-c3)

### ESP32-S2
#### Buy
https://www.adafruit.com/product/5325 (Adafruit QT Py ESP32-S2 WiFi Dev Board)

#### Board
https://circuitpython.org/board/adafruit_qtpy_esp32s2/

#### UF2 Bootloader
To install the UF2 bootloader, follow the steps to _Install, Repair, or Update UF2 Bootloader_ at the bottom of https://circuitpython.org/board/adafruit_qtpy_esp32s2/

#### Pinout
<img text="ESP32-S2 Pinout, (c) Adafruit" src="https://cdn-learn.adafruit.com/assets/assets/000/107/493/original/adafruit_products_Adafruit_QT_Py_ESP32-S2_Pinout.png?1640130293" width="800"/>

* https://learn.adafruit.com/assets/107493 (Pinout)
* https://learn.adafruit.com/adafruit-qt-py-esp32-s2/pinouts
* https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/_images/esp32-s2_saola1-pinout.jpg (esp32s2_saola)

#### Schematic
<img text="ESP32-S2 Schematic, (c) Adafruit" src="https://cdn-learn.adafruit.com/assets/assets/000/110/384/original/adafruit_products_QT_Py_rev_C_sch.png?1648589651" width="640"/>

* https://learn.adafruit.com/assets/110384 (Schematic)
* https://learn.adafruit.com/adafruit-qt-py-esp32-s2/downloads
* https://github.com/adafruit/Adafruit-QT-Py-ESP32-S2-PCB

#### Datasheets
* [ESP32-S2 Series Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s2_datasheet_en.pdf)
* [ESP32-S2 Technical Reference Manual](https://www.espressif.com/sites/default/files/documentation/esp32-s2_technical_reference_manual_en.pdf)
* [ESP32-S2 WROVER Technical Reference Manual](https://cdn-learn.adafruit.com/assets/assets/000/096/707/original/esp32-s2-wrover_esp32-s2-wrover-i_datasheet_en.pdf)
* https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/hw-reference/esp32s2/user-guide-saola-1-v1.2.html (esp32s2_saola)

### ESP32-C3
#### Buy
https://www.adafruit.com/product/5405 (Adafruit QT Py ESP32-C3 WiFi Dev Board)

#### Board
https://circuitpython.org/board/adafruit_qtpy_esp32c3/

#### UF2 Bootloader
To install the UF2 bootloader, follow the steps to _Install, Repair, or Update UF2 Bootloader_ at the bottom of https://circuitpython.org/board/adafruit_qtpy_esp32c3/

#### Pinout
<img text="ESP32-C3 Pinout, (c) Adafruit" src="https://cdn-learn.adafruit.com/assets/assets/000/109/663/original/adafruit_products_image.png" width="640"/>

* https://learn.adafruit.com/assets/109663 (Pinout)
* https://learn.adafruit.com/adafruit-qt-py-esp32-c3-wifi-dev-board/pinouts

#### Schematic
<img text="ESP32-C3 Layout, (c) Adafruit" src="https://cdn-learn.adafruit.com/assets/assets/000/109/793/original/adafruit_products_QTC3_sch.png?1647545127" width="640"/>

* https://learn.adafruit.com/assets/109793 (Schematic)
* https://learn.adafruit.com/adafruit-qt-py-esp32-c3-wifi-dev-board/downloads
* https://github.com/adafruit/Adafruit-QT-Py-ESP32-C3-PCB

#### Datasheets
* [ESP32-C3 Series Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf)
* [ESP32-C3 Technical Reference Manual](https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf)

## GPIO & sensors
### Blinky (digital output)
Try [blink](blink)

<img src="QtPyEsp32S2BlinkWiring.png" width="320"/>

### Button (digital input)
Try [button](button)

<img src="QtPyEsp32S2ButtonWiring.png" width="320"/>

### DHT11 temperature & humidity
Try [dht](dht)

<img src="QtPyEsp32S2_TODO.png" width="320"/>

### More sensors
See [TODO](https://TODO)

## Wi-Fi & HTTP
TODO
