import smbus

DEVICE = 0x23
bus = smbus.SMBus(1)
ONE_TIME_HIGH_RES_MODE_1 = 0x20


def convert_to_number(data):
    result = (data[1] + (256 * data[0])) / 1.2
    return result


def read_light(addr=DEVICE):
    data = bus.read_i2c_block_data(addr, ONE_TIME_HIGH_RES_MODE_1)
    return convert_to_number(data)


def get_light(time):
    value = read_light()
    x = {"sensorID": "0", "typeSensor": "light", "typeValue": "float", "value": value, "time": str(time)}
    return x


def signals():
    from gpiozero import LED
    red = LED(16)
    green = LED(20)
    blue = LED(21)
    current = red
    import time
    while True:
        val = read_light()
        if val > 20:
            if current is not blue:
                current.off()
                current = blue
                current.on()
        elif val > 60:
            if current is not green:
                current.off()
                current = green
                current.on()
        else:
            if current is not red:
                current.off()
                current = red
                current.on()
        time.sleep(1)