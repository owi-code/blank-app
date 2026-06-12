import streamlit as st

# ====================
# KONFIGURASI AWAL
# ====================
st.set_page_config(page_title="GraviLab – Analisis Gravimetri", page_icon="⚗️", layout="wide")
st.markdown("""<style>.block-container{padding-top:2rem;}.rumus-box{background:#f0f8ff;border-left:4px solid #2c7be5;padding:12px 16px;border-radius:6px;font-family:monospace;white-space:pre-line;color:#000;}.reaksi-box{background:#f8f9fa;border:1px solid #dee2e6;border-radius:10px;padding:16px;}div.stButton > button:first-child {background-color:#ff2b2b;color:white;border:none;}</style>""", unsafe_allow_html=True)

# ====================
# BILAH SAMPING
# ====================
st.sidebar.title("⚗️ GraviLab")
st.sidebar.caption("Panduan Praktikum Analisis Gravimetri\n2026")
st.sidebar.divider()
menu = st.sidebar.radio("Pilih Fitur", ["🏠 Beranda", "📋 Panduan Prosedur", "🧮 Kalkulator Gravimetri", "🔬 Penjelasan Reagen", "⚗️ Reaksi Kimia Visual"])

# ====================
# HALAMAN BERANDA
# ====================
if menu == "🏠 Beranda":
    st.title("⚗️ GraviLab")
    st.subheader("Panduan Digital Praktikum Analisis Gravimetri")
    st.caption("Program Studi Analisis Kimia · 2026")
    st.divider()
    st.markdown("Selamat datang di GraviLab — aplikasi bantu praktikum Analisis Gravimetri digital. Pilih fitur di bilah samping kiri untuk memulai.")
    c1,c2=st.columns(2)
    with c1:
        st.info("📋 **Panduan Prosedur**\n\nDaftar langkah demi langkah lengkap sesuai prosedur laboratorium & standar SNI.")
        st.info("🔬 **Penjelasan Reagen**\n\nAlasan pemakaian zat, fungsi, dan zat pengganti yang diperbolehkan/dilarang.")
    with c2:
        st.info("🧮 **Kalkulator Gravimetri**\n\nMasukkan data penimbangan → hasil kadar langsung terhitung otomatis.")
        st.info("⚗️ **Reaksi Kimia Visual**\n\nTampilan persamaan reaksi lengkap beserta penjelasannya.")
    st.divider()
    st.subheader("📚 Daftar Percobaan & Standar Acuan")
    st.markdown("| No | Judul Percobaan | Metode | Standar Acuan |\n|:-:|:---|:---|:---|\n|1| Kadar Air Tepung Terigu | Pengeringan Oven 130°C | SNI 3751:2009, SNI 01-2891-1992 |\n|2| Kadar Abu Tepung Terigu | Pengabuan Tanur 550°C | SNI 3751:2018, SNI 01-3185-1992 |\n|3| Kadar Sulfat dalam Garam Glauber | Pengendapan BaSO₄ | SNI 06-2513-1991, SNI 19-1665-2000 |\n|4| Kadar Besi dalam Garam Besi(II) | Oksidasi & Pengendapan Fe₂O₃ | SNI 06-1568-1989, SNI 19-1449-1989 |\n|5| Kadar Barium dengan Metode Seragam | Pengendapan Terkendali | SNI 06-2054-1990, SNI 19-3656-1994 |")

