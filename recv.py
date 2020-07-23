import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev


GPIO.setmode(GPIO.BCM)

pipes =[[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2,]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 17)  # Aктивировать модуль ("CSN" to RPi GPIO#8 "CE0","CE" to RPi GPIO#17)

radio.setPayloadSize(32)# Размер пакета, в байтах
radio.setChannel(0x60)# Выбираем канал (На котором нет шумов!)

radio.setDataRate(NRF24.BR_2MBPS)# Cкорость обмена.
# На выбор NRF24.BR_2MBPS, NRF24.BR_1MBPS, NRF24.BR_250KBPS
radio.setPALevel(NRF24.PA_MIN)# Уровень мощности передатчика.
# На выбор NRF24.PA_MIN, NRF24.PA_LOW, NRF24.PA_HIGH, NRF24.PA_MAX
radio.setAutoAck(True)# Режим подтверждения приёма
# (True=вкл) (Fail=выкл)

radio.enableDynamicPayloads()# Разрешить динамически изменяемый размер блока данных на всех трубах.
radio.enableAckPayload()# Разрешить отсылку данных в ответ на входящий сигнал


radio.openReadingPipe(1, pipes[1])# Открываем 1 трубу с адресом 1 передатчика [0xc2, 0xc2, 0xc2, 0xc2, 0xc2,], для приема данных.
radio.printDetails()# Получить дамп информации о текущих настройках модуля.


radio.startListening() # Включаем приемник, начинаем прослушивать открытые трубы.

while True:
    askPL = [1]
    while not radio.available(0):
        time.sleep(1/100)

    receivedMessage = []
    radio.read(receivedMessage, radio.getDynamicPayloadSize())
    print("Получил: {}".format(receivedMessage))

    print("Перевод полученного сообщения в символы юникода ...")
    string = ""
    for n in receivedMessage:
        # Декодировать в стандартный набор Unicode
        if (n >= 32 and n <= 126):
            string += chr(n)
    print(string)

    radio.writeAckPayload(1, askPL, len(askPL))
    print("Загруженный ответ полезной нагрузки {}".format(askPL))
