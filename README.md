# Deteksi Rambut Panjang

Proyek ini bertujuan untuk mendeteksi panjang rambut menggunakan model machine learning yang diimplementasikan dengan Flask sebagai backend dan TailwindCSS untuk tampilan frontend. Proyek ini mendemonstrasikan cara mengintegrasikan Python dengan model machine learning dan menampilkan hasil deteksi di web menggunakan desain yang responsif dengan TailwindCSS.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Introduction

Aplikasi ini memungkinkan pengguna untuk mengunggah gambar dan mendeteksi apakah gambar tersebut menunjukkan seseorang dengan rambut panjang. Deteksi dilakukan menggunakan model machine learning yang telah dilatih sebelumnya, dengan Flask sebagai server untuk menangani logika backend dan TailwindCSS untuk styling tampilan web.

## Installation

### Prerequisites
- **Python 3.x**
- **Node.js** dan **npm** (Node Package Manager) untuk TailwindCSS

### Langkah-langkah Instalasi

1. Clone repository ini:
    ```bash
    git clone https://github.com/WayuAji30/deteksi-rambut-panjang.git
    cd deteksi-rambut-panjang
    ```

2. Install dependencies untuk Python:
    ```bash
    pip install -r requirements.txt
    ```

3. Install dependencies untuk TailwindCSS menggunakan npm:
    ```bash
    npm install
    ```

## Usage

### Menjalankan Aplikasi

Untuk menjalankan aplikasi Flask dan memulai TailwindCSS dalam mode pengembangan, ikuti langkah-langkah berikut:

1. Jalankan server Flask dengan perintah berikut:
    ```bash
    python main.py
    ```

   Server Flask akan berjalan di `http://127.0.0.1:5000/`.

2. Di terminal lain, jalankan TailwindCSS dengan perintah:
    ```bash
    npm run dev
    ```

   Perintah ini akan memonitor perubahan pada file CSS dan mengompilasi ulang TailwindCSS secara otomatis. Pastikan kedua terminal berjalan bersamaan.

## Features

- **Upload Gambar**: Pengguna dapat mengunggah gambar untuk dideteksi.
- **Deteksi Rambut Panjang**: Sistem menggunakan model machine learning untuk mendeteksi panjang rambut.
- **Responsif**: Tampilan website didesain agar responsif di berbagai perangkat menggunakan TailwindCSS.

## Dependencies

- **Flask**: Framework Python untuk menangani backend dan routing.
- **TailwindCSS**: Framework utilitas CSS untuk styling responsif.
- **Numpy, OpenCV, TensorFlow/Keras**: Digunakan dalam model machine learning untuk deteksi gambar.
- **Node.js & npm**: Digunakan untuk mengelola dependencies frontend dan mengembangkan TailwindCSS.

## Configuration

- **Flask Configuration**: Konfigurasi aplikasi Flask dapat disesuaikan di file `main.py`.
- **TailwindCSS Configuration**: Konfigurasi TailwindCSS dapat diubah di file `tailwind.config.js`.

## Troubleshooting

- **Masalah saat menjalankan Flask**: Pastikan Anda telah menginstall semua dependencies Python yang diperlukan. Jika ada error, coba jalankan perintah `pip install -r requirements.txt` kembali.
- **CSS tidak ter-update**: Jika perubahan pada styling tidak terlihat, pastikan `npm run dev` berjalan agar TailwindCSS dapat dikompilasi secara otomatis.
- **Model Machine Learning Error**: Pastikan model yang digunakan sudah dilatih dengan benar dan file model tersedia di direktori proyek.

## Contributors

- BAMBI TEAM

## License

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
