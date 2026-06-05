import streamlit as st

# ========== KONFIGURASI ==========
st.set_page_config(page_title="GraviLab – Analisis Gravimetri", page_icon="⚗️", layout="wide")
st.markdown("""<style>.block-container{padding-top:2rem;}.rumus-box{background:#f0f8ff;border-left:4px solid #2c7be5;padding:12px 16px;border-radius:6px;font-family:monospace;color:#000;}.reaksi-box{background:#f8f9fa;border:1px solid #dee2e6;border-radius:10px;padding:16px;}</style>""", unsafe_allow_html=True)

# ========== SIDEBAR ==========
st.sidebar.title("⚗️ GraviLab")
st.sidebar.caption("Panduan Praktikum Analisis Gravimetri\nPoliteknik AKA Bogor · 2026")
st.sidebar.divider()
menu = st.sidebar.radio("Pilih Fitur", ["🏠 Beranda", "📋 Panduan Prosedur", "🧮 Kalkulator Gravimetri", "🔬 Penjelasan Reagen", "⚗️ Reaksi Kimia Visual"])

# ========== BERANDA ==========
if menu == "🏠 Beranda":
    st.title("⚗️ GraviLab")
    st.subheader("Panduan Digital Praktikum Analisis Gravimetri")
    st.caption("Politeknik AKA Bogor · Program Studi Analisis Kimia · 2026")
    st.divider()
    st.markdown("Selamat datang di **GraviLab** — aplikasi bantu praktikum Analisis Gravimetri digital. Pilih fitur di sidebar kiri untuk memulai.")
    c1,c2=st.columns(2)
    with c1:
        st.info("**📋 Panduan Prosedur**\n\nChecklist langkah demi langkah 5 percobaan.")
        st.info("**🔬 Penjelasan Reagen**\n\nKenapa pakai zat ini? Bisa diganti apa?")
    with c2:
        st.info("**🧮 Kalkulator Gravimetri**\n\nInput bobot → hasil kadar otomatis.")
        st.info("**⚗️ Reaksi Kimia Visual**\n\nTampilan reaksi lengkap & jelas.")
    st.divider()
    st.subheader("📚 Daftar Percobaan")
    st.markdown("| No | Judul Percobaan | Metode | Referensi |\n|:-:|:---|:---|:---|\n|1| Kadar Air Tepung Terigu | Oven 130°C | SNI 3751:2009 |\n|2| Kadar Abu Tepung Terigu | Tanur 550°C | SNI 3751:2018 |\n|3| Kadar Sulfat dalam Garam Glauber | Pengendapan BaSO₄ | — |\n|4| Kadar Besi dalam Garam Besi(II) | Oksidasi & Endap Fe₂O₃ | — |\n|5| Kadar Barium dengan Metode Homogen | Pengendapan Seragam | — |")

