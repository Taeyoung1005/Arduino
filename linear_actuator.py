from serial import Serial
from time import time
from datetime import datetime

def sensor_log() : 
    thres = 300
    is_end = None
    is_start = False
    dateformat = "%Y-%m-%d %H:%M:%S"
    command_input = True
    final = None
    is_final = None

    arduino = Serial(
        port='COM6',   # Window
        baudrate=9600 # 보드 레이트 (통신 속도)
    )

    while True:
        if arduino.readable() : 
            ma = arduino.readline().decode()
            ma = float(ma.strip('\n').strip('\r'))
            if command_input == True and final != '3':
                while True:
                    command = input('아두이노에게 내릴 명령 (0-줄어듬, 1-늘어남, 2-멈춤): ')

                    if command == '0':
                        length_var = '0'
                    elif command == '1':
                        length_var = '1'
                    
                    if command == '0' or command =='1' or command =='2':
                        break
                if command == '0' or command == '1':
                    final = input('아두이노에게 내릴 명령 (3-끝까지): ')

                arduino.write(command.encode())
                command_input = False
                # if command == '2':
                #     command_input = True
                # else:
                #     command_input = False

            if ma >= thres and not is_start:
                start = time()
                start_time = datetime.now().strftime(dateformat)
                is_start = True
                is_end = True
                is_final = False
                command_input = True
            
            if ma < thres and is_end:
                end = time()
                end_time = datetime.now().strftime(dateformat)
                act_time = round(end-start, 2)
                if length_var == '1':
                    length = act_time * 11.441647597254
                elif length_var == '0':
                    length = act_time * 11.76470588235294
                length = round(length, 2)
                save(start_time, end_time, act_time, length)
                print(f'{start_time} ~ {end_time} {act_time}초 {length}mm')
                is_end = False
                is_start = False
                is_final = True
                command_input = True

            if is_final == True:
                final = None
                is_final = False

def save(start_time, end_time, act_time, length):
    file = open('./activate_time.txt', 'a', encoding='UTF-8')
    file.write(f'{start_time} ~ {end_time} {act_time}초 {length}mm\n')    
   
sensor_log()
        