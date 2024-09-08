import streamlit as st
import pandas as pd

# Analysis Functions
def blood_pressure_analysis(systolic, diastolic, age=None, conditions=None):
    pulse_pressure = systolic - diastolic
    map_value = diastolic + (pulse_pressure / 3)
    
    risk_category = ""
    if systolic < 90 or diastolic < 60:
        risk_category = "Hypotension: Risk of dizziness, fainting, shock."
    elif 90 <= systolic <= 120 and 60 <= diastolic <= 80:
        risk_category = "Normal BP: No immediate risks."
    elif 121 <= systolic <= 139 or 81 <= diastolic <= 89:
        risk_category = "Elevated BP: Increased risk of hypertension, lifestyle changes recommended."
    else:
        risk_category = "Hypertension: Risk of heart attack, stroke, kidney damage."

    if age:
        if age > 60 and risk_category == "Normal BP: No immediate risks.":
            risk_category += " Monitor regularly due to age-related risks."
        if conditions and "diabetes" in conditions.lower():
            risk_category += " Increased risk due to diabetes."

    return {
        "Risk Category": risk_category,
        "Pulse Pressure": pulse_pressure,
        "Mean Arterial Pressure (MAP)": map_value
    }

def blood_sugar_analysis(fasting_glucose, postprandial_glucose, a1c=None):
    risk_category = ""
    if fasting_glucose < 70:
        risk_category = "Hypoglycemia: Risk of confusion, seizures, unconsciousness."
    elif 70 <= fasting_glucose <= 99:
        risk_category = "Normal Fasting Glucose: No immediate risks."
    elif 100 <= fasting_glucose <= 125:
        risk_category = "Pre-Diabetes: Monitor closely, risk of developing diabetes."
    else:
        if postprandial_glucose > 200:
            risk_category = "Diabetes: High risk of cardiovascular disease, nerve damage, immediate intervention needed."
        else:
            risk_category = "Diabetes: Risk of complications, requires medical attention."

    if a1c:
        if a1c >= 6.5:
            risk_category += " A1C indicates diabetes."
        elif 5.7 <= a1c < 6.5:
            risk_category += " A1C indicates pre-diabetes."

    return {
        "Risk Category": risk_category,
        "Recommendations": "Consult with a healthcare provider for personalized advice."
    }

def ecg_analysis(heart_rate, st_elevation=False, t_wave_inversion=False, arrhythmia=False, qt_interval=None):
    risk_category = ""
    if st_elevation or t_wave_inversion or arrhythmia:
        risk_category = "Abnormal ECG: Risk of heart attack, heart failure, arrhythmias."
    elif 60 <= heart_rate <= 100:
        risk_category = "Normal ECG: No immediate risks."
    elif heart_rate < 60:
        risk_category = "Bradycardia: Risk of fainting, fatigue, heart failure."
    else:
        risk_category = "Tachycardia: Risk of heart failure, stroke."

    if qt_interval:
        if qt_interval > 450:
            risk_category += " Prolonged QT: Increased risk of torsades de pointes, sudden death."

    return {
        "Risk Category": risk_category,
        "Recommendations": "Consider further tests if abnormalities persist."
    }

def spO2_analysis(spO2, during_exercise=False):
    risk_category = ""
    if spO2 >= 95:
        risk_category = "Normal SpO2: No immediate risks."
    elif 90 <= spO2 < 95:
        risk_category = "Mild Hypoxemia: Monitor closely, possible respiratory issues."
    elif 85 <= spO2 < 90:
        risk_category = "Moderate Hypoxemia: Risk of respiratory distress, seek medical attention."
    else:
        risk_category = "Severe Hypoxemia: Risk of respiratory failure, organ damage, immediate intervention required."

    if during_exercise and spO2 < 95:
        risk_category += " Reduced exercise tolerance observed, may indicate underlying issues."

    return {
        "Risk Category": risk_category,
        "Recommendations": "Consider pulmonary function tests if hypoxemia persists."
    }

