# Параметры MQTT-соединения
MQTT_PARAMS = {'PUBLISHER': "lutyisan", # Имя клиента (любое)
               'TRANSPORT': "websockets", # Выбор протокола tcp или websockets
               'PATH': "/ws", # URL
               'USER_NAME': "admin", # Логин
               'USER_PASS': "admin",  # Пароль
               'HOST': "46.8.210.67",  # Адрес брокера
               'PORT': 15675,  # Порт брокера
               'SLEEPING_TIME': 3} # Период оиправки данных

# dict девайса с сигналами
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

# dict девайса с сигналами
el_counter = {'name': "el-counter",
           'volt_a': 221,
           "volt_b": 219,
           'volt_c': 223,
           "curr_a": 34,
           "curr_b": 32,
           "curr_c": 29,
           "act_en": 2245,
           "react_en": 237,
           "full_en": 2700,
           "act_pow": 6.00,
           "react_pow": 4.00,
           "full_pow": 9.00,
           }

# dict девайса с сигналами
cool_water_counter = {"name": 'cool-water', "volume": 4356}

# dict девайса с сигналами
heat_water_counter = {'name': "heat-water", "volume": 3871}

# dict девайса с сигналами
dn_station = {'name': "dn-1",
                   "pump1_work": False,
                   "pump1_alarm": True,
                   "pump2_work": False,
                   "pump2_alarm": True,
                   "ls-1": True,
                   "ls-2": False,
                   "ls_3": False}

# dict девайса с сигналами
ahu = {'name': "ahu",
                   "te_oat": 25.8,
                   "te_sf": 23.1,
                   "te_rf": 24.5,
                   "te_heat": 38.3,
                   "heat_valve": 1.0,
                   "cool_valve": 76.2,
                   "rec_valve": 10.6,
                   "sf_state": True,
                   "rf_state": False,
                   "heat_pump_state": False,
                   "cool_pump_state": True,
                   "rec_pump_state": False,
                   "sf_dumper": True,
                   "rf_dumper": False,
                   "rec_dumper": True,
                   "termostat": False,
                   "flter_1": True,
                   "filter_2": True,
                   "filter_3": False,
                   "start_ahu": True,
                   "temp_set": 22,
                   "season": 1,
                   "start_heat_pump": 2,
                   "start_cool_pump": 2,
                   "start_rec_pump": 2,
                   "start_sf_dumper": True,
                   "start_rf_dumper": False,
                   "start_rec_dumper": True
                   }
itp = {"name": "itp",
       "te_1": 68.3,
       "te_2": 62.3,
       "te_3": 60.3,
       "te_4": 51.3,
       "te_5": 65.3,
       "te_6": 57.3,
       "pe_1": 4.6,
       "pe_2": 3.6,
       "pe_3": 4.4,
       "pe_4": 4.1,
       "valve_1": 34,
       "valve_2": 12,
       "pump_1": True,
       "pump_2": False,
       "pump_3": False,
       "pump_4": True,
       "dps_1": True,
       "dps_2": False,
       "dps_3": False,
       "dps-4": True,
       "set_gvs_temp": 55.0,
       "set_ot_temp": 68
       }
DEVICES = [heat_counter, el_counter, cool_water_counter, heat_water_counter, dn_station,ahu, itp]

