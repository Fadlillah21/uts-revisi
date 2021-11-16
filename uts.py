team = ['cadangan', 'inti']
hari = ['senin','selasa','rabu','kamis','jumat','sabtu','minggu']
minggu = ['pertama', 'kedua', 'ketiga','keempat']

while True:
    #looping team
    print('==jadwal latihan==')
    for a in range(0, len(team)):
        print(f'{a+1}.{team[a]}')
    pilih = int(input('pilih team anda: '))

    #looping minggu
    print('===minggu ke- ===')
    for i in range(0, len(minggu)):
        print(f'{i+1}.{minggu[i]}')
    ming = int(input('pilih minggu :'))

    #looping hari
    print('===hari ===')
    for j in range(0, len(hari)):
        print(f'{j+1}.{hari[j]}')
    har = int(input('masukan hari dengan angka :'))
    print('=============================')
    print('=======jadwal latihan=======')
    print(f'team : {team[pilih-1]}')
    print(f'minggu {minggu[ming-1]}')
    print(f'hari :{hari[har-1]}')

    #looping jadwal
    if har == 1:
        print('latihan')
        break
    elif har == 3:
        print('latihan')
        break
    elif har == 5:
        print('latihan fisik')
        break
    elif har == 7:
        print('sparing')
        break
    else:
        print('libur')
        break
print('==============================')