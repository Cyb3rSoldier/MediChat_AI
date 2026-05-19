import re
import uuid
from datetime import datetime

# =====================================================================
# 1. CORE DATASET STORAGE
# =====================================================================
MEDICHAT_DATASET = {
    "version": "1.0.0",
    "last_updated": "2026-05-17",
    "diseases": [
        {
            "id": "D001",
            "name": "Influenza (Flu)",
            "symptoms": ["fever", "chills", "muscle aches", "headache", "sore throat", "dry cough", "fatigue", "runny nose"],
            "description": "Influenza is a highly contagious viral respiratory illness caused by influenza A or B viruses.",
            "doctors": [{"specialty": "General Practitioner (GP)", "reason": "First point of contact for diagnosis and antivirals"}],
            "behaviors": ["Rest at home", "Drink fluids", "Take paracetamol", "Seek emergency care if breathing is difficult"],
            "severity": "moderate",
            "urgency": "soon",
            "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
        },
        {
            "id": "D002",
            "name": "Type 2 Diabetes Mellitus",
            "symptoms": ["increased thirst", "frequent urination", "fatigue", "blurred vision", "slow healing wounds", "unexplained weight loss"],
            "description": "Type 2 diabetes is a chronic metabolic disorder where the body becomes resistant to insulin.",
            "doctors": [{"specialty": "Endocrinologist", "reason": "Primary specialist for blood sugar control"}],
            "behaviors": ["Adopt a low-glycemic diet", "Exercise 150 mins/week", "Inspect feet daily"],
            "severity": "moderate",
            "urgency": "soon",
            "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
        },
        {
            "id": "D003",
            "name": "Hypertension (High Blood Pressure)",
            "symptoms": ["headache", "dizziness", "blurred vision", "chest pain", "shortness of breath", "palpitations"],
            "description": "Hypertension is a condition where the force of blood against artery walls is persistently elevated.",
            "doctors": [{"specialty": "Cardiologist", "reason": "Manages cardiovascular complications"}],
            "behaviors": ["Reduce sodium intake", "Follow the DASH diet", "Monitor blood pressure at home"],
            "severity": "moderate",
            "urgency": "soon",
            "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
        },
        {
            "id": "D004",
            "name": "Migraine",
            "symptoms": ["severe headache", "nausea", "vomiting", "sensitivity to light", "sensitivity to sound", "throbbing pain", "headache"],
            "description": "Migraine is a complex neurological condition characterized by recurrent episodes of severe headache.",
            "doctors": [{"specialty": "Neurologist", "reason": "Diagnosis and management of chronic migraine"}],
            "behaviors": ["Keep a migraine diary", "Avoid known triggers", "Rest in a dark quiet room"],
            "severity": "moderate",
            "urgency": "soon",
            "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
        },
        {
            "id": "D005",
            "name": "Gastroesophageal Reflux Disease (GERD)",
            "symptoms": ["heartburn", "acid reflux", "chest pain", "difficulty swallowing", "sour taste in mouth", "bloating"],
            "description": "GERD is a chronic digestive disorder where stomach acid or bile flows back into the esophagus.",
            "doctors": [{"specialty": "Gastroenterologist", "reason": "For endoscopy and complication management"}],
            "behaviors": ["Eat smaller meals", "Do not lie down within 3 hours of eating", "Elevate bed head"],
            "severity": "mild",
            "urgency": "routine",
            "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
        },
        {
    "id": "D006",
    "name": "Asthma",
    "symptoms": ["shortness of breath", "dry cough", "chest pain", "fatigue"],
    "description": "A chronic inflammatory airway disease causing recurrent breathing difficulties.",
    "doctors": [{"specialty": "Pulmonologist", "reason": "Manages airway inflammation and inhaler plans"}],
    "behaviors": ["Use prescribed inhaler", "Avoid smoke and dust", "Keep an asthma action plan"],
    "severity": "moderate", "urgency": "soon",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D007",
    "name": "Anemia (Iron Deficiency)",
    "symptoms": ["fatigue", "dizziness", "shortness of breath", "headache", "palpitations"],
    "description": "A condition where lack of iron reduces red blood cell production, limiting oxygen transport.",
    "doctors": [{"specialty": "Hematologist", "reason": "Diagnoses blood disorders and prescribes iron therapy"}],
    "behaviors": ["Eat iron-rich foods (red meat, spinach)", "Take prescribed iron supplements", "Avoid tea/coffee with meals"],
    "severity": "mild", "urgency": "routine",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D008",
    "name": "Urinary Tract Infection (UTI)",
    "symptoms": ["frequent urination", "burning urination", "pelvic pain", "fatigue", "fever"],
    "description": "A bacterial infection affecting any part of the urinary system, most commonly the bladder.",
    "doctors": [{"specialty": "Urologist", "reason": "Treats recurrent or complicated urinary infections"}],
    "behaviors": ["Drink plenty of water", "Complete the full antibiotic course", "Avoid holding urine"],
    "severity": "mild", "urgency": "soon",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D009",
    "name": "Allergic Rhinitis (Hay Fever)",
    "symptoms": ["sneezing", "runny nose", "itchy eyes", "fatigue", "headache"],
    "description": "An allergic response to airborne allergens like pollen, dust mites, or pet dander causing nasal and eye inflammation.",
    "doctors": [
        {"specialty": "Allergist", "reason": "Performs allergy testing and immunotherapy"},
        {"specialty": "ENT Specialist", "reason": "Manages chronic nasal symptoms"}
    ],
    "behaviors": ["Avoid known allergens", "Use antihistamines as prescribed", "Keep windows closed during high pollen season", "Shower after outdoor exposure"],
    "severity": "mild", "urgency": "routine",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D010",
    "name": "Rheumatoid Arthritis",
    "symptoms": ["joint pain", "swollen joints", "fatigue", "fever", "loss of appetite", "morning stiffness"],
    "description": "An autoimmune disease where the immune system mistakenly attacks joint linings, causing chronic inflammation and deformity.",
    "doctors": [
        {"specialty": "Rheumatologist", "reason": "Primary specialist for autoimmune joint disease management"},
        {"specialty": "Physical Therapist", "reason": "Maintains joint function and mobility"}
    ],
    "behaviors": ["Take prescribed disease-modifying drugs consistently", "Do low-impact exercises like swimming", "Apply warm compresses to stiff joints", "Never stop medication without consulting your doctor"],
    "severity": "moderate", "urgency": "soon",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D011",
    "name": "Hypothyroidism (Underactive Thyroid)",
    "symptoms": ["fatigue", "weight gain", "dry skin", "hair loss", "depression", "cold hands", "constipation", "memory loss"],
    "description": "A condition where the thyroid gland does not produce enough thyroid hormone, slowing down the body's metabolism.",
    "doctors": [
        {"specialty": "Endocrinologist", "reason": "Manages thyroid hormone levels and medication dosing"}
    ],
    "behaviors": ["Take levothyroxine at the same time daily", "Avoid taking it with calcium or iron supplements", "Get TSH blood tests every 6 months", "Eat selenium-rich foods like Brazil nuts"],
    "severity": "mild", "urgency": "routine",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D012",
    "name": "Hyperthyroidism (Overactive Thyroid)",
    "symptoms": ["weight loss", "palpitations", "anxiety", "excessive sweating", "fatigue", "tremors", "insomnia"],
    "description": "A condition where the thyroid gland produces excess hormones, accelerating the body's metabolic processes.",
    "doctors": [
        {"specialty": "Endocrinologist", "reason": "Prescribes antithyroid drugs or radioiodine therapy"}
    ],
    "behaviors": ["Avoid iodine-rich foods like seaweed", "Limit caffeine", "Get regular thyroid function tests", "Monitor heart rate daily"],
    "severity": "moderate", "urgency": "soon",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D013",
    "name": "Irritable Bowel Syndrome (IBS)",
    "symptoms": ["abdominal pain", "bloating", "diarrhea", "constipation", "fatigue", "nausea"],
    "description": "A functional gastrointestinal disorder causing chronic abdominal discomfort without underlying structural damage.",
    "doctors": [
        {"specialty": "Gastroenterologist", "reason": "Diagnoses and manages functional bowel conditions"}
    ],
    "behaviors": ["Follow a low-FODMAP diet", "Track food triggers in a diary", "Manage stress through mindfulness", "Stay hydrated"],
    "severity": "mild", "urgency": "routine",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D014",
    "name": "Peptic Ulcer Disease",
    "symptoms": ["abdominal pain", "nausea", "vomiting", "bloating", "loss of appetite", "heartburn"],
    "description": "Open sores that develop on the inner lining of the stomach or upper small intestine, often caused by H. pylori bacteria or NSAIDs.",
    "doctors": [
        {"specialty": "Gastroenterologist", "reason": "Performs endoscopy and manages H. pylori eradication therapy"}
    ],
    "behaviors": ["Avoid NSAIDs like ibuprofen", "Stop smoking", "Eat smaller meals frequently", "Avoid spicy and acidic foods"],
    "severity": "moderate", "urgency": "soon",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D015",
    "name": "Chronic Kidney Disease (CKD)",
    "symptoms": ["fatigue", "swollen joints", "shortness of breath", "frequent urination", "nausea", "loss of appetite", "headache", "dark urine"],
    "description": "A progressive loss of kidney function over months or years, affecting the body's ability to filter waste from blood.",
    "doctors": [
        {"specialty": "Nephrologist", "reason": "Manages kidney function, dialysis planning, and transplant referral"}
    ],
    "behaviors": ["Follow a low-sodium low-protein diet", "Monitor blood pressure daily", "Avoid NSAIDs completely", "Attend all kidney function tests"],
    "severity": "severe", "urgency": "urgent",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D016",
    "name": "Liver Cirrhosis",
    "symptoms": ["fatigue", "yellowing skin", "abdominal pain", "nausea", "loss of appetite", "dark urine", "pale stools", "swollen joints"],
    "description": "Late-stage liver scarring caused by liver diseases like hepatitis and chronic alcohol use, impairing liver function.",
    "doctors": [
        {"specialty": "Hepatologist", "reason": "Specialist for advanced liver disease and transplant evaluation"},
        {"specialty": "Gastroenterologist", "reason": "Manages complications like varices and ascites"}
    ],
    "behaviors": ["Completely abstain from alcohol", "Follow a low-sodium diet", "Avoid raw seafood", "Get vaccinated for Hepatitis A and B"],
    "severity": "severe", "urgency": "urgent",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D017",
    "name": "Depression (Major Depressive Disorder)",
    "symptoms": ["depression", "fatigue", "insomnia", "loss of appetite", "difficulty concentrating", "headache", "anxiety"],
    "description": "A serious mood disorder causing persistent feelings of sadness, emptiness, and loss of interest lasting at least two weeks.",
    "doctors": [
        {"specialty": "Psychiatrist", "reason": "Prescribes antidepressants and manages medication"},
        {"specialty": "Psychologist", "reason": "Provides cognitive behavioral therapy (CBT)"}
    ],
    "behaviors": ["Seek professional help immediately", "Maintain a daily routine", "Exercise at least 30 minutes daily", "Avoid alcohol and isolation", "Tell a trusted person how you feel"],
    "severity": "moderate", "urgency": "soon",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D018",
    "name": "Generalized Anxiety Disorder (GAD)",
    "symptoms": ["anxiety", "insomnia", "fatigue", "headache", "difficulty concentrating", "muscle aches", "palpitations"],
    "description": "A mental health disorder characterized by persistent, excessive, and uncontrollable worry about everyday situations.",
    "doctors": [
        {"specialty": "Psychiatrist", "reason": "Evaluates and prescribes appropriate anxiolytic medications"},
        {"specialty": "Psychologist", "reason": "Delivers cognitive behavioral therapy for anxiety management"}
    ],
    "behaviors": ["Practice deep breathing and mindfulness daily", "Limit caffeine intake", "Maintain consistent sleep schedule", "Avoid avoidance behaviors"],
    "severity": "moderate", "urgency": "soon",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D019",
    "name": "Pneumonia",
    "symptoms": ["fever", "chills", "dry cough", "shortness of breath", "chest pain", "fatigue", "nausea"],
    "description": "An infection that inflames the air sacs in one or both lungs, which may fill with fluid or pus.",
    "doctors": [
        {"specialty": "Pulmonologist", "reason": "Manages severe or recurrent lung infections"},
        {"specialty": "General Practitioner (GP)", "reason": "Prescribes antibiotics for community-acquired pneumonia"}
    ],
    "behaviors": ["Complete the full antibiotic or antiviral course", "Rest and stay hydrated", "Use a humidifier", "Seek emergency care if oxygen levels drop"],
    "severity": "severe", "urgency": "urgent",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D020",
    "name": "Tuberculosis (TB)",
    "symptoms": ["dry cough", "night sweats", "fever", "unexplained weight loss", "fatigue", "chest pain", "loss of appetite"],
    "description": "A serious bacterial infection caused by Mycobacterium tuberculosis, primarily affecting the lungs but can spread to other organs.",
    "doctors": [
        {"specialty": "Infectious Disease Specialist", "reason": "Manages multi-drug TB treatment regimens"},
        {"specialty": "Pulmonologist", "reason": "Monitors lung damage and respiratory function"}
    ],
    "behaviors": ["Never miss a dose of TB medication", "Cover mouth when coughing", "Ensure good ventilation at home", "Notify close contacts for screening"],
    "severity": "severe", "urgency": "urgent",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D021",
    "name": "Dengue Fever",
    "symptoms": ["fever", "severe headache", "muscle aches", "joint pain", "nausea", "vomiting", "fatigue", "skin rash"],
    "description": "A mosquito-borne viral disease causing high fever and severe flu-like symptoms, common in tropical regions.",
    "doctors": [
        {"specialty": "Infectious Disease Specialist", "reason": "Monitors for dengue hemorrhagic fever complications"},
        {"specialty": "General Practitioner (GP)", "reason": "Initial diagnosis and supportive care"}
    ],
    "behaviors": ["Rest and drink plenty of oral rehydration fluids", "Take paracetamol only — never aspirin or ibuprofen", "Use mosquito nets and repellents", "Monitor platelet count daily if hospitalized"],
    "severity": "severe", "urgency": "urgent",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D022",
    "name": "Malaria",
    "symptoms": ["fever", "chills", "headache", "nausea", "vomiting", "muscle aches", "fatigue", "sweating"],
    "description": "A life-threatening parasitic disease transmitted by infected Anopheles mosquitoes, causing cyclical fever episodes.",
    "doctors": [
        {"specialty": "Infectious Disease Specialist", "reason": "Prescribes antimalarial drugs and manages complications"},
        {"specialty": "General Practitioner (GP)", "reason": "Rapid diagnostic testing and initial treatment"}
    ],
    "behaviors": ["Complete the full antimalarial medication course", "Sleep under insecticide-treated nets", "Use mosquito repellents containing DEET", "Seek emergency care for confusion or seizures"],
    "severity": "severe", "urgency": "urgent",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D023",
    "name": "Osteoporosis",
    "symptoms": ["back pain", "joint pain", "fatigue", "loss of height", "bone fractures"],
    "description": "A condition where bones become weak and brittle due to reduced bone density, increasing fracture risk significantly.",
    "doctors": [
        {"specialty": "Rheumatologist", "reason": "Manages bone density treatment and bisphosphonate therapy"},
        {"specialty": "Orthopedic Surgeon", "reason": "Treats fractures resulting from bone weakness"}
    ],
    "behaviors": ["Take calcium and vitamin D supplements daily", "Do weight-bearing exercises like walking", "Avoid smoking and excess alcohol", "Remove fall hazards at home"],
    "severity": "moderate", "urgency": "routine",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D024",
    "name": "Eczema (Atopic Dermatitis)",
    "symptoms": ["skin rash", "dry skin", "itchy eyes", "fatigue", "burning sensation"],
    "description": "A chronic inflammatory skin condition causing itchy, red, and cracked skin, often linked to allergies and asthma.",
    "doctors": [
        {"specialty": "Dermatologist", "reason": "Prescribes topical corticosteroids and biologic treatments"},
        {"specialty": "Allergist", "reason": "Identifies food and environmental triggers"}
    ],
    "behaviors": ["Moisturize skin immediately after bathing", "Avoid harsh soaps and detergents", "Wear soft cotton clothing", "Identify and avoid personal triggers"],
    "severity": "mild", "urgency": "routine",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D025",
    "name": "Psoriasis",
    "symptoms": ["skin rash", "dry skin", "joint pain", "burning sensation", "fatigue"],
    "description": "A chronic autoimmune skin condition causing rapid buildup of skin cells, resulting in scaling, inflammation, and red patches.",
    "doctors": [
        {"specialty": "Dermatologist", "reason": "Manages topical, light, and biologic therapies"},
        {"specialty": "Rheumatologist", "reason": "Treats psoriatic arthritis if joints are involved"}
    ],
    "behaviors": ["Keep skin well moisturized", "Avoid skin injuries and infections", "Manage stress effectively", "Avoid smoking and alcohol"],
    "severity": "moderate", "urgency": "routine",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D026",
    "name": "Polycystic Ovary Syndrome (PCOS)",
    "symptoms": ["irregular periods", "weight gain", "hair loss", "fatigue", "mood swings", "blurred vision", "excessive sweating"],
    "description": "A hormonal disorder in women causing enlarged ovaries with small cysts, irregular periods, and excess androgen levels.",
    "doctors": [
        {"specialty": "Gynecologist", "reason": "Primary management of menstrual and reproductive symptoms"},
        {"specialty": "Endocrinologist", "reason": "Manages insulin resistance and hormonal imbalance"}
    ],
    "behaviors": ["Maintain a healthy weight through low-GI diet", "Exercise regularly to improve insulin sensitivity", "Track menstrual cycles", "Discuss fertility options with your doctor"],
    "severity": "moderate", "urgency": "soon",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D027",
    "name": "Endometriosis",
    "symptoms": ["painful periods", "pelvic pain", "fatigue", "nausea", "back pain", "irregular periods"],
    "description": "A condition where tissue similar to the uterine lining grows outside the uterus, causing chronic pelvic pain and fertility issues.",
    "doctors": [
        {"specialty": "Gynecologist", "reason": "Diagnoses via laparoscopy and manages hormonal treatment"},
        {"specialty": "Pain Management Specialist", "reason": "Addresses chronic pelvic pain"}
    ],
    "behaviors": ["Use prescribed hormonal therapy consistently", "Apply heat pads for cramp relief", "Track pain patterns in a diary", "Discuss surgical options if medication fails"],
    "severity": "moderate", "urgency": "soon",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D028",
    "name": "Chronic Obstructive Pulmonary Disease (COPD)",
    "symptoms": ["shortness of breath", "dry cough", "wheezing", "fatigue", "chest pain", "frequent infections"],
    "description": "A chronic inflammatory lung disease that causes obstructed airflow, primarily caused by long-term exposure to irritants like cigarette smoke.",
    "doctors": [
        {"specialty": "Pulmonologist", "reason": "Manages bronchodilator therapy and oxygen supplementation"}
    ],
    "behaviors": ["Stop smoking immediately", "Use prescribed inhalers correctly", "Get annual flu and pneumonia vaccines", "Practice breathing exercises daily"],
    "severity": "severe", "urgency": "urgent",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D029",
    "name": "Heart Failure",
    "symptoms": ["shortness of breath", "fatigue", "chest pain", "palpitations", "swollen joints", "dizziness", "loss of appetite"],
    "description": "A chronic condition where the heart muscle does not pump blood as effectively as it should, causing fluid buildup in the lungs and body.",
    "doctors": [
        {"specialty": "Cardiologist", "reason": "Manages heart function, diuretics, and device therapy"}
    ],
    "behaviors": ["Weigh yourself every morning — report 2kg gain in 2 days", "Restrict salt to under 2g per day", "Take all heart medications as prescribed", "Seek emergency care for sudden breathlessness"],
    "severity": "severe", "urgency": "urgent",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D030",
    "name": "Stroke (Cerebrovascular Accident)",
    "symptoms": ["severe headache", "dizziness", "blurred vision", "numbness", "difficulty concentrating", "vomiting"],
    "description": "A medical emergency where blood supply to part of the brain is cut off, causing brain cells to die within minutes.",
    "doctors": [
        {"specialty": "Neurologist", "reason": "Manages acute stroke treatment and rehabilitation"},
        {"specialty": "Emergency Medicine Specialist", "reason": "Immediate clot-busting or surgical intervention"}
    ],
    "behaviors": ["Call emergency services immediately — FAST: Face drooping, Arm weakness, Speech difficulty, Time to call", "Do not give food or water", "Note the exact time symptoms started", "Begin rehabilitation as early as possible"],
    "severity": "severe", "urgency": "urgent",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D031",
    "name": "Alzheimer's Disease",
    "symptoms": ["memory loss", "difficulty concentrating", "mood swings", "depression", "fatigue", "insomnia"],
    "description": "A progressive neurodegenerative disease that destroys memory and cognitive function, the most common cause of dementia.",
    "doctors": [
        {"specialty": "Neurologist", "reason": "Diagnoses and manages cognitive decline medications"},
        {"specialty": "Geriatrician", "reason": "Provides holistic care for elderly patients with dementia"}
    ],
    "behaviors": ["Engage in mentally stimulating activities daily", "Establish consistent daily routines", "Ensure home safety modifications", "Arrange caregiver support networks"],
    "severity": "severe", "urgency": "soon",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D032",
    "name": "Parkinson's Disease",
    "symptoms": ["tremors", "muscle aches", "fatigue", "depression", "insomnia", "difficulty concentrating", "dizziness"],
    "description": "A progressive nervous system disorder affecting movement, characterized by tremors, stiffness, and slowing of movement.",
    "doctors": [
        {"specialty": "Neurologist", "reason": "Manages levodopa therapy and movement disorder treatment"},
        {"specialty": "Physical Therapist", "reason": "Maintains mobility and balance through targeted exercises"}
    ],
    "behaviors": ["Take medications at exactly the same time daily", "Exercise consistently — boxing and dancing shown to help", "Remove fall hazards at home", "Use assistive devices as needed"],
    "severity": "severe", "urgency": "soon",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D033",
    "name": "Otitis Media (Ear Infection)",
    "symptoms": ["ear pain", "fever", "headache", "hearing loss", "nausea", "fatigue"],
    "description": "An infection of the middle ear, most commonly caused by bacteria or viruses, frequently occurring after a cold or respiratory infection.",
    "doctors": [
        {"specialty": "ENT Specialist", "reason": "Manages recurrent ear infections and hearing evaluation"},
        {"specialty": "General Practitioner (GP)", "reason": "Prescribes antibiotics for bacterial ear infections"}
    ],
    "behaviors": ["Complete antibiotic course if prescribed", "Apply warm compress to the ear for pain relief", "Do not insert objects into the ear", "Follow up if symptoms persist beyond 3 days"],
    "severity": "mild", "urgency": "soon",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D034",
    "name": "Conjunctivitis (Pink Eye)",
    "symptoms": ["itchy eyes", "eye pain", "headache", "sensitivity to light", "runny nose", "fever"],
    "description": "An inflammation or infection of the conjunctiva, the transparent membrane lining the eyelid, causing redness and discharge.",
    "doctors": [
        {"specialty": "Ophthalmologist", "reason": "Distinguishes bacterial, viral, and allergic types and prescribes appropriate drops"}
    ],
    "behaviors": ["Wash hands frequently", "Do not touch or rub your eyes", "Do not share towels or pillowcases", "Remove contact lenses until fully healed"],
    "severity": "mild", "urgency": "routine",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
},
{
    "id": "D035",
    "name": "Colorectal Cancer (Early Warning Signs)",
    "symptoms": ["rectal bleeding", "abdominal pain", "constipation", "diarrhea", "unexplained weight loss", "fatigue", "loss of appetite"],
    "description": "Cancer of the colon or rectum — early detection through screening significantly improves survival rates.",
    "doctors": [
        {"specialty": "Oncologist", "reason": "Manages chemotherapy and cancer treatment planning"},
        {"specialty": "Gastroenterologist", "reason": "Performs colonoscopy for diagnosis and polyp removal"},
        {"specialty": "Colorectal Surgeon", "reason": "Performs surgical resection of tumors"}
    ],
    "behaviors": ["Schedule a colonoscopy immediately if over 45 or symptomatic", "Adopt a high-fiber low-red-meat diet", "Stop smoking and limit alcohol", "Report any blood in stool to a doctor without delay"],
    "severity": "severe", "urgency": "urgent",
    "disclaimer": "This information is for educational purposes only. Consult a licensed physician."
}
    ]
}

