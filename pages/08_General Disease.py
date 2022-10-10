import sklearn as sk
import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

st.set_page_config(page_title="General Disease Predictor", page_icon="")
model = pickle.load(open("gendisease.sav", "rb"))

symptoms = [
    "itching",
    "skin_rash",
    "nodal_skin_eruptions",
    "continuous_sneezing",
    "shivering",
    "chills",
    "joint_pain",
    "stomach_pain",
    "acidity",
    "ulcers_on_tongue",
    "muscle_wasting",
    "vomiting",
    "burning_micturition",
    "spotting_ urination",
    "fatigue",
    "weight_gain",
    "anxiety",
    "cold_hands_and_feets",
    "mood_swings",
    "weight_loss",
    "restlessness",
    "lethargy",
    "patches_in_throat",
    "irregular_sugar_level",
    "cough",
    "high_fever",
    "sunken_eyes",
    "breathlessness",
    "sweating",
    "dehydration",
    "indigestion",
    "headache",
    "yellowish_skin",
    "dark_urine",
    "nausea",
    "loss_of_appetite",
    "pain_behind_the_eyes",
    "back_pain",
    "constipation",
    "abdominal_pain",
    "diarrhoea",
    "mild_fever",
    "yellow_urine",
    "yellowing_of_eyes",
    "acute_liver_failure",
    "fluid_overload",
    "swelling_of_stomach",
    "swelled_lymph_nodes",
    "malaise",
    "blurred_and_distorted_vision",
    "phlegm",
    "throat_irritation",
    "redness_of_eyes",
    "sinus_pressure",
    "runny_nose",
    "congestion",
    "chest_pain",
    "weakness_in_limbs",
    "fast_heart_rate",
    "pain_during_bowel_movements",
    "pain_in_anal_region",
    "bloody_stool",
    "irritation_in_anus",
    "neck_pain",
    "dizziness",
    "cramps",
    "bruising",
    "obesity",
    "swollen_legs",
    "swollen_blood_vessels",
    "puffy_face_and_eyes",
    "enlarged_thyroid",
    "brittle_nails",
    "swollen_extremeties",
    "excessive_hunger",
    "extra_marital_contacts",
    "drying_and_tingling_lips",
    "slurred_speech",
    "knee_pain",
    "hip_joint_pain",
    "muscle_weakness",
    "stiff_neck",
    "swelling_joints",
    "movement_stiffness",
    "spinning_movements",
    "loss_of_balance",
    "unsteadiness",
    "weakness_of_one_body_side",
    "loss_of_smell",
    "bladder_discomfort",
    "foul_smell_of urine",
    "continuous_feel_of_urine",
    "passage_of_gases",
    "internal_itching",
    "toxic_look_(typhos)",
    "depression",
    "irritability",
    "muscle_pain",
    "altered_sensorium",
    "red_spots_over_body",
    "belly_pain",
    "abnormal_menstruation",
    "dischromic _patches",
    "watering_from_eyes",
    "increased_appetite",
    "polyuria",
    "family_history",
    "mucoid_sputum",
    "rusty_sputum",
    "lack_of_concentration",
    "visual_disturbances",
    "receiving_blood_transfusion",
    "receiving_unsterile_injections",
    "coma",
    "stomach_bleeding",
    "distention_of_abdomen",
    "history_of_alcohol_consumption",
    "fluid_overload.1",
    "blood_in_sputum",
    "prominent_veins_on_calf",
    "palpitations",
    "painful_walking",
    "pus_filled_pimples",
    "blackheads",
    "scurring",
    "skin_peeling",
    "silver_like_dusting",
    "small_dents_in_nails",
    "inflammatory_nails",
    "blister",
    "red_sore_around_nose",
    "yellow_crust_ooze",
]
Data = "Training.csv"
data = pd.read_csv(Data).dropna(axis=1)
encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])
symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index

data_dict = {"symptom_index": symptom_index, "predictions_classes": encoder.classes_}


def predictDisease(symptoms):
    symptoms = symptoms.split(",")

    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1

    input_data = np.array(input_data).reshape(1, -1)
    svm_prediction = data_dict["predictions_classes"][model.predict(input_data)[0]]
    return svm_prediction


st.header("General Disease Predictor")
st.write(
    "Choose any symptoms that you are experiencing based on the category and we will do the best to diagnose it"
)

skin = [
    "itching",
    "skin_rash",
    "nodal_skin_eruptions",
    "cold_hands_and_feets",
    "yellowish_skin",
    "puffy_face_and_eyes",
    "brittle_nails",
    "swollen_extremeties",
    "blister",
    "inflammatory_nails",
    "small_dents_in_nails",
    "skin_peeling",
    "pus_filled_pimples",
    "blackheads",
    "scurring",
]

digestion = [
    "stomach_pain",
    "acidity",
    "ulcers_on_tongue",
    "vomiting" "weight_gain",
    "patches_in_throat",
    "irregular_sugar_level",
    "indigestion",
    "loss_of_appetite",
    "constipation",
    "abdominal_pain",
    "diarrhoea",
    "swelling_of_stomach",
    "fluid_overload",
    "pain_during_bowel_movements",
    "pain_in_anal_region",
    "bloody_stool",
    "stomach_bleeding",
    "irritation_in_anus",
    "cramps",
    "passage_of_gases",
    "belly_pain",
]

other = []
for i in symptoms:
    if i in skin or i in digestion:
        pass
    else:
        other.append(i)
for i in range(len(other)):
    other[i] = other[i].replace("_", " ")
    other[i] = other[i].title()
for i in range(len(skin)):
    skin[i] = skin[i].replace("_", " ")
    skin[i] = skin[i].title()
st.subheader("Skin")
skinselect = st.multiselect(
    "Choose anny symptoms that is related to the integumentary system", skin
)
for i in range(len(digestion)):
    digestion[i] = digestion[i].replace("_", " ")
    digestion[i] = digestion[i].title()
st.subheader("Digestive System")
digestionselect = st.multiselect(
    "Choose any symptoms that are related to the digestive system", digestion
)
st.subheader("Other")
otherselect = st.multiselect("Choose any other symptoms", other)
patientsymp = skinselect + digestionselect + otherselect
finalstr = ""
for i in range(len(patientsymp)):
    if i != len(patientsymp) - 1:
        finalstr += patientsymp[i] + ","
    else:
        finalstr += patientsymp[i]
if st.button("Predict"):
    st.write(predictDisease(finalstr))