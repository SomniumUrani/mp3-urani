# MP3 - Urani House

## Button layout

![xd](img/button_layout.jpg)

## Special outsource components on PCB

| Name                  | MPN             | Source | Source No. | Description                                                  |
| --------------------- | --------------- | ------ | ---------- | ------------------------------------------------------------ |
| LCD                   | HS24CG003-ARX   | LCSC   | C5329583   | 240*320 dots (RGB) SPI INTERFACE                             |
| FPC connector for LCD | LW10251-16      | LCSC   | C375934    | CONN FFC FPC 16POS 1mm TOP CNT SMD R/A                       |
| TF slot               | TF PUSH         | LCSC   | C393941    | CONN MICRO SD CARD (TF CARD) PUSH-PUSH SMD                   |
| Debug Slider          | YSSP2AG00       | LCSC   | C5188558   | 300mA Surface Mount,Vertical DPDT 4V SMD Slide Switches RoHS |
| Audio Jack            | PJ-393-7A       | LCSC   | C128990    | CONN JACK STEREO 3.5mm SMD                                   |
| Crystal oscilator     | 2.D.1.260000704 | LCSC   | C42420962  | CRYSTAL 26MHz 7pF SMD                                        |

## Electric chars

| Description   | Num             | V min | typ | V max | mA  |
| ------------- | --------------- | ----- | --- | ----- | --- |
| MCU           | STM32F412       | 1.7   | -   | 3.6   | 30  |
| MCU           | ESP32           | 3     | 3.3 | 3.6   | 450 |
| LCD backlight | HS24CG003-ARX   | 2.8   | 3   | 3.2   | 80  |
| LCD vdd       | NHS24CG003-ARXA | 1.65  | 1.8 | 3.3   | -   |
| IO expander   | PCF8574T        | 2.5   | -   | 6     | 25  |
| DAC           | PCM5102A        | 3.1   | 3.3 | 3.46  | 10  |

## Communication protocols peripherals

### SPI - MISO/MOSI

| Peripheral | Max speed | Use          |
| ---------- | --------- | ------------ |
| SPI 1      | 50 Mbit/s | LCD          |
| SPI 2      | 25 Mbit/s | None         |
| SPI 3      | 25 Mbit/s | None         |
| SPI 4      | 50 Mbit/s | None         |
| SPI 5      | 50 Mbit/s | LCD touch IC |

### I2C - SDA/SCL

Their frequency can be increased up to 1 MHz. For more details on
the complete solution, refer to the nearest STMicroelectronics sales office.

| Peripheral | Max speed | Use           |
| ---------- | --------- | ------------- |
| I2C x      | 1 MHz     | None          |
| I2C x      | 400 KHz   | HMI expansion |
| I2C x      | 400 KHz   | None          |
| I2C x      | 400 KHz   | None          |