# ========== PANDUAN PROSEDUR ==========
elif menu == "📋 Panduan Prosedur":
    st.title("📋 Panduan Prosedur Interaktif")
    st.divider()
    tab1,tab2,tab3,tab4,tab5=st.tabs(["Perc 1","Perc 2","Perc 3","Perc 4","Perc 5"])
    with tab1:
        st.subheader("Percobaan 1: Penetapan Kadar Air dalam Tepung Terigu")
        st.caption("SNI 3751:2009 | Suhu Pengeringan 130°C")
        st.markdown("**🧪 Bahan:** Tepung terigu, kertas saring")
        st.markdown("**🛠 Alat:** Neraca analitik, oven, wadah timbang, tang penjepit, desikator")
        langkah=["Panaskan wadah kosong 1 jam di 130°C → dinginkan, timbang W₀","Timbang tepat 2 gram sampel ke wadah → catat W₁","Panaskan 1 jam pada suhu 130°C","Dinginkan dalam desikator → timbang hingga bobot tetap W₂"]
        selesai=sum(st.checkbox(l,key=f"p1_{i}") for i,l in enumerate(langkah))
        st.progress(selesai/len(langkah),text=f"Progress: {selesai}/{len(langkah)}")
    with tab2:
        st.subheader("Percobaan 2: Penetapan Kadar Abu dalam Tepung Terigu")
        st.caption("SNI 3751:2018 | Suhu Pengabuan 550°C")
        st.markdown("**🧪 Bahan:** Tepung terigu")
        st.markdown("**🛠 Alat:** Neraca analitik, tanur pengabuan, cawan porselin, Bunsen, tang penjepit, desikator")
        langkah=["Panaskan cawan kosong di tanur → bobot tetap W₀","Timbang sampel 3–5 gram → catat W₁","Arangkan di atas pembakar sampai tak berasap, abukan 8 jam di tanur 550°C","Dinginkan → timbang sampai bobot tetap W₂"]
        selesai=sum(st.checkbox(l,key=f"p2_{i}") for i,l in enumerate(langkah))
        st.progress(selesai/len(langkah),text=f"Progress: {selesai}/{len(langkah)}")
    with tab3:
        st.subheader("Percobaan 3: Penetapan Kadar Sulfat dalam Garam Glauber")
        st.markdown("**🧪 Bahan:** Garam glauber, HCl 4N, BaCl₂ 10%, AgNO₃ 0,1N")
        st.markdown("**🛠 Alat:** Gelas kimia, penangas air, corong kaca, kertas saring, tanur, neraca analitik")
        langkah=["Timbang 0,5 gram sampel → larutkan dalam air suling","Asamkan dengan HCl 4N, panaskan hingga mendidih","Tambahkan larutan BaCl₂ panas perlahan, diamkan 1 jam","Cuci endapan sampai bebas Cl⁻, saring, pijar hingga bobot tetap"]
        selesai=sum(st.checkbox(l,key=f"p3_{i}") for i,l in enumerate(langkah))
        st.progress(selesai/len(langkah),text=f"Progress: {selesai}/{len(langkah)}")
    with tab4:
        st.subheader("Percobaan 4: Penetapan Kadar Besi dalam Garam Besi(II)")
        st.markdown("**🧪 Bahan:** Garam besi(II), HNO₃ pekat, Amonia kocok 1:1, NH₄NO₃ 1%")
        st.markdown("**🛠 Alat:** Gelas kimia, pembakar, corong, kertas saring, tanur, neraca analitik")
        langkah=["Timbang 0,25 gram sampel → larutkan air suling + HCl encer","Tambah HNO₃ pekat → panaskan untuk oksidasi sempurna","Panaskan, teteskan amonia berlebih sampai endap Fe(OH)₃ terbentuk","Cuci dengan NH₄NO₃, pijar jadi Fe₂O₃ → timbang"]
        selesai=sum(st.checkbox(l,key=f"p4_{i}") for i,l in enumerate(langkah))
        st.progress(selesai/len(langkah),text=f"Progress: {selesai}/{len(langkah)}")
    with tab5:
        st.subheader("Percobaan 5: Penetapan Kadar Barium dengan Metode Homogen")
        st.markdown("**🧪 Bahan:** Larutan BaCl₂, HCl 2N, K₂CrO₄, Urea, air suling")
        st.markdown("**🛠 Alat:** Pipet ukur, gelas kimia, penangas air, corong kaca, oven, neraca analitik")
        langkah=["Pipet 25 mL larutan BaCl₂ 0,1M → tambah HCl encer","Tambah larutan K₂CrO₄ dan kristal urea → encerkan sampai tanda batas","Panaskan mendidih perlahan ±90 menit sampai pH naik & endap sempurna","Saring, cuci, oven 110°C sampai bobot tetap"]
        selesai=sum(st.checkbox(l,key=f"p5_{i}") for i,l in enumerate(langkah))
        st.progress(selesai/len(langkah),text=f"Progress: {selesai}/{len(langkah)}")

