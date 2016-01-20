'''
SOAL 1
classname = Turida, 2 attribut: noRT dan jumPenduduk
fungsitampilDetail() untuk menampilkan data dalam kelas

class Turida:
    def __init__(self, nRT, jPenduduk):
        self.noRT = nRT
        self.jumPenduduk = jPenduduk

    def tampilDetail(self):
        print "Nomor RT : ", self.noRT
        print "Jumlah Penduduk : ", self.jumPenduduk

A = Turida("5", "120")
A.tampilDetail()
'''
'''
SOAL 2
classname = Universitas, isinya :
    attribute: list dengan nama fakultas
    konstruktor, destruktor
    fungsi insert() -> masukkan nama fakultas
    fungsi tampil() -> menampilkan seluruh nama fakulktas yg telah dimasukkan

3 buah objek dari kelas universitas dg nama: unram, ugm, itb
 dengan fungsi insert, masukkan 5 nama fakultas pada masing2 univ, tampilkan dengan fungsi tampil()


class Universitas:
    def __init__(self, nUniv):
        self.fakultas = []
        self.namaUniv = nUniv

    def insertData(self, nFakultas):
        self.namaFakultas = nFakultas
        self.fakultas.append(self.namaFakultas)

    def tampilData(self):
        print "Nama Universitas : ", self.namaUniv
        print "Jurusan yang tersedia : "
        for i in range(len(self.fakultas)):
            print "-", self.fakultas[i]

unram = Universitas("UNRAM")
unram.insertData("Pertanian")
unram.insertData("Informatika")
unram.insertData("Ekonomi")
unram.insertData("Kedokteran")
unram.tampilData()

ugm = Universitas("UGM")
ugm.insertData("Teknik Industri")
ugm.insertData("Teknik Informatika")
ugm.insertData("Teknik Kimia")
ugm.insertData("Teknik Nuklir")
ugm.tampilData()

itb = Universitas("ITB")
itb.insertData("MIPA")
itb.insertData("Informatika")
itb.insertData("Pertambangan")
itb.insertData("SBM")
itb.tampilData()
'''
'''
SOAL 3
2 buah kelas: Hewan (induk) dan Kucing (turunan)
Kelas Hewan, memiliki:
    attribut : nama, jenisKelamin, usia
    fungsi : makan() -> bagaimana hewan itu makan, suara() -> bagaimana suara dari hewan

Kelas Kucing : mewarisi
    atribut nama dan usia
    fungsi suara()


class Hewan:
    def __init__(self, nama, jKelamin, usia):
        self.nama = nama
        self.__jenisKelamin = jKelamin
        self.usia = usia

    def __makan(self):
        print "makan ikan"

    def suara(self):
        print "mengeong"

class Kucing(Hewan):
    def __init__(self):
        Hewan.__init__(self, "Kucing", "Jantan", 15)

A = Kucing()
A.suara()
'''

'''
SOAL 4
4 kelas: Manusia, Pegawai, Guru, Mahasiswa
Manusia :
    atribut : nama, usia
    induk dari Pegawai

Pegawai(Manusia):
    atribut : NIP wajib,
    fungsi : detail pegawai

Guru(Manusia, Pegawai):
    fungsi job() -> mendefinisikan pekerjaan seorang guru

Mahasiswa(Guru):
    fungsi job() -> override job() di Guru
'''

class Manusia:
    def __init__(self, nManusia, uManusia):
        self.nama = nManusia
        self.usia = uManusia

class Pegawai(Manusia):
    def __init__(self, nip, nManusia, uManusia):
        Manusia.__init__(self, nManusia, uManusia)
        self.nip = nip

    def detailPegawai(self):
        print "Nama \t :", self.nama
        print "NIP \t :", self.nip
        print "Usia \t :", self.usia

class Guru(Manusia,Pegawai):
    def __init__(self, nip, nManusia, uManusia):
        Pegawai.__init__(self, nip, nManusia, uManusia)

    def job(self):
        print "Mengajar siswa di kelas"

class Mahasiswa(Guru):
    def __init__(self):
        pass

    def job(self):
        print "Belajar di kelas"


#OPegawai = Pegawai("123456789", "Dewi", 23)
#OPegawai.detailPegawai()

OGuru = Guru("123456789", "Dewi", 23)
OGuru.detailPegawai()
OGuru.job()

OMahasiswa = Mahasiswa()
OMahasiswa.job()
'''

# soal no. 6
class A:
    c = ""
    def __init__(self, nama):
        self.c = nama

    def detail(self):
        print("C : %s" %self.c)

# instansiasi objek
tes = A("dewi")
tes.detail()

# soal no 7
class Mahasiswa:
    nama = ""
    __nim = ""

    def __init__(self, nama, nim):
        self.nama = nama
        self.__nim = nim

class Siswa(Mahasiswa):
    def __init__(self):
        Mahasiswa.__init__(self, nama="Dewi", nim="44151005")

    def tampil(self):
        print(self.nama)
        # print(Mahasiswa.__nim) # nim ga bisa ditampilkan, karena di-set private

sws = Siswa()
sws.tampil()
print("Kelas turunan : ", Siswa.__name__)
print("Kelas induk : ", Siswa.__bases__)

'''