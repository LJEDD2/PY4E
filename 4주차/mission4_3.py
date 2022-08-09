def wrong_guest_book(guest_book):
    filehand = open('m4_3.txt','w')
    filehand.write(guest_book)
    filehand.close()


    file = open("m4_3.txt")
    for line in file:
        sep = line.find(',')
        g_name = line[0:sep]
        g_phone = line[sep+1:].rstrip()
        #print(g_name,g_phone)

        if not g_phone.startswith('010') or '-' not in g_phone or len(g_phone) != 13:
            print(f'잘못 쓴 사람 : {g_name}')
            print(f'잘못 쓴 번호 : {g_phone}\n')

guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

wrong_guest_book(guest_book)