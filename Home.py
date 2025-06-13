# Home.py
import streamlit as st
from PIL import Image
import json

# ------------ Page settings ------------
st.set_page_config(
    page_title="NIOT • National Institute of Ocean Technology",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------ Inject shared CSS ------------
with open("custom_styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ------------ Header strip ------------
col1, col2, col3 = st.columns([1,2,1], gap="medium")
with col1:
    st.image("assets/niot_logo.png", width=110)
with col2:
    st.markdown("<h1 class='app-title'>National Institute of Ocean Technology</h1>",
                unsafe_allow_html=True)
with col3:
    st.image("assets/moes_logo.png", width=190)

st.markdown("---")

# ------------ About NIOT ------------
st.subheader("Overview")
st.write(
    "Established in **November 1993** as an autonomous society under the *Ministry "
    "of Earth Sciences, Government of India*, NIOT’s mandate is to develop "
    "indigenous technologies to tap ocean resources and solve engineering "
    "challenges in India’s ~2 million km² Exclusive Economic Zone."            # founding
)

st.markdown(
"""
### Mission
> *“Develop reliable, indigenous ocean technologies that lead to self‑reliance and
economic, environmental and strategic benefits for the nation.”*

### Key Research Areas
- **Deep‑Sea Technologies** – manned & unmanned submersibles, mining tools :contentReference[oaicite:1]{index=1}  
- **Ocean Observation & Electronics** – data buoys, tsunami early‑warning systems :contentReference[oaicite:2]{index=2}  
- **Coastal & Offshore Engineering** – moorings, pipelines, island shore protection :contentReference[oaicite:3]{index=3}  
- **Ocean Renewable Energy & Desalination** – LTTD plants supplying drinking water to the Lakshadweep islands :contentReference[oaicite:4]{index=4}  

### Flagship Projects
| Project | Purpose |
|---------|---------|
| **Matsya 6000** crewed submersible | Carry 3 aquanauts to 6 km depth for *Samudrayaan* mission :contentReference[oaicite:5]{index=5} |
| **Deep Ocean Mission** | End‑to‑end tech for seafloor mining & biodiversity studies :contentReference[oaicite:6]{index=6} |
| **LTTD Desalination Plants** | 100 k L/day potable water units, moving toward net‑zero energy :contentReference[oaicite:7]{index=7} |

### Headquarters
:office: Velachery‑Tambaram Main Rd, Pallikaranai, Chennai 600 100, Tamil Nadu, India :contentReference[oaicite:8]{index=8}
""")

st.info(
    "👆 Use the sidebar to navigate to **SAMUDRA Enhancer** and try NIOT‑style "
    "underwater image processing on your own photos."
)
