#import pytholog as pl
import pickle


new_kb = pl.KnowledgeBase("disease")

new_kb(["disease(malaria, cold, fever, rn)",
        "disease(dengue, fever, rash, throat)",
        "disease(jaundice, rash, aches, itching)",])
        

print(new_kb.query(pl.Expr("disease(X, cold, fever, rn)"))[0]['X'])

print(type(new_kb.query(pl.Expr("disease(X, cold, fever, rn)"))))

pickle.dump(new_kb, open("kbpickle.pkl","wb"))



