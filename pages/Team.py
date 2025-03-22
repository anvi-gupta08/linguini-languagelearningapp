import streamlit as st

st.set_page_config(page_title="About the Developer", layout="wide")

st.markdown(
    """
    <style>
    .developer-section {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.1);
        margin: 40px auto;
        max-width: 800px;
        text-align: center;
    }
    .developer-image {
        width: 150px;
        height: 150px;
        background: #CCCCCC;
        border-radius: 50%;
        margin: 20px auto;
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: bold;
        font-size: 18px;
        color: #666;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
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




    st.markdown(
        """
        <div class="developer-section">
            <h1>About the Developer</h1>
            <p>
                Hi there! I'm Anvi Gupta, 17 from Mumbai, student and developer with a strong focus on coding, web design, and data analysis.
                I am super passionate about computer science, coding, linguistics, literature, and I'm so happy you can read this right now.
                I’m actively involved in research projects and leadership roles, particularly in tech-driven initiatives. My goal is to create meaningful 
                solutions that positively impact communities and individuals. Thanks for accompanying me on my journey!
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

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