SYMPTOM_VOCABULARY = {
    "fever": ["high temperature", "pyrexia", "feverish", "body hot", "cold"],
    "chills": ["shivering", "cold flashes"],
    "muscle aches": ["body aches", "muscle pain", "sore muscles"],
    "headache": ["head pain", "migraine", "cephalalgia"],
    "sore throat": ["throat pain", "throat irritation", "pain swallowing"],
    "dry cough": ["hacking cough", "coughing no mucus"],
    "fatigue": ["tiredness", "weakness", "lethargy", "exhaustion"],
    "runny nose": ["nasal discharge", "sneezing"],
    "increased thirst": ["polydipsia", "always thirsty"],
    "frequent urination": ["polyuria", "peeing a lot"],
    "blurred vision": ["blurry eyes", "impaired eyesight"],
    "slow healing wounds": ["cuts not healing"],
    "unexplained weight loss": ["losing weight fast"],
    "dizziness": ["lightheadedness", "giddiness", "spinning head"],
    "chest pain": ["angina", "heart pain", "tight chest"],
    "shortness of breath": ["dyspnea", "breathlessness", "difficulty breathing"],
    "palpitations": ["racing heart", "pounding chest"],
    "nausea": ["feeling sick", "queasiness"],
    "vomiting": ["throwing up", "emesis"],
    "sensitivity to light": ["photophobia", "eyes hurt in light"],
    "sensitivity to sound": ["phonophobia", "loud noises hurt"],
    "throbbing pain": ["pulsating pain", "pounding head"],
    "heartburn": ["burning chest", "acid burn"],
    "acid reflux": ["sour burps", "stomach acid coming up"],
    "difficulty swallowing": ["dysphagia"],
    "sour taste in mouth": ["acid taste"],
    "bloating": ["swollen stomach", "gas pain"],
    "burning urination": ["painful urination", "dysuria", "stinging when peeing"],
"pelvic pain": ["lower abdomen pain", "bladder pain", "groin pain"],
"sneezing": ["constant sneezing", "sneezing fits", "achoo"],
"itchy eyes": ["eye irritation", "watery eyes", "red eyes"],
"skin rash": ["redness on skin", "hives", "skin irritation", "itchy skin", "rash"],
"joint pain": ["arthralgia", "aching joints", "stiff joints", "joint swelling"],
"night sweats": ["sweating at night", "waking up sweating", "nocturnal sweating"],
"wheezing": ["whistling breath", "noisy breathing", "breathing sounds"],
"back pain": ["lower back pain", "spine pain", "backache", "lumbar pain"],
"abdominal pain": ["stomach pain", "belly pain", "stomach cramps", "tummy ache"],
"diarrhea": ["loose stools", "watery stool", "frequent bowel movements"],
"constipation": ["hard stool", "no bowel movement", "difficulty passing stool"],
"loss of appetite": ["not hungry", "no appetite", "dont want to eat"],
"weight gain": ["gaining weight", "getting fat", "obesity"],
"burning urination": ["painful urination", "dysuria", "stinging when peeing"],
"pelvic pain": ["lower abdomen pain", "bladder pain", "groin pain"],
"swollen lymph nodes": ["swollen glands", "lumps in neck", "neck swelling"],
"memory loss": ["forgetfulness", "cant remember", "memory problems", "confusion"],
"tremors": ["shaking hands", "body trembling", "shaking"],
"yellowing skin": ["jaundice", "yellow eyes", "yellow skin"],
"dark urine": ["brown urine", "tea colored urine", "dark pee"],
"pale stools": ["white stool", "clay colored stool", "light colored poo"],
"hair loss": ["balding", "thinning hair", "losing hair", "alopecia"],
"dry skin": ["flaky skin", "peeling skin", "rough skin"],
"cold hands": ["cold feet", "numb hands", "poor circulation fingers"],
"ear pain": ["earache", "pain in ear", "ear pressure"],
"hearing loss": ["cant hear well", "muffled hearing", "hard of hearing"],
"eye pain": ["pain behind eyes", "sore eyes", "eye pressure"],
"painful periods": ["menstrual cramps", "period pain", "dysmenorrhea"],
"irregular periods": ["missed period", "late period", "menstrual irregularity"],
"mood swings": ["emotional changes", "irritability", "sudden anger", "crying spells"],
"anxiety": ["nervousness", "panic", "feeling anxious", "worry", "restlessness"],
"depression": ["feeling sad", "hopelessness", "low mood", "feeling empty"],
"insomnia": ["cant sleep", "trouble sleeping", "sleeplessness", "waking at night"],
"excessive thirst": ["always thirsty", "polydipsia", "drinking too much water"],
"numbness": ["tingling", "pins and needles", "numb limbs", "loss of sensation"],
"swollen joints": ["puffy joints", "inflamed joints", "swelling in knees"],
"burning sensation": ["burning feeling", "burning skin", "hot sensation"],
"rectal bleeding": ["blood in stool", "bloody stool", "bleeding from rectum"],
"frequent infections": ["getting sick often", "repeated infections", "low immunity"],
"excessive sweating": ["hyperhidrosis", "sweating too much", "profuse sweating"],
"difficulty concentrating": ["brain fog", "cant focus", "loss of concentration"]
}