# ====================
# HALAMAN PANDUAN PROSEDUR
# ====================
elif menu == "📋 Panduan Prosedur":
    st.title("📋 Panduan Prosedur Interaktif")
    st.divider()
    tab1,tab2,tab3,tab4,tab5=st.tabs(["Percobaan 1","Percobaan 2","Percobaan 3","Percobaan 4","Percobaan 5"])

    # --- PERCOBAAN 1: KADAR AIR ---
    with tab1:
        st.subheader("Percobaan 1: Penetapan Kadar Air dalam Tepung Terigu")
        st.caption("Suhu Pengeringan 130°C")
        metode_pilih = st.radio("Pilih Prosedur Kerja:", ["📘 Prosedur Standar Laboratorium", "📙 Standar SNI 3751:2009", "📗 Standar SNI 01-2891-1992"])

        if metode_pilih == "📘 Prosedur Standar Laboratorium":
            st.markdown("🧪 **Bahan:** Tepung terigu, kertas saring bebas abu")
            st.markdown("🛠 **Alat:** Neraca analitik, pengering udara listrik, wadah timbang aluminium, tang penjepit, desikator")
            langkah = [
                "Panaskan wadah timbang kosong pada suhu 130°C selama 60 menit, dinginkan dalam desikator, timbang hingga bobot tetap → catat sebagai W₀",
                "Timbang sampel tepung terigu tepat 2,0000 gram ke dalam wadah timbang yang sudah diketahui bobotnya → catat bobot wadah + sampel sebagai W₁",
                "Panaskan kembali wadah berisi sampel pada suhu 130°C selama 60 menit",
                "Pindahkan ke desikator, dinginkan hingga suhu ruang, timbang ulang. Ulangi pemanasan dan penimbangan hingga selisih bobot ≤ 0,0002 g → catat bobot tetap sebagai W₂"
            ]
        elif metode_pilih == "📙 Standar SNI 3751:2009":
            st.markdown("🧪 **Bahan:** Tepung terigu")
            st.markdown("🛠 **Alat:** Neraca analitik, oven pengering, cawan timbang, desikator")
            langkah = [
                "Panaskan cawan timbang kosong di oven 130°C selama 30 menit, dinginkan desikator, timbang → W₀",
                "Masukkan sekitar 2 g sampel ke cawan, ratakan, timbang segera → W₁",
                "Panaskan di suhu 130°C selama 60 menit",
                "Dinginkan, timbang. Ulangi pemanasan 30 menit sampai bobot tetap → W₂"
            ]
        else: # SNI 01-2891-1992
            st.markdown("🧪 **Bahan:** Tepung terigu")
            st.markdown("🛠 **Alat:** Neraca analitik, oven, wadah timbang, desikator")
            langkah = [
                "Panaskan wadah kosong 1 jam pada 105°C, dinginkan, timbang → W₀",
                "Timbang 5 g sampel tepat ke wadah → W₁",
                "Keringkan pada suhu 105°C selama 3 jam",
                "Dinginkan, timbang. Keringkan lagi 30 menit sampai bobot tetap → W₂"
            ]

        # SISTEM CEKLIS BERURUTAN TERKUNCI
        ceklis = [False]*len(langkah)
        ceklis[0] = st.checkbox(langkah[0], key="p1_0")
        ceklis[1] = st.checkbox(langkah[1], key="p1_1", disabled=not ceklis[0])
        ceklis[2] = st.checkbox(langkah[2], key="p1_2", disabled=not ceklis[1])
        ceklis[3] = st.checkbox(langkah[3], key="p1_3", disabled=not ceklis[2])
        selesai = sum(ceklis)
        st.progress(selesai/len(langkah), text=f"Kemajuan: {selesai}/{len(langkah)} langkah selesai")

    # --- PERCOBAAN 2: KADAR ABU ---
    with tab2:
        st.subheader("Percobaan 2: Penetapan Kadar Abu dalam Tepung Terigu")
        st.caption("Suhu Pengabuan 550°C")
        metode_pilih = st.radio("Pilih Prosedur Kerja:", ["📘 Prosedur Standar Laboratorium", "📙 Standar SNI 3751:2018", "📗 Standar SNI 01-3185-1992"])

        if metode_pilih == "📘 Prosedur Standar Laboratorium":
            st.markdown("🧪 **Bahan:** Tepung terigu")
            st.markdown("🛠 **Alat:** Neraca analitik, tanur pengabuan, cawan porselin, pembakar Bunsen, tang penjepit, desikator")
            langkah = [
                "Panaskan cawan porselin kosong dalam tanur pada suhu 550°C selama 60 menit, dinginkan desikator, timbang hingga bobot tetap → W₀",
                "Timbang sampel tepung sebanyak 3–5 gram ke dalam cawan porselin → catat bobot cawan + sampel sebagai W₁",
                "Arangkan sampel di atas pembakar Bunsen sampai tidak berasap sama sekali, kemudian masukkan ke tanur 550°C selama 8 jam sampai abu berwarna putih kelabu",
                "Dinginkan cawan di atas piring logam, masukkan ke desikator, timbang ulang. Pijar ulang 30 menit sampai bobot tetap → W₂"
            ]
        elif metode_pilih == "📙 Standar SNI 3751:2018":
            st.markdown("🧪 **Bahan:** Tepung terigu")
            st.markdown("🛠 **Alat:** Neraca analitik, tanur, cawan porselin, desikator")
            langkah = [
                "Panaskan cawan kosong 550°C 1 jam, dinginkan, timbang → W₀",
                "Timbang 2–5 g sampel ke cawan → W₁",
                "Arangkan perlahan, masukkan tanur 550°C sampai abu putih bersih",
                "Dinginkan, timbang. Pijar ulang sampai bobot tetap → W₂"
            ]
        else: # SNI 01-3185-1992
            st.markdown("🧪 **Bahan:** Tepung terigu")
            st.markdown("🛠 **Alat:** Neraca analitik, tanur, cawan, desikator")
            langkah = [
                "Panaskan cawan 600°C 1 jam, dinginkan, timbang → W₀",
                "Panaskan 5 g sampel ke cawan → W₁",
                "Arangkan, abukan 600°C selama 4 jam",
                "Dinginkan, timbang. Ulangi pemijaran sampai bobot tetap → W₂"
            ]

        # SISTEM CEKLIS BERURUTAN TERKUNCI
        ceklis = [False]*len(langkah)
        ceklis[0] = st.checkbox(langkah[0], key="p2_0")
        ceklis[1] = st.checkbox(langkah[1], key="p2_1", disabled=not ceklis[0])
        ceklis[2] = st.checkbox(langkah[2], key="p2_2", disabled=not ceklis[1])
        ceklis[3] = st.checkbox(langkah[3], key="p2_3", disabled=not ceklis[2])
        selesai = sum(ceklis)
        st.progress(selesai/len(langkah), text=f"Kemajuan: {selesai}/{len(langkah)} langkah selesai")

    # --- PERCOBAAN 3: KADAR SULFAT ---
    with tab3:
        st.subheader("Percobaan 3: Penetapan Kadar Sulfat dalam Garam Glauber")
        metode_pilih = st.radio("Pilih Prosedur Kerja:", ["📘 Prosedur Standar Laboratorium", "📙 Standar SNI 06-2513-1991", "📗 Standar SNI 19-1665-2000"])

        if metode_pilih == "📘 Prosedur Standar Laboratorium":
            st.markdown("🧪 **Bahan:** Garam glauber, larutan HCl 4N, larutan BaCl₂ 10%, larutan AgNO₃ 0,1N")
            st.markdown("🛠 **Alat:** Gelas kimia 400 mL, penangas air, corong kaca, kertas saring bebas abu, tanur pemijaran, neraca analitik")
            langkah = [
                "Timbang sampel garam glauber sebanyak 0,5000 gram tepat, larutkan dalam 200 mL air suling dalam gelas kimia",
                "Tambahkan 2 mL larutan HCl 4N, panaskan di atas penangas air sampai mendidih",
                "Teteskan larutan BaCl₂ 10% panas perlahan-lahan sambil diaduk terus sampai pengendapan sempurna, diamkan 1 jam di penangas air panas",
                "Saring endapan dengan kertas saring bebas abu, cuci dengan air panas sampai bebas ion klorida (uji dengan AgNO₃), keringkan, pijar 800°C sampai bobot tetap → timbang endapan BaSO₄"
            ]
        elif metode_pilih == "📙 Standar SNI 06-2513-1991":
            st.markdown("🧪 **Bahan:** Sampel sulfat, HCl, BaCl₂")
            st.markdown("🛠 **Alat:** Gelas kimia, penangas, corong, kertas saring, tanur")
            langkah = [
                "Larutkan sampel dalam air, tambah HCl sampai asam",
                "Panaskan mendidih, tambah BaCl₂ berlebih perlahan",
                "Diamkan semalam, saring, cuci netral",
                "Pijar 800°C, timbang sampai bobot tetap"
            ]
        else:
            st.markdown("🧪 **Bahan:** Sampel, HCl, BaCl₂")
            st.markdown("🛠 **Alat:** Gelas kimia, pemanas, corong, tanur")
            langkah = [
                "Timbang sampel, larutkan air, tambah HCl",
                "Panaskan, tambah BaCl₂ panas perlahan",
                "Diamkan 2 jam, saring, cuci bersih",
                "Pijar, timbang endapan"
            ]

        # SISTEM CEKLIS BERURUTAN TERKUNCI
        ceklis = [False]*len(langkah)
        ceklis[0] = st.checkbox(langkah[0], key="p3_0")
        ceklis[1] = st.checkbox(langkah[1], key="p3_1", disabled=not ceklis[0])
        ceklis[2] = st.checkbox(langkah[2], key="p3_2", disabled=not ceklis[1])
        ceklis[3] = st.checkbox(langkah[3], key="p3_3", disabled=not ceklis[2])
        selesai = sum(ceklis)
        st.progress(selesai/len(langkah), text=f"Kemajuan: {selesai}/{len(langkah)} langkah selesai")

    # --- PERCOBAAN 4: KADAR BESI ---
    with tab4:
        st.subheader("Percobaan 4: Penetapan Kadar Besi dalam Garam Besi(II)")
        metode_pilih = st.radio("Pilih Prosedur Kerja:", ["📘 Prosedur Standar Laboratorium", "📙 Standar SNI 06-1568-1989", "📗 Standar SNI 19-1449-1989"])

        if metode_pilih == "📘 Prosedur Standar Laboratorium":
            st.markdown("🧪 **Bahan:** Garam besi(II), larutan HCl encer, HNO₃ pekat, larutan amonia 1:1, larutan NH₄NO₃ 1%")
            st.markdown("🛠 **Alat:** Gelas kimia 400 mL, pembakar, corong kaca, kertas saring bebas abu, tanur pemijaran, neraca analitik")
            langkah = [
                "Timbang sampel garam besi(II) sebanyak 0,2500 gram tepat, larutkan dalam 100 mL air suling + 5 mL HCl encer",
                "Tambahkan 2 mL HNO₃ pekat, panaskan sampai mendidih untuk mengoksidasi sempurna ion Fe²⁺ menjadi Fe³⁺",
                "Dinginkan sedikit, teteskan larutan amonia 1:1 berlebih sambil diaduk sampai endapan Fe(OH)₃ terbentuk sempurna dan larutan bersifat basa",
                "Saring endapan, cuci dengan larutan NH₄NO₃ 1% sampai bebas ion klorida, keringkan, pijar 800°C sampai menjadi Fe₂O₃ dan bobot tetap → timbang"
            ]
        elif metode_pilih == "📙 Standar SNI 06-1568-1989":
            st.markdown("🧪 **Bahan:** Sampel besi, HCl, HNO₃, amonia")
            st.markdown("🛠 **Alat:** Gelas kimia, pemanas, corong, tanur")
            langkah = [
                "Larutkan sampel dalam air + HCl",
                "Oksidasi dengan HNO₃ panas",
                "Endapkan dengan amonia berlebih",
                "Saring, cuci, pijar jadi oksida besi, timbang"
            ]
        else:
            st.markdown("🧪 **Bahan:** Sampel, asam kuat, pengoksidasi, amonia")
            st.markdown("🛠 **Alat:** Gelas kimia, corong, tanur")
            langkah = [
                "Timbang dan larutkan sampel",
                "Oksidasi ion besi",
                "Endapkan sebagai hidroksida",
                "Pijar jadi oksida, timbang"
            ]

        # SISTEM CEKLIS BERURUTAN TERKUNCI
        ceklis = [False]*len(langkah)
        ceklis[0] = st.checkbox(langkah[0], key="p4_0")
        ceklis[1] = st.checkbox(langkah[1], key="p4_1", disabled=not ceklis[0])
        ceklis[2] = st.checkbox(langkah[2], key="p4_2", disabled=not ceklis[1])
        ceklis[3] = st.checkbox(langkah[3], key="p4_3", disabled=not ceklis[2])
        selesai = sum(ceklis)
        st.progress(selesai/len(langkah), text=f"Kemajuan: {selesai}/{len(langkah)} langkah selesai")

    # --- PERCOBAAN 5: KADAR BARIUM ---
    with tab5:
        st.subheader("Percobaan 5: Penetapan Kadar Barium dengan Metode Seragam")
        metode_pilih = st.radio("Pilih Prosedur Kerja:", ["📘 Prosedur Standar Laboratorium", "📙 Standar SNI 06-2054-1990", "📗 Standar SNI 19-3656-1994"])

        if metode_pilih == "📘 Prosedur Standar Laboratorium":
            st.markdown("🧪 **Bahan:** Larutan induk BaCl₂ 0,1 M, larutan HCl 2N, larutan K₂CrO₄ 10%, kristal urea, air suling")
            st.markdown("🛠 **Alat:** Pipet ukur, gelas kimia 400 mL, penangas air mendidih, corong kaca, kertas saring, desikator, neraca analitik")
            langkah = [
                "Ambil tepat 25,0 mL larutan BaCl₂ 0,1 M masukkan ke gelas kimia, tambahkan 2 mL larutan HCl 2N",
                "Tambahkan 10 mL larutan K₂CrO₄ 10% dan 5 gram kristal urea, aduk sampai larut sempurna, encerkan sampai volume 200 mL",
                "Panaskan perlahan di atas penangas air mendidih selama ± 90 menit sampai pH naik dan endapan kuning terbentuk merata",
                "Dinginkan, saring endapan BaCrO₄, cuci bersih, keringkan dalam oven 110°C sampai bobot tetap → timbang"
            ]
        elif metode_pilih == "📙 Standar SNI 06-2054-1990":
            st.markdown("🧪 **Bahan:** Larutan barium, HCl, urea, kalium kromat")
            st.markdown("🛠 **Alat:** Pipet, gelas kimia, pemanas, corong, oven")
            langkah = [
                "Ambil volume tertentu larutan sampel, buat suasana asam lemah dengan HCl",
                "Tambahkan urea dan pereaksi kromat secukupnya",
                "Panaskan lama agar endapan terbentuk perlahan dan merata",
                "Saring, cuci, keringkan 120°C, timbang tetap"
            ]
        else:
            st.markdown("🧪 **Bahan:** Sampel barium, asam, urea, pengendap")
            st.markdown("🛠 **Alat:** Gelas kimia, penangas, corong, alat timbang")
            langkah = [
                "Siapkan larutan sampel, atur keasaman",
                "Tambahkan zat pengatur pH perlahan dan pereaksi",
                "Panaskan sampai pengendapan sempurna",
                "Pisahkan endapan, keringkan, timbang tetap"
            ]

        # SISTEM CEKLIS BERURUTAN TERKUNCI
        ceklis = [False]*len(langkah)
        ceklis[0] = st.checkbox(langkah[0], key="p5_0")
        ceklis[1] = st.checkbox(langkah[1], key="p5_1", disabled=not ceklis[0])
        ceklis[2] = st.checkbox(langkah[2], key="p5_2", disabled=not ceklis[1])
        ceklis[3] = st.checkbox(langkah[3], key="p5_3", disabled=not ceklis[2])
        selesai = sum(ceklis)
        st.progress(selesai/len(langkah), text=f"Kemajuan: {selesai}/{len(langkah)} langkah selesai")

