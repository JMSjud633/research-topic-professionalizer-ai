from typing import List, Dict
from ..models import TitleOption, NoveltyAnalysis

def analyze_novelty(raw_idea: str, domain: str, location: str = "") -> NoveltyAnalysis:
    loc_str = location if location else "konteks lingkungan tropis / lokal spesifik"
    return NoveltyAnalysis(
        topic_novelty="Moderat — Topik relasi fenomena lingkungan dan kesejahteraan/performa siswa sering diteliti pada skala makro, namun jarang dieksplorasi secara mikro-lokal.",
        methodological_novelty="Tinggi jika mengombinasikan sensor iklim mikro digital real-time dengan logbook kesehatan dan analisis multivariat kontrol kovariat.",
        contextual_novelty=f"Tinggi — Kebaruan kontekstual terletak pada investigasi spesifik pada populasi {loc_str}, di mana adaptasi fisiologis dan sarana ventilasi lokal memiliki karakteristik unik.",
        practical_novelty="Menghasilkan rekomendasi kebijakan adaptasi iklim mikro sekolah, jadwal olahraga luar ruang berbasis indeks bahaya panas, dan pedoman ventilasi kelas sehat.",
        potential_novelty_statement=f"Kebaruan potensial terletak pada pembuktian peran variabel moderasi kualitas ventilasi ruang terhadap korelasi antara fluktuasi iklim mikro lokal dan tingkat morbiditas harian siswa di {loc_str}."
    )

