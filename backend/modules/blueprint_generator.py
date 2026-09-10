from typing import List
from ..models import ResearchBlueprint, TitleOption, VariableItem, FeasibilityReport

def generate_blueprint(
    raw_idea: str,
    domain: str,
    selected_title_obj: TitleOption,
    variables: List[VariableItem],
    feasibility: FeasibilityReport,
    user_level: str,
    location: str = ""
) -> ResearchBlueprint:
    
    loc_display = location if location else "lingkungan sekolah perkotaan tropis"
    
    ivs = [v.variable for v in variables if "Independent" in v.category]
    dvs = [v.variable for v in variables if "Dependent" in v.category]
    cvs = [v.variable for v in variables if "Control" in v.category]
    confounders = [v.variable for v in variables if "Confounding" in v.category]
    
    title = selected_title_obj.title
    
    research_questions = [
        f"Bagaimana profil fluktuasi kondisi {ivs[0] if ivs else 'variabel bebas'} yang teramati di {loc_display} selama masa observasi?",
        f"Apakah terdapat hubungan atau pengaruh signifikan antara {ivs[0] if ivs else 'variabel bebas'} dengan {dvs[0] if dvs else 'variabel terikat'}?",
        f"Sejauh mana faktor lingkungan fisik ({cvs[0] if cvs else 'variabel kontrol'}) memoderasi hubungan antara {ivs[0] if ivs else 'X'} dan {dvs[0] if dvs else 'Y'}?"
    ]
    
    hypotheses = [
        f"H0: Tidak terdapat korelasi atau pengaruh yang signifikan antara {ivs[0] if ivs else 'X'} dan {dvs[0] if dvs else 'Y'} pada populasi target.",
        f"H1: Terdapat korelasi yang signifikan secara statistik antara {ivs[0] if ivs else 'X'} dan {dvs[0] if dvs else 'Y'} setelah mengendalikan variabel pengganggu."
    ]
    
    stat_methods = [
        "Analisis Statistik Deskriptif (Mean, Median, Standar Deviasi, Distribusi Frekuensi)",
        "Uji Prasyarat Analisis (Uji Normalitas Shapiro-Wilk / Kolmogorov-Smirnov & Uji Homogenitas Levene)",
        "Uji Korelasi Pearson (jika parametrik) atau Spearman Rank (jika non-parametrik)",
        "Analisis Regresi Linier Berganda / Regresi Poisson untuk mengontrol variabel konfounder"
    ]
    
    return ResearchBlueprint(
        proposed_title=title,
        research_field=domain,
        research_problem=f"Fenomena {raw_idea} sering diasumsikan memiliki dampak langsung tanpa landasan pengukuran empiris yang terstandar. Diperlukan investigasi berbasis data konkret untuk membuktikan seberapa besar faktor lingkungan fisik ini memengaruhi morbiditas dan kesejahteraan subjek di {loc_display}.",
        research_background=f"Kondisi lingkungan dan faktor mikro sering kali berfluktuasi secara dinamis. Kurangnya pemahaman terhadap mekanisme spesifik antara paparan lingkungan mikro dan manifestasi kesehatan/performa menyebabkan mitigasi di tingkat institusi sering bersifat reaktif dan tidak berbasis bukti empiris.",
        research_gap="Sebagian besar literatur terdahulu berfokus pada data makro-regional berskala besar yang mengabaikan dinamika iklim mikro di dalam ruang belajar serta karakteristik personal subjek secara real-time.",
        research_objective=f"Menginvestigasi secara empiris pola hubungan antara {ivs[0] if ivs else 'variabel bebas'} terhadap {dvs[0] if dvs else 'variabel terikat'}, serta mengevaluasi efektivitas kontrol variabel lingkungan fisik di {loc_display}.",
        research_questions=research_questions,
        hypotheses=hypotheses,
        independent_variables=ivs,
        dependent_variables=dvs,
        control_variables=cvs,
        confounding_variables=confounders,
        research_design=selected_title_obj.suitable_method,
        population=f"Seluruh siswa/responden di institusi pendidikan target di {loc_display} (Perkiraan N = 300 - 600 individu).",
        sample=f"Sampel representatif terpilih (N = 120 - 180 individu) dihitung menggunakan rumus Slovin atau G*Power dengan power (1-β) = 0.80 dan α = 0.05.",
        sampling_technique="Stratified Random Sampling proporsional berdasarkan tingkatan kelas dan orientasi ruang kelas.",
        data_collection="Pengukuran instrumen sensor lingkungan secara berkala setiap 60 menit, sinkronisasi log absensi dan keluhan harian, serta pengisian kuesioner gejala terstandarisasi.",
        research_instruments="Data logger termo-higrometer digital terkalibrasi, formulir audit ventilasi ruangan, dan kuesioner baku skrining gejala kesehatan tervalidasi.",
        data_analysis="Pembersihan data (data cleaning), transformasi skor, pengujian asumsi statistik klasik, analisis korelasi bivariat, dan pemodelan regresi multivariat menggunakan software statistik (JASP / R / SPSS).",
        recommended_statistical_methods=stat_methods,
        expected_contribution="Menghasilkan bukti empiris lokal untuk penyusunan panduan mitigasi iklim mikro sekolah, jadwal aktivitas fisik adaptif, serta rekomendasi desain ventilasi ruang belajar sehat.",
        potential_limitations="Desain observasional cross-sectional membatasi klaim kausalitas mutlak; variasi imunitas genetik siswa dan riwayat nutrisi di luar sekolah tidak dapat dikontrol 100%.",
        ethical_considerations="Penerbitan Ethical Clearance / Surat Izin Penelitian, penandatanganan lembar Informed Consent (dan Parent Consent bagi responden di bawah umur), serta jaminan perlindungan anonimitas data medis sesuai etika penelitian ilmiah.",
        feasibility_score=f"{feasibility.total_score} / 5.0 ({feasibility.percentage}%) — Status: {feasibility.status}",
        research_maturity_level=user_level
    )
