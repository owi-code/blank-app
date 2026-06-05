import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="GraviLab",
    page_icon="⚗️",
    layout="wide"
)

st.markdown("""
<style>
.block-container{padding-top:1.5rem;}

.rumus-box{
background:#f5f5f5;
padding:14px;
border-left:4px solid orange;
border-radius:8px;
color:black;
margin:10px 0;
}

</style>
""", unsafe_allow_html=True)

# =========================
# DATA PROSEDUR
# =========================
prosedur={

"Percobaan 1":{
"judul":"Penetapan Kadar Air dalam Tepung Terigu",
"caption":"SNI 3751:2009 | Oven 130°C | 1 jam",
"langkah":[
"Timbang wadah kosong + tutup, oven (130±3)°C selama 1 jam",
"Dinginkan desikator 30 menit, timbang sebagai W₀",
"Timbang sampel 2 g, catat W₁",
"Oven 130°C selama 1 jam",
"Masukkan desikator 15 menit",
"Timbang sebagai W₂"
]},

"Percobaan 2":{
"judul":"Penetapan Kadar Abu",
"caption":"Tanur 550°C",
"langkah":[
"Panaskan cawan + tanur",
"Dinginkan dan timbang W₀",
"Timbang sampel 3–5 g → W₁",
"Arangkan sampel",
"Tanur 550°C ±8 jam",
"Dinginkan desikator",
"Ulangi sampai bobot tetap → W₂"
]},

"Percobaan 3":{
"judul":"Penetapan Sulfat dalam Garam Glauber",
"caption":"Metode BaSO₄",
"langkah":[
"Timbang 0,5 g sampel",
"Tambahkan 3 mL HCl 4N",
"Tambah BaCl₂ panas",
"Diamkan 1 jam",
"Saring dan cuci bebas Cl⁻",
"Teteskan H₂SO₄ pekat",
"Pijarkan 750°C"
]},

"Percobaan 4":{
"judul":"Penetapan Fe",
"caption":"Fe(OH)₃ → Fe₂O₃",
"langkah":[
"Timbang 0,25 g sampel",
"Tambah HNO₃ pekat",
"Tambahkan NH₄OH",
"Diamkan 30–40 menit",
"Saring + cuci NH₄NO₃",
"Arangkan kertas",
"Pijarkan hingga bobot tetap"
]},

"Percobaan 5":{
"judul":"Penetapan Ba sebagai BaCrO₄",
"caption":"Homogeneous precipitation",
"langkah":[
"Pipet 25 mL BaCl₂",
"Asamkan HCl",
"Tambah K₂CrO₄",
"Tambah 7,5 g urea",
"Panaskan ±90 menit",
"Saring",
"Oven 110°C"
]}
}

# =========================
# REAGEN
# =========================
reagen={

"HCl":
"Suasana asam untuk mencegah endapan pengganggu.",

"BaCl₂":
"Mengendapkan sulfat menjadi BaSO₄.",

"HNO₃":
"Mengoksidasi Fe²⁺ menjadi Fe³⁺.",

"NH₄OH":
"Mengendapkan Fe(OH)₃.",

"Urea":
"Menaikkan pH perlahan agar endapan lebih murni.",

"K₂CrO₄":
"Mengendapkan Ba²⁺ sebagai BaCrO₄.",

"NH₄NO₃":
"Mencegah peptisasi saat pencucian.",

"H₂SO₄":
"Mencegah reduksi BaSO₄."
}

# =========================
# SIDEBAR
# =========================
menu=st.sidebar.radio(
"Pilih Fitur",
[
"🏠 Beranda",
"📋 Panduan Prosedur",
"🧮 Kalkulator Gravimetri",
"🔬 Penjelasan Reagen",
"⚗️ Reaksi Kimia Visual"
]
)

# =========================
# BERANDA
# =========================
if menu=="🏠 Beranda":

    st.title("⚗️ GraviLab")
    st.subheader("Panduan Praktikum Analisis Gravimetri")

    c1,c2=st.columns(2)

    with c1:
        st.info("📋 Panduan Prosedur")
        st.info("🔬 Penjelasan Reagen")

    with c2:
        st.info("🧮 Kalkulator Gravimetri")
        st.info("⚗️ Reaksi Kimia Visual")

