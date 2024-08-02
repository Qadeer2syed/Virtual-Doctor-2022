import pickle
import flask
from flask import render_template, request
import os
import numpy as np 
#import kb
from retrieve_name import retrieve_name
#import pytholog as pl
from sympy import *
from sympy import And,Or,Not



app = flask.Flask(__name__)


model = pickle.load(open("svcpickle01.pkl","rb"))
#new_kb = pickle.load(open("kbpickle.pkl","rb"))
#@app.route('/predict', methods=['GET', 'POST'])
#def predict():
#    features = flask.request.get_json(force=True)['features']
#    prediction = model.predict([features])[0,0]
#    response = {'prediction': prediction}
#   return  flask.jsonify(response)



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
        
        # fever = 10000
        # rash = 10000
        # throat = 10000
        
        # fever = retrieve_name(fever)
        # rash = retrieve_name(rash)
        # throat = retrieve_name(throat)
        
        # #kbResult = new_kb.query(pl.Expr("disease(X, cold, fever, rn)"))[0]['X']
        # kbResult = new_kb.query(pl.Expr(f"disease(X, {fever[0]}, {fever[1]}, {fever[2]})"))[0]['X']
        
        
        
        if(itching==10000):
               itching=True
        else:
               itching=False
       
        if(skin_rash==10000):
               skin_rash=True
        else:
               skin_rash=False
       
        if(nodal_skin_eruptions==10000):
            nodal_skin_eruptions=True
        else:
                nodal_skin_eruptions=False
       
        if(continuous_sneezing==10000):
            continuous_sneezing=True
        else:
                continuous_sneezing=False
       
        if(shivering==10000):
            shivering=True
        else:
                shivering=False
       
        if(chills==10000):
            chills=True
        else:
               chills=False
       
        if(joint_pain==10000):
            joint_pain=True
        else:
                joint_pain=False
       
        if(stomach_pain==10000):
           stomach_pain=True
        else:
                stomach_pain=False
       
        if(acidity==10000):
            acidity=True
        else:
               acidity=False
       
        if(ulcers_on_tongue==10000):
            ulcers_on_tongue=True
        else:
                ulcers_on_tongue=False
       
        if(muscle_wasting==10000):
            muscle_wasting=True
        else:
                muscle_wasting=False
       
        if(vomiting==10000):
            vomiting=True
        else:
                vomiting=False
       
        if(burning_micturition==10000):
            burning_micturition=True
        else:
                burning_micturition=False
       
        if(spotting_urination==10000):
            spotting_urination=True
        else:
                spotting_urination=False
       
        if(fatigue==10000):
            fatigue=True
        else:
                fatigue=False
       
        if(weight_gain==10000):
            weight_gain=True
        else:
                weight_gain=False
       
        if(anxiety==10000):
            anxiety=True
        else:
                anxiety=False
       
        if(cold_hands_and_feets==10000):
             cold_hands_and_feets=True
        else:
                 cold_hands_and_feets=False
       
        if(mood_swings==10000):
            mood_swings=True
        else:
                mood_swings=False
       
        if(weight_loss==10000):
            weight_loss=True
        else:
                weight_loss=False
       
        if(restlessness==10000):
            restlessness=True
        else:
                restlessness=False
       
        if(lethargy==10000):
            lethargy=True
        else:
                lethargy=False
       
        if(patches_in_throat==10000):
            patches_in_throat=True
        else:
                patches_in_throat=False
       
        if(irregular_sugar_level==10000):
             irregular_sugar_level=True
        else:
                 irregular_sugar_level=False
       
        if(cough==10000):
            cough=True
        else:
                cough=False
       
        if(high_fever==10000):
            high_fever=True
        else:
                high_fever=False
       
        if(sunken_eyes==10000):
            sunken_eyes=True
        else:
                sunken_eyes=False
       
        if(breathlessness==10000):
            breathlessness=True
        else:
                breathlessness=False
       
        if(sweating==10000):
            sweating=True
        else:
                sweating=False
       
        if(dehydration==10000):
            dehydration=True
        else:
                dehydration=False
       
        if(indigestion==10000):
            indigestion=True
        else:
                indigestion=False
       
        if(headache==10000):
            headache=True
        else:
                headache=False
       
        if(yellowish_skin==10000):
            yellowish_skin=True
        else:
                yellowish_skin=False
       
        if(dark_urine==10000):
            dark_urine=True
        else:
                dark_urine=False
       
        if(nausea==10000):
            nausea=True
        else:
                nausea=False
       
        if(loss_of_appetite==10000):
            loss_of_appetite=True
        else:
                loss_of_appetite=False
       
        if(pain_behind_the_eyes==10000):
            pain_behind_the_eyes=True
        else:
                pain_behind_the_eyes=False
       
        if(back_pain==10000):
            back_pain=True
        else:
                back_pain=False
       
        if(constipation==10000):
            constipation=True
        else:
                constipation=False
       
        if(abdominal_pain==10000):
            abdominal_pain=True
        else:
                abdominal_pain=False
       
        if(diarrhoea==10000):
            diarrhoea=True
        else:
                diarrhoea=False
       
        if(mild_fever==10000):
            mild_fever=True
        else:
                mild_fever=False
       
        if(yellow_urine==10000):
            yellow_urine=True
        else:
                yellow_urine=False
       
        if(yellowing_of_eyes==10000):
            yellowing_of_eyes=True
        else:
                yellowing_of_eyes=False
       
        if(acute_liver_failure==10000):
            acute_liver_failure=True
        else:
                acute_liver_failure=False
       
        if(fluid_overload==10000):
            fluid_overload=True
        else:
                fluid_overload=False
       
        if(swelling_of_stomach==10000):
            swelling_of_stomach=True
        else:
                swelling_of_stomach=False
       
        if(swelled_lymph_nodes==10000):
            swelled_lymph_nodes=True
        else:
                swelled_lymph_nodes=False
       
        if(malaise==10000):
            malaise=True
        else:
                malaise=False
       
        if(blurred_and_distorted_vision==10000):
            blurred_and_distorted_vision=True
        else:
                blurred_and_distorted_vision=False
       
        if(phlegm==10000):
            phlegm=True
        else:
                phlegm=False
       
        if(throat_irritation==10000):
            throat_irritation=True
        else:
                throat_irritation=False
       
        if(redness_of_eyes==10000):
            redness_of_eyes=True
        else:
                redness_of_eyes=False
       
        if(sinus_pressure==10000):
            sinus_pressure=True
        else:
                sinus_pressure=False
       
        if(runny_nose==10000):
            runny_nose=True
        else:
                runny_nose=False
       
        if(congestion==10000):
            congestion=True
        else:
                congestion=False
       
        if(chest_pain==10000):
            chest_pain=True
        else:
                chest_pain=False
       
        if(weakness_in_limbs==10000):
            weakness_in_limbs=True
        else:
                weakness_in_limbs=False
       
        if(fast_heart_rate==10000):
            fast_heart_rate=True
        else:
                fast_heart_rate=False
       
        if(pain_during_bowel_movements==10000):
            pain_during_bowel_movements=True
        else:
                pain_during_bowel_movements=False
       
        if(pain_in_anal_region==10000):
            pain_in_anal_region=True
        else:
                pain_in_anal_region=False
       
        if(bloody_stool==10000):
            bloody_stool=True
        else:
                bloody_stool=False
       
        if(irritation_in_anus==10000):
            irritation_in_anus=True
        else:
                irritation_in_anus=False
       
        if(neck_pain==10000):
            neck_pain=True
        else:
                neck_pain=False
       
        if(dizziness==10000):
            dizziness=True
        else:
                dizziness=False
       
        if(cramps==10000):
            cramps=True
        else:
                cramps=False
       
        if(bruising==10000):
            bruising=True
        else:
                bruising=False
       
        if(obesity==10000):
            obesity=True
        else:
                obesity=False
       
        if(swollen_legs==10000):
            swollen_legs=True
        else:
                swollen_legs=False
       
        if(swollen_blood_vessels==10000):
            swollen_blood_vessels=True
        else:
                swollen_blood_vessels=False
       
        if(puffy_face_and_eyes==10000):
            puffy_face_and_eyes=True
        else:
                puffy_face_and_eyes=False
       
        if(enlarged_thyroid==10000):
            enlarged_thyroid=True
        else:
                enlarged_thyroid=False
       
        if(brittle_nails==10000):
            brittle_nails=True
        else:
                brittle_nails=False
       
        if(swollen_extremeties==10000):
            swollen_extremeties=True
        else:
               swollen_extremeties=False
       
        if(excessive_hunger==10000):
            excessive_hunger=True
        else:
                excessive_hunger=False
       
        if(extra_marital_contacts==10000):
            extra_marital_contacts=True
        else:
                extra_marital_contacts=False
       
        if(drying_and_tingling_lips==10000):
            drying_and_tingling_lips=True
        else:
                drying_and_tingling_lips=False
       
        if(slurred_speech==10000):
            slurred_speech=True
        else:
                slurred_speech=False
       
        if(knee_pain==10000):
            knee_pain=True
        else:
                knee_pain=False
       
        if(hip_joint_pain==10000):
            hip_joint_pain=True
        else:
                hip_joint_pain=False
       
        if(muscle_weakness==10000):
            muscle_weakness=True
        else:
                muscle_weakness=False
       
        if(stiff_neck==10000):
            stiff_neck=True
        else:
                stiff_neck=False
       
        if(swelling_joints==10000):
            swelling_joints=True
        else:
                swelling_joints=False
       
        if(movement_stiffness==10000):
            movement_stiffness=True
        else:
                movement_stiffness=False
       
        if(spinning_movements==10000):
            spinning_movements=True
        else:
                spinning_movements=False
       
        if(loss_of_balance==10000):
            loss_of_balance=True
        else:
                loss_of_balance=False
       
        if(unsteadiness==10000):
            unsteadiness=True
        else:
                unsteadiness=False
       
        if(weakness_of_one_body_side==10000):
            weakness_of_one_body_side=True
        else:
                weakness_of_one_body_side=False
       
        if(loss_of_smell==10000):
            loss_of_smell=True
        else:
                loss_of_smell=False
       
        if(bladder_discomfort==10000):
            bladder_discomfort=True
        else:
                bladder_discomfort=False
       
        if(foul_smell_of_urine==10000):
            foul_smell_of_urine=True
        else:
                foul_smell_of_urine=False
       
        if(continuous_feel_of_urine==10000):
            continuous_feel_of_urine=True
        else:
                continuous_feel_of_urine=False
       
        if(passage_of_gases==10000):
            passage_of_gases=True
        else:
                passage_of_gases=False
       
        if(internal_itching==10000):
            internal_itching=True
        else:
                internal_itching=False
       
        if(toxic_look_typhos==10000):
            toxic_look_typhos=True
        else:
                toxic_look_typhos=False
       
        if(depression==10000):
            depression=True
        else:
                depression=False
       
        if(irritability==10000):
            irritability=True
        else:
                irritability=False
       
        if(muscle_pain==10000):
            muscle_pain=True
        else:
                muscle_pain=False
       
        if(altered_sensorium==10000):
            altered_sensorium=True
        else:
                altered_sensorium=False
       
        if(red_spots_over_body==10000):
            red_spots_over_body=True
        else:
                red_spots_over_body=False
       
        if(belly_pain==10000):
            belly_pain=True
        else:
                belly_pain=False
       
        if(abnormal_menstruation==10000):
            abnormal_menstruation=True
        else:
                abnormal_menstruation=False
       
        if(dischromic_patches==10000):
            dischromic_patches=True
        else:
                dischromic_patches=False
       
        if(watering_from_eyes==10000):
            watering_from_eyes=True
        else:
                watering_from_eyes=False
       
        if(increased_appetite==10000):
            increased_appetite=True
        else:
                increased_appetite=False
       
        if(polyuria==10000):
            polyuria=True
        else:
               polyuria=False
       
        if(family_history==10000):
            family_history=True
        else:
                family_history=False
       
        if(mucoid_sputum==10000):
            mucoid_sputum=True
        else:
                mucoid_sputum=False
       
        if(rusty_sputum==10000):
            rusty_sputum=True
        else:
                rusty_sputum=False
       
        if(lack_of_concentration==10000):
            lack_of_concentration=True
        else:
                lack_of_concentration=False
       
        if(visual_disturbances==10000):
            visual_disturbances=True
        else:
                visual_disturbances=False
       
        if(receiving_blood_transfusion==10000):
            receiving_blood_transfusion=True
        else:
                receiving_blood_transfusion=False
       
        if(receiving_unsterile_injections==10000):
            receiving_unsterile_injections=True
        else:
                receiving_unsterile_injections=False
       
        if(coma==10000):
            coma=True
        else:
               coma=False
       
        if(stomach_bleeding==10000):
            stomach_bleeding=True
        else:
                stomach_bleeding=False
       
        if(distention_of_abdomen==10000):
            distention_of_abdomen=True
        else:
                distention_of_abdomen=False
       
        if(history_of_alcohol_consumption==10000):
            history_of_alcohol_consumption=True
        else:
                history_of_alcohol_consumption=False
       
        if(fluid_overload==10000):
            fluid_overload=True
        else:
                fluid_overload=False
       
        if(blood_in_sputum==10000):
            blood_in_sputum=True
        else:
                blood_in_sputum=False
       
        if(prominent_veins_on_calf==10000):
            prominent_veins_on_calf=True
        else:
                prominent_veins_on_calf=False
       
        if(palpitations==10000):
            palpitations=True
        else:
                palpitations=False
       
        if(painful_walking==10000):
            painful_walking=True
        else:
                painful_walking=False
       
        if(pus_filled_pimples==10000):
            pus_filled_pimples=True
        else:
                pus_filled_pimples=False
       
        if(blackheads==10000):
            blackheads=True
        else:
                blackheads=False
       
        if(scurring==10000):
            scurring=True
        else:
               scurring=False
       
        if(skin_peeling==10000):
            skin_peeling=True
        else:
                skin_peeling=False
       
        if(silver_like_dusting==10000):
            silver_like_dusting=True
        else:
                silver_like_dusting=False
       
        if(small_dents_in_nails==10000):
            small_dents_in_nails=True
        else:
                small_dents_in_nails=False
       
        if(inflammatory_nails==10000):
            inflammatory_nails=True
        else:
                inflammatory_nails=False
       
        if(blister==10000):
            blister=True
        else:
                blister=False
       
        if(red_sore_around_nose==10000):
            red_sore_around_nose=True
        else:
                red_sore_around_nose=False
       
        if(yellow_crust_ooze==10000):
            yellow_crust_ooze=True
        else:
            yellow_crust_ooze=False
   
    
    #diseases
    
        kbResult = 'None'

        Gastroenteritis = And(diarrhoea,dehydration,sunken_eyes,vomiting)
        if(Gastroenteritis==True):
            kbResult =  'Gastroenteritis'

        Bronchial_Asthma = And(mucoid_sputum,breathlessness,high_fever,cough,fatigue)
        if(Bronchial_Asthma==True):
            kbResult =  'Bronchial Asthma'

        Hypertension = And(Or(lack_of_concentration,loss_of_balance,dizziness,chest_pain,headache),Not(Or(itching,shivering,skin_rash,stomach_pain,fatigue,weight_loss,loss_of_smell)))
        if(Hypertension==True):
            kbResult =  'Hypertension'

        Migraine = And(Or(visual_disturbances,irritability,depression,stiff_neck,excessive_hunger,blurred_and_distorted_vision,headache,indigestion,acidity),Not(Or(shivering,skin_rash,vomiting,high_fever,nausea,weakness_in_limbs)))
        if(Migraine==True):
            kbResult =  'Migraine'

        Cervical_spondylosis = And(loss_of_balance,dizziness,neck_pain,weakness_in_limbs,back_pain)
        if(Cervical_spondylosis==True):
            kbResult =  'cervical spondylosis'

        Paralysis = And(muscle_pain,weakness_of_one_body_side,headache,vomiting)
        if(Paralysis==True):
            kbResult =  'Paralysis'

        Jaundice = And(abdominal_pain,dark_urine,yellowish_skin,high_fever,weight_loss,fatigue,vomiting,itching)
        if(Jaundice==True):
            kbResult =  'Jaundice'

        Malaria = And(And(muscle_pain,diarrhoea,nausea,headache,sweating,high_fever,chills),Or(vomiting,))
        if(Malaria==True):
            kbResult =  'Malaria'

        Chicken_pox = And(And(red_spots_over_body,pain_behind_the_eyes,headache,high_fever,skin_rash),Or(itching,lethargy,fatigue,swelled_lymph_nodes,mild_fever))
        if(Chicken_pox==True):
            kbResult =  'Chicken_pox'

        Dengue = And(And(muscle_pain,skin_rash,chills,joint_pain,vomiting,fatigue,high_fever,headache),Or(pain_behind_the_eyes,back_pain,nausea,loss_of_appetite,loss_of_appetite,malaise))
        if(Dengue==True):
            kbResult =  'Dengue'

        Typhoid = And(And(chills,fatigue,high_fever,headache,nausea), Or(constipation,abdominal_pain,diarrhoea,toxic_look_typhos,belly_pain,vomiting))
        if(Typhoid==True):
            kbResult =  'Typhoid'

        Hepatitis = And(And(yellowish_skin,dark_urine,loss_of_appetite,abdominal_pain,yellowing_of_eyes), Or(itching,joint_pain,fatigue,lethargy,yellow_urine,diarrhoea,mild_fever,malaise,muscle_pain,receiving_blood_transfusion))
        if(Hepatitis==True):
            kbResult =  'Hepatitis'

        Alcoholic_hepatitis = And(fluid_overload,history_of_alcohol_consumption,distention_of_abdomen,swelling_of_stomach,abdominal_pain,yellowish_skin)
        if(Alcoholic_hepatitis==True):
            kbResult =  'Alcoholic hepatitis'

        Tuberculosis = And(And(blood_in_sputum,chest_pain,phlegm,malaise,swelled_lymph_nodes,yellowing_of_eyes,mild_fever,loss_of_appetite),Or(sweating,breathlessness,high_fever,cough,chills,fatigue))
        if(Tuberculosis==True):
            kbResult =  'Tuberculosis'

        Common_Cold = And(And(runny_nose,sinus_pressure,redness_of_eyes,throat_irritation,phlegm,headache,high_fever,cough,chills,continuous_sneezing),Or(malaise,swelled_lymph_nodes,malaise,swelled_lymph_nodes,muscle_pain,loss_of_smell,chest_pain,))
        if(Common_Cold==True):
            kbResult =  'Common Cold'

        Pneumonia = And(And(rusty_sputum,phlegm,sweating,breathlessness,high_fever,chills),Or(fast_heart_rate,chest_pain,cough,fatigue,malaise))
        if(Pneumonia==True):
            kbResult =  'Pneumonia'

        Dimorphic_hemmorhoids = And(irritation_in_anus,bloody_stool,pain_in_anal_region,pain_during_bowel_movements,constipation)
        if(Dimorphic_hemmorhoids==True):
            kbResult =  'Dimorphic hemmorhoids'

        Heart_attack = And(chest_pain,sweating,breathlessness,vomiting)
        if(Heart_attack==True):
            kbResult =  'Heart attack'

        Varicose_veins = And(And(prominent_veins_on_calf,swollen_blood_vessels,swollen_legs,cramps),Or(bruising,obesity,fatigue))
        if(Varicose_veins==True):
            kbResult =  'Varicose veins'

        Hypothyroidism = And(And(abnormal_menstruation,irritability,fatigue,mood_swings), Or(weight_gain,weight_loss,cold_hands_and_feets,depression,muscle_weakness,excessive_hunger,swollen_extremeties,brittle_nails,enlarged_thyroid,puffy_face_and_eyes,dizziness,fast_heart_rate,diarrhoea,sweating,lethargy,restlessness))
        if(Hypothyroidism==True):
            kbResult =  'Hypothyroidism'

        Hypoglycemia = And(And(palpitations,irritability,slurred_speech,excessive_hunger,blurred_and_distorted_vision,fatigue,anxiety,),Or(nausea,vomiting,sweating,headache))
        if(Hypoglycemia==True):
            kbResult =  'Hypoglycemia'

        Osteoarthristis = And(And(painful_walking,swelling_joints,joint_pain), Or(hip_joint_pain,knee_pain,neck_pain,))
        if(Osteoarthristis==True):
            kbResult =  'Osteoarthristis'

        Arthritis = And(And(painful_walking,movement_stiffness,swelling_joints),Or(stiff_neck,muscle_weakness))
        if(Arthritis==True):
            kbResult =  'Arthritis'

        vertigo = And(And(unsteadiness,loss_of_balance,headache),Or(spinning_movements,nausea,vomiting))
        if(vertigo==True):
            kbResult =  'vertigo'

        Acne = And(And(scurring,pus_filled_pimples),Or(pus_filled_pimples,skin_rash))
        if(Acne==True):
            kbResult =  'Acne'

        Urinary_tract_infection = And(And(continuous_feel_of_urine,foul_smell_of_urine),Or(burning_micturition,bladder_discomfort))
        if(Urinary_tract_infection==True):
            kbResult =  'Urinary tract infection'

        Psoriasis = Or(inflammatory_nails,small_dents_in_nails,silver_like_dusting,skin_peeling)
        if(Psoriasis==True):
            kbResult =  'Psoriasis'

        Impetigo = Or(red_sore_around_nose,blister,yellow_crust_ooze)
        if(Impetigo==True):
            kbResult =  'Impetigo'

        Fungal_infection = And(Or(itching,skin_rash,nodal_skin_eruptions,shivering,dischromic_patches), Not(Or(continuous_sneezing,stomach_pain,high_fever,mild_fever)))
        if(Fungal_infection==True):
            kbResult =  'Fungal infection'


        Allergy = And(Or(continuous_sneezing,shivering,chills,watering_from_eyes),Not(Or(itching,nodal_skin_eruptions,stomach_pain,fatigue,high_fever,headache,muscle_pain)))
        if(Allergy==True):
            kbResult =  'Allergy'

        GERD = And(Or(chest_pain,cough,vomiting,ulcers_on_tongue,acidity,stomach_pain),Not(Or(shivering,continuous_sneezing,fatigue,breathlessness,headache,high_fever,joint_pain)))
        if(GERD==True):
            kbResult =  'GERD'

        Chronic_cholestasis = And(Or(yellowing_of_eyes,abdominal_pain,loss_of_appetite,nausea,yellowish_skin,vomiting,itching),Not(Or(skin_rash,nodal_skin_eruptions,shivering,joint_pain,cough,high_fever,muscle_pain)))
        if(Chronic_cholestasis==True):
            kbResult =  'Chronic cholestasis'

        Drug_Reaction = And(Or(itching,skin_rash,stomach_pain,burning_micturition,spotting_urination),Not(Or(nodal_skin_eruptions,shivering,vomiting,high_fever,headache,abdominal_pain,phlegm)))
        if(Drug_Reaction==True):
            kbResult =  'Drug Reaction'

        Peptic_ulcer_diseae = And(Or(internal_itching,passage_of_gases,abdominal_pain,loss_of_appetite,indigestion,vomiting),Not(Or(vomiting,shivering,weight_gain,high_fever,back_pain,chest_pain,stomach_pain)))
        if(Peptic_ulcer_diseae==True):
            kbResult =  'Peptic ulcer diseae'

        AIDS = And(And(extra_marital_contacts,high_fever,muscle_wasting),Not(Or(itching,shivering,headache,nausea,chest_pain)))
        if(AIDS==True):
            kbResult =  'AIDS'

        Diabetes = And(Or(increased_appetite,polyuria,excessive_hunger,obesity,blurred_and_distorted_vision,irregular_sugar_level,lethargy,restlessness,weight_loss,fatigue),Not(Or(shivering,high_fever,headache,runny_nose,loss_of_appetite)))
        if(Diabetes==True):
            kbResult =  'Diabetes'

        
        
        return render_template('output.html', say=diagnosis[0], sayAgain = kbResult)

if __name__ == "__main__":
    app.run()

 

