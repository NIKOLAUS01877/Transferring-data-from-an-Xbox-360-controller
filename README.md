# Transferring-data-from-an-Xbox-360-controller
Data transfer from an Xbox 360 controller connected to a Raspberry Pi via NRF24L01 + PA + LNA radio modules.

Connecting nRF24L01 + to Raspberry Pi<br/>
nRF24L01+	Raspberry Pi<br/>
GND	6 / GND<br/>
VCC	1 / 3.3V<br/>
CE	11 / GPIO17<br/>
CSN	24 / GPIO8 / SPI_CE0_N<br/>
SCK	23 / GPIO11 / SPI0_CLK<br/>
MOSI	19 / GPIO10 / SPI0_MOSI<br/>
MISO	21 / GPIO9 / SPI0_MISO<br/>
IRQ	—<br/>
Links to used libraries<br/>
lib_nrf24<br/>
https://github.com/BLavery/lib_nrf24<br/>
Gamepad<br/>
https://github.com/piborg/Gamepad<br/>
