import streamlit as st

st.set_page_config(page_title="Language Learning Platform", layout="wide")

st.markdown(
    """
    <style>
    /* Button style */
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

    /* Welcome section with white background */
    .welcome-section {
        background: #ffffff; /* White background for text box */
        border-radius: 20px;
        padding: 25px;
        animation: fadeIn 1.5s;
        text-align: center; /* Center the text */
    }

    /* Content section with white background */
    .content-section {
        background: #ffffff; /* White background */
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
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

    /* Center the widget (button) */
    .center-widget {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px; /* Adjust as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create content using columns
with st.container():

    col1, col2 = st.columns([2, 3])

    with col1:
        st.image(
            'logo.png',  # Local image file path
            width=300
        )

    with col2:
        st.markdown(
            """
            <div class="welcome-section">
                <h2 style="color: #000000;">Vowel Positioning in Languages</h2>
                <p style="color: #000000;">
                    Vowel positioning varies significantly across languages, creating unique pronunciation challenges for language learners. Each language has its own set of vowel sounds, characterized by specific placements of the tongue, lips, and jaw. For example, English has a relatively complex vowel system with around 12 distinct vowels, varying widely in tongue height, backness, and lip rounding. In contrast, languages like Spanish have only five vowel sounds, which are simpler and more consistent in their positioning.
                </p>
                <p style="color: #000000;">
                    These differences in vowel positioning mean that certain vowels in a new language may feel unfamiliar or physically challenging to produce accurately, as they may require new or less-used tongue and lip placements. Understanding these differences helps learners anticipate pronunciation challenges and work toward more accurate pronunciation in their target language.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="content-section">
            <h2 style="color: #000000;">How Our App Works</h2>
            <p style="color: #000000;">
                <strong>Native and Spoken Language Analysis:</strong> Once you input your native and spoken languages, our system analyzes the typical vowel placement in these languages. This helps us identify languages that have similar vowel positioning, making them easier for you to learn and pronounce.
            </p>
            <p style="color: #000000;">
                <strong>Speech Impairment Consideration:</strong> If you have a speech defect, our technology analyzes which part of your vocal tract is affected. We then match you with languages where vowels are distributed differently, focusing on areas where you’re less likely to face obstacles, so you can learn with confidence and ease.
            </p>
            <p style="color: #000000;">
                <strong>Personalized Recommendations and Tools:</strong> With these insights, we provide a list of recommended languages that align with your natural vocal habits and, if applicable, accommodate any vocal challenges. Alongside the recommendations, we offer tools, resources, and exercises tailored to your needs, helping you build pronunciation, vocabulary, and fluency in a way that feels natural.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Center the button (widget) using the new CSS class
st.markdown(
    """
    <div class="center-widget">
        <button class="test-button">Start Learning</button>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer content with dark green background
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
    unsafe_allow_html=True
)

st.markdown(
    """
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    """,
    unsafe_allow_html=True
)
