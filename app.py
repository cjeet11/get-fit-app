import streamlit as st
from datetime import date

st.set_page_config(page_title="Get Fit Pro", page_icon="💪", layout="wide")

st.title("💪 Get Fit: Complete Health System")

# --- SIDEBAR ---
with st.sidebar:
    st.header("👤 User Profile")
    name = st.text_input("Name")
    dob = st.date_input("Date of Birth", date(1995, 1, 1))
    weight = st.number_input("Weight (kg)", value=70.0)
    height = st.number_input("Height (cm)", value=170.0)
    diet_pref = st.radio("Diet Preference", ["Vegetarian", "Non-Vegetarian"])
    goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "General Fitness"])

bmi = round(weight / ((height/100)**2), 2)

# --- MAIN INTERFACE ---
tab1, tab2, tab3, tab4 = st.tabs(["🏋️ 90-Min Workout", "🥗 Full Diet Plan", "🧘 Yoga & Pain Relief", "⏰ Daily Routine"])

with tab1:
    st.header("Master Workout Chart (90 Minutes)")
    st.info("Follow this sequence for a complete 1.5-hour session.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Warm-up (15 Mins)")
        st.write("""
        * **0-5m:** Brisk Walk / Jumping Jacks
        * **5-10m:** Dynamic Stretching (Arm circles, Leg swings)
        * **10-15m:** High Knees & Butt Kicks
        """)
        
        st.subheader("2. Main Strength/Cardio (50 Mins)")
        if goal == "Weight Loss":
            st.write("* **Burpees:** 4 sets x 12 reps\n* **Mountain Climbers:** 4 sets x 30 sec\n* **Squat Jumps:** 4 sets x 15 reps\n* **Plank:** 3 sets x 1 min\n* **Pushups:** 4 sets x Max reps")
        else:
            st.write("* **Weighted Squats:** 4 sets x 10 reps\n* **Bench Press/Pushups:** 4 sets x 10 reps\n* **Deadlifts:** 3 sets x 8 reps\n* **Pull-ups/Rows:** 4 sets x 10 reps")

    with col2:
        st.subheader("3. Core & Accessory (15 Mins)")
        st.write("* **Bicycle Crunches:** 3 sets x 20\n* **Russian Twists:** 3 sets x 30\n* **Leg Raises:** 3 sets x 15")
        
        st.subheader("4. Cool-down & Static Stretching (10 Mins)")
        st.write("* **Cobra Stretch:** 1 min\n* **Hamstring Stretch:** 2 mins\n* **Deep Breathing:** 2 mins")

with tab2:
    st.header(f"{diet_pref} Daily Nutrition Plan")
    
    if diet_pref == "Vegetarian":
        st.table({
            "Meal": ["Breakfast", "Mid-Morning", "Lunch", "Evening Snack", "Dinner"],
            "Menu": [
                "Oats with nuts, seeds, and 1 Banana",
                "A bowl of Papaya or 1 Apple",
                "2 Chapatis, 1 bowl Dal, Paneer Sabzi, and Salad",
                "Roasted Makhana or Handful of Almonds",
                "Brown Rice/Quinoa, Moong Dal, and sautéed Veggies"
            ]
        })
    else:
        st.table({
            "Meal": ["Breakfast", "Mid-Morning", "Lunch", "Evening Snack", "Dinner"],
            "Menu": [
                "3 Egg White Omelet with Whole Wheat Toast",
                "Fruit Salad or Greek Yogurt",
                "Grilled Chicken Breast (150g), Brown Rice, and Salad",
                "1 Boiled Egg or Protein Shake",
                "Baked Fish or Lean Meat with Steamed Broccoli"
            ]
        })

with tab3:
    st.header("Yoga & Pain Relief Tutorials")
    area = st.selectbox("Where is the pain?", ["Lower Back", "Neck & Shoulders", "Full Body Stiffness"])
    
    if area == "Lower Back":
        st.write("**Recommended:** Cat-Cow Pose & Child's Pose")
        st.video("https://www.youtube.com/watch?v=WouR49WQCX4") # Example Yoga Link
    elif area == "Neck & Shoulders":
        st.write("**Recommended:** Ear-to-Shoulder Stretch & Thread the Needle")
        st.video("https://www.youtube.com/watch?v=X3-gK_mS_6I")

with tab4:
    st.header("Optimal Daily Schedule")
    st.write(f"💧 **Water Target:** {round(weight * 0.035, 1)} Liters per day")
    st.write("😴 **Sleep Goal:** 10:30 PM to 6:30 AM")
    st.write("🧘 **Mental Peace:** 10 Minutes of 'Anulom Vilom' Pranayama at 7:00 AM")
