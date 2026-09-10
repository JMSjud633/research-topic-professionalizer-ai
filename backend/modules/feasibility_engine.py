from typing import List
from ..models import FeasibilityReport, FeasibilityScoreDetail, RiskItem

def evaluate_feasibility(raw_idea: str, user_level: str, time_constraint: str) -> FeasibilityReport:
    text = raw_idea.lower()
    
    # 0 = Impossible, 1 = Very difficult, 2 = Difficult, 3 = Reasonable, 4 = Good, 5 = Excellent
    details = [
        FeasibilityScoreDetail(
            dimension="Time Feasibility",
            score=4,
            rating="Good",
            analysis=f"Periode riset '{time_constraint}' cukup untuk desain cross-sectional, korelasional, atau studi observasional terfokus.",
            recommendation="Batasi periode pengambilan data lapangan menjadi 4-8 minggu dengan protokol terstruktur agar analisis data dan penulisan laporan tidak terburu-buru."
        ),
        FeasibilityScoreDetail(
            dimension="Resource Feasibility",
            score=4,
            rating="Good",
            analysis="Instrumen ukur, kuesioner baku, dan sensor dasar relatif terjangkau serta tersedia di lingkungan sekolah/kampus tanpa memerlukan anggaran riset bernilai besar.",
            recommendation="Gunakan instrumen digital open-source atau sensor komersial terkalibrasi untuk memangkas biaya perolehan data."
        ),
        FeasibilityScoreDetail(
            dimension="Data Feasibility",
            score=3,
            rating="Reasonable",
            analysis="Data primer dapat dihimpun langsung dari responden, namun membutuhkan izin formal dari institusi dan kedisiplinan pencatatan absensi/logbook.",
            recommendation="Siapkan surat perizinan institusional sedini mungkin dan gunakan instrumen formulir digital (Google Forms/KoboToolbox) untuk meminimalisasi missing data."
        ),
        FeasibilityScoreDetail(
            dimension="Sample Feasibility",
            score=4,
            rating="Good",
            analysis="Ukuran sampel memadai (misal: N = 100-250 responden) dapat dicapai dengan mudah di lingkungan institusi pendidikan formal.",
            recommendation="Gunakan teknik stratified random sampling atau cluster sampling untuk memastikan keterwakilan seluruh tingkatan/kelompok."
        ),
        FeasibilityScoreDetail(
            dimension="Ethical Feasibility",
            score=4,
            rating="Good",
            analysis="Penelitian berisiko minimal (*minimal risk*), tidak menggunakan prosedur medis invasif ataupun perlakuan biologis berbahaya.",
            recommendation="Wajib menyertakan Informed Consent bagi responden (dan izin orang tua jika siswa di bawah usia 18 tahun) serta menjamin anonimitas data kesehatan."
        ),
        FeasibilityScoreDetail(
            dimension="Technical Feasibility",
            score=4,
            rating="Good",
            analysis=f"Tingkat keahlian peneliti pada level '{user_level}' sangat memadai untuk mengoperasikan instrumen dan menjalankan uji statistik standar.",
            recommendation="Gunakan software analisis statistik standar seperti JASP, R, SPSS, atau Python (scipy/statsmodels) untuk analisis data yang transparan dan dapat direplikasi."
        )
    ]
    
    total = sum(d.score for d in details) / len(details)
    percentage = (total / 5.0) * 100
    status = "Highly Feasible" if total >= 4.0 else ("Feasible with Minor Adjustments" if total >= 3.0 else "Challenging / Needs Redesign")
    
    return FeasibilityReport(
        total_score=round(total, 2),
        percentage=round(percentage, 1),
        status=status,
        details=details
    )

def detect_risks_and_biases(raw_idea: str) -> List[RiskItem]:
    text = raw_idea.lower()
    risks = []
    
    # 1. Confirmation Bias / Presupposition
    if any(word in text for word in ["pengaruh buruk", "dampak negatif", "bahaya", "keberhasilan", "keunggulan", "efektivitas"]):
        risks.append(RiskItem(
            risk_type="Presupposition / Confirmation Bias",
            explanation="Rumusan ide awal cenderung mengasumsikan arah dampak (misalnya menganggap hasilnya pasti negatif/berbahaya) sebelum pengujian empiris dimulai.",
            solution="Gunakan formulasi netral: 'Hubungan antara...', 'Pengaruh...', atau 'Analisis asosiasi...'. Biarkan data empiris yang membuktikan apakah dampaknya positif, negatif, atau tidak signifikan."
        ))
    else:
        risks.append(RiskItem(
            risk_type="Confirmation Bias",
            explanation="Kecenderungan peneliti hanya mencari bukti empiris yang mengonfirmasi ekspektasi awal hubungan antar variabel.",
            solution="Wajib merumuskan Hipotesis Nol (H0) yang setara dan menetapkan kriteria uji signifikansi (p-value / confidence interval) sebelum data dianalisis."
        ))
        
    # 2. Confounding Variables / False Causality
    risks.append(RiskItem(
        risk_type="Kekeliruan Asosiasi vs Kausalitas (Correlation != Causation)",
        explanation="Mengklaim adanya pengaruh langsung (sebab-akibat) padahal desain riset yang digunakan bersifat observasional atau cross-sectional tanpa randomisasi murni.",
        solution="Gunakan istilah 'asosiasi' atau 'prediktor' jika menggunakan desain observasional, dan masukkan variabel kontrol (seperti status gizi, ventilasi ruang, kondisi sosioekonomi) ke dalam model regresi multivariat."
    ))
    
    # 3. Measurement & Self-Report Bias
    risks.append(RiskItem(
        risk_type="Measurement / Recall Bias",
        explanation="Jika data kesehatan atau kebiasaan hanya mengandalkan kuesioner ingatan siswa, data rentan bias ketidakakuratan ingatan masa lalu.",
        solution="Kombinasikan data kuesioner subjektif dengan data objektif (misal: logbook kehadiran UKS, catatan absensi resmi sekolah, atau pengukuran sensor terkalibrasi)."
    ))
    
    # 4. Inappropriate Scope
    risks.append(RiskItem(
        risk_type="Definisi Operasional Ambiguitas",
        explanation="Konsep utama masih terlalu abstrak sehingga sulit direplikasi oleh peneliti independen.",
        solution="Definisikan secara eksplisit setiap indikator dalam tabel operasionalisasi variabel beserta batasan skala pengukurannya."
    ))
    
    return risks