# ========== KALKULATOR ==========
elif menu == "🧮 Kalkulator Gravimetri":
    st.title("🧮 Kalkulator Gravimetri Otomatis")
    st.divider()
    tab1,tab2,tab3,tab4,tab5=st.tabs(["Air","Abu","Sulfat","Fe","Ba"])
    with tab1:
        st.markdown('<div class="rumus-box">Kadar Air (%) = [(W₁ - W₂) / (W₁ - W₀)] × 100</div>',unsafe_allow_html=True)
        w0=st.number_input("Bobot wadah kosong (W₀)",format="%.4f",key="wa0")
        w1=st.number_input("Bobot wadah + sampel awal (W₁)",format="%.4f",key="wa1")
        w2=st.number_input("Bobot wadah + residu kering (W₂)",format="%.4f",key="wa2")
        if st.button("Hitung Kadar Air",type="primary"):
            kadar=((w1-w2)/(w1-w0))*100 if w1>w0 and w2<=w1 else -1
            st.success(f"✅ Kadar Air = {kadar:.4f} %") if kadar>=0 else st.error("⚠️ Cek kembali data input!")
    with tab2:
        st.markdown('<div class="rumus-box">Kadar Abu (%) = [(W₂ - W₀) / (W₁ - W₀)] × 100</div>',unsafe_allow_html=True)
        w0=st.number_input("Bobot cawan kosong (W₀)",format="%.4f",key="wu0")
        w1=st.number_input("Bobot cawan + sampel awal (W₁)",format="%.4f",key="wu1")
        w2=st.number_input("Bobot cawan + abu (W₂)",format="%.4f",key="wu2")
        if st.button("Hitung Kadar Abu",type="primary"):
            kadar=((w2-w0)/(w1-w0))*100 if w1>w0 and w2>=w0 else -1
            st.success(f"✅ Kadar Abu = {kadar:.4f} %") if kadar>=0 else st.error("⚠️ Cek kembali data input!")
    with tab3:
        st.markdown('<div class="rumus-box">Kadar SO₄ (%) = 0,4116 × [(W₂ - W₀)/(W₁ - W₀)] × 100</div>',unsafe_allow_html=True)
        w0=st.number_input("Bobot cawan + kertas saring kosong (W₀)",format="%.4f",key="ws0")
        w1=st.number_input("Bobot sampel awal (W₁)",format="%.4f",key="ws1")
        w2=st.number_input("Bobot residu BaSO₄ + wadah (W₂)",format="%.4f",key="ws2")
        if st.button("Hitung Kadar Sulfat",type="primary"):
            kadar=0.4116*((w2-w0)/(w1-w0))*100 if w1>w0 and w2>=w0 else -1
            st.success(f"✅ Kadar SO₄ = {kadar:.4f} %") if kadar>=0 else st.error("⚠️ Cek kembali data input!")
    with tab4:
        st.markdown('<div class="rumus-box">Kadar Fe (%) = 0,6994 × [(W₂ - W₀)/(W₁ - W₀)] × 100</div>',unsafe_allow_html=True)
        w0=st.number_input("Bobot wadah kosong + abu kertas (W₀)",format="%.4f",key="wf0")
        w1=st.number_input("Bobot sampel awal (W₁)",format="%.4f",key="wf1")
        w2=st.number_input("Bobot residu Fe₂O₃ + wadah (W₂)",format="%.4f",key="wf2")
        if st.button("Hitung Kadar Besi",type="primary"):
            kadar=0.6994*((w2-w0)/(w1-w0))*100 if w1>w0 and w2>=w0 else -1
            st.success(f"✅ Kadar Fe = {kadar:.4f} %") if kadar>=0 else st.error("⚠️ Cek kembali data input!")
    with tab5:
        st.markdown('<div class="rumus-box">Kadar Ba (%) = 0,5421 × [(W₁ - W₀)/Volume(mL)] × 100</div>',unsafe_allow_html=True)
        w0=st.number_input("Bobot wadah kosong (W₀)",format="%.4f",key="wb0")
        w1=st.number_input("Bobot wadah + endapan BaCrO₄ (W₁)",format="%.4f",key="wb1")
        vol=st.number_input("Volume larutan sampel (mL)",format="%.2f",key="vb")
        if st.button("Hitung Kadar Barium",type="primary"):
            kadar=0.5421*((w1-w0)/vol)*100 if w1>w0 and vol>0 else -1
            st.success(f"✅ Kadar Ba = {kadar:.4f} %") if kadar>=0 else st.error("⚠️ Cek kembali data input!")

# ========== PENJELASAN REAGEN ==========
elif menu == "🔬 Penjelasan Reagen":
    st.title("🔬 Penjelasan Reagen")
    st.divider()
    daftar=[
        {"nama":"HCl","pakai":"Perc 3,4,5","fungsi":"Buat suasana asam agar hanya ion target mengendap sempurna","alt":["❌ H₂SO₄ (mengganggu analisis sulfat)","❌ HNO₃ (bersifat oksidator kuat)"]},
        {"nama":"BaCl₂","pakai":"Perc 3","fungsi":"Pengendap sulfat membentuk BaSO₄ yang sukar larut","alt":["✅ Ba(NO₃)₂ (bisa dipakai)","✅ Ba(CH₃COO)₂ (bisa dipakai)"]},
        {"nama":"HNO₃ Pekat","pakai":"Perc 4","fungsi":"Oksidator mengubah Fe²⁺ menjadi Fe³⁺ agar mudah diendapkan","alt":["✅ H₂O₂ (lebih aman)","✅ Air bromin (oksidator kuat)"]},
        {"nama":"Amonia","pakai":"Perc 4,5","fungsi":"Basa lemah untuk pengatur pH dan pengendap Fe(OH)₃","alt":["✅ Urea (menaikkan pH perlahan)","❌ NaOH/KOH (terlalu kuat, larutkan endapan)"]},
        {"nama":"Urea","pakai":"Perc 5","fungsi":"Terurai perlahan → NH₃ merata di larutan, pengendapan homogen","alt":["✅ Heksametilentetramina","❌ Amonia langsung (endapan kasar)"]},
        {"nama":"NH₄NO₃","pakai":"Perc 4","fungsi":"Larutan pencuci cegah peptisasi koloid pada endapan","alt":["✅ NH₄Cl encer","❌ Air suling saja (endapan bisa terurai)"]},
        {"nama":"H₂SO₄ Pekat","pakai":"Perc 3","fungsi":"Cegah reduksi BaSO₄ menjadi BaS saat pemanasan suhu tinggi","alt":["❌ Tidak ada pengganti yang cocok"]}
    ]
    for z in daftar:
        with st.expander(f"🧪 {z['nama']} — digunakan pada: {z['pakai']}"):
            st.markdown(f"**Fungsi:** {z['fungsi']}\n\n**Alternatif:**\n"+"\n".join(f"- {a}" for a in z['alt']))

