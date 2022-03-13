# Magnetometer Encoder

This quick guide/experiment uses the [PiicoDev Magnetometer](https://core-electronics.com.au/piicodev-magnetometer-qmc6310.html "PiicoDev Magnetometer") to read an angle.
### Parts
* [PiicoDev Magnetometer QMC6310](https://core-electronics.com.au/piicodev-magnetometer-qmc6310.html "PiicoDev Magnetometer QMC6310")
* [Small magnet](https://core-electronics.com.au/magnet-square-0-125.html)
* [M.25 standoffs](https://core-electronics.com.au/search/?q=m2.5+standoff)
* 3D printed parts (STL's in Repo)
* [PiicoDev OLED Display Module (128x64) SSD1306](https://core-electronics.com.au/piicodev-oled-display-module-128x64-ssd1306.html)
* [A couple PiicoDev cables](https://core-electronics.com.au/piicodev.html#Cables_1309)
* [PiicoDev Expansion Board for Raspberry Pi Pico](https://core-electronics.com.au/piicodev-expansion-board-for-raspberry-pi-pico.html)
* [Raspberry Pi Pico](https://core-electronics.com.au/raspberry-pi-pico-soldered-headers.html)

*Code uses functions from the [PiicoDev Unified](https://github.com/CoreElectronics/CE-PiicoDev-Unified "PiicoDev Unified"), [PiicoDev Magnetometer QMC631](https://github.com/CoreElectronics/CE-PiicoDev-QMC6310-MicroPython-Module "PiicoDev Magnetometer QMC631")0 and [PiicoDev OLED Module SSD1306](https://github.com/CoreElectronics/CE-PiicoDev-SSD1306-MicroPython-Module "PiicoDev OLED Module SSD1306")* 
Check out those Repo's and guides for more interesting information!
### Function description
**magList()**
Returns a list of the magnetic flux in each axis [X,Y,Z]

**listComp(listOne,listTwo,operator = 0)**
Compares two lists,  (operator; 0=greater than, 1=less than, 2=equal to)
Returns a list with same dimensions with elements corresponding to the operator

**initRotation(delay = 200)**
Figures out which axis the magnet is rotating in and does some quick checking - propmts for the magnet to be rotated
Returns a list of the plane that the magnet is rotating on
*Proposed features*
* Input a function to rotate the magnet with a motor so it can happen automatically
* Retry after a set period (sometimes it freezes up)

**magAngle(caliData)**
Returns the angle of the magnet in radians
Requires the calibration data created in **initRotation()**
