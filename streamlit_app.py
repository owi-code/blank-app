import streamlit as st

import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="GraviLab",
    page_icon="⚗️",
    layout="wide"
)

st.sidebar.title("⚗️ GraviLab")
st.sidebar.caption("Panduan Praktikum Gravimetri\nAKA Bogor · 2026")

menu = st.sidebar.radio(
    "Menu",
    [
        "🏠 Beranda",
        "📋 Panduan Prosedur",
        "🧮 Kalkulator Gravimetri",
        "🔬 Penjelasan Reagen",
        "⚗️ Reaksi Kimia"
    ]
)

# =========================
# BERANDA
# =========================
if menu == "🏠 Beranda":

    st.title("⚗️ GraviLab")
    st.subheader("Panduan Praktikum Analisis Gravimetri")

    c1,c2 = st.columns(2)

    with c1:
        st.info("📋 Panduan prosedur praktikum")
        st.info("🔬 Penjelasan reagen")

    with c2:
        st.info("🧮 Kalkulator kadar")
        st.info("⚗️ Reaksi kimia")

    st.markdown("""
|No|Percobaan|
|--|--|
|1|Kadar Air|
|2|Kadar Abu|
|3|Kadar Sulfat|
|4|Kadar Fe|
|5|Kadar Ba|
""")

# =========================
# PANDUAN PROSEDUR
# =========================
elif menu == "📋 Panduan Prosedur":

    st.title("📋 Panduan Prosedur")

    percobaan = {
        "P1 Kadar Air":[
            "Panaskan wadah",
            "Timbang W0",
            "Tambah sampel",
            "Oven 130°C",
            "Desikator",
            "Timbang W2"
        ],

        "P2 Kadar Abu":[
            "Siapkan cawan",
            "Timbang W0",
            "Tambah sampel",
            "Arangkan",
            "Tanur 550°C",
            "Timbang"
        ],

        "P3 Sulfat":[
            "Timbang sampel",
            "Tambah HCl",
            "Tambah BaCl₂",
            "Diamkan",
            "Saring",
            "Pijarkan"
        ],

        "P4 Fe":[
            "Larutkan sampel",
            "Tambah HNO₃",
            "Tambah NH₄OH",
            "Diamkan",
            "Saring",
            "Pijarkan"
        ],

        "P5 Ba":[
            "Pipet BaCl₂",
            "Tambah K₂CrO₄",
            "Tambah urea",
            "Panaskan",
            "Saring",
            "Timbang"
        ]
    }

    for judul, langkah in percobaan.items():

        st.subheader(judul)

        done=0

        for i,l in enumerate(langkah):

            if st.checkbox(
                l,
                key=f"{judul}{i}"
            ):
                done+=1

        st.progress(done/len(langkah))

# =========================
# KALKULATOR
# =========================
elif menu == "🧮 Kalkulator Gravimetri":

    st.title("🧮 Kalkulator")

    jenis = st.selectbox(
        "Pilih",
        ["Air","Abu","Sulfat","Fe","Ba"]
    )

    if jenis != "Ba":

        w0 = st.number_input("W0")
        w1 = st.number_input("W1")
        w2 = st.number_input("W2")

    if jenis=="Ba":
        w0 = st.number_input("W0")
        w1 = st.number_input("W1")
        vol = st.number_input("Volume")

    if st.button("Hitung"):

        if jenis=="Air":
            hasil=((w1-w2)/(w1-w0))*100

        elif jenis=="Abu":
            hasil=((w2-w0)/(w1-w0))*100

        elif jenis=="Sulfat":
            hasil=(96.06/233.39)*((w2-w0)/(w1-w0))*100

        elif jenis=="Fe":
            hasil=((2*55.845)/159.69)*((w2-w0)/(w1-w0))*100

        elif jenis=="Ba":
            hasil=(137.33/253.33)*((w1-w0)/vol)*100

        st.success(f"Hasil = {hasil:.4f}%")

# =========================
# REAGEN
# =========================
elif menu == "🔬 Penjelasan Reagen":

    data = {

        "HCl":"Membuat suasana asam",

        "BaCl₂":"Mengendapkan sulfat",

        "HNO₃":"Oksidasi Fe²⁺",

        "NH₄OH":"Mengendapkan ion",

        "Urea":"Naikkan pH perlahan",

        "K₂CrO₄":"Mengendapkan Ba",

        "NH₄NO₃":"Cegah peptisasi",

        "H₂SO₄":"Stabilkan BaSO₄"
    }

    for k,v in data.items():

        with st.expander(k):

            st.write(v)

# =========================
# REAKSI KIMIA
# =========================
elif menu == "⚗️ Reaksi Kimia":

    t1,t2,t3 = st.tabs(
        ["P3","P4","P5"]
    )

    with t1:

        st.latex(
        r"Na_2SO_4 + BaCl_2 \rightarrow BaSO_4\downarrow +2NaCl"
        )

        st.latex(
        r"BaSO_4+4C\rightarrow BaS+4CO"
        )

    with t2:

        st.latex(
        r"3Fe^{2+}+NO_3^-+4H^+\rightarrow3Fe^{3+}+NO+2H_2O"
        )

        st.latex(
        r"Fe^{3+}+3NH_4OH\rightarrow Fe(OH)_3\downarrow"
        )

        st.latex(
        r"2Fe(OH)_3\rightarrow Fe_2O_3+3H_2O"
        )

    with t3:

        st.latex(
        r"CO(NH_2)_2+H_2O\rightarrow2NH_3+CO_2"
        )

        st.latex(
        r"Ba^{2+}+CrO_4^{2-}\rightarrow BaCrO_4\downarrow"
        )

        st.latex(
        r"2CrO_4^{2-}+2H^+\leftrightarrow Cr_2O_7^{2-}+H_2O"
        )