def generate_title_options(raw_idea: str, domain: str, location: str = "", user_level: str = "Level 3") -> List[TitleOption]:
    text = raw_idea.lower()
    loc = f" di {location}" if location else " di Lingkungan Sekolah Menengah"
    
    if "cuaca" in text or "kesehatan" in text:
        titles = [
            TitleOption(
                category="Option A — Conservative Academic",
                title=f"Analisis Hubungan Parameter Iklim Mikro dan Keluhan Kesehatan Akut Siswa{loc}",
                strength="Formulasi netral, aman secara metodologis, terhindar dari asumsi kausalitas prematur, dan mudah diuji secara empiris.",
                weakness="Cenderung konvensional dan belum menonjolkan kebaruan teknik analisis lanjutan.",
                suitable_method="Kuantitatif Korelasional / Cross-Sectional Survey",
                difficulty_level="Sedang (Cocok untuk skripsi S1 / tugas akhir mandiri)",
                recommended_researcher_level="Level 2 - Level 3 (SMA Lanjutan / Mahasiswa S1)",
                scores={
                    "Clarity": 9.2, "Specificity": 8.0, "Researchability": 9.0,
                    "Feasibility": 8.8, "Academic Quality": 8.5, "Objectivity": 9.5, "Potential Novelty": 6.8
                },
                overall_score=8.54
            ),
            TitleOption(
                category="Option B — More Specific",
                title=f"Korelasi Fluktuasi Suhu Ambien dan Kelembapan Relatif terhadap Insidensi Gejala Respiratori Akut Siswa{loc}",
                strength="Variabel bebas dan terikat telah teroperasionalisasi dengan sangat presisi (suhu ambien, kelembapan, gejala respiratori).",
                weakness="Memerlukan instrumen pencatatan suhu berkala yang disiplin dan instrumen skrining medis yang terstandardisasi.",
                suitable_method="Studi Observasional Analitik dengan Repeated Measures",
                difficulty_level="Menengah-Tinggi (Perlu pemantauan berkala)",
                recommended_researcher_level="Level 3 (Undergraduate / Mahasiswa S1)",
                scores={
                    "Clarity": 9.0, "Specificity": 9.2, "Researchability": 8.6,
                    "Feasibility": 8.2, "Academic Quality": 8.9, "Objectivity": 9.4, "Potential Novelty": 7.6
                },
                overall_score=8.70
            ),
            TitleOption(
                category="Option C — Method-Oriented",
                title=f"Pemodelan Regresi Multivariat Pengaruh Heat Index dan Ventilasi Kelas terhadap Tingkat Absensi Sakit Siswa{loc}",
                strength="Menegaskan pendekatan analitik mutakhir (multivariat) dan mengikutsertakan variabel kontrol fisik ruangan.",
                weakness="Menuntut pemahaman ekonometrika/statistika inferensial yang solid dalam uji asumsi klasik regresi.",
                suitable_method="Kuantitatif Analitik dengan Multiple Linear / Poisson Regression",
                difficulty_level="Tinggi (Statistika Lanjutan)",
                recommended_researcher_level="Level 3 - Level 4 (Mahasiswa S1 Tingkat Akhir / S2)",
                scores={
                    "Clarity": 8.8, "Specificity": 9.0, "Researchability": 8.5,
                    "Feasibility": 7.8, "Academic Quality": 9.2, "Objectivity": 9.2, "Potential Novelty": 8.2
                },
                overall_score=8.67
            ),
            TitleOption(
                category="Option D — Advanced",
                title=f"Dinamika Paparan Stres Termal Harian dan Pengaruhnya terhadap Respon Fisiologis serta Kelelahan Kognitif Siswa{loc}",
                strength="Kedalaman analisis tinggi dengan memadukan aspek stres termal lingkungan dan performa kognitif/fisiologis.",
                weakness="Memerlukan sensor biometrik (denyut nadi/suhu tubuh) atau instrumen tes kognitif berkala yang relatif rumit.",
                suitable_method="Quasi-Experimental Time-Series Design",
                difficulty_level="Sangat Tinggi (Laboratorium / Uji Lapangan Intensif)",
                recommended_researcher_level="Level 4 (Research-Intensive / Pascasarjana)",
                scores={
                    "Clarity": 8.5, "Specificity": 8.8, "Researchability": 7.8,
                    "Feasibility": 7.0, "Academic Quality": 9.4, "Objectivity": 9.0, "Potential Novelty": 8.8
                },
                overall_score=8.47
            ),
            TitleOption(
                category="Option E — Interdisciplinary",
                title=f"Kajian Biometeorologi Pendidikan: Integrasi Sensor IoT Iklim Mikro dan Dampak Ergonomis Ruang Belajar terhadap Kesejahteraan Siswa",
                strength="Menghubungkan tiga disiplin ilmu sekaligus: Meteorologi Lingkungan, Teknik Arsitektur/Ergonomi, dan Kesehatan Pendidikan.",
                weakness="Cakupan luas, membutuhkan kolaborasi lintas bidang atau penguasaan instrumen ganda.",
                suitable_method="Mixed-Methods (Sensor Kuantitatif IoT & Kuesioner Ergonomi)",
                difficulty_level="Tinggi (Interdisipliner)",
                recommended_researcher_level="Level 4 - Level 5 (Riset Kolaboratif Profesional)",
                scores={
                    "Clarity": 8.4, "Specificity": 8.6, "Researchability": 8.0,
                    "Feasibility": 7.2, "Academic Quality": 9.1, "Objectivity": 9.0, "Potential Novelty": 9.0
                },
                overall_score=8.47
            )
        ]
    elif "ai" in text or "belajar" in text:
        titles = [
            TitleOption(
                category="Option A — Conservative Academic",
                title=f"Hubungan Intensitas Penggunaan AI Generatif dengan Regulasi Diri dalam Belajar Siswa{loc}",
                strength="Formulasi netral tanpa asumsi negatif, mudah dieksekusi melalui survei kuesioner baku.",
                weakness="Belum menangkap dinamika kualitatif pengalaman siswa saat bernavigasi dengan AI.",
                suitable_method="Kuantitatif Korelasional",
                difficulty_level="Sedang",
                recommended_researcher_level="Level 2 - Level 3",
                scores={"Clarity": 9.4, "Specificity": 8.5, "Researchability": 9.2, "Feasibility": 9.0, "Academic Quality": 8.6, "Objectivity": 9.6, "Potential Novelty": 7.5},
                overall_score=8.83
            ),
            TitleOption(
                category="Option B — More Specific",
                title=f"Asosiasi Frekuensi Prompting Tools AI dengan Keterampilan Berpikir Kritis pada Pembelajaran Sains{loc}",
                strength="Menyasar ranah spesifik (prompting AI vs higher-order thinking skills di bidang sains).",
                weakness="Memerlukan rubrik penilaian tes berpikir kritis yang telah divalidasi ahli.",
                suitable_method="Kuantitatif Komparatif & Regresi",
                difficulty_level="Menengah-Tinggi",
                recommended_researcher_level="Level 3",
                scores={"Clarity": 9.0, "Specificity": 9.2, "Researchability": 8.7, "Feasibility": 8.4, "Academic Quality": 9.0, "Objectivity": 9.2, "Potential Novelty": 8.2},
                overall_score=8.81
            ),
            TitleOption(
                category="Option C — Method-Oriented",
                title=f"Analisis Jalur (Path Analysis) Pengaruh Adopsi AI terhadap Efikasi Diri Akademik yang Dimediasi Strategi Kognitif Siswa",
                strength="Menjelaskan mekanisme kausal struktural melalui variabel mediasi secara elegan.",
                weakness="Menuntut ukuran sampel relatif besar (N > 150) untuk memenuhi asumsi pemodelan jalur / SEM.",
                suitable_method="Kuantitatif Analitik Structural Equation Modeling (SEM-PLS)",
                difficulty_level="Tinggi",
                recommended_researcher_level="Level 3 - Level 4",
                scores={"Clarity": 8.8, "Specificity": 8.9, "Researchability": 8.4, "Feasibility": 8.0, "Academic Quality": 9.3, "Objectivity": 9.4, "Potential Novelty": 8.5},
                overall_score=8.76
            ),
            TitleOption(
                category="Option D — Advanced",
                title=f"Eksperimen Semu: Efektivitas Integrasi Scaffolding AI dalam Pembelajaran Berbasis Masalah terhadap Kinerja Pemecahan Masalah Kompleks",
                strength="Desain eksperimental yang kuat untuk menguji kausalitas murni perlakuan scaffolding AI.",
                weakness="Membutuhkan kelas kontrol dan kelas eksperimen yang setara serta modul ajar yang terkontrol ketat.",
                suitable_method="Quasi-Experimental Pretest-Posttest Non-Equivalent Control Group Design",
                difficulty_level="Tinggi",
                recommended_researcher_level="Level 3 - Level 4",
                scores={"Clarity": 8.9, "Specificity": 9.1, "Researchability": 8.3, "Feasibility": 7.8, "Academic Quality": 9.4, "Objectivity": 9.1, "Potential Novelty": 8.9},
                overall_score=8.79
            ),
            TitleOption(
                category="Option E — Interdisciplinary",
                title=f"Dinamika Sosio-Teknis Pembelajaran Berbantuan AI: Integrasi Analisis Log Komputasi dan Persepsi Etika Siswa",
                strength="Menggabungkan data science (log usage analysis) dengan sosiologi pendidikan dan etika teknologi.",
                weakness="Memerlukan akses ke log data sistem dan izin privasi data yang ketat.",
                suitable_method="Mixed-Methods Sequential Explanatory Design",
                difficulty_level="Tinggi",
                recommended_researcher_level="Level 4 - Level 5",
                scores={"Clarity": 8.5, "Specificity": 8.7, "Researchability": 8.0, "Feasibility": 7.4, "Academic Quality": 9.2, "Objectivity": 9.0, "Potential Novelty": 9.1},
                overall_score=8.56
            )
        ]
    else:
        # Generic academic progression
        titles = [
            TitleOption(
                category="Option A — Conservative Academic",
                title=f"Analisis Deskriptif dan Korelasional Determinan {raw_idea.title()}{loc}",
                strength="Aman, netral, dan realistis untuk dituntaskan sesuai kaidah metodologi baku.",
                weakness="Potensi kebaruan konvensional.",
                suitable_method="Kuantitatif Survei Korelasional",
                difficulty_level="Sedang",
                recommended_researcher_level="Level 2 - Level 3",
                scores={"Clarity": 9.0, "Specificity": 8.0, "Researchability": 9.0, "Feasibility": 9.0, "Academic Quality": 8.4, "Objectivity": 9.5, "Potential Novelty": 6.5},
                overall_score=8.49
            ),
            TitleOption(
                category="Option B — More Specific",
                title=f"Identifikasi Parameter Kunci dan Pola Asosiasi pada Fenomena {raw_idea.title()}{loc}",
                strength="Memperjelas variabel operasional yang dapat diukur.",
                weakness="Membutuhkan instrumen pengukuran yang terverifikasi reliabilitasnya.",
                suitable_method="Kuantitatif Analitik",
                difficulty_level="Sedang-Tinggi",
                recommended_researcher_level="Level 3",
                scores={"Clarity": 8.8, "Specificity": 9.0, "Researchability": 8.6, "Feasibility": 8.4, "Academic Quality": 8.8, "Objectivity": 9.2, "Potential Novelty": 7.8},
                overall_score=8.66
            ),
            TitleOption(
                category="Option C — Method-Oriented",
                title=f"Penerapan Model Analitik Multivariat dalam Menguji Faktor Penentu {raw_idea.title()}",
                strength="Menegaskan rigor metodologi dan pengujian hipotesis terstruktur.",
                weakness="Memerlukan data dengan sebaran normal dan terpenuhinya asumsi statistik.",
                suitable_method="Analisis Regresi Multivariat / Pemodelan Struktural",
                difficulty_level="Tinggi",
                recommended_researcher_level="Level 3 - Level 4",
                scores={"Clarity": 8.7, "Specificity": 8.8, "Researchability": 8.4, "Feasibility": 8.0, "Academic Quality": 9.1, "Objectivity": 9.2, "Potential Novelty": 8.1},
                overall_score=8.61
            ),
            TitleOption(
                category="Option D — Advanced",
                title=f"Evaluasi Komparatif Longitudinal Pola Perubahan dan Dinamika {raw_idea.title()}",
                strength="Memiliki nilai saintifik tinggi dengan analisis runtun waktu atau perbandingan terkontrol.",
                weakness="Membutuhkan durasi penelitian yang lebih panjang.",
                suitable_method="Studi Longitudinal / Desain Kuasi-Eksperimen",
                difficulty_level="Sangat Tinggi",
                recommended_researcher_level="Level 4",
                scores={"Clarity": 8.5, "Specificity": 8.9, "Researchability": 7.9, "Feasibility": 7.2, "Academic Quality": 9.3, "Objectivity": 9.1, "Potential Novelty": 8.7},
                overall_score=8.51
            ),
            TitleOption(
                category="Option E — Interdisciplinary",
                title=f"Pendekatan Sosio-Teknis Terintegrasi terhadap Kajian Fenomena {raw_idea.title()}",
                strength="Memberikan wawasan holistik dari kombinasi bidang ilmu berbeda.",
                weakness="Kompleksitas sintesis data kualitatif dan kuantitatif.",
                suitable_method="Mixed-Methods Convergent Parallel Design",
                difficulty_level="Tinggi",
                recommended_researcher_level="Level 4 - Level 5",
                scores={"Clarity": 8.3, "Specificity": 8.5, "Researchability": 8.0, "Feasibility": 7.5, "Academic Quality": 9.0, "Objectivity": 8.9, "Potential Novelty": 8.9},
                overall_score=8.44
            )
        ]
    return titles
