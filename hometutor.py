import streamlit as st
import pandas as pd
import time

# ==========================================
# ⚙️ APP CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Home Tutor Hub",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS to make it look like a mobile app
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #FF4B4B;
        color: white;
    }
    .big-font {
        font-size: 20px !important;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🧒 MRUNAL'S ZONE (Class 4)
# ==========================================
def mrunal_zone():
    st.header("🧒 Mrunal's Learning World")
    st.info("Subject: English & Hindi (Term 1)")

    # TAB SELECTION
    tab1, tab2 = st.tabs(["📚 English: The Turkish Cap", "🇮🇳 Hindi: Naya Ujiyara"])

    with tab1:
        [span_2](start_span)st.subheader("Chapter: The Turkish Cap[span_2](end_span)")
        st.write("Let's practice **Collective Nouns** from your syllabus!")
        
        # Interactive Quiz
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://img.icons8.com/color/96/group.png", caption="A Group of...")
        
        with col2:
            answer = st.radio("What do we call a group of Soldiers?", 
                            ["A Bunch", "A Regiment", "A School"])
            
            if st.button("Check English Answer"):
                if answer == "A Regiment":
                    st.success("✅ Correct! A Regiment of Soldiers.")
                    st.balloons()
                else:
                    st.error("Oops! Try again.")

    with tab2:
        [span_3](start_span)st.subheader("कविता: नया उजियारा (Naya Ujiyara)[span_3](end_span)")
        st.write("Match the word to its meaning:")
        
        word_choice = st.selectbox("Choose a word:", ["Ujiyara (उजियारा)", "Mati (माटी)"])
        
        if word_choice == "Ujiyara (उजियारा)":
            user_meaning = st.text_input("Type the meaning in English:")
            if "light" in user_meaning.lower() or "bright" in user_meaning.lower():
                st.success("✨ Sahi Jawab! (Correct)")
            elif user_meaning:
                st.warning("Hint: It comes from the Sun.")

# ==========================================
# 👩‍🎓 GARGI'S ZONE (Class 8)
# ==========================================
def gargi_zone():
    st.header("👩‍🎓 Gargi's Science Lab")
    st.info("Module: Crop Production & Management (NCERT)")

    st.write("### 🌾 Mission: Zero Hunger (SDG 2)")
    
    # Simulation Slider
    water_level = st.slider("Select Irrigation Water Level (Liters)", 
                          min_value=1000, max_value=10000, step=500)
    
    # Dynamic Chart
    st.write(f"Analyzing Crop Yield for **{water_level} Liters**...")
    
    if water_level > 7000:
        st.warning("⚠️ High Water Usage! Consider Drip Irrigation.")
        yield_percent = 80
    elif water_level < 3000:
        st.error("⚠️ Too Dry! Crops are dying.")
        yield_percent = 20
    else:
        st.success("✅ Optimal Range for Wheat.")
        yield_percent = 95
        
    # Simple Bar Chart
    chart_data = pd.DataFrame({
        'Method': ['Selected Level', 'Drip Irrigation'],
        'Yield %': [yield_percent, 90]
    })
    st.bar_chart(chart_data, x='Method', y='Yield %')

    # Think Tank Challenge
    with st.expander("🧠 Open Think Tank Challenge"):
        st.write("Why is Drip Irrigation better for Sandy Soil?")
        st.text_area("Your Hypothesis:")
        if st.button("Submit to Tutor"):
            st.info("Tutor Bot: Good thought! Sandy soil cannot hold water, so dripping it slowly helps roots absorb it before it drains away.")

# ==========================================
# 🏠 MAIN APP LOGIC
# ==========================================
st.title("🏠 Home Tutor Hub")
st.write("Select your profile to begin:")

col_m, col_g = st.columns(2)

with col_m:
    if st.button("🧒 Enter Mrunal's Room"):
        st.session_state['user'] = 'Mrunal'

with col_g:
    if st.button("👩‍🎓 Enter Gargi's Lab"):
        st.session_state['user'] = 'Gargi'

# Display the selected zone
if 'user' in st.session_state:
    st.divider()
    if st.session_state['user'] == 'Mrunal':
        mrunal_zone()
    elif st.session_state['user'] == 'Gargi':
        gargi_zone()