def cholesterol_analysis(total_cholesterol, hdl, ldl):
    risk_category = ""
    if total_cholesterol < 200 and hdl >= 60 and ldl < 100:
        risk_category = "Optimal Cholesterol Levels: Low risk of heart disease."
    elif 200 <= total_cholesterol < 240 or hdl < 60 or ldl >= 100:
        risk_category = "Borderline High Cholesterol: Moderate risk, consider lifestyle changes."
    else:
        risk_category = "High Cholesterol: High risk of heart disease, medical intervention recommended."

    return {
        "Risk Category": risk_category,
        "Recommendations": "Consult with a healthcare provider for further testing and treatment."
    }

def kidney_function_analysis(creatinine, age, gender):
    risk_category = ""
    normal_range = (0.6, 1.2) if gender == 'Male' else (0.5, 1.1)
    if normal_range[0] <= creatinine <= normal_range[1]:
        risk_category = "Normal Kidney Function: No immediate risks."
    else:
        if creatinine > normal_range[1]:
            risk_category = "Possible Kidney Dysfunction: Risk of kidney disease, requires further testing."
        else:
            risk_category = "Low Creatinine: May indicate low muscle mass or malnutrition, consult a doctor."

    return {
        "Risk Category": risk_category,
        "Recommendations": "Consider GFR test for detailed kidney function analysis."
    }

def hemoglobin_analysis(hemoglobin, gender):
    risk_category = ""
    normal_range = (13.8, 17.2) if gender == 'Male' else (12.1, 15.1)
    if normal_range[0] <= hemoglobin <= normal_range[1]:
        risk_category = "Normal Hemoglobin Levels: No immediate risks."
    elif hemoglobin < normal_range[0]:
        risk_category = "Anemia: Risk of fatigue, weakness, consult with a healthcare provider."
    else:
        risk_category = "High Hemoglobin: May indicate dehydration or other underlying conditions, further testing recommended."

    return {
        "Risk Category": risk_category,
        "Recommendations": "Consider a complete blood count (CBC) test for further evaluation."
    }

def troponin_analysis(troponin):
    risk_category = ""
    if troponin < 0.04:
        risk_category = "Normal Troponin Levels: No immediate risks."
    else:
        risk_category = "Elevated Troponin: Possible heart attack, seek immediate medical attention."

    return {
        "Risk Category": risk_category,
        "Recommendations": "Consider emergency medical services for elevated troponin levels."
    }

def bmi_analysis(weight, height):
    bmi = weight / (height ** 2)
    risk_category = ""
    if bmi < 18.5:
        risk_category = "Underweight: Risk of malnutrition, consult with a healthcare provider."
    elif 18.5 <= bmi < 24.9:
        risk_category = "Normal Weight: No immediate risks."
    elif 25 <= bmi < 29.9:
        risk_category = "Overweight: Risk of cardiovascular disease, consider lifestyle changes."
    else:
        risk_category = "Obesity: High risk of cardiovascular disease, diabetes, and other health conditions. Medical intervention recommended."

    return {
        "Risk Category": risk_category,
        "BMI": round(bmi, 2)
    }

def liver_function_analysis(alt, ast, bilirubin):
    risk_category = ""
    if alt < 40 and ast < 40 and bilirubin < 1.2:
        risk_category = "Normal Liver Function: No immediate risks."
    else:
        if alt > 40 or ast > 40:
            risk_category = "Possible Liver Inflammation: Risk of liver disease, further testing recommended."
        if bilirubin > 1.2:
            risk_category += " Elevated Bilirubin: Risk of jaundice, liver dysfunction."

    return {
        "Risk Category": risk_category,
        "Recommendations": "Consult with a healthcare provider for a liver function test if abnormalities are detected."
    }

def thyroid_function_analysis(tsh, t3, t4):
    risk_category = ""
    if 0.4 <= tsh <= 4.0 and 80 <= t3 <= 200 and 5.0 <= t4 <= 12.0:
        risk_category = "Normal Thyroid Function: No immediate risks."
    elif tsh > 4.0:
        risk_category = "Hypothyroidism: Risk of fatigue, weight gain, cold intolerance."
    elif tsh < 0.4:
        risk_category = "Hyperthyroidism: Risk of weight loss, rapid heartbeat, anxiety."
    
    return {
        "Risk Category": risk_category,
        "Recommendations": "Consider thyroid function tests for detailed evaluation if abnormalities persist."
    }