# ====================
# HALAMAN KALKULATOR GRAVIMETRI
# ====================
elif menu == "🧮 Kalkulator Gravimetri":
    st.title("🧮 Kalkulator Gravimetri Otomatis")
    st.divider()
    tab1,tab2,tab3,tab4,tab5=st.tabs(["Kadar Air","Kadar Abu","Kadar Sulfat","Kadar Besi","Kadar Barium"])

    # --- PERCOBAAN 1: KADAR AIR ---
    with tab1:
        st.markdown('<div class="rumus-box">📌 Rumus:\nKadar Air (%) = [( (W₁ - W₀) - (W₂ - W₀) ) / (W₁ - W₀)] × 100\n\nKeterangan:\nW₀ = Bobot wadah kosong (g)\nW₁ = Bobot wadah + sampel awal (g)\nW₂ = Bobot wadah + residu setelah dikeringkan (g)</div>',unsafe_allow_html=True)
        w0=st.number_input("Bobot wadah kosong (W₀)", format="%.4f", key="wa0")
        w1=st.number_input("Bobot wadah + sampel awal (W₁)", format="%.4f", key="wa1")
        w2=st.number_input("Bobot wadah + residu kering (W₂)", format="%.4f", key="wa2")
        if st.button("Hitung Kadar Air", type="primary"):
            if w1 > w0 and w2 <= w1:
                kadar = (((w1 - w0) - (w2 - w0)) / (w1 - w0)) * 100
                st.success(f"✅ Kadar Air = {kadar:.4f} %")
            else:
                st.error("⚠️ Periksa kembali nilai masukan! Pastikan W₁ > W₀ dan W₂ ≤ W₁")

    # --- PERCOBAAN 2: KADAR ABU ---
    with tab2:
        st.markdown('<div class="rumus-box">📌 Rumus:\nKadar Abu (%) = [(W₂ - W₀) / (W₁ - W₀)] × 100\n\nKeterangan:\nW₀ = Bobot cawan kosong (g)\nW₁ = Bobot cawan + sampel awal (g)\nW₂ = Bobot cawan + abu setelah dipijar (g)</div>',unsafe_allow_html=True)
        w0=st.number_input("Bobot cawan kosong (W₀)", format="%.4f", key="wu0")
        w1=st.number_input("Bobot cawan + sampel awal (W₁)", format="%.4f", key="wu1")
        w2=st.number_input("Bobot cawan + abu (W₂)", format="%.4f", key="wu2")
        if st.button("Hitung Kadar Abu", type="primary"):
            if w1 > w0 and w2 >= w0:
                kadar = ((w2 - w0) / (w1 - w0)) * 100
                st.success(f"✅ Kadar Abu = {kadar:.4f} %")
            else:
                st.error("⚠️ Periksa kembali nilai masukan! Pastikan W₁ > W₀ dan W₂ ≥ W₀")

    # --- PERCOBAAN 3: KADAR SULFAT ---
    with tab3:
        st.markdown('<div class="rumus-box">📌 Rumus:\nKadar SO₄²⁻ (%) = (BM SO₄²⁻ / BM BaSO₄) × [(W₂ - W₀) / W₁] × 100\nBM SO₄²⁻ = 96,06 ; BM BaSO₄ = 233,39\n\nKeterangan:\nW₀ = Bobot cawan + kertas kosong (g)\nW₁ = Bobot sampel yang ditimbang awal (g)\nW₂ = Bobot cawan + endapan BaSO₄ (g)</div>',unsafe_allow_html=True)
        w0=st.number_input("Bobot cawan + kertas saring kosong (W₀)", format="%.4f", key="ws0")
        w1=st.number_input("Bobot sampel awal (W₁)", format="%.4f", key="ws1")
        w2=st.number_input("Bobot cawan + endapan BaSO₄ (W₂)", format="%.4f", key="ws2")
        if st.button("Hitung Kadar Sulfat", type="primary"):
            if w1 > 0 and w2 >= w0:
                kadar = (96.06 / 233.39) * ((w2 - w0) / w1) * 100
                st.success(f"✅ Kadar SO₄²⁻ = {kadar:.4f} %")
            else:
                st.error("⚠️ Periksa kembali nilai masukan! Pastikan W₁ > 0 dan W₂ ≥ W₀")

    # --- PERCOBAAN 4: KADAR BESI ---
    with tab4:
        st.markdown('<div class="rumus-box">📌 Rumus:\nKadar Fe (%) = [(2 × Ar Fe) / BM Fe₂O₃] × [(W₂ - W₀) / (W₁ - W₀)] × 100\nAr Fe = 55,85 ; BM Fe₂O₃ = 159,69\n\nKeterangan:\nW₀ = Bobot cawan + sisa abu kertas (g)\nW₁ = Bobot sampel awal (g)\nW₂ = Bobot cawan + endapan Fe₂O₃ (g)</div>',unsafe_allow_html=True)
        w0=st.number_input("Bobot cawan kosong (W₀)", format="%.4f", key="wf0")
        w1=st.number_input("Bobot sampel awal (W₁)", format="%.4f", key="wf1")
        w2=st.number_input("Bobot cawan + endapan Fe₂O₃ (W₂)", format="%.4f", key="wf2")
        if st.button("Hitung Kadar Besi", type="primary"):
            if w1 > w0 and w2 >= w0:
                kadar = ((2 * 55.85) / 159.69) * ((w2 - w0) / (w1 - w0)) * 100
                st.success(f"✅ Kadar Fe = {kadar:.4f} %")
            else:
                st.error("⚠️ Periksa kembali nilai masukan! Pastikan W₁ > W₀ dan W₂ ≥ W₀")

    # --- PERCOBAAN 5: KADAR BARIUM ---
    with tab5:
        st.markdown('<div class="rumus-box">📌 Rumus:\nKadar Ba (%) = (Ar Ba / BM BaCrO₄) × [(W₁ - W₀) / Volume Sampel] × 100\nAr Ba = 137,33 ; BM BaCrO₄ = 253,32\n\nKeterangan:\nW₀ = Bobot wadah kosong (g)\nW₁ = Bobot wadah + endapan BaCrO₄ (g)\nVolume = Volume larutan sampel (mL)</div>',unsafe_allow_html=True)
        w0=st.number_input("Bobot wadah kosong (W₀)", format="%.4f", key="wb0")
        w1=st.number_input("Bobot wadah + endapan BaCrO₄ (W₁)", format="%.4f", key="wb1")
        vol=st.number_input("Volume larutan sampel (mL)", format="%.2f", key="vb")
        if st.button("Hitung Kadar Barium", type="primary"):
            if w1 > w0 and vol > 0:
                kadar = (137.33 / 253.32) * ((w1 - w0) / vol) * 100
                st.success(f"✅ Kadar Ba = {kadar:.4f} %")
            else:
                st.error("⚠️ Periksa kembali nilai masukan! Pastikan W₁ > W₀ dan Volume > 0")

