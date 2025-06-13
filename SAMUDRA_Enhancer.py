# pages/02_SAMUDRA_Enhancer.py
import streamlit as st, cv2, numpy as np
from PIL import Image

st.set_page_config(page_title="SAMUDRA Image Enhancer", page_icon="🖼️", layout="wide")

with open("custom_styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header
cols = st.columns([1,2,2,1], gap="medium")
with cols[0]: st.image("assets/iit_logo.png",  width=90)
with cols[1]:
    st.markdown("<h1 class='app-title'>SAMUDRA</h1><p>Dive Deeper, See Clearer</p>",
                unsafe_allow_html=True)
with cols[2]: st.image("assets/moes_logo.png", width=190)
with cols[3]: st.image("assets/niot_logo.png", width=90)
st.markdown("---")

# Sidebar uploader
uploaded = st.sidebar.file_uploader(
    "Upload Image (JPG • JPEG • PNG, ≤200 MB)", type=["jpg", "jpeg", "png"]
)

# ---- Image‑processing helpers ----
def enhance_image(bgr):
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    l_eq = clahe.apply(l)
    bgr_eq = cv2.cvtColor(cv2.merge([l_eq, a, b]), cv2.COLOR_LAB2BGR)
    wb = cv2.xphoto.createSimpleWB().balanceWhite(bgr_eq)
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    return cv2.filter2D(wb, -1, kernel)

def detect_coral(bgr):
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0,50,50), (10,255,255)) | cv2.inRange(hsv, (160,50,50), (179,255,255))
    contours,_ = cv2.findContours(cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8)),
                                  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return [cv2.boundingRect(c) for c in contours if cv2.contourArea(c) > 800]

def detect_fish(bgr):
    g = cv2.GaussianBlur(cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY), (5,5), 0)
    _,th = cv2.threshold(g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cnts,_ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return [cv2.boundingRect(c) for c in cnts if 500 < cv2.contourArea(c) < 50000]

def draw_boxes(bgr, fish, coral):
    out = bgr.copy()
    for x,y,w,h in fish:  cv2.rectangle(out, (x,y), (x+w,y+h), (255,0,0), 2)
    for x,y,w,h in coral: cv2.rectangle(out, (x,y), (x+w,y+h), (0,0,255), 2)
    return out

# ---- Main workflow ----
if uploaded:
    rgb = np.array(Image.open(uploaded).convert("RGB"))
    bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

    enhanced = enhance_image(bgr)
    fish, coral = detect_fish(enhanced), detect_coral(enhanced)
    detected = draw_boxes(enhanced, fish, coral)

    for col, title, img in zip(st.columns(3), ("Original","Enhanced","Detected"),
                               (rgb, cv2.cvtColor(enhanced,cv2.COLOR_BGR2RGB),
                                cv2.cvtColor(detected,cv2.COLOR_BGR2RGB))):
        col.subheader(title)
        col.image(img, use_container_width=True)

    st.success(f"Fish detected: {len(fish)}   |   Coral patches: {len(coral)}")
else:
    st.sidebar.info("⬅️  Upload an image to begin")
    st.write("Awaiting underwater photo…")