class NLPTextProcessor:
    @staticmethod
    def normalize(text):
        if not text:
            return ""
        text = text.lower()
        contractions = {"i've": "i have", "i'm": "i am", "don't": "do not", "can't": "cannot"}
        for key, val in contractions.items():
            text = text.replace(key, val)
        text = re.sub(re.compile(r'[^\w\s]'), '', text)
        return " ".join(text.split()).strip()

class SymptomExtractorBFS:
    def __init__(self, threshold=0.65):
        self.threshold = threshold

    def extract(self, raw_input):
        normalized = NLPTextProcessor.normalize(raw_input)
        extracted = []
        for symptom, aliases in SYMPTOM_VOCABULARY.items():
            if symptom in normalized:
                if symptom not in extracted:
                    extracted.append(symptom)
                continue
            if aliases:
                for alias in aliases:
                    if alias in normalized:
                        if symptom not in extracted:
                            extracted.append(symptom)
                        break
        return extracted

class DiseaseMatcher:
    @staticmethod
    def find_matches(extracted_symptoms):
        if not extracted_symptoms:
            return []
        candidates = []
        user_symptoms_set = set(extracted_symptoms)
        for disease in MEDICHAT_DATASET["diseases"]:
            disease_symptoms_set = set(disease["symptoms"])
            matched = user_symptoms_set.intersection(disease_symptoms_set)
            if matched:
                match_rate = len(matched) / len(user_symptoms_set)
                confidence = len(matched) / len(disease_symptoms_set)
                candidates.append({
                    "disease": disease,
                    "match_rate": round(match_rate, 4),
                    "confidence": round(confidence, 4),
                    "total_symptoms": len(disease_symptoms_set)
                })
        candidates.sort(key=lambda x: (x["match_rate"], -x["total_symptoms"]), reverse=True)
        return candidates

class SessionStoreManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self):
        s_id = str(uuid.uuid4())
        self.sessions[s_id] = {
            "id": s_id,
            "title": "New Consultation",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "messages": []
        }
        return s_id

    def get_all_sessions(self):
        return sorted(list(self.sessions.values()), key=lambda x: x["created_at"], reverse=True)

    def delete_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]
            return True
        return False

    def add_message(self, session_id, sender, text, diagnostic_payload=None):
        if session_id not in self.sessions:
            return
        if sender == "user" and len(self.sessions[session_id]["messages"]) == 0:
            truncated_title = text[:25] + "..." if len(text) > 25 else text
            self.sessions[session_id]["title"] = truncated_title

        message_node = {
            "sender": sender,
            "text": text,
            "timestamp": datetime.now().strftime("%I:%M %p"),
            "data": diagnostic_payload
        }
        self.sessions[session_id]["messages"].append(message_node)
        return message_node