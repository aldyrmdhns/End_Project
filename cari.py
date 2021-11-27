data = {
    101 : {'Nama' : 'Anthony Stark', 'Umur' : 28, 'Jenis Kelamin' : 'Laki Laki', 'Bidang' : 'IT'},
    113 : {'Nama' : 'Nicholas Roven', 'Umur' : 27, 'Jenis Kelamin' : 'Laki Laki', 'Bidang' : 'Humas'},
    122 : {'Nama' : 'Marie Labelle', 'Umur' : 26, 'Jenis Kelamin' : 'Perempuan', 'Bidang' : 'Keuangan'},
    110 : {'Nama' : 'Rick Ashford', 'Umur' : 21, 'Jenis Kelamin' : 'Laki Laki', 'Bidang' : 'IT'}
} 

cari = input('Masukkan Nama Pegawai : ')
cari = cari.title()

for id, info in data.items():
    if cari in info.values():
        for key, value in info.items():
            print(key, ':', value)
    elif cari not in info.values():
        print('no')
