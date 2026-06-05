# ================================================
# GRAVILAB - Panduan Praktikum Analisis Gravimetri
# Politeknik AKA Bogor - Program Studi Analisis Kimia
#
# Framework : Streamlit
# Fitur     :
#   1. Panduan Prosedur Interaktif (checklist)
#   2. Kalkulator Gravimetri Otomatis
#   3. Penjelasan Reagen (fungsi, alasan, alternatif)
#   4. Reaksi Kimia Visual
# ================================================

import streamlit as st

# ------------------------------------------------
# KONFIGURASI HALAMAN
# Pengaturan dasar tampilan web Streamlit
# ------------------------------------------------
st.set_page_config(
    page_title="GraviLab – Analisis Gravimetri",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------
# CSS TAMBAHAN
# Sedikit styling agar tampilan lebih rapi
# ------------------------------------------------
st.markdown("""
    <style>
        .block-container { padding-top: 2rem; }
        .stTabs [data-baseweb="tab"] { font-size: 0.9rem; font-weight: 600; }
        .rumus-box {
            background: #1e2a3a;
            border-left: 4px solid #f0a500;
            padding: 12px 16px;
            border-radius: 6px;
            font-family: monospace;
            font-size: 0.95rem;
            margin: 10px 0;
        }
        .reaksi-box {
            background: #0d1b2a;
            border: 1px solid #30363d;
            border-radius: 10px;
            padding: 16px 20px;
            margin-bottom: 12px;
        }
        .note-box {
            background: rgba(240,165,0,0.08);
            border-left: 3px solid #f0a500;
            padding: 10px 14px;
            border-radius: 0 6px 6px 0;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)


# ================================================
# SIDEBAR NAVIGASI
# Menu utama untuk berpindah antar fitur
# ================================================
st.sidebar.title("⚗️ GraviLab")
st.sidebar.caption("Panduan Praktikum Analisis Gravimetri\nPoliteknik AKA Bogor · 2026")
st.sidebar.divider()

menu = st.sidebar.radio(
    "Pilih Fitur",
    options=[
        "🏠 Beranda",
        "📋 Panduan Prosedur",
        "🧮 Kalkulator Gravimetri",
        "🔬 Penjelasan Reagen",
        "⚗️ Reaksi Kimia Visual"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Dibuat dengan Streamlit 🎈")


# ================================================
# HALAMAN 1: BERANDA
# ================================================
if menu == "🏠 Beranda":

    st.title("⚗️ GraviLab")
    st.subheader("Panduan Digital Praktikum Analisis Gravimetri")
    st.caption("Politeknik AKA Bogor · Program Studi Analisis Kimia · 2026")
    st.divider()

    # Penjelasan singkat aplikasi
    st.markdown("""
    Selamat datang di **GraviLab** — aplikasi bantu praktikum Analisis Gravimetri digital.
    Pilih fitur di sidebar kiri untuk memulai.
    """)

    # Tampilkan 4 kartu fitur dalam grid 2 kolom
    col1, col2 = st.columns(2)

    with col1:
        st.info("**📋 Panduan Prosedur**\n\nChecklist step-by-step 5 percobaan. Tandai langkah yang sudah selesai saat praktikum berlangsung.")
        st.info("**🔬 Penjelasan Reagen**\n\nKenapa pakai HCl? Kenapa BaCl₂? Bisa diganti apa? Semua dijelaskan lengkap.")

    with col2:
        st.info("**🧮 Kalkulator Gravimetri**\n\nInput W0, W1, W2 → hasil kadar (%) dihitung otomatis sesuai rumus tiap percobaan.")
        st.info("**⚗️ Reaksi Kimia Visual**\n\nSemua reaksi kimia tiap percobaan ditampilkan dengan keterangan yang mudah dipahami.")

    st.divider()

    # Daftar 5 percobaan di diktat
    st.subheader("📚 Daftar Percobaan")
    st.markdown("""
    | No | Judul Percobaan | Metode | Referensi |
    |----|----------------|--------|-----------|
    | 1 | Penetapan Kadar Air dalam Tepung Terigu | Pengeringan Oven 130°C | SNI 3751:2009 |
    | 2 | Penetapan Kadar Abu dalam Tepung Terigu | Pemijaran 550°C | SNI 3751:2018 |
    | 3 | Penetapan Kadar Sulfat dalam Garam Glauber | Pengendapan BaSO₄ | — |
    | 4 | Penetapan Kadar Fe dalam Garam Besi(II) | Pengendapan Fe(OH)₃ → Fe₂O₃ | — |
    | 5 | Penetapan Kadar Ba sebagai BaCrO₄ | Homogeneous Precipitation | — |
    """)


# ================================================
# HALAMAN 2: PANDUAN PROSEDUR INTERAKTIF
# Fitur checklist langkah praktikum per percobaan
# ================================================
elif menu == "📋 Panduan Prosedur":

    st.title("📋 Panduan Prosedur Interaktif")
    st.caption("Centang tiap langkah saat praktikum berlangsung agar tidak ada yang terlewat.")
    st.divider()

    # Tab untuk memilih percobaan mana
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Percobaan 1", "Percobaan 2", "Percobaan 3",
        "Percobaan 4", "Percobaan 5"
    ])

    # ---- PERCOBAAN 1: Kadar Air ----
    with tab1:
        st.subheader("Penetapan Kadar Air dalam Tepung Terigu")
        st.caption("SNI 3751:2009 | Oven 130°C | 1 jam")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**🧪 Bahan**")
            st.markdown("- Tepung terigu")
        with col2:
            st.markdown("**🛠 Peralatan**")
            st.markdown("""
            - Neraca analitik (0,1 mg)
            - Oven terkalibrasi (1°C)
            - Wadah timbang aluminium + tutup
            - Desikator
            """)

        st.markdown("**📌 Prinsip:** Kehilangan bobot akibat penguapan air pada pemanasan 130°C selama 1 jam.")
        st.divider()

        # Checklist langkah-langkah prosedur
        st.markdown("**✅ Langkah Prosedur:**")
        langkah_p1 = [
            "Timbang wadah kosong + tutup, panaskan oven (130 ± 3)°C selama **1 jam**",
            "Dinginkan dalam desikator **30 menit**, timbang sebagai **W₀**",
            "Timbang sampel **2 g** ke wadah (tutup di bawah), catat sebagai **W₁**",
            "Panaskan dalam oven (130 ± 3)°C selama **1 jam** (tidak tertutup rapat)",
            "Masukkan ke desikator **15 menit**, lalu pindah ke desikator kecil",
            "Timbang sebagai **W₂**, lalu hitung kadar air"
        ]
        selesai_p1 = 0
        for i, langkah in enumerate(langkah_p1):
            if st.checkbox(langkah, key=f"p1_{i}"):
                selesai_p1 += 1

        # Progress bar
        st.progress(selesai_p1 / len(langkah_p1), text=f"Progress: {selesai_p1}/{len(langkah_p1)} langkah selesai")

    # ---- PERCOBAAN 2: Kadar Abu ----
    with tab2:
        st.subheader("Penetapan Kadar Abu dalam Tepung Terigu")
        st.caption("SNI 3751:2018 | Tanur 550°C | 8 jam")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**🧪 Bahan**")
            st.markdown("- Tepung terigu")
        with col2:
            st.markdown("**🛠 Peralatan**")
            st.markdown("""
            - Neraca analitik
            - Cawan porselen
            - Bunsen & Tanur
            - Desikator
            """)

        st.markdown("**📌 Prinsip:** Pemijaran (550 ± 10)°C hingga terbentuk oksida logam. Oksida ditimbang sebagai kadar abu.")
        st.divider()

        st.markdown("**✅ Langkah Prosedur:**")
        langkah_p2 = [
            "Bersihkan cawan, panaskan Bunsen, masukkan tanur (550 ± 10)°C selama **1 jam**",
            "Dinginkan dalam desikator, timbang bobot tetap sebagai **W₀**",
            "Timbang sampel **(3–5) g** ke cawan, catat sebagai **W₁**",
            "Arangkan sampel di atas Bunsen hingga berasap hitam",
            "Abukan dalam tanur (550 ± 10)°C selama **8 jam** sampai putih",
            "Dinginkan desikator **30 menit**, timbang",
            "Ulangi tanur 1 jam → timbang sampai selisih ≤ 4 mg, catat sebagai **W₂**"
        ]
        selesai_p2 = 0
        for i, langkah in enumerate(langkah_p2):
            if st.checkbox(langkah, key=f"p2_{i}"):
                selesai_p2 += 1
        st.progress(selesai_p2 / len(langkah_p2), text=f"Progress: {selesai_p2}/{len(langkah_p2)} langkah selesai")

    # ---- PERCOBAAN 3: Kadar Sulfat ----
    with tab3:
        st.subheader("Penetapan Kadar Sulfat dalam Garam Glauber")
        st.caption("Pengendapan sebagai BaSO₄ | Tanur 750°C")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**🧪 Bahan**")
            st.markdown("""
            - Garam Glauber (Na₂SO₄·10H₂O)
            - HCl 4N
            - BaCl₂ 0,5N
            - AgNO₃ 0,1N
            - H₂SO₄ pekat
            """)
        with col2:
            st.markdown("**🛠 Peralatan**")
            st.markdown("""
            - Neraca analitik
            - Piala gelas 500 mL
            - Kertas saring Whatman 42
            - Cawan porselen + Tanur
            - Desikator
            """)

        st.markdown("**📌 Prinsip:** SO₄²⁻ diendapkan sebagai BaSO₄ dalam suasana asam HCl.")
        st.divider()

        st.markdown("**✅ Langkah Prosedur:**")
        langkah_p3 = [
            "Timbang **0,5 g** garam Glauber, larutkan 250–300 mL air suling",
            "Asamkan dengan **3 mL HCl 4N**, panaskan sampai mendidih",
            "Tambahkan 10 mL BaCl₂ 0,5N + 10 mL air suling (keduanya mendidih), aduk cepat ±5 detik",
            "Diamkan **1 jam** di penangas air/api kecil. Uji endapan sempurna dengan setetes BaCl₂",
            "Cuci endapan air panas sampai **bebas Cl⁻** (uji dengan AgNO₃)",
            "Masukkan ke kertas saring Whatman 42, tetesi **1 tetes H₂SO₄ pekat**, uapkan di ruang asam",
            "Pijarkan tanur **750°C** sampai bobot tetap, catat sebagai **W₂**"
        ]
        selesai_p3 = 0
        for i, langkah in enumerate(langkah_p3):
            if st.checkbox(langkah, key=f"p3_{i}"):
                selesai_p3 += 1
        st.progress(selesai_p3 / len(langkah_p3), text=f"Progress: {selesai_p3}/{len(langkah_p3)} langkah selesai")

    # ---- PERCOBAAN 4: Kadar Fe ----
    with tab4:
        st.subheader("Penetapan Kadar Fe dalam Garam Besi(II)")
        st.caption("Pengendapan Fe(OH)₃ → dipijarkan sebagai Fe₂O₃")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**🧪 Bahan**")
            st.markdown("""
            - Garam Besi(II)
            - HNO₃ pekat
            - Amonia (NH₄OH)
            - NH₄NO₃ 1%
            - AgNO₃ 0,1N & BaCl₂ 10%
            """)
        with col2:
            st.markdown("**🛠 Peralatan**")
            st.markdown("""
            - Neraca analitik
            - Piala gelas 400 mL
            - Kertas saring Whatman 41
            - Cawan porselen + Tanur
            """)

        st.markdown("**📌 Prinsip:** Fe²⁺ dioksidasi HNO₃ → Fe³⁺, diendapkan NH₄OH sebagai Fe(OH)₃, dipijarkan → Fe₂O₃.")
        st.divider()

        st.markdown("**✅ Langkah Prosedur:**")
        langkah_p4 = [
            "Timbang teliti **0,25 g** sampel, larutkan 100 mL air suling",
            "Tambahkan **10 tetes HNO₃ pekat**, panaskan mendidih. Uji oksidasi sempurna dengan setetes amonia",
            "Encerkan sampai 100 mL, panaskan hampir mendidih, endapkan dengan **amonia** sampai sempurna",
            "Diamkan **30–40 menit** di atas api kecil",
            "Saring Whatman 41, cuci dengan **NH₄NO₃ 1%** panas (3–4 kali). Uji bebas Cl⁻ dan SO₄²⁻",
            "Pindah ke cawan porselen, panaskan perlahan, arangkan kertas saring",
            "Pijarkan sampai bobot tetap, dinginkan, timbang sebagai **W₂**"
        ]
        selesai_p4 = 0
        for i, langkah in enumerate(langkah_p4):
            if st.checkbox(langkah, key=f"p4_{i}"):
                selesai_p4 += 1
        st.progress(selesai_p4 / len(langkah_p4), text=f"Progress: {selesai_p4}/{len(langkah_p4)} langkah selesai")

    # ---- PERCOBAAN 5: Kadar Ba ----
    with tab5:
        st.subheader("Penetapan Kadar Ba sebagai BaCrO₄")
        st.caption("Metode Homogeneous Precipitation | Oven 110°C")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**🧪 Bahan**")
            st.markdown("""
            - BaCl₂ 0,1 M
            - HCl 4N
            - K₂CrO₄ 4%
            - Urea
            - NH₄OH (1:19)
            """)
        with col2:
            st.markdown("**🛠 Peralatan**")
            st.markdown("""
            - Pipet volumetri
            - Piala gelas
            - Kertas saring Whatman 40
            - Oven + Neraca + Desikator
            """)

        st.markdown("**📌 Prinsip:** Urea dihidrolisis perlahan → NH₃ naikan pH bertahap → BaCrO₄ mengendap lambat dan murni.")
        st.divider()

        st.markdown("**✅ Langkah Prosedur:**")
        langkah_p5 = [
            "Pipet **25 mL BaCl₂ 0,1M**, asamkan dengan 5 mL HCl 4N",
            "Tambahkan **15 mL K₂CrO₄ 4%**, encerkan sampai 250 mL",
            "Tambahkan **7,5 g urea**, aduk sampai larut",
            "Panaskan mendidih, tunggu **90 menit** sampai tidak terbentuk kekeruhan baru",
            "Saring Whatman 40 (bobot awal = W₀), cuci dengan NH₄OH (1:19)",
            "Panaskan oven **110°C**, dinginkan, timbang sebagai **W₁**"
        ]
        selesai_p5 = 0
        for i, langkah in enumerate(langkah_p5):
            if st.checkbox(langkah, key=f"p5_{i}"):
                selesai_p5 += 1
        st.progress(selesai_p5 / len(langkah_p5), text=f"Progress: {selesai_p5}/{len(langkah_p5)} langkah selesai")


# ================================================
# HALAMAN 3: KALKULATOR GRAVIMETRI
# Hitung kadar otomatis dari input bobot
# ================================================
elif menu == "🧮 Kalkulator Gravimetri":

    st.title("🧮 Kalkulator Gravimetri Otomatis")
    st.caption("Masukkan data timbangan, kadar dihitung otomatis sesuai rumus tiap percobaan.")
    st.divider()

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Kadar Air", "Kadar Abu", "Kadar Sulfat",
        "Kadar Fe", "Kadar Ba"
    ])

    # ---- KALKULATOR 1: Kadar Air ----
    with tab1:
        st.subheader("Percobaan 1 – Kadar Air dalam Tepung Terigu")

        # Tampilkan rumus dulu sebelum input
        st.markdown("""
        <div class="rumus-box">
        Kadar Air (%) = [(W₁ – W₀) – (W₂ – W₀)] / (W₁ – W₀) × 100
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            w0_1 = st.number_input("W₀ – Wadah Kosong (g)", min_value=0.0, format="%.4f", key="w0_1")
        with col2:
            w1_1 = st.number_input("W₁ – Wadah + Sampel Sebelum (g)", min_value=0.0, format="%.4f", key="w1_1")
        with col3:
            w2_1 = st.number_input("W₂ – Wadah + Sampel Sesudah (g)", min_value=0.0, format="%.4f", key="w2_1")

        if st.button("⚗️ Hitung Kadar Air", type="primary"):
            # Validasi logika data
            if w1_1 <= w0_1:
                st.error("⚠️ W₁ harus lebih besar dari W₀ (sampel harus berbobot positif).")
            elif w2_1 > w1_1:
                st.error("⚠️ W₂ tidak boleh lebih besar dari W₁.")
            else:
                bobot_sampel = w1_1 - w0_1
                bobot_teruap = w1_1 - w2_1
                kadar = (bobot_teruap / bobot_sampel) * 100

                st.success(f"✅ **Kadar Air = {kadar:.4f} %**")
                st.markdown(f"""
                **Rincian Perhitungan:**
                - Bobot sampel (W₁ – W₀) = **{bobot_sampel:.4f} g**
                - Bobot teruapkan (W₁ – W₂) = **{bobot_teruap:.4f} g**
                - Kadar Air = {bobot_teruap:.4f} / {bobot_sampel:.4f} × 100 = **{kadar:.4f} %**
                """)

    # ---- KALKULATOR 2: Kadar Abu ----
    with tab2:
        st.subheader("Percobaan 2 – Kadar Abu dalam Tepung Terigu")

        st.markdown("""
        <div class="rumus-box">
        Kadar Abu (%) = (W₂ – W₀) / (W₁ – W₀) × 100
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            w0_2 = st.number_input("W₀ – Cawan Kosong (g)", min_value=0.0, format="%.4f", key="w0_2")
        with col2:
            w1_2 = st.number_input("W₁ – Cawan + Sampel Sebelum (g)", min_value=0.0, format="%.4f", key="w1_2")
        with col3:
            w2_2 = st.number_input("W₂ – Cawan + Abu Sesudah (g)", min_value=0.0, format="%.4f", key="w2_2")

        if st.button("⚗️ Hitung Kadar Abu", type="primary"):
            if w1_2 <= w0_2:
                st.error("⚠️ W₁ harus lebih besar dari W₀.")
            elif w2_2 < w0_2:
                st.error("⚠️ W₂ tidak boleh lebih kecil dari W₀.")
            else:
                bobot_sampel = w1_2 - w0_2
                bobot_abu    = w2_2 - w0_2
                kadar        = (bobot_abu / bobot_sampel) * 100

                st.success(f"✅ **Kadar Abu = {kadar:.4f} %**")
                st.markdown(f"""
                **Rincian Perhitungan:**
                - Bobot sampel (W₁ – W₀) = **{bobot_sampel:.4f} g**
                - Bobot abu (W₂ – W₀) = **{bobot_abu:.4f} g**
                - Kadar Abu = {bobot_abu:.4f} / {bobot_sampel:.4f} × 100 = **{kadar:.4f} %**
                """)

    # ---- KALKULATOR 3: Kadar Sulfat ----
    with tab3:
        st.subheader("Percobaan 3 – Kadar Sulfat (SO₄²⁻) dalam Garam Glauber")

        st.markdown("""
        <div class="rumus-box">
        Kadar SO₄²⁻ (%) = (Mr SO₄ / Mr BaSO₄) × (W₂ – W₀) / (W₁ – W₀) × 100
        Mr SO₄ = 96,06 g/mol | Mr BaSO₄ = 233,39 g/mol → Faktor = 0,4116
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            w0_3 = st.number_input("W₀ – Cawan Kosong (g)", min_value=0.0, format="%.4f", key="w0_3")
        with col2:
            w1_3 = st.number_input("W₁ – Cawan + Sampel (g)", min_value=0.0, format="%.4f", key="w1_3")
        with col3:
            w2_3 = st.number_input("W₂ – Cawan + Abu BaSO₄ (g)", min_value=0.0, format="%.4f", key="w2_3")

        if st.button("⚗️ Hitung Kadar Sulfat", type="primary"):
            if w1_3 <= w0_3:
                st.error("⚠️ W₁ harus lebih besar dari W₀.")
            elif w2_3 < w0_3:
                st.error("⚠️ W₂ tidak boleh lebih kecil dari W₀.")
            else:
                # Konstanta bobot molekul
                Mr_SO4   = 96.06
                Mr_BaSO4 = 233.39
                faktor   = Mr_SO4 / Mr_BaSO4

                bobot_sampel = w1_3 - w0_3
                bobot_abu    = w2_3 - w0_3
                kadar        = faktor * (bobot_abu / bobot_sampel) * 100

                st.success(f"✅ **Kadar SO₄²⁻ = {kadar:.4f} %**")
                st.markdown(f"""
                **Rincian Perhitungan:**
                - Faktor gravimetri (Mr SO₄ / Mr BaSO₄) = {Mr_SO4} / {Mr_BaSO4} = **{faktor:.4f}**
                - Bobot sampel = **{bobot_sampel:.4f} g**
                - Bobot BaSO₄ = **{bobot_abu:.4f} g**
                - Kadar SO₄²⁻ = {faktor:.4f} × {bobot_abu:.4f} / {bobot_sampel:.4f} × 100 = **{kadar:.4f} %**
                """)

    # ---- KALKULATOR 4: Kadar Fe ----
    with tab4:
        st.subheader("Percobaan 4 – Kadar Fe dalam Garam Besi(II)")

        st.markdown("""
        <div class="rumus-box">
        Kadar Fe (%) = (2 × Ar Fe / Mr Fe₂O₃) × (W₂ – W₀) / (W₁ – W₀) × 100
        Ar Fe = 55,845 | Mr Fe₂O₃ = 159,69 → Faktor = 0,6994
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            w0_4 = st.number_input("W₀ – Cawan Kosong (g)", min_value=0.0, format="%.4f", key="w0_4")
        with col2:
            w1_4 = st.number_input("W₁ – Cawan + Sampel (g)", min_value=0.0, format="%.4f", key="w1_4")
        with col3:
            w2_4 = st.number_input("W₂ – Cawan + Fe₂O₃ (g)", min_value=0.0, format="%.4f", key="w2_4")

        if st.button("⚗️ Hitung Kadar Fe", type="primary"):
            if w1_4 <= w0_4:
                st.error("⚠️ W₁ harus lebih besar dari W₀.")
            elif w2_4 < w0_4:
                st.error("⚠️ W₂ tidak boleh lebih kecil dari W₀.")
            else:
                Ar_Fe    = 55.845
                Mr_Fe2O3 = 159.69
                faktor   = (2 * Ar_Fe) / Mr_Fe2O3

                bobot_sampel = w1_4 - w0_4
                bobot_fe2o3  = w2_4 - w0_4
                kadar        = faktor * (bobot_fe2o3 / bobot_sampel) * 100

                st.success(f"✅ **Kadar Fe = {kadar:.4f} %**")
                st.markdown(f"""
                **Rincian Perhitungan:**
                - Faktor gravimetri (2×Ar Fe / Mr Fe₂O₃) = (2×{Ar_Fe}) / {Mr_Fe2O3} = **{faktor:.4f}**
                - Bobot sampel = **{bobot_sampel:.4f} g**
                - Bobot Fe₂O₃ = **{bobot_fe2o3:.4f} g**
                - Kadar Fe = {faktor:.4f} × {bobot_fe2o3:.4f} / {bobot_sampel:.4f} × 100 = **{kadar:.4f} %**
                """)

    # ---- KALKULATOR 5: Kadar Ba ----
    with tab5:
        st.subheader("Percobaan 5 – Kadar Ba sebagai BaCrO₄")

        st.markdown("""
        <div class="rumus-box">
        Kadar Ba (%) = (Ar Ba / Mr BaCrO₄) × (W₁ – W₀) / Volume (mL) × 100
        Ar Ba = 137,33 | Mr BaCrO₄ = 253,33 → Faktor = 0,5421
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            w0_5 = st.number_input("W₀ – Kertas Saring + Wadah (g)", min_value=0.0, format="%.4f", key="w0_5")
        with col2:
            w1_5 = st.number_input("W₁ – Endapan + Kertas + Wadah (g)", min_value=0.0, format="%.4f", key="w1_5")
        with col3:
            vol_5 = st.number_input("Volume Sampel (mL)", min_value=0.0, format="%.2f", key="vol_5")

        if st.button("⚗️ Hitung Kadar Ba", type="primary"):
            if w1_5 <= w0_5:
                st.error("⚠️ W₁ harus lebih besar dari W₀.")
            elif vol_5 <= 0:
                st.error("⚠️ Volume sampel harus lebih besar dari 0.")
            else:
                Ar_Ba     = 137.33
                Mr_BaCrO4 = 253.33
                faktor    = Ar_Ba / Mr_BaCrO4

                bobot_endapan = w1_5 - w0_5
                kadar         = faktor * (bobot_endapan / vol_5) * 100

                st.success(f"✅ **Kadar Ba = {kadar:.4f} %**")
                st.markdown(f"""
                **Rincian Perhitungan:**
                - Faktor gravimetri (Ar Ba / Mr BaCrO₄) = {Ar_Ba} / {Mr_BaCrO4} = **{faktor:.4f}**
                - Bobot endapan (W₁ – W₀) = **{bobot_endapan:.4f} g**
                - Volume sampel = **{vol_5} mL**
                - Kadar Ba = {faktor:.4f} × {bobot_endapan:.4f} / {vol_5} × 100 = **{kadar:.4f} %**
                """)


# ================================================
# HALAMAN 4: PENJELASAN REAGEN
# Fungsi zat, alasan pakai, dan alternatif
# ================================================
elif menu == "🔬 Penjelasan Reagen":

    st.title("🔬 Penjelasan Reagen & Reagent")
    st.caption("Kenapa pakai zat ini? Apa fungsinya? Bisa diganti dengan apa?")
    st.divider()

    # Data semua reagen dalam list of dict agar mudah di-loop
    reagen_list = [
        {
            "nama": "HCl (Asam Klorida)",
            "dipakai": "Percobaan 3, 4, 5",
            "fungsi": "Membuat suasana **asam** agar hanya ion target yang mengendap. Mencegah pengendapan pengganggu seperti fosfat, karbonat, dan kromat dari barium yang juga tidak larut di lingkungan netral.",
            "alasan": "HCl dipilih karena ion **Cl⁻ tidak ikut mengendap** bersama BaSO₄ atau BaCrO₄. Ion SO₄²⁻ dari H₂SO₄ akan mengganggu penetapan sulfat. Ion NO₃⁻ dari HNO₃ bersifat oksidator yang tidak diinginkan di tahap pengasaman awal.",
            "alternatif": [
                ("❌ H₂SO₄", "TIDAK bisa → SO₄²⁻ nya mengganggu penetapan sulfat"),
                ("❌ HNO₃ (di sini)", "TIDAK bisa → NO₃⁻ bersifat oksidator, tidak cocok untuk tahap ini"),
                ("❌ CH₃COOH", "Asam terlalu lemah, tidak cukup untuk supresi pengendapan pengganggu")
            ]
        },
        {
            "nama": "BaCl₂ (Barium Klorida)",
            "dipakai": "Percobaan 3",
            "fungsi": "Sebagai **pereaksi pengendap** ion sulfat. Reaksi: Na₂SO₄ + BaCl₂ → BaSO₄↓ + 2NaCl. Endapan BaSO₄ sangat tidak larut (Ksp ≈ 10⁻¹⁰).",
            "alasan": "BaCl₂ dipilih karena mudah larut dalam air, tidak membawa anion pengganggu (Cl⁻ tidak mengendap bersama BaSO₄), tersedia luas, dan harganya relatif terjangkau.",
            "alternatif": [
                ("✅ Ba(NO₃)₂", "Bisa digunakan, larut baik — tapi NO₃⁻ bersifat oksidator, kurang umum"),
                ("✅ Ba(CH₃COO)₂", "Bisa digunakan, aman — tapi lebih mahal dari BaCl₂")
            ]
        },
        {
            "nama": "HNO₃ Pekat",
            "dipakai": "Percobaan 4",
            "fungsi": "Sebagai **oksidator kuat**: mengoksidasi Fe²⁺ → Fe³⁺. Reaksi: 3Fe²⁺ + NO₃⁻ + 4H⁺ → 3Fe³⁺ + NO↑ + 2H₂O. Fe³⁺ diperlukan agar dapat diendapkan sempurna sebagai Fe(OH)₃.",
            "alasan": "Fe²⁺ tidak bisa diendapkan sempurna oleh amonia. Fe(OH)₂ lebih mudah larut dibanding Fe(OH)₃. Juga Fe(OH)₂ mudah teroksidasi tidak terkontrol di udara menjadi Fe(OH)₃, menyulitkan analisis.",
            "alternatif": [
                ("✅ H₂O₂", "Bisa — oksidator lebih lembut, tidak menghasilkan gas NO beracun"),
                ("✅ Air bromin (Br₂)", "Bisa — oksidator kuat, tapi uap bromin berbahaya"),
                ("❌ KMnO₄", "Tidak disarankan — membawa Mn²⁺ yang bisa ikut mengendap sebagai pengotor")
            ]
        },
        {
            "nama": "Amonia (NH₄OH)",
            "dipakai": "Percobaan 4, Pencucian Percobaan 5",
            "fungsi": "Sebagai **basa pengendap**: menaikkan pH sehingga Fe³⁺ mengendap sebagai Fe(OH)₃. Reaksi: Fe³⁺ + 3NH₄OH → Fe(OH)₃↓ + 3NH₄⁺.",
            "alasan": "Amonia adalah **basa lemah** — kelebihannya tidak membentuk endapan lain dan NH₄⁺ mudah diuapkan saat pemijaran tanpa meninggalkan residu. NaOH yang berlebih justru melarutkan kembali Fe(OH)₃ dan Na⁺ tidak bisa dihilangkan saat pemijaran.",
            "alternatif": [
                ("✅ Urea (hidrolisis)", "Bisa — menghasilkan NH₃ perlahan, dipakai di percobaan 5"),
                ("❌ NaOH", "Tidak disarankan — basa kuat, kelebihan melarutkan endapan + Na⁺ tidak bisa diuapkan"),
                ("❌ KOH", "Tidak disarankan — sama masalahnya dengan NaOH")
            ]
        },
        {
            "nama": "Urea (CO(NH₂)₂)",
            "dipakai": "Percobaan 5",
            "fungsi": "Kunci metode **homogeneous precipitation**. Urea terhidrolisis perlahan oleh panas: CO(NH₂)₂ + H₂O → 2NH₃ + CO₂. NH₃ yang dihasilkan secara bertahap menaikkan pH sehingga BaCrO₄ mengendap lambat dalam kristal lebih besar dan lebih murni.",
            "alasan": "Jika amonia ditambah langsung, pH naik tiba-tiba → pengendapan cepat → endapan sangat halus, amorf, sulit disaring, mudah terkontaminasi. Urea memberi kenaikan pH yang **lambat dan merata** di seluruh larutan.",
            "alternatif": [
                ("✅ Heksametilentetramina", "Bisa — prinsip sama, hidrolisis lambat → basa, tapi lebih mahal"),
                ("❌ NH₃ langsung", "Tidak disarankan — endapan kasar, kotor, dan tidak merata")
            ]
        },
        {
            "nama": "K₂CrO₄ (Kalium Kromat)",
            "dipakai": "Percobaan 5",
            "fungsi": "Sebagai **pereaksi pengendap barium**. Reaksi: Ba²⁺ + CrO₄²⁻ → BaCrO₄↓ (endapan kuning). BaCrO₄ tidak larut dalam larutan netral-basa.",
            "alasan": "Dalam suasana asam, CrO₄²⁻ berubah ke Cr₂O₇²⁻ (dikromat) yang tidak bisa mengendapkan Ba²⁺. Saat urea terhidrolisis dan pH naik, CrO₄²⁻ terbentuk kembali dan mulai mengendapkan BaCrO₄. Ini mengontrol kapan dan seberapa cepat pengendapan berlangsung.",
            "alternatif": [
                ("✅ Na₂CrO₄", "Bisa — fungsi sama, sama-sama sumber ion kromat (CrO₄²⁻)"),
                ("— BaSO₄ (metode lain)", "Percobaan 3 menggunakan prinsip berbeda dengan BaCl₂ + SO₄²⁻")
            ]
        },
        {
            "nama": "NH₄NO₃ 1% (larutan pencuci)",
            "dipakai": "Percobaan 4",
            "fungsi": "Sebagai **larutan pencuci endapan Fe(OH)₃**. Mengandung elektrolit NH₄⁺ yang mencegah peptisasi (pecahnya koloid endapan menjadi partikel sangat halus yang lolos dari kertas saring).",
            "alasan": "Air suling murni tanpa elektrolit dapat menyebabkan endapan koloid Fe(OH)₃ terpeptisasi dan lolos dari pori kertas saring, menyebabkan kehilangan massa dan hasil yang lebih rendah dari seharusnya.",
            "alternatif": [
                ("✅ NH₄Cl encer", "Bisa — sama-sama elektrolit yang mudah menguap saat pemijaran"),
                ("❌ Air suling saja", "Tidak disarankan — risiko peptisasi endapan → hasil kurang akurat")
            ]
        },
        {
            "nama": "H₂SO₄ Pekat (1 tetes)",
            "dipakai": "Percobaan 3",
            "fungsi": "Mencegah **reduksi BaSO₄ oleh karbon** dari abu kertas saring. Reaksi yang harus dicegah: BaSO₄ + 4C → BaS + 4CO. Penetesan H₂SO₄ pekat lalu diuapkan memastikan BaSO₄ tetap stabil saat pemijaran.",
            "alasan": "Hanya 1 tetes karena tujuannya hanya membuat suasana oksidatif lokal. Kelebihan H₂SO₄ bisa merusak cawan porselen atau menyebabkan percikan berbahaya saat dipanaskan.",
            "alternatif": [
                ("❌ Tidak bisa diganti", "Fungsinya sangat spesifik untuk stabilisasi BaSO₄ saat pemijaran karbon")
            ]
        }
    ]

    # Loop tampilkan semua reagen dalam expander (accordion)
    for r in reagen_list:
        with st.expander(f"🧪 {r['nama']}  —  dipakai di: {r['dipakai']}"):
            col1, col2 = st.columns([1, 1])

            with col1:
                st.markdown("**⚙️ Fungsi Utama**")
                st.markdown(r["fungsi"])
                st.markdown("**❓ Alasan Penggunaan**")
                st.markdown(r["alasan"])

            with col2:
                st.markdown("**🔄 Alternatif Pengganti**")
                for nama_alt, keterangan in r["alternatif"]:
                    st.markdown(f"- **{nama_alt}**: {keterangan}")


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

    # ---- REAKSI PERCOBAAN 2 ----
    with tab2:
        st.subheader("Percobaan 2 – Pembentukan Oksida Logam saat Pemijaran 550°C")

        st.markdown("**Reaksi Umum Pembakaran Organik:**")
        col1, col2, col3, col4, col5 = st.columns([2,1,2,1,2])
        col1.info("Mineral organik")
        col2.markdown("<div style='text-align:center;font-size:1.3rem;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col3.info("O₂")
        col4.markdown("<div style='text-align:center;font-size:1.3rem;padding-top:8px'>→</div>", unsafe_allow_html=True)
        col5.warning("Oksida Logam ↓")

        st.markdown("""
        > **Penjelasan:** Saat dipanaskan 550°C, semua senyawa organik (C, H, N) terbakar menjadi CO₂, H₂O, dan N₂ yang menguap.
        Yang tersisa hanyalah oksida logam padat — inilah yang ditimbang sebagai **kadar abu**.
        Contoh: 2 FeCO₃ + ½ O₂ → Fe₂O₃ + 2 CO₂
        """)

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
