#include <iostream>
using namespace std;

int main() {
    // ===== DATA PLAYSTATION =====
    string kodePS = "";
    string tipePS = "";
    int hargaPerJam = 0;

    // ===== DATA PENYEWAAN =====
    string namaPenyewa = "";
    int lamaSewa = 0;
    int totalBayar = 0;

    int menu, pilih;
    char kembali;

    do {
        cout << "\n====================================\n";
        cout << "SISTEM RENTAL PLAYSTATION\n";
        cout << "====================================\n";
        cout << "1. Mengelola PlayStation\n";
        cout << "2. Penyewaan PlayStation\n";
        cout << "3. Pembayaran PlayStation\n";
        cout << "0. Keluar\n";
        cout << "====================================\n";
        cout << "Masukkan Pilihan: ";
        cin >> menu;

        // ================= MENU 1 =================
        if (menu == 1) {
            pilih = -1;
            do {
                cout << "\nHALAMAN MENGELOLA PLAYSTATION\n";
                cout << "================================\n";
                cout << "1. Tambah PlayStation\n";
                cout << "2. Edit PlayStation\n";
                cout << "3. Lihat PlayStation\n";
                cout << "0. Kembali\n";
                cout << "================================\n";
                cout << "Masukkan Pilihan: ";
                cin >> pilih;

                // ----- Tambah -----
                if (pilih == 1) {
                    cout << "\nFORM TAMBAH PLAYSTATION\n";
                    cout << "================================\n";
                    cout << "Input Kode PlayStation : ";
                    cin >> kodePS;
                    cout << "Input Tipe PlayStation : ";
                    cin >> tipePS;
                    cout << "Input Harga / Jam      : ";
                    cin >> hargaPerJam;

                    cout << "Data berhasil ditambahkan.\n";
                    cout << "Kembali ke menu kelola? (Y/T): ";
                    cin >> kembali;
                    if (kembali == 'T' || kembali == 't')
                        pilih = 0;
                }

                // ----- Edit -----
                else if (pilih == 2) {
                    if (kodePS == "") {
                        cout << "Data belum tersedia.\n";
                    } else {
                        cout << "Tipe PlayStation Baru : ";
                        cin >> tipePS;
                        cout << "Harga / Jam Baru      : ";
                        cin >> hargaPerJam;
                        cout << "Data berhasil diubah.\n";
                    }

                    cout << "Kembali ke menu kelola? (Y/T): ";
                    cin >> kembali;
                    if (kembali == 'T' || kembali == 't')
                        pilih = 0;
                }

                // ----- Lihat (INI YANG DIPERBAIKI) -----
                else if (pilih == 3) {
                    if (kodePS == "") {
                        cout << "Belum ada data PlayStation.\n";
                    } else {
                        cout << "\nKode PlayStation : " << kodePS << endl;
                        cout << "Tipe PlayStation : " << tipePS << endl;
                        cout << "Harga / Jam      : Rp " << hargaPerJam << endl;
                    }

                    cout << "Kembali ke menu kelola? (Y/T): ";
                    cin >> kembali;
                    if (kembali == 'T' || kembali == 't')
                        pilih = 0;
                }

            } while (pilih != 0);
        }

        // ================= MENU 2 =================
        else if (menu == 2) {
            if (kodePS == "") {
                cout << "\nData PlayStation belum tersedia.\n";
            } else {
                cout << "\nHALAMAN PENYEWAAN PLAYSTATION\n";
                cout << "================================\n";
                cout << "Nama Penyewa      : ";
                cin >> namaPenyewa;
                cout << "Lama Sewa (jam)   : ";
                cin >> lamaSewa;

                totalBayar = lamaSewa * hargaPerJam;

                cout << "Data penyewaan berhasil disimpan.\n";
            }
        }

        // ================= MENU 3 =================
        else if (menu == 3) {
            if (lamaSewa == 0) {
                cout << "\nBelum ada data penyewaan.\n";
            } else {
                cout << "\nHALAMAN PEMBAYARAN PLAYSTATION\n";
                cout << "================================\n";
                cout << "Nama Penyewa : " << namaPenyewa << endl;
                cout << "Lama Sewa    : " << lamaSewa << " jam\n";
                cout << "Total Bayar  : Rp " << totalBayar << endl;
                cout << "Pembayaran berhasil.\n";
            }
        }

    } while (menu != 0);

    cout << "\nTerima kasih telah menggunakan sistem.\n";
    
    return 0;
}
