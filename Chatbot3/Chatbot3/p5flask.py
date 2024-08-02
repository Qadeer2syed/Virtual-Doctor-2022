import pickle
import flask
from flask import render_template, request
import os
import numpy as np 
import kb
import retrieve_name



app = flask.Flask(__name__)


model = pickle.load(open("svcpickle.pkl","rb"))
 
#@app.route('/predict', methods=['GET', 'POST'])
#def predict():
#    features = flask.request.get_json(force=True)['features']
#    prediction = model.predict([features])[0,0]
#    response = {'prediction': prediction}
#    return flask.jsonify(response)



#@app.route('/', methods=['GET', 'POST'])
#def form():
#   return render_template('form.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
        itching = request.form['itching']                        

        skin_rash = request.form['skin_rash']

        nodal_skin_eruptions = request.form['nodal_skin_eruptions']
        
        continuous_sneezing = request.form['continuous_sneezing']

        shivering = request.form['shivering']

        chills = request.form['chills']

        joint_pain = request.form['joint_pain']

        stomach_pain = request.form['stomach_pain']

        acidity = request.form['acidity']

        ulcers_on_tongue = request.form['ulcers_on_tongue']

        muscle_wasting = request.form['muscle_wasting']

        vomiting = request.form['vomiting']

        burning_micturition = request.form['burning_micturition']

        spotting_urination = request.form['spotting_urination']

        fatigue = request.form['fatigue']

        weight_gain = request.form['weight_gain']

        anxiety = request.form['anxiety']

        cold_hands_and_feets = request.form['cold_hands_and_feets']

        mood_swings = request.form['mood_swings']

        weight_loss = request.form['weight_loss']

        restlessness = request.form['restlessness']

        lethargy = request.form['lethargy']

        patches_in_throat = request.form['patches_in_throat']

        irregular_sugar_level = request.form['irregular_sugar_level']

        cough = request.form['cough']

        high_fever = request.form['high_fever']

        sunken_eyes = request.form['sunken_eyes']

        breathlessness = request.form['breathlessness']
        
        sweating = request.form['sweating']

        dehydration = request.form['dehydration']

        indigestion = request.form['indigestion']

        headache = request.form['headache']

        yellowish_skin = request.form['yellowish_skin']

        dark_urine = request.form['dark_urine']

        nausea = request.form['nausea']

        loss_of_appetite = request.form['loss_of_appetite']

        pain_behind_the_eyes = request.form['pain_behind_the_eyes']

        back_pain = request.form['back_pain']

        constipation = request.form['constipation']

        abdominal_pain = request.form['abdominal_pain']

        diarrhoea = request.form['diarrhoea']

        mild_fever = request.form['mild_fever']

        yellow_urine = request.form['yellow_urine']

        yellowing_of_eyes = request.form['yellowing_of_eyes']

        acute_liver_failure = request.form['acute_liver_failure']

        fluid_overload = request.form['fluid_overload']

        swelling_of_stomach = request.form['swelling_of_stomach']

        swelled_lymph_nodes = request.form['swelled_lymph_nodes']

        malaise = request.form['malaise']

        blurred_and_distorted_vision = request.form['blurred_and_distorted_vision']

        phlegm = request.form['phlegm']

        throat_irritation = request.form['throat_irritation']

        redness_of_eyes = request.form['redness_of_eyes']

        sinus_pressure = request.form['sinus_pressure']

        runny_nose = request.form['runny_nose']

        congestion = request.form['congestion']

        chest_pain = request.form['chest_pain']

        weakness_in_limbs = request.form['weakness_in_limbs']

        fast_heart_rate = request.form['fast_heart_rate']

        pain_during_bowel_movements = request.form['pain_during_bowel_movements']

        pain_in_anal_region = request.form['pain_in_anal_region']

        bloody_stool = request.form['bloody_stool']

        irritation_in_anus = request.form['irritation_in_anus']

        neck_pain = request.form['neck_pain']

        dizziness = request.form['dizziness']

        cramps = request.form['cramps']

        bruising = request.form['bruising']

        obesity = request.form['obesity']

        swollen_legs = request.form['swollen_legs']

        swollen_blood_vessels = request.form['swollen_blood_vessels']

        puffy_face_and_eyes = request.form['puffy_face_and_eyes']

        enlarged_thyroid = request.form['enlarged_thyroid']

        brittle_nails = request.form['brittle_nails']

        swollen_extremeties = request.form['swollen_extremeties']

        excessive_hunger = request.form['excessive_hunger']

        extra_marital_contacts = request.form['extra_marital_contacts']

        drying_and_tingling_lips = request.form['drying_and_tingling_lips']

        slurred_speech = request.form['slurred_speech']

        knee_pain = request.form['knee_pain']

        hip_joint_pain = request.form['hip_joint_pain']

        muscle_weakness = request.form['muscle_weakness']

        stiff_neck = request.form['stiff_neck']

        swelling_joints = request.form['swelling_joints']

        movement_stiffness = request.form['movement_stiffness']

        spinning_movements = request.form['spinning_movements']

        loss_of_balance = request.form['loss_of_balance']

        unsteadiness = request.form['unsteadiness']

        weakness_of_one_body_side = request.form['weakness_of_one_body_side']

        loss_of_smell = request.form['loss_of_smell']

        bladder_discomfort = request.form['bladder_discomfort']

        foul_smell_of_urine = request.form['foul_smell_of_urine']

        continuous_feel_of_urine = request.form['continuous_feel_of_urine']

        passage_of_gases = request.form['passage_of_gases']

        internal_itching = request.form['internal_itching']

        toxic_look_typhos = request.form['toxic_look_typhos']

        depression = request.form['depression']

        irritability = request.form['irritability']

        muscle_pain = request.form['muscle_pain']

        altered_sensorium = request.form['altered_sensorium']

        red_spots_over_body = request.form['red_spots_over_body']

        belly_pain = request.form['belly_pain']

        abnormal_menstruation = request.form['abnormal_menstruation']

        dischromic_patches = request.form['dischromic_patches']

        watering_from_eyes = request.form['watering_from_eyes']

        increased_appetite = request.form['increased_appetite']

        polyuria = request.form['polyuria']

        family_history = request.form['family_history']

        mucoid_sputum = request.form['mucoid_sputum']

        rusty_sputum = request.form['rusty_sputum']

        lack_of_concentration = request.form['lack_of_concentration']

        visual_disturbances = request.form['visual_disturbances']

        receiving_blood_transfusion = request.form['receiving_blood_transfusion']

        receiving_unsterile_injections = request.form['receiving_unsterile_injections']

        coma = request.form['coma']

        stomach_bleeding = request.form['stomach_bleeding']

        distention_of_abdomen = request.form['distention_of_abdomen']

        history_of_alcohol_consumption = request.form['history_of_alcohol_consumption']

        fluid_overload = request.form['fluid_overload']

        blood_in_sputum = request.form['blood_in_sputum']

        prominent_veins_on_calf = request.form['prominent_veins_on_calf']

        palpitations = request.form['palpitations']

        painful_walking = request.form['painful_walking']

        pus_filled_pimples = request.form['pus_filled_pimples']

        blackheads = request.form['blackheads']

        scurring = request.form['scurring']

        skin_peeling = request.form['skin_peeling']

        silver_like_dusting = request.form['silver_like_dusting']

        small_dents_in_nails = request.form['small_dents_in_nails']
            
        inflammatory_nails = request.form['inflammatory_nails']

        blister = request.form['blister']

        red_sore_around_nose = request.form['red_sore_around_nose']

        yellow_crust_ooze = request.form['yellow_crust_ooze']

        array=np.array([itching,
        skin_rash,
        nodal_skin_eruptions,
        continuous_sneezing,
        shivering,
        chills,
        joint_pain,
        stomach_pain,
        acidity,
        ulcers_on_tongue,
        muscle_wasting,
        vomiting,
        burning_micturition,
        spotting_urination,
        fatigue,
        weight_gain,
        anxiety,
        cold_hands_and_feets,
        mood_swings,
        weight_loss,
        restlessness,
        lethargy,
        patches_in_throat,
        irregular_sugar_level,
        cough,
        high_fever,
        sunken_eyes,
        breathlessness,
        sweating,
        dehydration,
        indigestion,
        headache,
        yellowish_skin,
        dark_urine,
        nausea,
        loss_of_appetite,
        pain_behind_the_eyes,
        back_pain,
        constipation,
        abdominal_pain,
        diarrhoea,
        mild_fever,
        yellow_urine,
        yellowing_of_eyes,
        acute_liver_failure,
        fluid_overload,
        swelling_of_stomach,
        swelled_lymph_nodes,
        malaise,
        blurred_and_distorted_vision,
        phlegm,
        throat_irritation,
        redness_of_eyes,
        sinus_pressure,
        runny_nose,
        congestion,
        chest_pain,
        weakness_in_limbs,
        fast_heart_rate,
        pain_during_bowel_movements,
        pain_in_anal_region,
        bloody_stool,
        irritation_in_anus,
        neck_pain,
        dizziness,
        cramps,
        bruising,
        obesity,
        swollen_legs,
        swollen_blood_vessels,
        puffy_face_and_eyes,
        enlarged_thyroid,
        brittle_nails,
        swollen_extremeties,
        excessive_hunger,
        extra_marital_contacts,
        drying_and_tingling_lips,
        slurred_speech,
        knee_pain,
        hip_joint_pain,
        muscle_weakness,
        stiff_neck,
        swelling_joints,
        movement_stiffness,
        spinning_movements,
        loss_of_balance,
        unsteadiness,
        weakness_of_one_body_side,
        loss_of_smell,
        bladder_discomfort,
        foul_smell_of_urine,
        continuous_feel_of_urine,
        passage_of_gases,
        internal_itching,
        toxic_look_typhos,
        depression,
        irritability,
        muscle_pain,
        altered_sensorium,
        red_spots_over_body,
        belly_pain,
        abnormal_menstruation,
        dischromic_patches,
        watering_from_eyes,
        increased_appetite,
        polyuria,
        family_history,
        mucoid_sputum,
        rusty_sputum,
        lack_of_concentration,
        visual_disturbances,
        receiving_blood_transfusion,
        receiving_unsterile_injections,
        coma,
        stomach_bleeding,
        distention_of_abdomen,
        history_of_alcohol_consumption,
        fluid_overload,
        blood_in_sputum,
        prominent_veins_on_calf,
        palpitations,
        painful_walking,
        pus_filled_pimples,
        blackheads,
        scurring,
        skin_peeling,
        silver_like_dusting,
        small_dents_in_nails,
        inflammatory_nails,
        blister,
        red_sore_around_nose,
        yellow_crust_ooze,])
        
        


        diagnosis = model.predict(array.reshape(1, -1))


        return render_template('output.html', say=diagnosis[0])

if __name__ == "__main__":
    app.run()

 

