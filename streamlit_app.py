import streamlit as st

# ========== KONFIGURASI ==========
st.set_page_config(page_title="GraviLab – Analisis Gravimetri", page_icon="⚗️", layout="wide")
st.markdown("""<style>.block-container{padding-top:2rem;}.rumus-box{background:#1e2a3a;border-left:4px solid #f0a500;padding:12px 16px;border-radius:6px;font-family:monospace;}.reaksi-box{background:#0d1b2a;border:1px solid #30363d;border-radius:10px;padding:16px;}</style>""", unsafe_allow_html=True)

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
    c1, c2 = st.columns(2)
    with c1:
        st.info("**📋 Panduan Prosedur**\n\nChecklist langkah demi langkah 5 percobaan.")
        st.info("**🔬 Penjelasan Reagen**\n\nKenapa pakai zat ini? Bisa diganti apa?")
    with c2:
        st.info("**🧮 Kalkulator Gravimetri**\n\nInput bobot → hasil kadar otomatis.")
        st.info("**⚗️ Reaksi Kimia Visual**\n\nTampilan reaksi lengkap & jelas.")
    st.divider()
    st.subheader("📚 Daftar Percobaan")
    st.markdown("| No | Judul Percobaan | Metode | Referensi |\n|:-:|:---|:---|:---|\n|1| Kadar Air Tepung Terigu | Oven 130°C | SNI 3751:2009 |\n|2| Kadar Abu Tepung Terigu | Tanur 550°C | SNI 3751:2018 |\n|3| Kadar Sulfat Garam Glauber | Endap BaSO₄ | — |\n|4| Kadar Fe Garam Besi(II) | Endap→Fe₂O₃ | — |\n|5| Kadar Ba | Homogeneous | — |")

# ========== PANDUAN PROSEDUR ==========
elif menu == "📋 Panduan Prosedur":
    st.title("📋 Panduan Prosedur Interaktif")
    st.divider()
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Perc 1", "Perc 2", "Perc 3", "Perc 4", "Perc 5"])
    with tab1:
        st.subheader("Kadar Air Tepung Terigu")
        st.caption("SNI 3751:2009 | Oven 130°C")
        c1, c2 = st.columns(2)
        c1.markdown("**🧪 Bahan:** Tepung terigu")
        c2.markdown("**🛠 Alat:** Neraca, Oven, Wadah timbang, Desikator")
        langkah = ["Panaskan wadah kosong 1 jam → timbang W₀", "Timbang sampel 2g → catat W₁", "Panaskan 1 jam di 130°C", "Dinginkan desikator → timbang W₂"]
        selesai = sum(st.checkbox(l, key=f"p1_{i}") for i, l in enumerate(langkah))
        st.progress(selesai / len(langkah), text=f"Progress: {selesai}/{len(langkah)}")
    with tab2:
        st.subheader("Kadar Abu Tepung Terigu")
        st.caption("SNI 3751:2018 | Tanur 550°C")
        langkah = ["Panaskan cawan kosong → bobot tetap W₀", "Timbang sampel 3–5g → catat W₁", "Arangkan di Bunsen, abukan 8 jam di tanur", "Timbang sampai bobot tetap → catat W₂"]
        selesai = sum(st.checkbox(l, key=f"p2_{i}") for i, l in enumerate(langkah))
        st.progress(selesai / len(langkah), text=f"Progress: {selesai}/{len(langkah)}")
    with tab3:
        st.subheader("Kadar Sulfat Garam Glauber")
        langkah = ["Timbang 0,5g sampel → larutkan", "Asamkan HCl 4N, panaskan mendidih", "Tambahkan BaCl₂ panas, diamkan 1 jam", "Cuci sampai bebas Cl⁻ → saring → pijar"]
        selesai = sum(st.checkbox(l, key=f"p3_{i}") for i, l in enumerate(langkah))
        st.progress(selesai / len(langkah), text=f"Progress: {selesai}/{len(langkah)}")
    with tab4:
        st.subheader("Kadar Fe Garam Besi(II)")
        langkah = ["Timbang 0,25g sampel → larutkan", "Tambah HNO₃ pekat → oksidasi sempurna", "Panaskan, tambah amonia → endapkan Fe(OH)₃", "Cuci, pijar jadi Fe₂O₃ → timbang"]
        selesai = sum(st.checkbox(l, key=f"p4_{i}") for i, l in enumerate(langkah))
        st.progress(selesai / len(langkah), text=f"Progress: {selesai}/{len(langkah)}")
    with tab5:
        st.subheader("Kadar Ba (Homogeneous)")
        langkah = ["Pipet 25mL BaCl₂ 0,1M → asamkan HCl", "Tambah K₂CrO₄ & urea → encerkan", "Panaskan mendidih ±90 menit", "Saring, cuci, oven 110°C → timbang"]
        selesai = sum(st.checkbox(l, key=f"p5_{i}") for i, l in enumerate(langkah))
        st.progress(selesai / len(langkah), text=f"Progress: {selesai}/{len(langkah)}")

