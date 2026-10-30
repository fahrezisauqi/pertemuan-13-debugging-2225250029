
# Pertemuan 13 - Debugging dan Testing

**Nama:** Fahrezi Sauqi Alghani  
**NIM:** 2225250029  
**Kelas:** 3E

## Kasus
Program digunakan untuk menghitung rata-rata nilai,
menentukan status kelulusan, dan mencari nilai tertinggi.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| T1 | [80,60,90,70] | 75.0 | 60.0 | FAIL |
| T2 | [100,80] | 90.0 | 36.0 | FAIL |
| T3 | 60 | Lulus | Tidak lulus | FAIL |
| T4 | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | [80,60,90,70] | 90 | 0 | FAIL |

## Bug Report

### Bug 1 - Rata-rata
Penyebab: Program selalu membagi jumlah nilai dengan 5.
Perbaikan: Menggunakan len(nilai).

### Bug 2 - Status kelulusan
Penyebab: Operator menggunakan > 60.
Perbaikan: Menggunakan >= 60.

### Bug 3 - Nilai tertinggi
Penyebab: Operator perbandingan menggunakan <.
Perbaikan: Menggunakan > dan memulai dari nilai pertama.

## Retest
T1: PASS - 75.0
T2: PASS - 90.0
T3: PASS - Lulus
T4: PASS - Tidak lulus
T5: PASS - 90

## Cara Menjalankan

py praktik/praktik_4_debugging.py

## Refleksi
Debugging membantu menemukan kesalahan program.
Test case membantu membandingkan hasil yang diharapkan
dengan hasil aktual. Setelah perbaikan, program harus
diuji kembali agar tidak menimbulkan bug baru.
