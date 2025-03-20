import streamlit as st
st.set_page_config(page_title="Language Learning Platform", layout="wide")

st.markdown(
    """
    <style>
    .top-nav-bar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #FFFFFF;
        padding: 15px 20px;
        border-bottom: 3px solid #CCCCCC;
        z-index: 1000;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .nav-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .test-button {
        background: linear-gradient(45deg, #1E90FF, #00BFFF);
        color: #FFFFFF;
        font-size: 18px;
        font-weight: bold;
        padding: 10px 25px;
        border: none;
        border-radius: 30px;
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease, background-color 0.3s ease;
    }
    .test-button:hover {
        background: linear-gradient(45deg, #0078D7, #0056B3);
        transform: scale(1.1);
    }
    .welcome-section {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 8px 10px rgba(0, 0, 0, 0.1);
        animation: fadeIn 1.5s;
    }
    a:link, a:visited {
    color: white;
    background-color: transparent;
    text-decoration: none;
}

a:hover, a:active {
    color: #e9ba8c;
    background-color: transparent;
    text-decoration: none;
}

/* Center the footer content */
    .footer {
        background-color: #06402b;
        color: #ffffff;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        width: 100%;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        margin-top: auto; /* Pushes footer to bottom */
    }
    .footer a {
        color: #ffffff;
        text-decoration: none;
        padding: 0 15px;
        font-size: 20px;
    }
    .footer a:hover {
        color: #e9ba8c;
    }
    .footer .social-icons {
        margin-top: 10px;
    }
    .footer .social-icons i {
        font-size: 30px;
        padding: 10px;
        transition: color 0.3s ease;
    }
    .footer .social-icons i:hover {
        color: #e9ba8c;
    }
@keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

vowel_systems = {
    "Mexican Spanish": {
        "i": ("High", "Front", "Unrounded"),
        "e": ("Mid", "Front", "Unrounded"),
        "a": ("Low", "Central", "Unrounded"),
        "o": ("Mid", "Back", "Rounded"),
        "u": ("High", "Back", "Rounded")
    },
    "Seoul Korean": {
        "i": ("High", "Front", "Unrounded"),
        "e̞": ("Mid", "Front", "Unrounded"),
        "ɯ": ("High", "Back", "Unrounded"),
        "o": ("High", "Back", "Rounded"),
        "u": ("High", "Back", "Rounded"),
        "ʌ̹": ("Mid", "Back", "Rounded"),
        "ɐ": ("Low", "Central", "Unrounded")
    },
    "French Oral": {
        "i": ("High", "Front", "Unrounded"),
        "e": ("Mid", "Front", "Unrounded"),
        "a": ("Low", "Front", "Unrounded"),
        "o": ("Mid", "Back", "Unrounded"),
        "u": ("High", "Back", "Unrounded"),
        "ə": ("Mid", "Central", "Unrounded"),
        "ɛ": ("Mid", "Front", "Unrounded"),
        "y": ("High", "Front", "Rounded"),
        "ø": ("Mid", "Front", "Rounded"),
        "œ": ("Mid", "Front", "Rounded"),
        "ɔ": ("Mid", "Back", "Unrounded"),
        "ɑ": ("Low", "Back", "Unrounded")
    },
    "Modern Hebrew": {
        "i": ("High", "Front", "Unrounded"),
        "e": ("Mid", "Front", "Unrounded"),
        "a": ("Low", "Central", "Unrounded"),
        "o": ("Mid", "Back", "Rounded"),
        "u": ("High", "Back", "Rounded")
    },
    "Bengali Oral": {
        "i": ("High", "Front", "Unrounded"),
        "e": ("Mid", "Front", "Unrounded"),
        "a": ("Low", "Central", "Unrounded"),
        "o": ("Mid", "Back", "Rounded"),
        "u": ("High", "Back", "Rounded"),
        "ɔ": ("Mid", "Back", "Rounded"),
        "æ~ɛ": ("Mid", "Front", "Unrounded")
    },
    "Hindi": {
        "iː": ("High", "Front", "Unrounded"),
        "eː": ("Mid", "Front", "Unrounded"),
        "ɛː": ("Low", "Front", "Unrounded"),
        "æː": ("Mid", "Front", "Unrounded"),
        "ɪ": ("High", "Front", "Unrounded"),
        "ə": ("Mid", "Central", "Unrounded"),
        "aː": ("Mid", "Central", "Unrounded"),
        "ʊ": ("Mid", "Back", "Rounded"),
        "uː": ("Mid", "Back", "Rounded"),
        "oː": ("Mid", "Back", "Rounded"),
        "ɔː": ("Mid", "Back", "Rounded")
    },
    "Italian": {
        "i": ("High", "Front", "Unrounded"),
        "e": ("Mid", "Front", "Unrounded"),
        "a": ("Low", "Central", "N/A"),
        "o": ("Mid", "Back", "Rounded"),
        "u": ("High", "Back", "Rounded"),
        "ɔ": ("Mid", "Back", "Rounded"),
        "ɛ": ("Mid", "Front", "Unrounded")
    },
    "Japanese": {
        "i": ("High", "Front", "Unrounded"),
        "e": ("Mid", "Front", "Unrounded"),
        "a": ("Low", "Central", "Unrounded"),
        "o": ("Mid", "Back", "Rounded"),
        "ɯ": ("High", "Back", "Unrounded")
    }
}

def get_language_concentration(vowel_system):
    backness_counts = {"Front": 0, "Central": 0, "Back": 0}
    for _, (_, backness, _) in vowel_system.items():
        backness_counts[backness] += 1
    max_backness = max(backness_counts, key=backness_counts.get)
    return max_backness

language_concentrations = {}
for language, vowels in vowel_systems.items():
    concentration = get_language_concentration(vowels)
    language_concentrations[language] = concentration

def recommend_languages_for_disorder(disorder, language_concentrations):
    affected_area = None
    if disorder["Front Area Affected"] == "Yes":
        affected_area = "Front"
    elif disorder["Central Area Affected"] == "Yes":
        affected_area = "Central"
    elif disorder["Back Area Affected"] == "Yes":
        affected_area = "Back"
    
    recommended_languages = [
        language for language, concentration in language_concentrations.items()
        if concentration != affected_area
    ]
    
    return recommended_languages

speech_defects = {
    "Stuttering": {
        "Front Area Affected": "No",
        "Central Area Affected": "Yes",
        "Back Area Affected": "No",
        "Notes": "Disruption in flow of speech."
    },
    "Dysarthria": {
        "Front Area Affected": "Yes",
        "Central Area Affected": "Yes",
        "Back Area Affected": "Yes",
        "Notes": "Muscle control issue affecting all areas."
    },
        "Aphasia": {
        "Front Area Affected": "No",
        "Central Area Affected": "No",
        "Back Area Affected": "No",
        "Notes": "Primarily brain-related, not vocal cords."
    },
    "Laryngitis": {
        "Front Area Affected": "Yes",
        "Central Area Affected": "Yes",
        "Back Area Affected": "Yes",
        "Notes": "Inflammation of vocal cords."
    },
    "Vocal Cord Paralysis": {
        "Front Area Affected": "Yes",
        "Central Area Affected": "Yes",
        "Back Area Affected": "Yes",
        "Notes": "Complete or partial loss of movement."
    },
    "Spasmodic Dysphonia": {
        "Front Area Affected": "No",
        "Central Area Affected": "Yes",
        "Back Area Affected": "Yes",
        "Notes": "Irregular vocal cord spasms."
    },
    "Polyps or Nodules": {
        "Front Area Affected": "Yes",
        "Central Area Affected": "Yes",
        "Back Area Affected": "No",
        "Notes": "Growths usually on front and central areas."
    },
    "Phonotrauma": {
        "Front Area Affected": "Yes",
        "Central Area Affected": "Yes",
        "Back Area Affected": "Yes",
        "Notes": "Trauma affecting all areas."
    },
    "Mutational Dysphonia": {
        "Front Area Affected": "No",
        "Central Area Affected": "Yes",
        "Back Area Affected": "Yes",
        "Notes": "Voice does not adjust to age."
    },
    "Functional Aphonia": {
        "Front Area Affected": "No",
        "Central Area Affected": "No",
        "Back Area Affected": "No",
        "Notes": "Psychological; no physical area affected."
    },
    "Glottal Insufficiency": {
        "Front Area Affected": "Yes",
        "Central Area Affected": "Yes",
        "Back Area Affected": "Yes",
        "Notes": "Incomplete closure of the vocal cords."
    },
    "Vocal Fold Scarring": {
        "Front Area Affected": "Yes",
        "Central Area Affected": "Yes",
        "Back Area Affected": "Yes",
        "Notes": "Scar tissue affects vibration."
    }
}

st.title("Language and Speech Defect Recommendation")

native_language = st.selectbox("Select your Native Language", list(vowel_systems.keys()))

speech_defect = st.selectbox("Select your Speech Defect", list(speech_defects.keys()))

disorder = speech_defects[speech_defect]
recommended_languages = recommend_languages_for_disorder(disorder, language_concentrations)

st.write(f"Based on your speech defect ({speech_defect}), the following languages are recommended for you:")
st.write(recommended_languages)

st.markdown(
    """
    <div class="footer">
        <div class="social-icons">
            <a href="https://twitter.com" target="_blank"><i class="fab fa-twitter"></i></a>
            <a href="https://facebook.com" target="_blank"><i class="fab fa-facebook-f"></i></a>
            <a href="https://linkedin.com" target="_blank"><i class="fab fa-linkedin-in"></i></a>
            <a href="https://instagram.com" target="_blank"><i class="fab fa-instagram"></i></a>
        </div>
        <p>&copy; 2025 LanguageMaster, All Rights Reserved</p>
    </div>
    """,
    unsafe_allow_html=True)

st.markdown(
    """
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    """,
    unsafe_allow_html=True
)