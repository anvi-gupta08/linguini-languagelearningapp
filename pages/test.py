import streamlit as st

st.markdown("""
<style>
/* Welcome section with peach background and centered text */
.welcome-section {
    background: #ffffff; /* Peach background for text box */
    border-radius: 20px;
    padding: 25px;
    animation: fadeIn 1.5s;
    text-align: center; /* Center the text */
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

.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #06402b; /* Dark Green background */
    color: white;
    text-align: center;
    font-size: 16px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.footer .social-icons {
    margin-top: 8px;
}

.footer .social-icons a {
    color: white;
    font-size: 20px;
    padding: 0 10px;
}

.footer .social-icons a:hover {
    color: #e9ba8c; /* Peach hover effect */
}
@keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)

# Center the button (widget) using the new CSS class
col1, col2 = st.columns([1, 2])

with col1:
    # Display the image without caption
    st.image('logo.png', width=250)

with col2:
    st.markdown(
        """
        <div class="welcome-section">
            <h2 style="color: #000000;">Welcome to Linguini!</h2>
            <p style="color: #000000;">
                A cutting-edge language-learning platform tailored to help you master new languages with ease and efficiency.
            </p>
            <p style="color: #000000;">
                Our advanced system customizes your learning experience based on your unique vocal patterns, making pronunciation easier and faster. With personalized language recommendations based on vowel charts, you’ll feel confident and comfortable as you speak.
            </p>
            <p style="color: #000000;">
                For those with speech challenges, we go further by offering recommendations that minimize difficulty, making language learning more accessible than ever before.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

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
