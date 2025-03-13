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
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="developer-section">
        <div class="developer-image">Image Placeholder</div>
        <h1>About the Developer</h1>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ac ex ac justo vehicula tincidunt.
            Phasellus fermentum nisi nec urna auctor, nec vehicula urna fermentum. In luctus, libero non vehicula
            dictum, lectus metus posuere sapien, ac fermentum nisl libero a libero. Curabitur in est id orci fermentum
            fermentum. Donec et libero eu ante luctus ultricies ut in mauris.
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