# ================================================
# HALAMAN 5: REAKSI KIMIA VISUAL
# Tampilan reaksi tiap percobaan dengan penjelasan
# ================================================
elif menu == "⚗️ Reaksi Kimia Visual":

    st.title("⚗️ Reaksi Kimia Visual")
    st.caption("Semua persamaan reaksi dari tiap percobaan beserta penjelasannya.")
    st.divider()

    # Legend warna zat
    st.markdown("**Keterangan warna:**")
    col1, col2, col3, col4 = st.columns(4)
    col1.info("🔵 Reaktan / Pereaksi")
    col2.success("🟢 Produk larut")
    col3.warning("🟡 Endapan (↓)")
    col4.error("🔴 Gas (↑)")
    st.divider()

    tab2, tab3, tab4, tab5 = st.tabs([
        "Percobaan 2", "Percobaan 3",
        "Percobaan 4", "Percobaan 5"
    ])

    # ---- REAKSI PERCOBAAN 3 ----
    with tab3:
        st.subheader("Percobaan 3 – Reaksi dalam Penetapan Sulfat")

        st.markdown("**Reaksi 1: Pengendapan BaSO₄**")
        col1, col2, col3, col4, col5, col6, col7 = st.columns([2,0.5,2,0.5,2,0.5,2])
        col1.info("Na₂SO₄")
        col2.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col3.info("BaCl₂")
        col4.markdown("<div style='text-align:center;padding-top:8px'>→</div>", unsafe_allow_html=True)
        col5.warning("BaSO₄ ↓ (putih)")
        col6.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col7.success("2 NaCl")

        st.markdown("> **Penjelasan:** BaSO₄ sangat tidak larut (Ksp ≈ 1,1×10⁻¹⁰). Suasana asam HCl mencegah pengendapan pengganggu seperti BaCO₃ atau BaCrO₄.")
        st.divider()

        st.markdown("**Reaksi 2: Reduksi BaSO₄ oleh Karbon (yang harus DICEGAH!)**")
        col1, col2, col3, col4, col5, col6, col7 = st.columns([2,0.5,2,0.5,2,0.5,2])
        col1.warning("BaSO₄")
        col2.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col3.info("4 C")
        col4.markdown("<div style='text-align:center;padding-top:8px'>→</div>", unsafe_allow_html=True)
        col5.success("BaS (larut)")
        col6.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col7.error("4 CO ↑")

        st.markdown("> **Penjelasan:** Inilah alasan mengapa **harus meneteskan H₂SO₄ pekat 1 tetes** sebelum pemijaran akhir — agar BaSO₄ tidak tersusut menjadi BaS yang larut.")

    # ---- REAKSI PERCOBAAN 4 ----
    with tab4:
        st.subheader("Percobaan 4 – Reaksi dalam Penetapan Besi")

        st.markdown("**Reaksi 1: Oksidasi Fe²⁺ → Fe³⁺ oleh HNO₃**")
        col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([2,0.4,1.5,0.4,1.5,0.4,2,0.4,1.5])
        col1.info("3 Fe²⁺")
        col2.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col3.info("NO₃⁻")
        col4.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col5.info("4 H⁺")
        col6.markdown("<div style='text-align:center;padding-top:8px'>→</div>", unsafe_allow_html=True)
        col7.success("3 Fe³⁺")
        col8.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col9.error("NO ↑")

        st.markdown("> **Penjelasan:** Fe²⁺ harus diubah ke Fe³⁺ karena Fe(OH)₂ lebih mudah larut dan tidak mengendap sempurna. Gas NO tidak berwarna tapi bereaksi dengan O₂ udara menjadi NO₂ (coklat) — lakukan di lemari asam!")
        st.divider()

        st.markdown("**Reaksi 2: Pengendapan Fe(OH)₃ oleh Amonia**")
        col1, col2, col3, col4, col5, col6, col7 = st.columns([2,0.5,2,0.5,2,0.5,2])
        col1.info("Fe³⁺")
        col2.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col3.info("3 NH₄OH")
        col4.markdown("<div style='text-align:center;padding-top:8px'>→</div>", unsafe_allow_html=True)
        col5.warning("Fe(OH)₃ ↓ (coklat)")
        col6.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col7.success("3 NH₄⁺")

        st.markdown("> **Penjelasan:** Fe(OH)₃ berwarna **coklat kemerahan**. Bersifat koloid → pencucian harus pakai NH₄NO₃ 1%, bukan air suling murni.")
        st.divider()

        st.markdown("**Reaksi 3: Pemijaran Fe(OH)₃ → Fe₂O₃**")
        col1, col2, col3, col4, col5 = st.columns([2,0.5,2,0.5,2])
        col1.info("2 Fe(OH)₃")
        col2.markdown("<div style='text-align:center;padding-top:8px'>→</div>", unsafe_allow_html=True)
        col3.warning("Fe₂O₃ ↓ (merah bata)")
        col4.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col5.error("3 H₂O ↑")

        st.markdown("> **Penjelasan:** Fe₂O₃ berwarna **merah bata** (hematit). Inilah zat yang ditimbang akhir. Faktor konversi: 2×Ar Fe / Mr Fe₂O₃ = **0,6994**.")

    # ---- REAKSI PERCOBAAN 5 ----
    with tab5:
        st.subheader("Percobaan 5 – Reaksi dalam Homogeneous Precipitation Ba")

        st.markdown("**Reaksi 1: Hidrolisis Urea (kunci metode homogeneous)**")
        col1, col2, col3, col4, col5, col6, col7 = st.columns([2,0.5,2,0.5,2,0.5,2])
        col1.info("CO(NH₂)₂")
        col2.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col3.info("H₂O")
        col4.markdown("<div style='text-align:center;padding-top:8px'>→</div>", unsafe_allow_html=True)
        col5.success("2 NH₃")
        col6.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col7.error("CO₂ ↑")

        st.markdown("> **Penjelasan:** Proses lambat dan merata di seluruh larutan → pH naik bertahap → BaCrO₄ mengendap dalam kristal lebih besar dan lebih murni dibanding pengendapan langsung.")
        st.divider()

        st.markdown("**Reaksi 2: Pengendapan BaCrO₄**")
        col1, col2, col3, col4, col5 = st.columns([2,0.5,2,0.5,2])
        col1.info("Ba²⁺")
        col2.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col3.info("CrO₄²⁻")
        col4.markdown("<div style='text-align:center;padding-top:8px'>→</div>", unsafe_allow_html=True)
        col5.warning("BaCrO₄ ↓ (kuning)")

        st.markdown("> **Penjelasan:** BaCrO₄ berwarna **kuning cerah**. Terbentuk hanya setelah pH cukup tinggi (urea terhidrolisis). Dalam suasana asam, CrO₄²⁻ berubah ke Cr₂O₇²⁻ yang tidak mengendapkan Ba²⁺.")
        st.divider()

        st.markdown("**Reaksi 3: Kesetimbangan Kromat ⇌ Dikromat (kontrol timing pengendapan)**")
        col1, col2, col3, col4, col5, col6, col7 = st.columns([2,0.5,2,0.5,2,0.5,2])
        col1.info("2 CrO₄²⁻ (kuning)")
        col2.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col3.info("2 H⁺")
        col4.markdown("<div style='text-align:center;padding-top:8px'>⇌</div>", unsafe_allow_html=True)
        col5.success("Cr₂O₇²⁻ (jingga)")
        col6.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col7.success("H₂O")

        st.markdown("""
        > **Penjelasan:**
        > - **Suasana asam (awal):** kesetimbangan geser ke kanan → Cr₂O₇²⁻ dominan → Ba²⁺ **tidak** mengendap
        > - **Setelah urea terhidrolisis (pH naik):** kesetimbangan geser ke kiri → CrO₄²⁻ dominan → BaCrO₄ **mulai mengendap**
        >
        > Inilah mekanisme cerdik yang membuat pengendapan terkontrol dan bertahap.
        """)
