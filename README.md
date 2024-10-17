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

### Menjalankan Aplikasi Flask

Untuk menjalankan aplikasi Flask, gunakan perintah berikut:
```bash
python main.py

### Menjalankan Tailwind CSS

Untuk menjalankan Tailwind CSS, gunakan perintah berikut:
```bash
npm run dev