# ========== KALKULATOR ==========
elif menu == "🧮 Kalkulator Gravimetri":
    st.title("🧮 Kalkulator Gravimetri Otomatis")
    st.divider()
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Air", "Abu", "Sulfat", "Fe", "Ba"])
    with tab1:
        st.markdown('<div class="rumus-box">Air (%) = [(W₁-W₀)-(W₂-W₀)]/(W₁-W₀)×100</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        w0 = c1.number_input("W₀", format="%.4f", key="wa0")
        w1 = c2.number_input("W₁", format="%.4f", key="wa1")
        w2 = c3.number_input("W₂", format="%.4f", key="wa2")
        if st.button("Hitung Air", type="primary"):
            kadar = ((w1 - w2) / (w1 - w0)) * 100 if w1 > w0 and w2 <= w1 else -1
            st.success(f"✅ Kadar Air = {kadar:.4f} %") if kadar >= 0 else st.error("Cek kembali data!")
    with tab2:
        st.markdown('<div class="rumus-box">Abu (%) = (W₂-W₀)/(W₁-W₀)×100</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        w0 = c1.number_input("W₀", format="%.4f", key="wu0")
        w1 = c2.number_input("W₁", format="%.4f", key="wu1")
        w2 = c3.number_input("W₂", format="%.4f", key="wu2")
        if st.button("Hitung Abu", type="primary"):
            kadar = ((w2 - w0) / (w1 - w0)) * 100 if w1 > w0 and w2 >= w0 else -1
            st.success(f"✅ Kadar Abu = {kadar:.4f} %") if kadar >= 0 else st.error("Cek kembali data!")
    with tab3:
        st.markdown('<div class="rumus-box">SO₄ (%) = 0,4116 × (W₂-W₀)/(W₁-W₀)×100</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        w0 = c1.number_input("W₀", format="%.4f", key="ws0")
        w1 = c2.number_input("W₁", format="%.4f", key="ws1")
        w2 = c3.number_input("W₂", format="%.4f", key="ws2")
        if st.button("Hitung Sulfat", type="primary"):
            kadar = 0.4116 * ((w2 - w0) / (w1 - w0)) * 100 if w1 > w0 and w2 >= w0 else -1
            st.success(f"✅ Kadar SO₄ = {kadar:.4f} %") if kadar >= 0 else st.error("Cek kembali data!")
    with tab4:
        st.markdown('<div class="rumus-box">Fe (%) = 0,6994 × (W₂-W₀)/(W₁-W₀)×100</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        w0 = c1.number_input("W₀", format="%.4f", key="wf0")
        w1 = c2.number_input("W₁", format="%.4f", key="wf1")
        w2 = c3.number_input("W₂", format="%.4f", key="wf2")
        if st.button("Hitung Fe", type="primary"):
            kadar = 0.6994 * ((w2 - w0) / (w1 - w0)) * 100 if w1 > w0 and w2 >= w0 else -1
            st.success(f"✅ Kadar Fe = {kadar:.4f} %") if kadar >= 0 else st.error("Cek kembali data!")
    with tab5:
        st.markdown('<div class="rumus-box">Ba (%) = 0,5421 × (W₁-W₀)/Vol × 100</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        w0 = c1.number_input("W₀", format="%.4f", key="wb0")
        w1 = c2.number_input("W₁", format="%.4f", key="wb1")
        vol = c3.number_input("Volume mL", format="%.2f", key="vb")
        if st.button("Hitung Ba", type="primary"):
            kadar = 0.5421 * ((w1 - w0) / vol) * 100 if w1 > w0 and vol > 0 else -1
            st.success(f"✅ Kadar Ba = {kadar:.4f} %") if kadar >= 0 else st.error("Cek kembali data!")

# ========== PENJELASAN REAGEN ==========
elif menu == "🔬 Penjelasan Reagen":
    st.title("🔬 Penjelasan Reagen")
    st.divider()
    daftar = [
        {"nama": "HCl", "pakai": "Perc 3,4,5", "fungsi": "Buat suasana asam agar hanya ion target mengendap", "alt": ["❌ H₂SO₄ (ganggu sulfat)", "❌ HNO₃ (oksidator)"]},
        {"nama": "BaCl₂", "pakai": "Perc 3", "fungsi": "Pengendap sulfat jadi BaSO₄ tak larut", "alt": ["✅ Ba(NO₃)₂ (bisa)", "✅ Ba(CH₃COO)₂ (bisa)"]},
        {"nama": "HNO₃ Pekat", "pakai": "Perc 4", "fungsi": "Oksidator Fe²⁺→Fe³⁺ agar mudah diendapkan", "alt": ["✅ H₂O₂ (aman)", "✅ Air bromin (kuat)"]},
        {"nama": "Amonia", "pakai": "Perc 4,5", "fungsi": "Basa lemah pengendap Fe(OH)₃", "alt": ["✅ Urea (perlahan)", "❌ NaOH/KOH (terlalu kuat)"]},
        {"nama": "Urea", "pakai": "Perc 5", "fungsi": "Hidrolisis perlahan → naikkan pH merata", "alt": ["✅ Heksametilentetramina", "❌ Amonia langsung"]},
        {"nama": "NH₄NO₃", "pakai": "Perc 4", "fungsi": "Pencuci mencegah peptisasi koloid", "alt": ["✅ NH₄Cl encer", "❌ Air suling saja"]},
        {"nama": "H₂SO₄ Pekat", "pakai": "Perc 3", "fungsi": "Cegah reduksi BaSO₄ jadi BaS saat pijar", "alt": ["❌ Tidak ada pengganti"]}
    ]
    for z in daftar:
        with st.expander(f"🧪 {z['nama']} — dipakai: {z['pakai']}"):
            st.markdown(f"**Fungsi:** {z['fungsi']}\n\n**Alternatif:**\n" + "\n".join(f"- {a}" for a in z['alt']))

# ========== REAKSI KIMIA VISUAL ==========
elif menu == "⚗️ Reaksi Kimia Visual":
    st.title("⚗️ Reaksi Kimia Visual")
    st.markdown("🔵 Reaktan  🟢 Larut  🟡 Endapan  🔴 Gas")
    st.divider()
    tab2, tab3, tab4, tab5 = st.tabs(["Perc 2", "Perc 3", "Perc 4", "Perc 5"])
    with tab2:
        st.markdown("**Pembentukan Abu:**\n> Organik + O₂ → **🟡 Oksida Logam ↓** + CO₂↑ + H₂O↑")
    with tab3:
        st.markdown("**Pengendapan:**\n> Na₂SO₄ + BaCl₂ → **🟡 BaSO₄ ↓ (putih)** + 2 NaCl\n\n**Cegah Reduksi:**\n> BaSO₄ + 4C → BaS + 4CO ↑  ⚠️ **DIHINDARI pakai H₂SO₄ pekat**")
    with tab4:
        st.markdown("**1. Oksidasi:**\n> 3Fe²⁺ + NO₃⁻ + 4H⁺ → 3Fe³⁺ + **🔴 NO ↑** + 2H₂O\n\n**2. Endapan:**\n> Fe³⁺ + 3NH₄OH → **🟡 Fe(OH)₃ ↓ (coklat)** + 3NH₄⁺\n\n**3. Pemanasan:**\n> 2Fe(OH)₃ → **🟡 Fe₂O₃ ↓ (merah bata)** + 3H₂O ↑")
    with tab5:
        st.markdown("**1. Hidrolisis Urea:**\n> CO(NH₂)₂ + H₂O → 2NH₃ + **🔴 CO₂ ↑**\n\n**2. Endapan:**\n> Ba²⁺ + CrO₄²⁻ → **🟡 BaCrO₄ ↓ (kuning)**\n\n**3. Kesetimbangan:**\n> 2CrO₄²⁻ + 2H⁺ ⇌ Cr₂O₇²⁻ + H₂O  (pH naik → geser kiri)")
