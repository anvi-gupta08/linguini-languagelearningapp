import streamlit as st
import base64

st.set_page_config(page_title="Language Learning Platform", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #bcecac; /* Light Green background */
        color: #212121;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        display: flex;
        flex-direction: column;
        min-height: 100vh; /* Ensures footer is pushed to bottom */
    }
    .main-content {
        flex: 1; /* Pushes footer down */
    }
    .top-nav-bar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #FFFFFF;
        padding: 20px;
        border-bottom: 2px solid #B0BEC5;
        z-index: 1000;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .nav-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    /* Style for the button widget */
    .test-button {
        background: #000000; /* Black background for button */
        color: #ffffff; /* White text */
        font-size: 18px;
        font-weight: bold;
        padding: 12px 30px;
        border: none;
        border-radius: 40px;
        cursor: pointer;
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease, background-color 0.3s ease;
        margin-top: 20px;
    }
    .test-button:hover {
        background: #444444; /* Darker black on hover */
        transform: scale(1.1);
    }

    /* Welcome section */
    .welcome-section {
        background: #ffffff;
        border-radius: 20px;
        padding: 25px;
        animation: fadeIn 1.5s;
        text-align: center;
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

    /* Styled image */
    .styled-image {
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-top: 20px;
        width: 250px;
        object-fit: cover;
    }
    
    .styled-image:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
    }

    /* Center the widget (button) */
    .center-widget {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
    }
    .header-row {
  display: flex;
  align-items: center;
  justify-content: center; /* Center image + text as a group */
  background-color: #06402b;
  padding: 15px 25px;
  border-radius: 12px;
  gap: 15px; /* Space between image and text */
}

.header-row h1 {
  color: white;
  margin: 0;
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
file_ = open("logo.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
st.markdown(f'''<div class="header-row">
  <img src="data:image/gif;base64,{data_url}" alt="cat gif">
  <h1>Linguini Learning</h1>
</div>''', unsafe_allow_html=True)

# Main Content Container
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Adjusted column widths to make the text box wider
col = st.columns([3.5, 1],vertical_alignment="center")  # Middle column (col2) is now 4, making it wider

with col[0]:
    st.markdown(
        """
        <div class="welcome-section">
            <h2 style="color: #000000;">Welcome to Linguini!</h2>

<p style="color: #000000;">
               Discover a language-learning platform designed to make mastering new languages easier and more effective. Our advanced technology adapts to your unique vocal patterns, providing a personalized experience that helps you improve pronunciation quickly and confidently. Whether you're a beginner or advanced learner, our platform is here to guide you every step of the way.

                
</p>
<p style="color: #000000;">
                1.Cutting-edge language-learning platform designed for efficient language mastery


                
</p>
<p style="color: #000000;">
                2. Customizes learning based on your unique vocal patterns for easier and faster pronunciation


                
</p>
<p style="color: #000000;">
                3. Personalized language recommendations tailored to individual vowel charts

                
</p>
<p style="color: #000000;">
                4. Boosts confidence and comfort in speaking with targeted practice


                
</p>

<p style="color: #000000;">
                5. Special recommendations for those with speech challenges, reducing difficulty and improving accessibility


</p>
        </div>
        """,
        unsafe_allow_html=True
    )
with col[1]:
    st.image('Screenshot__456_-removebg-preview.png', width=250)

with st.container():
    col1, col2 = st.columns([1, 2],vertical_alignment="center")

    with col1:
        # Image on the left
        st.image('Screenshot__449_-removebg-preview.png', width=300)

    with col2:
        # Text content on the right
        st.markdown(
            """
            <div class="welcome-section" style="margin-top: 20px;">
                <h2 style="color: #000000;">Vowel Positioning in Languages</h2>
                <p style="color: #000000;">
                    Vowel positioning varies significantly across languages, creating unique pronunciation challenges for language learners. Each language has its own set of vowel sounds, characterized by specific placements of the tongue, lips, and jaw. For example, English has a relatively complex vowel system with around 12 distinct vowels, varying widely in tongue height, backness, and lip rounding. In contrast, languages like Spanish have only five vowel sounds, which are simpler and more consistent in their positioning.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    col3, col4 = st.columns([2, 1],vertical_alignment="center")

    with col4:
        # Image on the left
        st.image('Screenshot__463_-removebg-preview.png', width=300)

    with col3:
        # Text content on the right
        st.markdown(
            """
            <div class="welcome-section" style="margin-top: 20px;">
                <p style="color: #000000;">
                Vowel sounds are often categorized based on their backness and roundness. Front vowels are produced with the tongue positioned towards the front of the mouth, like in the English sound /i/ in "see." Back vowels, like the /u/ sound in "too," are formed with the tongue towards the back. Central vowels fall in between, with the tongue placed in the middle of the mouth. Additionally, some vowels can be rounded, where the lips are pursed (as in the French /u/), while others are unrounded, where the lips are relaxed.
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

# Closing Main Content Div
st.markdown('</div>', unsafe_allow_html=True)

# Footer
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
