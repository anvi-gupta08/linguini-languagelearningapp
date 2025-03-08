import streamlit as st

st.set_page_config(page_title="About the Developer", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #ADD8E6, #ffffff);
        color: #000000;
        font-family: Arial, sans-serif;
    }
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
    footer {
        background-color: #000000;
        color: #FFFFFF;
        text-align: center;
        padding: 20px 0;
        position: fixed;
        bottom: 0;
        width: 100%;
    }
    footer a {
        color: #FFFFFF;
        text-decoration: none;
        margin: 0 10px;
    }
    footer a:hover {
        text-decoration: underline;
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
