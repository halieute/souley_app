from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | John Doe"
PAGE_ICON = ":wave:"
NAME = "Souleymane Maman Nouri Souley"
DESCRIPTION = """
A dedicated and highly skilled Fisheries and Aquaculture Specialist with over 2 years of experience in fisheries management, aquaculture practices, and environmental assessment. Expertise in sustainable resource management, marine biology, and ecological impact studies. Proven ability to conduct comprehensive environmental assessments and develop strategic plans to enhance aquaculture production while ensuring ecological balance.
"""
EMAIL = "souleymanemamannourisouley1995@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "www.linkedin.com/in/souleymane-maman-nouri-souley-06b88a1a9",
    "GitHub": "https://github.com/halieute",
    "Twitter": "https://x.com/NouriSoule22856?t=4zDyk1SPtPulr55QZVjeXw&s=09",
}
PROJECTS = {
    "🏆 Mormyridae settlement on the Niger River: Diversity, Structure and Exploitation in the Niamey area (Niger Republic)": "International_Conference_On_Oceanography_Marine_Biology_Sustainable_Fisheries_and_Aquaculture_ICOcean2024",
    "🏆 Mormyridae settlement on the Niger River: Diversity, Structure and exploitation in Niamey area.": "In writting",
    "🏆 Writting CV using and deployment python": "In improving",
    "🏆 Writting an webapp and deployment using python": "Improving",
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

    # --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


    # --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 3 Years expereince on that field
- ✔️ Strong hands on experience and knowledge in Python, R and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), R, MATLAB
- 📊 Data Visulization: Matplotlib, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write(
    """
- ► Used Python and SQL to study and curiosity
- ► Improvement through implementation
- ► Learning
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Try to built data models and maps to generate meaningful insights from data
- ► Modeled targets likely to renew
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst | Chegg**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