# ====================
# HALAMAN PENJELASAN REAGEN
# ====================
elif menu == "🔬 Penjelasan Reagen":
    st.title("🔬 Penjelasan Reagen")
    st.divider()
    daftar=[
        {"nama":"Asam Klorida · HCl","pakai":"Percobaan 3, 4, dan 5","fungsi":"Membuat suasana asam agar hanya ion sasaran yang mengendap sempurna sekaligus mencegah pengendapan zat pengganggu","alt":["❌ Dilarang pakai H₂SO₄ · mengganggu analisis ion sulfat","❌ Dilarang pakai HNO₃ · bersifat pengoksidasi kuat dan mengubah kondisi reaksi"]},
        {"nama":"Barium Klorida · BaCl₂","pakai":"Percobaan 3","fungsi":"Zat pengendap khusus ion sulfat membentuk endapan BaSO₄ yang sangat sukar larut","alt":["✅ Bisa diganti Ba(NO₃)₂ · larut dan tidak meninggalkan residu","✅ Bisa diganti Ba(CH₃COO)₂ · aman dan reaksinya serupa"]},
        {"nama":"Asam Nitrat Pekat · HNO₃","pakai":"Percobaan 4","fungsi":"Bertindak sebagai pengoksidasi kuat mengubah ion Fe²⁺ menjadi Fe³⁺ agar mudah diendapkan sempurna","alt":["✅ Bisa diganti Larutan H₂O₂ · lebih aman dan tidak berasap","✅ Bisa diganti Air Bromin · daya oksidasi kuat"]},
        {"nama":"Larutan Amonia · NH₄OH","pakai":"Percobaan 4 dan 5","fungsi":"Basa lemah untuk mengatur nilai pH sekaligus zat pengendap Fe(OH)₃","alt":["✅ Bisa diganti Kristal Urea · menaikkan pH perlahan dan merata","❌ Dilarang pakai NaOH/KOH · basa terlalu kuat malah melarutkan kembali endapan"]},
        {"nama":"Urea · CO(NH₂)₂","pakai":"Percobaan 5","fungsi":"Terurai perlahan menjadi amonia merata di seluruh larutan → kunci keberhasilan metode pengendapan seragam","alt":["✅ Bisa diganti Heksametilentetramina · mekanisme kerjanya mirip","❌ Dilarang langsung pakai amonia · endapan kasar dan kotor"]},
        {"nama":"Amonium Nitrat · NH₄NO₃","pakai":"Percobaan 4","fungsi":"Larutan pencuci khusus mencegah pemecahan endapan berbentuk koloid saat penyaringan","alt":["✅ Bisa diganti Larutan NH₄Cl encer · efeknya sama","❌ Dilarang pakai air suling saja · endapan bisa terurai kembali"]},
        {"nama":"Asam Sulfat Pekat · H₂SO₄","pakai":"Percobaan 3","fungsi":"Mencegah reduksi BaSO₄ menjadi BaS yang larut saat dipanaskan suhu sangat tinggi","alt":["❌ Tidak ada zat pengganti yang cocok dan aman"]}
    ]
    for z in daftar:
        with st.expander(f"🧪 {z['nama']} — dipakai pada: {z['pakai']}"):
            st.markdown(f"**Fungsi:** {z['fungsi']}\n\n**Zat Pengganti / Catatan:**\n"+"\n".join(f"- {a}" for a in z['alt']))