def electrolyte_balance_analysis(sodium, potassium, chloride):
    risk_category = ""
    if 135 <= sodium <= 145 and 3.5 <= potassium <= 5.0 and 98 <= chloride <= 106:
        risk_category = "Normal Electrolyte Balance: No immediate risks."
    else:
        if sodium < 135:
            risk_category = "Hyponatremia: Risk of confusion, seizures, and fatigue."
        elif sodium > 145:
            risk_category = "Hypernatremia: Risk of dehydration, kidney problems."
        if potassium < 3.5:
            risk_category += " Hypokalemia: Risk of muscle weakness, arrhythmias."
        elif potassium > 5.0:
            risk_category += " Hyperkalemia: Risk of cardiac issues."
        if chloride < 98:
            risk_category += " Hypochloremia: Risk of metabolic alkalosis."
        elif chloride > 106:
            risk_category += " Hyperchloremia: Risk of metabolic acidosis."

    return {
        "Risk Category": risk_category,
        "Recommendations": "Consult with a healthcare provider for further testing if imbalances are detected."
    }

def vitamin_d_analysis(vitamin_d):
    risk_category = ""
    if vitamin_d >= 30:
        risk_category = "Normal Vitamin D Levels: No immediate risks."
    elif 20 <= vitamin_d < 30:
        risk_category = "Vitamin D Insufficiency: Risk of bone weakness, consider supplementation."
    else:
        risk_category = "Vitamin D Deficiency: High risk of bone and muscle issues, consult with a healthcare provider."

    return {
        "Risk Category": risk_category,
        "Recommendations": "Consider vitamin D supplementation and sun exposure, consult with a healthcare provider for personalized advice."
    }

def crp_analysis(crp):
    risk_category = ""
    if crp < 5:
        risk_category = "Normal CRP Levels: No immediate risks."
    else:
        risk_category = "Elevated CRP: Indicates inflammation or infection, further testing may be required."

    return {
        "Risk Category": risk_category,
        "Recommendations": "Consult with a healthcare provider to identify underlying causes of elevated CRP."
    }

def egfr_analysis(creatinine, age, gender):
    # eGFR calculation formula (simplified)
    if gender == 'Male':
        eGFR = 141 * (creatinine / 0.9) ** -0.411 * 0.993 ** age
    else:
        eGFR = 141 * (creatinine / 0.7) ** -0.329 * 0.993 ** age

    risk_category = ""
    if eGFR >= 90:
        risk_category = "Normal eGFR: No immediate risks."
    elif 60 <= eGFR < 90:
        risk_category = "Mildly Reduced eGFR: Monitor kidney function."
    else:
        risk_category = "Reduced eGFR: Risk of kidney disease, further testing required."

    return {
        "Risk Category": risk_category,
        "eGFR": round(eGFR, 2)
    }

normal_values = {
    "Blood Pressure": "Systolic: 90-120 mm Hg, Diastolic: 60-80 mm Hg",
    "Blood Sugar": "Fasting Glucose: 70-99 mg/dL, Postprandial Glucose: <200 mg/dL, A1C: <5.7%",
    "ECG": "Heart Rate: 60-100 bpm, QT Interval: 300-450 ms",
    "Oxygen Saturation": "SpO2: 95-100%",
    "Cholesterol": "Total Cholesterol: <200 mg/dL, HDL: ≥60 mg/dL, LDL: <100 mg/dL",
    "Kidney Function": "Creatinine: 0.6-1.2 mg/dL (Male), 0.5-1.1 mg/dL (Female)",
    "Hemoglobin": "Male: 13.8-17.2 g/dL, Female: 12.1-15.1 g/dL",
    "Troponin": "Troponin: <0.04 ng/mL",
    "BMI": "BMI: 18.5-24.9 kg/m²",
    "Liver Function": "ALT: 0-100 U/L, AST: 0-100 U/L, Bilirubin: 0-3 mg/dL",
    "Thyroid Function": "TSH: 0.1-10.0 µIU/mL, T3: 60-200 ng/dL, T4: 4.5-12.0 µg/dL",
    "Electrolyte Balance": "Sodium: 120-160 mEq/L, Potassium: 3.0-6.0 mEq/L, Chloride: 80-120 mEq/L",
    "Vitamin D": "Vitamin D: 20-50 ng/mL",
    "CRP": "CRP: <5 mg/L",
    "eGFR": "eGFR: 90-120 mL/min/1.73 m²"
}

