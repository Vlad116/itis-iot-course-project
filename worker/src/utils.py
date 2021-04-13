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