# ====================
# HALAMAN REAKSI KIMIA VISUAL
# ====================
elif menu == "⚗️ Reaksi Kimia Visual":
    st.title("⚗️ Reaksi Kimia Visual")
    st.caption("Seluruh persamaan reaksi kimia dari setiap percobaan lengkap beserta penjelasan terperinci")
    st.divider()
    st.markdown("**Keterangan Warna:**")
    col1, col2, col3, col4 = st.columns(4)
    col1.info("🔵 Zat Pereaksi / Bahan Awal")
    col2.success("🟢 Produk Larut dalam Air")
    col3.warning("🟡 Endapan Tidak Larut (↓)")
    col4.error("🔴 Gas yang Terlepas (↑)")
    st.divider()
    tab3, tab4, tab5 = st.tabs(["Percobaan 3","Percobaan 4","Percobaan 5"])
    with tab3:
        st.subheader("Percobaan 3 · Penetapan Kadar Sulfat")
        st.markdown("**Reaksi Utama: Pembentukan Endapan Barium Sulfat**")
        col1, col2, col3, col4, col5, col6, col7 = st.columns([2,0.5,2,0.5,2,0.5,2])
        col1.info("Na₂SO₄")
        col2.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col3.info("BaCl₂")
        col4.markdown("<div style='text-align:center;padding-top:8px'>→</div>", unsafe_allow_html=True)
        col5.warning("BaSO₄ ↓ · Putih")
        col6.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col7.success("2 NaCl")
        st.markdown("> **Penjelasan:** Nilai Hasil Kali Kelarutan Ksp ≈ 1,1 × 10⁻¹⁰ artinya sangat sukar larut. Suasana asam mencegah terbentuknya endapan pengganggu seperti BaCO₃ atau BaCrO₄.")
        st.divider()
        st.markdown("**Reaksi Samping yang Harus Dicegah: Reduksi oleh Karbon**")
        col1, col2, col3, col4, col5, col6, col7 = st.columns([2,0.5,2,0.5,2,0.5,2])
        col1.warning("BaSO₄")
        col2.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col3.info("4 C")
        col4.markdown("<div style='text-align:center;padding-top:8px'>→</div>", unsafe_allow_html=True)
        col5.success("BaS · Mudah Larut")
        col6.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col7.error("4 CO ↑")
        st.markdown("> **Penjelasan:** Inilah alasan wajib meneteskan 1 tetes asam sulfat pekat sebelum pemijaran akhir — agar BaSO₄ tidak berubah menjadi BaS yang larut dan hasil analisis menjadi rendah.")
    with tab4:
        st.subheader("Percobaan 4 · Penetapan Kadar Besi")
        st.markdown("**Reaksi 1: Pengoksidasi Ion Besi(II) ke Besi(III)**")
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
        st.markdown("> **Penjelasan:** Ion Fe²⁺ harus diubah jadi Fe³⁺ karena hidroksida Fe²⁺ mudah larut dan tidak mengendap sempurna. Gas NO tak berwarna di udara segera jadi NO₂ berwarna coklat — lakukan di lemari asam.")
        st.divider()
        st.markdown("**Reaksi 2: Pembentukan Endapan Besi(III) Hidroksida**")
        col1, col2, col3, col4, col5, col6, col7 = st.columns([2,0.5,2,0.5,2,0.5,2])
        col1.info("Fe³⁺")
        col2.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col3.info("3 NH₄OH")
        col4.markdown("<div style='text-align:center;padding-top:8px'>→</div>", unsafe_allow_html=True)
        col5.warning("Fe(OH)₃ ↓ · Coklat Merah")
        col6.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col7.success("3 NH₄⁺")
        st.markdown("> **Penjelasan:** Bersifat koloid halus — itulah sebabnya pencuci wajib pakai larutan garam NH₄NO₃ bukan air saja agar tidak terurai kembali.")
        st.divider()
        st.markdown("**Reaksi 3: Pemijaran Menjadi Besi(III) Oksida**")
        col1, col2, col3, col4, col5 = st.columns([2,0.5,2,0.5,2])
        col1.info("2 Fe(OH)₃")
        col2.markdown("<div style='text-align:center;padding-top:8px'>→</div>", unsafe_allow_html=True)
        col3.warning("Fe₂O₃ ↓ · Merah Bata")
        col4.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col5.error("3 H₂O ↑")
        st.markdown("> **Penjelasan:** Fe₂O₃ berwarna merah bata stabil sampai suhu 900 °C — zat inilah yang ditimbang sebagai dasar perhitungan akhir kadar besi.")
    with tab5:
        st.subheader("Percobaan 5 · Penetapan Kadar Barium")
        st.markdown("**Reaksi 1: Hidrolisis Urea · Kunci Metode Seragam**")
        col1, col2, col3, col4, col5, col6, col7 = st.columns([2,0.5,2,0.5,2,0.5,2])
        col1.info("CO(NH₂)₂")
        col2.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col3.info("H₂O")
        col4.markdown("<div style='text-align:center;padding-top:8px'>→</div>", unsafe_allow_html=True)
        col5.success("2 NH₃")
        col6.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col7.error("CO₂ ↑")
        st.markdown("> **Penjelasan:** Terjadi perlahan dan merata ke seluruh larutan — nilai pH naik perlahan sehingga kristal endapan tumbuh besar, padat, dan sangat murni dibanding cara penambahan amonia langsung.")
        st.divider()
        st.markdown("**Reaksi 2: Pembentukan Endapan Barium Kromat**")
        col1, col2, col3, col4, col5 = st.columns([2,0.5,2,0.5,2])
        col1.info("Ba²⁺")
        col2.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col3.info("CrO₄²⁻")
        col4.markdown("<div style='text-align:center;padding-top:8px'>→</div>", unsafe_allow_html=True)
        col5.warning("BaCrO₄ ↓ · Kuning Terang")
        st.markdown("> **Penjelasan:** Hanya terbentuk sempurna saat nilai pH sudah cukup tinggi. Di suasana asam ion kromat berubah jadi dikromat yang tidak mengendapkan barium.")
        st.divider()
        st.markdown("**Reaksi 3: Kesetimbangan Ion Kromat ⇌ Ion Dikromat**")
        col1, col2, col3, col4, col5, col6, col7 = st.columns([2,0.5,2,0.5,2,0.5,2])
        col1.info("2 CrO₄²⁻ · Kuning")
        col2.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col3.info("2 H⁺")
        col4.markdown("<div style='text-align:center;padding-top:8px'>⇌</div>", unsafe_allow_html=True)
        col5.success("Cr₂O₇²⁻ · Jingga")
        col6.markdown("<div style='text-align:center;padding-top:8px'>+</div>", unsafe_allow_html=True)
        col7.success("H₂O")
        st.markdown("""
> **Penjelasan Mekanisme:**
> - **Awal Suasana Asam:** Kesetimbangan bergeser ke kanan → ion dikromat dominan → **tidak terbentuk endapan**
> - **Setelah Urea Terurai:** pH naik → kesetimbangan bergeser ke kiri → ion kromat dominan → **baru terbentuk endapan BaCrO₄** perlahan dan seragam
""")
