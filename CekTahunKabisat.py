tahun = int(input("Cek Tahun Kabisat! Masukan Tahun : "))

def TahunKabisat(tahun):
    if (tahun % 4) == 0:
        if (tahun % 100) == 0:
            if (tahun % 400) == 0:
                print('TAHUN', tahun , 'ADALAH TAHUN KABISAT')
            else:
                print('TAHUN' , tahun , 'ADALAH BUKAN TAHUN KABISAT')
        else:
            print('TAHUN', tahun , 'ADALAH TAHUN KABISAT')
    else:
        print('TAHUN' , tahun , 'ADALAH BUKAN TAHUN KABISAT')

TahunKabisat(tahun)