def hitung_biaya_hotel(jenis_kamar, durasi_menginap):
    tarif = 0
    if jenis_kamar.lower() == "standard": #lower digunakan agar input "Standard","standard", "STANDARD"
        tarif = 200000
    elif jenis_kamar.lower() == "deluxe":
        tarif = 350000
    else: 
        print("Kamar tidak ditemukan!")
        return 0
    
    total_biaya = tarif * durasi_menginap
    return total_biaya

print("=====================PEMESANAN HOTEL==========================")
jenis_kamar = input("Pilih jenis kamar (deluxe/standard): ")
tgl_checkin = int(input("Pilih tanggal check-in (Harus berupa angka!): "))
tgl_checkout = int(input("Pilih tanggal check-out(Harus berupa angka!): "))

durasi_menginap = tgl_checkout - tgl_checkin

total_biaya = hitung_biaya_hotel(jenis_kamar, durasi_menginap)

print("=================DETAIL PESANAN HOTEL================")
print("Jenis Kamar: ", jenis_kamar)
print("Tanggal Check-In: ", tgl_checkin)
print("Tanggal Check-Out: ", tgl_checkout)
print("Durasi Menginap: ", durasi_menginap, "Malam")
print("=====================================================")
print("Total Biaya: ", total_biaya)


