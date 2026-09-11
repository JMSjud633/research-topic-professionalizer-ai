# ResPro AI — AI Research Topic Professionalization System

<div align="center">

An expert AI web platform that transforms rough, vague, or poorly formulated research ideas into **professional, academically defensible, and feasible research blueprints**.

[![Web App](https://img.shields.io/badge/Web%20Platform-Online%20Access-brightgreen?style=for-the-badge&logo=google-chrome)](https://github.com/JMSjud633/research-topic-professionalizer-ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

### 🌐 [Klik Disini untuk Membuka Aplikasi Langsung (Tanpa Download)](https://render.com/deploy?repo=https://github.com/JMSjud633/research-topic-professionalizer-ai)

> **Pengguna tidak perlu mengunduh (*download*) file apa pun atau menginstal Python.** Cukup buka link aplikasi melalui browser internet di HP atau laptop.

</div>

---

## 🌟 Fitur Utama Platform

1. **Scope & Diagnostic Engine**: Menganalisis apakah ide terlalu luas (*Too Broad*), sudah tepat (*Appropriate*), atau terlalu sempit (*Too Narrow*) disertai pertanyaan kritis penguji.
2. **Variable Matrix**: Mengoperasionalkan variabel (Bebas/X, Terikat/Y, Kontrol/Z, Perancu/W) lengkap dengan indikator ukur dan instrumen kuesioner tervalidasi.
3. **Feasibility & Risk Engine**: Menguji 6 dimensi kelayakan (Waktu, Biaya/Sumber Daya, Data, Sampel, Etika, Teknis) serta mendeteksi bias asumsi.
4. **5 Variasi Judul Akademik**:
   - Opsi A: Konservatif / Formal
   - Opsi B: Spesifik & Terarah
   - Opsi C: Berorientasi Metode
   - Opsi D: Mutakhir / Advance
   - Opsi E: Interdisipliner
5. **Research Blueprint Generator**: Menyusun otomatis Latar Belakang Masalah, Research Gap, Rumusan Masalah, Hipotesis $H_0/H_1$, Metode Sampling, dan Uji Statistik yang Direkomendasikan.
6. **Integrasi Literatur Nyata (Crossref API)**: Pencarian metadata jurnal ilmiah asli secara real-time (*Strictly zero hallucinated citations*).
7. **Ekspor Dokumen**: Unduh hasil rancangan ke format Markdown (`.md`), Teks (`.txt`), atau Cetak ke PDF.

---

## 🛡️ Prinsip Akademik (Anti-Halusinasi)
- **Zero Hallucinated Citations**: Data referensi dicari langsung secara real-time melalui metadata resmi Crossref tanpa mengarang nama penulis, DOI, atau jurnal fiktif.
- **Academic Rigor**: Menitikberatkan pada keketatan desain metodologi dan kelayakan empiris.

---

<details>
<summary>🛠️ <b>Khusus Pengembang / Local Setup (Opsional)</b></summary>

Jika Anda seorang pengembang (*developer*) yang ingin memodifikasi kode sumber secara offline di komputer lokal:

1. Clone repositori:
   ```bash
   git clone https://github.com/JMSjud633/research-topic-professionalizer-ai.git
   cd research-topic-professionalizer-ai
   ```
2. Pasang dependensi:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan server:
   ```bash
   python -m uvicorn backend.main:app --port 8088 --host 127.0.0.1
   ```
   Atau klik `run.bat` di Windows.

</details>

---

## 📄 License
MIT License. Terbuka untuk mahasiswa, dosen, peneliti, dan institusi akademik
