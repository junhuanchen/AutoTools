# coding:utf-8

try:    
    import serial.tools.list_ports

    print("Looking for upload port...")
    plist = list(serial.tools.list_ports.comports())

    serialName = ''

    if len(plist) <= 0:
        print("Serial Not Found!")
    else:
        plist_0 = list(plist[len(plist) - 1])
        serialName = plist_0[0]
        print("Auto-detected:" + serialName)

    FLASH_MODE = "dio"
    FLASH_FREQ = "40m"

    FLASH_START = "0x1000"

    from esptool import main 

    import sys

    bak = sys.argv

    sys.argv = [
            'AutoFlash.py', '--chip', 'esp32', 
            '--port', serialName, 
            '--baud', '460800', # 921600
            'write_flash', '-z',
            '--flash_mode', FLASH_MODE, 
            '--flash_size', '4MB',
            '--flash_freq', FLASH_FREQ,
            FLASH_START, 'firmware.bin'
    ]

    try:
            pos = bak.index('--port')
            if pos is not False:
                    sys.argv[4] = bak[pos + 1]
    except ValueError:
            pass

    try:
            pos = bak.index('--baud')
            if pos is not False:
                    sys.argv[6] = bak[pos + 1]
    except ValueError:
            pass

    # print(sys.argv)

    main()
except Exception as e:
    print(e)

import os
os.system("pause")
