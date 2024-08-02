
from sympy import *
from sympy import And,Or,Not

def prescription(disease,age,gender,diabetes,highbp,allergy):
    age5=false
    age20=false
    age40=false
    age60=false


    if(gender=='Male'):
        male=true
        female=false
    else:
        female=true
        male=false

    if(age<5):
        age5=true
        
    elif(age<20 and age>=5):
        age20=true
        
    elif(age>=20 and age<40):
        age40=true
        
    elif(age>=40):
        age60=true


    if(diabetes==1000):
        diabetes=true
    else:
        diabetes=false

    if(highbp==1000):
        highbp=true
    else:
        highbp=false  

    if(allergy==1000):
        allergy=true  

    if(disease == Fungal_infection):

        Fluocinonide = Not(Or(age5,allergy))
        if(Fluocinonide==true):
            return 'Fluocinonide'

        Itraconazole = Not(female)
        if(Itraconazole==true):
            return 'Itraconazole'

        return'fluconazole'

    if(disease == Allergy):

        Montelukast = Not(Or(age5,highbp))
        if(Montelukast==true):
            return 'Montelukast'

        Nasacort = And(male)
        if(Nasacort==true):
            return'Nasacort'

        return 'Levocetirizine'

    if(disease == GERD):

        Dexilant = Not(Or(diabetes,age20,age5))
        if(Dexilant==true):
            return 'Dexilant'

        Prevacid = Not(Or(highbp,diabetes))
        if(Prevacid==true):
            return 'Prevacid'

        return'Prilosec'


    if(disease == Chronic_cholestasis):
        return 'Ursodeoxycholic acid'

    if(disease == Drug_Reaction):

        Corticosteroids = Not(Or(age5,diabetes,highbp))
        if(Corticosteroids==true):
            return 'Corticosteroids'

        Antihistamines = Not(Or(age60,diabetes))
        if(Antihistamines==true):
            return 'Antihistamines'

        return'diphenhydramine'   


    if(disease == Peptic_ulcer_disease):

        Protonix = Not(Or(age5,age20,age40))
        if(Protonix==true):
            return 'Protonix'

        Librax = Not(Or(male,age5))
        if(Librax==true):
            return 'Librax'

        return'Pepcid'   


    if(disease == AIDS):

        Marinol = Not(Or(male,age5,age20))
        if(Marinol==true):
            return 'Marinol'

        Dronabinol = Not(Or(female,age5,age20))
        if(Dronabinol==true):
            return 'Dronabinol'

        return'Somatropin'


    if(disease == Diabetes):

        Glucophage = Not(Or(age5,male))
        if(Glucophage==true):
            return 'Glucophage'

        Pioglitazone = Not(Or(age5,female))
        if(Pioglitazone==true):
            return 'Pioglitazone'

        return'Dulaglutide'


    if(disease == Gastroenteritis):

        Ondansetron = Not(Or(age5,age60,allergy))
        if(Ondansetron==true):
            return 'Ondansetron'

        Pantoprazole = Not(Or(age5))
        if(Pantoprazole==true):
            return 'Pantoprazole'

        return'Reglan'

    
    if(disease == Bronchial_Asthma):

        Advair_Diskus = Not(Or(age60,allergy))
        if(Advair_Diskus==true):
            return 'Advair Diskus'

        Prednisone = Not(Or(age5,age60))
        if(Prednisone==true):
            return 'Prednisone'

        return'Breo Ellipta'


    if(disease == Hypertension):

        Timoptic = Not(Or(age5))
        if(Timoptic==true):
            return 'Timoptic'

        Uptrami = Not(Or(age5,allergy))
        if(Uptrami==true):
            return 'Uptrami'

        return'Letairis'


    if(disease == Migraine):

        Excedrin = Not(Or(age60,age40,highbp))
        if(Excedrin==true):
            return 'Excedrin'

        Zonegran = Not(Or(age5,female))
        if(Zonegran==true):
            return 'Zonegran'

        return'Metoclopramide'


    if(disease == Cervical_spondylosis):

        Baclofen = Not(Or(age5,allergy))
        if(Baclofen==true):
            return 'Baclofen'

        Onabotulinumtoxin = Not(Or(age5,age20,diabetes))
        if(Onabotulinumtoxin==true):
            return 'Onabotulinumtoxin'

        return'Lioresal'

    
    if(disease == Paralysis):

        Nadolol = Not(Or(age60,age5,highbp))
        if(Nadolol==true):
            return 'Nadolol'

        Nimodipine = Not(Or(age60))
        if(Nimodipine==true):
            return 'Nimodipine'

        return'Osmotic_diuretics'



    if(disease == Jaundice):

        phenobarbital = Not(Or(age40,allergy))
        if(phenobarbital==true):
            return 'phenobarbital'

        colestipol = Not(Or(age60,diabetes,highbp))
        if(colestipol==true):
            return 'colestipol'

        return'acetaminophen'


    if(disease == Malaria):

        sulfadoxine = Not(Or(age5))
        if(sulfadoxine==true):
            return 'Pyrimethamine / sulfadoxine'

        Atovaquone = Not(Or(allergy))
        if(Atovaquone==true):
            return 'Atovaquone / proguanil'

        return'Doxycycline' 


    if(disease == Chicken_pox):

        acyclovir = Not(Or(age60,highbp))
        if(acyclovir==true):
            return 'acyclovir'

        valacyclovir = Not(Or(allergy))
        if(valacyclovir==true):
            return 'valacyclovir'

        return'famciclovir' 

    
    if(disease == Dengue):

        return'acetaminophenacetaminophen' 


    if(disease == Typhoid):

        Ciprofloxacin = Not(Or(age5,age20))
        if(Ciprofloxacin==true):
            return 'Ciprofloxacin'

        Azithromycin = Not(Or(age5))
        if(Azithromycin==true):
            return 'Azithromycin'

        return'Ceftriaxone'


    if(disease == hepatitis_A):

        return'No specific treatment'


    if(disease == Hepatitis_B):

        Tenofovir = Not(Or(age5,allergy))
        if(Tenofovir==true):
            return 'Tenofovir'

        Lamivudine = Not(Or(diabetes))
        if(Lamivudine==true):
            return 'Lamivudine'

        return'Viread'


    if(disease == Hepatitis_C):

        Ledipasvir = Not(Or(age5,age20))
        if(Ledipasvir==true):
            return 'Ledipasvir / sofosbuvir'

        Elbasvir = Not(Or(allergy,highbp))
        if(Elbasvir==true):
            return 'Elbasvir/grazoprevir'

        return'Zepatier'


    if(disease == Hepatitis_D):

        return'Pegylated interferon alpha'


    if(disease == Hepatitis_E):

        return'Ribavirin'

    

    if(disease == Alcoholic_hepatitis):

        Corticosteroids = Not(Or(age5,age20,age60,female))
        if(Corticosteroids==true):
            return 'Corticosteroids'

        return'Pentoxifylline'


    if(disease == Tuberculosis):

        Rifampin = Not(Or(age5,allergy,female))
        if(Rifampin==true):
            return 'Rifampin'

        Isoniazid = Not(Or(age60,allergy))
        if(Isoniazid==true):
            return 'Isoniazid'

        return'Rifadin'


    if(disease == Common_Cold):

        Oxymetazoline = Not(Or(age5))
        if(Oxymetazoline==true):
            return 'Oxymetazoline'

        Chlorpheniramine = Not(Or(age20,highbp))
        if(Chlorpheniramine==true):
            return 'Chlorpheniramine'

        return'Guaifenesin'


    if(disease == Pneumonia):

        Avelox = Not(Or(age60,age5,diabetes))
        if(Avelox==true):
            return 'Avelox'

        Clarithromycin = Not(Or(allergy))
        if(Clarithromycin==true):
            return 'Clarithromycin'

        return'Moxifloxacin'



    if(disease == piles):

        Proctofoam = Not(Or(age5,highbp))
        if(Proctofoam==true):
            return 'Proctofoam'

        Neulasta = Not(Or(age60,male))
        if(Neulasta==true):
            return 'Neulasta'

        return'Proctosol'


    if(disease == Heart_attack):

        Lisinopril = Not(Or(age60,highbp))
        if(Lisinopril==true):
            return 'Lisinopril'

        Clopidogrel = Not(Or(age5,age20))
        if(Clopidogrel==true):
            return 'Clopidogrel'

        return'Nitrolingual_Pumpspray'


    if(disease == Varicose_veins):

        Horse_chestnut = Not(Or(female))
        if(Horse_chestnut==true):
            return 'Horse chestnut'

        return'Polidocanol'


    if(disease == Hypothyroidism):

        levothyroxine = Not(Or(male,age60))
        if(levothyroxine==true):
            return 'levothyroxine'

        Synthroid = Not(Or(female,age60,allergy))
        if(Synthroid==true):
            return 'Synthroid'

        return'Armour Thyroid'


    if(disease == Hyperthyroidism):

        methimazole = Not(Or(allergy,diabetes))
        if(methimazole==true):
            return 'methimazole'

        return'propylithiouracil'


    if(disease == Hypoglycemia):

        Diazoxide = Not(Or(age5,allergy))
        if(Diazoxide==true):
            return 'Diazoxide'

        Proglycem = Not(Or(age5,male))
        if(Proglycem==true):
            return 'Proglycem'

        return'Insta-Glucose'


    if(disease == Osteoarthristis):

        Acetaminophen = Not(Or(age5,age20))
        if(Acetaminophen==true):
            return 'Acetaminophen'

        Duloxetine = Not(Or(age5,highbp))
        if(Duloxetine==true):
            return 'Duloxetine'

        return'Nonsteroidal anti-inflammatory drugs'


    if(disease == Arthritis):

        Nabumetone = Not(Or(age5,age20,male))
        if(Nabumetone==true):
            return 'Nabumetone'

        Meloxicam = Not(Or(age5,female))
        if(Meloxicam==true):
            return 'Meloxicam'

        return'Orthovisc'


    if(disease == vertigo):

        Dramamine_II = Not(Or(age60,diabetes))
        if(Dramamine_II==true):
            return 'Dramamine II'

        meclizine = Not(Or(age60,diabetes,highbp))
        if(meclizine==true):
            return 'meclizine'

        return'Bonine'


    if(disease == Acne):

        adapalene = Not(Or(allergy))
        if(adapalene==true):
            return 'adapalene / benzoyl peroxide'

        doxycycline = Not(Or(allergy,female))
        if(doxycycline==true):
            return 'doxycycline'

        return'isotretinoin'


    if(disease == Urinary_tract_infection):

        Fosfomycin = Not(Or(female,age5))
        if(Fosfomycin==true):
            return 'Fosfomycin'

        Cephalexin = Not(Or(male,age5,age60))
        if(Cephalexin==true):
            return 'Cephalexin'

        return'Trimethoprim/sulfamethoxazole'


    if(disease == Psoriasis):

        ustekinumab = Not(Or(male,age5,highbp))
        if(ustekinumab==true):
            return 'ustekinumab'

        Stelara = Not(Or(age5,diabetes))
        if(Stelara==true):
            return 'Stelara'

        return'adalimumab'


    if(disease == Impetigo):

        Altabax = Not(Or(diabetes,age5,age20))
        if(Altabax==true):
            return 'Altabax'

        retapamulin = Not(Or(age5,age20,allergy))
        if(retapamulin==true):
            return 'retapamulin'

        return'mupirocin'





    


    







    
    


    
    


    


    

       
