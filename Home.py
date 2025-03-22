import streamlit as st

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

    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }

    /* Center the widget (button) */
    .center-widget {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
    }

    </style>
    """,
    unsafe_allow_html=True
)
col = st.columns([3,9])
col[0].image('logo.png')
col[1].text('')
col[1].text('')
col[1].text('')
col[1].text('')
col[1].markdown("<h1 style='text-align: center; color: white;'>Linguini Learning</h1>", unsafe_allow_html=True)

# Main Content Container
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Adjusted column widths to make the text box wider
col1, col2 , col3 = st.columns([1, 2.5, 1])  # Middle column (col2) is now 4, making it wider

with col1:
    st.image('logo.png', width=250)

with col2:
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
with col3:
    st.image('Screenshot__456_-removebg-preview.png', width=250)

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
