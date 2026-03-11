import streamlit as st
import pandas as pd
import joblib

model = joblib.load("best_model.pkl")

st.set_page_config(
    page_title="Churn Prediction",
    page_icon="📊",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;800&family=DM+Sans:wght@300;400;500&display=swap');

* { font-family: 'DM Sans', sans-serif; }

.stApp {
    background: #0a0a0f;
    color: #e8e8f0;
}

/* Ana başlıq */
.main-header {
    text-align: center;
    padding: 2.5rem 0 1rem 0;
}
.main-header h1 {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 2.8rem;
    background: linear-gradient(135deg, #a78bfa, #60a5fa, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    letter-spacing: -1px;
}
.main-header p {
    color: #6b7280;
    font-size: 0.95rem;
    margin-top: 0.5rem;
    font-weight: 300;
}

/* Kart */
.card {
    background: #13131f;
    border: 1px solid #1f1f35;
    border-radius: 16px;
    padding: 1.8rem;
    margin-bottom: 1.2rem;
}
.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #a78bfa;
    margin-bottom: 1rem;
}

/* Input stilləri */
.stNumberInput > div > div > input,
.stSelectbox > div > div {
    background: #1a1a2e !important;
    border: 1px solid #2a2a45 !important;
    border-radius: 10px !important;
    color: #e8e8f0 !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stNumberInput > div > div > input:focus,
.stSelectbox > div > div:focus {
    border-color: #a78bfa !important;
    box-shadow: 0 0 0 2px rgba(167, 139, 250, 0.15) !important;
}

/* Label */
.stNumberInput label, .stSelectbox label {
    color: #9ca3af !important;
    font-size: 0.85rem !important;
    font-weight: 400 !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #2563eb) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 2rem !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    letter-spacing: 0.5px !important;
    width: 100% !important;
    margin-top: 1rem !important;
    transition: all 0.3s ease !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(124, 58, 237, 0.4) !important;
}

/* Nəticə kartları */
.result-box {
    border-radius: 14px;
    padding: 1.5rem;
    margin-top: 1rem;
    text-align: center;
}
.result-churn {
    background: linear-gradient(135deg, rgba(239,68,68,0.15), rgba(239,68,68,0.05));
    border: 1px solid rgba(239,68,68,0.3);
}
.result-safe {
    background: linear-gradient(135deg, rgba(52,211,153,0.15), rgba(52,211,153,0.05));
    border: 1px solid rgba(52,211,153,0.3);
}
.result-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.7rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
    opacity: 0.7;
}
.result-value {
    font-family: 'Syne', sans-serif;
    font-size: 2.5rem;
    font-weight: 800;
}
.result-churn .result-value { color: #f87171; }
.result-safe .result-value { color: #34d399; }

/* Progress bar */
.prob-bar-container {
    background: #1a1a2e;
    border-radius: 999px;
    height: 8px;
    margin-top: 1rem;
    overflow: hidden;
}
.prob-bar-fill {
    height: 100%;
    border-radius: 999px;
    transition: width 0.8s ease;
}

/* Divider */
hr { border-color: #1f1f35 !important; }

/* Selectbox dropdown */
div[data-baseweb="select"] > div {
    background: #1a1a2e !important;
    border-color: #2a2a45 !important;
}
</style>

<div class="main-header">
    <h1>Churn Prediction</h1>
</div>
""", unsafe_allow_html=True)


# ── Şəxsi məlumatlar ──────────────────────────────────────────
st.markdown('<div class="card"><div class="card-title">👤 Şəxsi Məlumatlar</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Yaş", min_value=18, max_value=100)
    gender = 1 if st.selectbox("Cins", ["Kişi", "Qadın"]) == "Qadın" else 0
with col2:
    geography = st.selectbox("Ölkə", ["France", "Germany", "Spain"])
    credit_score = st.number_input("Kredit Skoru", min_value=300, max_value=850)
st.markdown('</div>', unsafe_allow_html=True)

# ── Hesab məlumatları ─────────────────────────────────────────
st.markdown('<div class="card"><div class="card-title">🏦 Hesab Məlumatları</div>', unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    balance = st.number_input("Balans ($)", min_value=0.0, value=50000.0, step=1000.0)
    tenure = st.number_input("Müştərilik Müddəti (il)", min_value=0, max_value=20)
with col4:
    num_products = st.number_input("Məhsul Sayı", min_value=1, max_value=4)
    is_active = 1 if st.selectbox("Aktiv Üzv?", ["Xeyr", "Bəli"]) == "Bəli" else 0
st.markdown('</div>', unsafe_allow_html=True)


# ── Predict düyməsi ───────────────────────────────────────────
if st.button("🔍  Proqnozlaşdır"):
    input_df = pd.DataFrame({
        'CreditScore': [credit_score],
        'Age': [age],
        'Balance': [balance],
        'Tenure': [tenure],
        'NumOfProducts': [num_products],
        'IsActiveMember': [is_active],
        'Gender': [gender],
        'Geography':[geography]
    })

    # ── Threshold ilə prediction ─────────────
    prob = model.predict_proba(input_df)[0][1]  # Churn ehtimalı
    threshold = 0.33
    prediction = int(prob >= threshold)  # 1 = churn, 0 = qalacaq
    prob_pct = round(prob * 100, 1)

    # ── Kart vizualizasiyası ─────────────
    if prediction == 1:
        box_class = "result-churn"
        icon = "⚠️"
        status = "CHURN RİSKİ VAR"
        bar_color = "linear-gradient(90deg, #ef4444, #f97316)"
    else:
        box_class = "result-safe"
        icon = "✅"
        status = "QALACAQ"
        bar_color = "linear-gradient(90deg, #10b981, #34d399)"

    st.markdown(f"""
    <div class="result-box {box_class}">
        <div class="result-label">{icon} Proqnoz Nəticəsi</div>
        <div class="result-value">{status}</div>
        <div style="color:#9ca3af; font-size:0.9rem; margin-top:0.5rem;">
            Churn Ehtimalı: <strong style="color:#e8e8f0">{prob_pct}%</strong>
        </div>
        <div class="prob-bar-container">
            <div class="prob-bar-fill" style="width:{prob_pct}%; background:{bar_color};"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("Prediction:", prediction)
    st.write("Probability of Churn:", prob)