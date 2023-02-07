from scapy.layers.inet import IP, ICMP, UDP

isrun = True

while isrun:
    try:
        src = input('Введите адрес отправителя: ')
        dst = input('Введите адрес получателя: ')

        sport = int(input('Введите порт отправителя: '))
        dport = int(input('Введите порт получателя: '))
        buff_1 = src.split('.')
        buff_2 = sport
        buff_3 = dst.split('.')
        buff_4 = dport
        if ((255 <= buff_2) and (buff_2 <= 65535) and (255 <= buff_4) and (buff_4 <= 65535)):
            if (len(buff_1) == 4 and len(buff_3) == 4):
                if (1 <= int(buff_1[0]) <= 255 and 1 <= int(buff_1[1]) <= 255 and 1 <= int(
                        buff_1[3]) <= 255 and 1 <= int(buff_1[2]) <= 255 and 1 <= int(buff_3[0]) <= 255 and 1 <= int(
                        buff_3[1]) <= 255 and 1 <= int(buff_3[3]) <= 255 and 1 <= int(buff_3[2]) <= 255):
                    isrun = False
                else:
                    print(str(buff_1) + str(buff_3))
                    print("Ошибка в адресе. Попробуйте еще раз")

                    isrun = True
            else:
                print("Ошибка в адресе (длина). Попробуйте еще раз")
                isrun = True
        else:
            print("Ошибка в порте. Попробуйте еще раз")
            isrun = True

    except Exception:
        print("Ошибка. Попробуйте еще раз")
        isrun = True

isrun = True
while isrun:
    try:
        package = IP(src=src, dst=dst) / UDP(sport=sport, dport=dport)
        print(package.show2(dump=True))
        isrun = False
    except Exception:
        print("Ошибка. Попробуйте еще раз")
        isrun = True