def display_dashboard():
    st.title("Expert Health Analysis Tool")

    
    if st.sidebar.button("View Normal Values and Ranges"):
        st.sidebar.subheader("Normal Values and Ranges")
        
        
        normal_values_df = pd.DataFrame(list(normal_values.items()), columns=["Function", "Normal Values"])
       
        st.sidebar.table(normal_values_df)

 
    st.sidebar.subheader("Select an Analysis Function")
    option = st.sidebar.selectbox(
        "List of Functions",
        ["Select Function", "Blood Pressure", "Blood Sugar", "ECG", "Oxygen Saturation", 
         "Cholesterol", "Kidney Function", "Hemoglobin", "Troponin", "BMI", 
         "Liver Function", "Thyroid Function", "Electrolyte Balance", "Vitamin D", "CRP", "eGFR"]
    )

   
    def display_normal_values():
        st.write("### List of Available Functions and Normal Values")
        
        
        normal_values_df = pd.DataFrame(list(normal_values.items()), columns=["Function", "Normal Values"])
        
        st.write(normal_values_df)

    if option == "Select Function":
        display_normal_values()

    if option == "Blood Pressure":
        st.subheader("Blood Pressure Analysis")
        systolic = st.sidebar.slider("Systolic BP (mm Hg)", 80, 200, 120)
        diastolic = st.sidebar.slider("Diastolic BP (mm Hg)", 50, 130, 80)
        age = st.sidebar.number_input("Age", 1, 100, 30)
        conditions = st.sidebar.text_input("Existing Conditions (e.g., diabetes)")
        bp_result = blood_pressure_analysis(systolic, diastolic, age, conditions)
        st.write(bp_result)

    elif option == "Blood Sugar":
        st.subheader("Blood Sugar Analysis")
        fasting_glucose = st.sidebar.slider("Fasting Glucose (mg/dL)", 50, 200, 90)
        postprandial_glucose = st.sidebar.slider("Postprandial Glucose (mg/dL)", 50, 300, 120)
        a1c = st.sidebar.slider("A1C Level (%)", 4.0, 12.0, 5.5)
        sugar_result = blood_sugar_analysis(fasting_glucose, postprandial_glucose, a1c)
        st.write(sugar_result)

    elif option == "ECG":
        st.subheader("ECG Analysis")
        heart_rate = st.sidebar.slider("Heart Rate (bpm)", 40, 180, 75)
        st_elevation = st.sidebar.checkbox("ST Elevation")
        t_wave_inversion = st.sidebar.checkbox("T-Wave Inversion")
        arrhythmia = st.sidebar.checkbox("Arrhythmia")
        qt_interval = st.sidebar.slider("QT Interval (ms)", 300, 500, 400)
        ecg_result = ecg_analysis(heart_rate, st_elevation, t_wave_inversion, arrhythmia, qt_interval)
        st.write(ecg_result)

    elif option == "Oxygen Saturation":
        st.subheader("Oxygen Saturation Analysis")
        spO2 = st.sidebar.slider("SpO2 Level (%)", 70, 100, 98)
        during_exercise = st.sidebar.checkbox("During Exercise")
        spo2_result = spO2_analysis(spO2, during_exercise)
        st.write(spo2_result)

    elif option == "Cholesterol":
        st.subheader("Cholesterol Analysis")
        total_cholesterol = st.sidebar.slider("Total Cholesterol (mg/dL)", 100, 400, 180)
        hdl = st.sidebar.slider("HDL Cholesterol (mg/dL)", 20, 100, 55)
        ldl = st.sidebar.slider("LDL Cholesterol (mg/dL)", 50, 200, 100)
        cholesterol_result = cholesterol_analysis(total_cholesterol, hdl, ldl)
        st.write(cholesterol_result)

    elif option == "Kidney Function":
        st.subheader("Kidney Function Analysis")
        creatinine = st.sidebar.slider("Creatinine Level (mg/dL)", 0.4, 2.0, 1.0)
        gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
        age = st.sidebar.number_input("Age", 1, 100, 30)
        kidney_result = kidney_function_analysis(creatinine, age, gender)
        st.write(kidney_result)

    elif option == "Hemoglobin":
        st.subheader("Hemoglobin Analysis")
        hemoglobin = st.sidebar.slider("Hemoglobin Level (g/dL)", 8, 20, 14)
        gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
        hemoglobin_result = hemoglobin_analysis(hemoglobin, gender)
        st.write(hemoglobin_result)

    elif option == "Troponin":
        st.subheader("Troponin Analysis")
        troponin = st.sidebar.slider("Troponin Level (ng/mL)", 0.0, 10.0, 0.02)
        troponin_result = troponin_analysis(troponin)
        st.write(troponin_result)

    elif option == "BMI":
        st.subheader("BMI Analysis")
        weight = st.sidebar.slider("Weight (kg)", 30, 200, 70)
        height = st.sidebar.slider("Height (m)", 1.2, 2.2, 1.75)
        bmi_result = bmi_analysis(weight, height)
        st.write(bmi_result)

    elif option == "Liver Function":
        st.subheader("Liver Function Analysis")
        alt = st.sidebar.slider("ALT (U/L)", 0, 100, 30)
        ast = st.sidebar.slider("AST (U/L)", 0, 100, 30)
        bilirubin = st.sidebar.slider("Bilirubin (mg/dL)", 0, 3, 1)
        liver_result = liver_function_analysis(alt, ast, bilirubin)
        st.write(liver_result)

    elif option == "Thyroid Function":
        st.subheader("Thyroid Function Analysis")
        tsh = st.sidebar.slider("TSH (µIU/mL)", 0.1, 10.0, 2.0)
        t3 = st.sidebar.slider("T3 (ng/dL)", 60, 200, 120)
        t4 = st.sidebar.slider("T4 (µg/dL)", 4.5, 12.0, 7.0)
        thyroid_result = thyroid_function_analysis(tsh, t3, t4)
        st.write(thyroid_result)

    elif option == "Electrolyte Balance":
        st.subheader("Electrolyte Balance Analysis")
        sodium = st.sidebar.slider("Sodium (mEq/L)", 120, 160, 140)
        potassium = st.sidebar.slider("Potassium (mEq/L)", 3.0, 6.0, 4.0)
        chloride = st.sidebar.slider("Chloride (mEq/L)", 80, 120, 100)
        electrolyte_result = electrolyte_balance_analysis(sodium, potassium, chloride)
        st.write(electrolyte_result)

    elif option == "Vitamin D":
        st.subheader("Vitamin D Analysis")
        vitamin_d = st.sidebar.slider("Vitamin D (ng/mL)", 10, 60, 30)
        vitamin_d_result = vitamin_d_analysis(vitamin_d)
        st.write(vitamin_d_result)

    elif option == "CRP":
        st.subheader("CRP Analysis")
        crp = st.sidebar.slider("CRP (mg/L)", 0, 50, 3)
        crp_result = crp_analysis(crp)
        st.write(crp_result)

    elif option == "eGFR":
        st.subheader("eGFR Analysis")
        egfr = st.sidebar.slider("eGFR (mL/min/1.73 m²)", 30, 150, 90)
        egfr_result = egfr_analysis(egfr)
        st.write(egfr_result)

if __name__ == '__main__':
    display_dashboard()
