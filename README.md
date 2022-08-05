# Эмулятор отправки значений объектов девайса на MQTT брокер 

Рабочая папка "device-simulator"
1. Установить библиотеки из файла requirements.txt
2. В файл env.py вписать параметры MQTT-соединения
3. Создать девайсы в виде словаря python, в файле есть 5 примеров
    Один из примеров:
        heat_counter = {'name': "heat-counter",
             'TE-1': 56,
             "TE-2": 34,
             'TE-3': 70,
             "TE-4": 60,
             "PE-1": 3.5,
             "PE-2": 2.8,
             "PE-3": 4.2,
             "PE-4": 3.5,
             "massa_in": 2321,
             "massa_out": 923,
             "volume_in": 628,
             "volume_out": 23,
             "heat_power": 2456,
             "heat_energy": 786}
4. Вписать имена девайсов  в переменную DEVICES, находится в файле env.py:
    Например:
        DEVICES = [heat_conter, cool_water_counter]