# =========================
# PANDUAN
# =========================
elif menu=="📋 Panduan Prosedur":

    tabs=st.tabs(list(prosedur.keys()))

    for tab,(nama,data) in zip(tabs,prosedur.items()):

        with tab:

            st.subheader(data["judul"])
            st.caption(data["caption"])

            selesai=0

            for i,x in enumerate(data["langkah"]):

                if st.checkbox(
                    x,
                    key=f"{nama}{i}"
                ):
                    selesai+=1

            st.progress(
                selesai/
                len(data["langkah"])
            )

# =========================
# KALKULATOR
# =========================
elif menu=="🧮 Kalkulator Gravimetri":

    tabs=st.tabs([
    "Air","Abu","SO₄","Fe","Ba"
    ])

    rumus={

    "Air":"""
(W₁−W₂)
─────── ×100
(W₁−W₀)
""",

    "Abu":"""
(W₂−W₀)
─────── ×100
(W₁−W₀)
""",

    "SO₄":"""
BM SO₄     W₂−W₀
────── × ────── ×100
BM BaSO₄   W₁−W₀

BM SO₄ = 96
BM BaSO₄ = 233
""",

    "Fe":"""
2×Ar Fe    W₂−W₀
─────── × ────── ×100
Mr Fe₂O₃   W₁−W₀

Ar Fe = 56
Mr Fe₂O₃ = 160
""",

    "Ba":"""
Ar Ba    W₁−W₀
───── × ────── ×100
Mr BaCrO₄ Volume

Ar Ba = 137
Mr BaCrO₄ = 253
"""
}

    for i,tab in enumerate(tabs):

        with tab:

            nama=list(rumus.keys())[i]

            st.markdown(
            f"<div class='rumus-box'><pre>{rumus[nama]}</pre></div>",
            unsafe_allow_html=True
            )

            w0=st.number_input("W0",key=f"w0{i}")
            w1=st.number_input("W1",key=f"w1{i}")
            w2=st.number_input("W2 / Volume",key=f"w2{i}")

# =========================
# REAGEN
# =========================
elif menu=="🔬 Penjelasan Reagen":

    st.title("🔬 Penjelasan Reagen")

    for nama,isi in reagen.items():

        with st.expander(nama):

            st.write(isi)

# =========================
# REAKSI
# =========================
elif menu=="⚗️ Reaksi Kimia Visual":

    tab3,tab4,tab5=st.tabs([
    "Percobaan 3",
    "Percobaan 4",
    "Percobaan 5"
    ])

    with tab3:

        st.subheader("Penetapan Sulfat")

        st.latex(
        r"Na_2SO_4 + BaCl_2 \rightarrow BaSO_4\downarrow +2NaCl"
        )

        st.info(
        "BaSO₄ mengendap putih."
        )

        st.latex(
        r"BaSO_4 +4C \rightarrow BaS +4CO"
        )

        st.warning(
        "Dicegah dengan H₂SO₄ pekat."
        )

    with tab4:

        st.subheader("Penetapan Fe")

        st.latex(
        r"3Fe^{2+}+NO_3^-+4H^+ \rightarrow 3Fe^{3+}+NO+2H_2O"
        )

        st.latex(
        r"Fe^{3+}+3NH_4OH \rightarrow Fe(OH)_3\downarrow"
        )

        st.latex(
        r"2Fe(OH)_3 \rightarrow Fe_2O_3 +3H_2O"
        )

        st.success(
        "Fe₂O₃ ditimbang."
        )

    with tab5:

        st.subheader("Penetapan Ba")

        st.latex(
        r"CO(NH_2)_2 + H_2O \rightarrow 2NH_3 + CO_2"
        )

        st.latex(
        r"Ba^{2+}+CrO_4^{2-}\rightarrow BaCrO_4\downarrow"
        )

        st.latex(
        r"2CrO_4^{2-}+2H^+ \rightleftharpoons Cr_2O_7^{2-}+H_2O"
        )

        st.info(
        "pH naik → BaCrO₄ mulai mengendap."
        )
