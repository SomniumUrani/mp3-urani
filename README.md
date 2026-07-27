# MP3 - Urani House

## Button layout

![xd](img/button_layout.jpg)

## Electric chars

| Description   | Num             | V min | typ | V max | mA  |
| ------------- | --------------- | ----- | --- | ----- | --- |
| MCU           | STM32F412       | 1.7   | -   | 3.6   | 30  |
| MCU           | ESP32           | 3     | 3.3 | 3.6   | 450 |
| LCD backlight | HS24CG003-ARX   | 2.8   | 3   | 3.2   | 80  |
| LCD vdd       | NHS24CG003-ARXA | 1.65  | 1.8 | 3.3   | -   |
| IO expander   | PCF8574T        | 2.5   | -   | 6     | 25  |
| DAC           | PCM5102A        | 3.1   | 3.3 | 3.46  | 10  |

## Components stuff
### Special outsource components on PCB

| Name                  | MPN                   | Source | Source No. | Description                                                                                 |
| --------------------- | --------------------- | ------ | ---------- | ------------------------------------------------------------------------------------------- |
| LCD                   | HS24CG003-ARX         | LCSC   | C5329583   | 240*320 dots (RGB) SPI INTERFACE                                                            |
| FPC connector for LCD | LW10251-16            | LCSC   | C375934    | CONN FFC FPC 16POS 1mm TOP CNT SMD R/A                                                      |
| TF slot               | TF PUSH               | LCSC   | C393941    | CONN MICRO SD CARD (TF CARD) PUSH-PUSH SMD                                                  |
| Debug Slider          | YSSP2AG00             | LCSC   | C5188558   | 300mA Surface Mount,Vertical DPDT 4V SMD Slide Switches RoHS                                |
| Audio Jack            | PJ-393-7A             | LCSC   | C128990    | CONN JACK STEREO 3.5mm SMD                                                                  |
| Crystal oscilator     | 2.D.1.260000704       | LCSC   | C42420962  | CRYSTAL 26MHz 7pF SMD                                                                       |
| PUSH switch           | R4A25211L             | LCSC   | C49393629  | 30,000 cycles 50mA Without SPST-NO Rectangular Button 12V 1.8N SMD Pushbutton Switches RoHS |
| Thermistor            | HNTC0805-104F3950FB   | LCSC   | C49247664  | 100kΩ 140uA 3950K ±1% 200mW ±1% 0805 NTC Thermistors RoHS                                   |
| USB c receptacle      | TYPE-C 16PIN 2MD(073) | LCSC   | C2765186   | CONN RCPT Type-C 16POS SMD R/A                                                              |

### Common components selection

| Name           | MPN                 | Source | Source No. | Description                            |
| -------------- | ------------------- | ------ | ---------- | -------------------------------------- |
| Inductor 1uH   | SNH.4020.TYB1R0MT00 | LCSC   | C2942331   | FIXED IND 1uH 2.15A 0.037Ω SMD,4x4mm   |
| Inductor 2.2uH | MNR4018T220MT       | LCSC   | C18222010  | FIXED IND 22uH 0.36Ω SMD,4x4mm         |
| GREEN LED      | XL-2012UGC          | LCSC   | C965815    | LED EMERALD GREEN WATER CLEAR 0805 SMD |
| BLUE LED       | XL-2012UBC          | LCSC   | C965817    | LED BLUE WATER CLEAR 0805 SMD          |
| RED LED        | XL-2012SURC         | LCSC   | C965812    | LED RED WATER CLEAR 0805 SMD           |



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
