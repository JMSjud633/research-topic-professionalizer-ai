from typing import List, Tuple
from ..models import VariableItem

def extract_and_operationalize_variables(raw_idea: str, domain: str) -> List[VariableItem]:
    text = raw_idea.lower()
    variables = []
    
    if "cuaca" in text or "iklim" in text or "suhu" in text:
        variables.append(VariableItem(
            variable="Variabilitas Iklim Mikro & Parameter Termal",
            category="Independent Variable (X)",
            definition="Fluktuasi kondisi atmosferik lokal di lingkungan sekolah yang memengaruhi kenyamanan fisiologis.",
            indicator="Suhu ambien (°C), Kelembapan relatif (%RH), dan Wet-Bulb Globe Temperature (WBGT).",
            measurement="Data kontinu numerik berskala rasio, dicatat interval per jam.",
            instrument="Stasiun cuaca otomatis / Data logger termo-higrometer terkalibrasi."
        ))
        
        variables.append(VariableItem(
            variable="Insidensi Gangguan Kesehatan Akut / Tingkat Morbiditas",
            category="Dependent Variable (Y)",
            definition="Manifestasi gangguan kesehatan fisik atau gejala akut yang dialami siswa selama periode observasi.",
            indicator="Frekuensi keluhan respiratori akut, kelelahan termal (heat fatigue), dan angka absensi sakit harian.",
            measurement="Frekuensi kejadian (count data) dan skor keparahan gejala (skala Likert 1-5).",
            instrument="Logbook absensi Unit Kesehatan Sekolah (UKS) & Kuesioner skrining gejala tervalidasi."
        ))
        
        variables.append(VariableItem(
            variable="Ventilasi & Karakteristik Fisik Ruang Kelas",
            category="Control Variable (Z)",
            definition="Kondisi arsitektur dan pendinginan ruangan yang dapat memoderasi paparan cuaca luar.",
            indicator="Rasio ventilasi alami, ada/tidaknya pendingin ruangan (AC), kepadatan siswa per m².",
            measurement="Skala kategorikal (Berventilasi AC / Alami) dan numerik m² per siswa.",
            instrument="Lembar observasi audit sarana lingkungan belajar."
        ))
        
        variables.append(VariableItem(
            variable="Status Imunitas & Kebiasaan Hidrasi Siswa",
            category="Confounding Variable (W)",
            definition="Faktor internal individu yang dapat memengaruhi kerentanan kesehatan terlepas dari faktor cuaca.",
            indicator="Volume asupan cairan harian (ml), status gizi (IMT/U), dan riwayat alergi/asma.",
            measurement="Mililiter per hari, indeks massa tubuh, data biner riwayat penyakit penyerta.",
            instrument="Formulir riwayat medis awal (medical history) & recall hidrasi 24 jam."
        ))
        
    elif "ai" in text or "kecerdasan buatan" in text or "chatgpt" in text:
        variables.append(VariableItem(
            variable="Intensitas & Pola Pemanfaatan AI Generatif",
            category="Independent Variable (X)",
            definition="Tingkat keterlibatan dan frekuensi interaksi siswa dalam memanfaatkan platform AI untuk tugas belajar.",
            indicator="Durasi penggunaan harian (menit/minggu), ragam tugas yang dibantu (ideasi, drafting, debugging).",
            measurement="Skala ordinal/interval berbasis frekuensi penggunaan terukur.",
            instrument="Kuesioner adopsi teknologi terstandar (Technology Acceptance Model scale) & log aktivitas."
        ))
        variables.append(VariableItem(
            variable="Kemandirian & Regulasi Diri dalam Belajar (Self-Regulated Learning)",
            category="Dependent Variable (Y)",
            definition="Kemampuan kognitif dan metakognitif siswa dalam mengelola proses belajar secara mandiri.",
            indicator="Perencanaan belajar, monitoring pemahaman, dan evaluasi hasil belajar secara mandiri.",
            measurement="Skor komposit skala interval (skala Likert 1-5).",
            instrument="Motivated Strategies for Learning Questionnaire (MSLQ) adaptasi Indonesia."
        ))
        variables.append(VariableItem(
            variable="Jenjang Pendidikan & Bidang Peminatan",
            category="Control Variable (Z)",
            definition="Karakteristik akademik responden yang dikendalikan agar tidak membiasakan interpretasi.",
            indicator="Kelas/Tingkat, jurusan (MIPA/IPS/Vokasi), dan kurikulum yang berlaku.",
            measurement="Data kategorikal nominal.",
            instrument="Kuesioner demografi responden."
        ))
        variables.append(VariableItem(
            variable="Literasi Digital & Motivasi Intrinsik Awal",
            category="Confounding Variable (W)",
            definition="Kompetensi teknologi awal dan dorongan internal yang secara independen memengaruhi hasil belajar.",
            indicator="Skor tes literasi digital dasar dan skor motivasi awal sebelum intervensi.",
            measurement="Skor tes kognitif dan inventori psikologis.",
            instrument="Rubrik asesmen literasi digital & Academic Motivation Scale (AMS)."
        ))
    else:
        variables.append(VariableItem(
            variable="Faktor Determinan / Variabel Bebas Utama",
            category="Independent Variable (X)",
            definition="Kondisi atau variabel prediktor yang dihipotesiskan memengaruhi fenomena yang diteliti.",
            indicator="Indikator terukur spesifik yang mencerminkan intensitas atau keberadaan faktor.",
            measurement="Skala metrik (interval/rasio) atau kategorikal terstruktur.",
            instrument="Alat ukur baku, sensor, atau kuesioner terstandarisasi."
        ))
        variables.append(VariableItem(
            variable="Hasil Observasi / Variabel Terikat Utama",
            category="Dependent Variable (Y)",
            definition="Kondisi respons atau luaran yang diukur untuk melihat efek atau hubungan dari variabel bebas.",
            indicator="Perubahan kuantitatif atau kualitatif pada subjek/objek penelitian.",
            measurement="Skor terstandar, nilai numerik terverifikasi, atau indikator performa.",
            instrument="Instrumen tes, catatan rekam medis, rubrik evaluasi, atau log sistem."
        ))
        variables.append(VariableItem(
            variable="Karakteristik Subjek & Lingkungan Terkontrol",
            category="Control Variable (Z)",
            definition="Variabel yang dijaga konstan atau dikontrol secara statistik untuk menghindari bias.",
            indicator="Kondisi demografis, durasi perlakuan, atau parameter lingkungan dasar.",
            measurement="Data kategorikal terstandar / nilai ambang batas konstan.",
            instrument="Formulir kriteria inklusi/eksklusi & protokol riset."
        ))
        variables.append(VariableItem(
            variable="Variabel Pengganggu Potensial (Confounders)",
            category="Confounding Variable (W)",
            definition="Faktor luar yang berkorelasi dengan X dan Y secara simultan sehingga dapat menimbulkan korelasi semu.",
            indicator="Faktor eksternal tidak terkendali yang dapat membiaskan estimasi efek.",
            measurement="Pencatatan multivariat untuk dimasukkan ke model regresi/kovarians.",
            instrument="Kuesioner kontrol kovariat atau model ANCOVA."
        ))
        
    return variables
