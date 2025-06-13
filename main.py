import streamlit as st
from utils import generate_landing_page
from logger import init_logger

logger = init_logger()
logger.info("Starting app")

st.set_page_config(
    layout="wide",
    page_title="🤖 Landing Page generator",
)

st.markdown('# Landing page generator')
# User input
st.header("Describe Your Landing Page")
user_input = st.text_area(
    "Enter your landing page details in natural language. Be as detailed as you need it (provide business name, product/service you're selling, target audience, color scheme...). Leave blank for a general-purpose landing page.",
    height=200
)

if st.button("Generate", type="primary"):
    with st.spinner('Generating landing page...'):
        try:
            logger.info('Starting to generate landing page')
            generated_html_file = generate_landing_page(user_input)
            logger.info('Landing page generation finished')

            # Display the generated code
            st.subheader("Generated Landing Page Code")
            st.code(generated_html_file, language="html")

            st.success('Landing page HTML successfully created!', icon="✅")

            file_name = "landing_page.html" if not user_input.strip() else "custom_landing_page.html"
            st.download_button(
                label="Download HTML",
                data=generated_html_file,
                file_name=file_name,
                mime="text/html",
                icon=":material/download:",
            )

            st.badge("Success", icon=":material/check:", color="green")


        except Exception as e:
            logger.info('Failed to create landing page.')
            st.badge("Fail", icon=":material/cancel:", color="red")
            st.error(f"An error occurred: {str(e)}")

# Instructions
st.sidebar.header("Instructions")
st.sidebar.markdown("""
1. Describe your landing page in natural language in the text box (e.g., theme, colors, call to action).
2. Leave the text box blank for a general-purpose landing page.
3. Click 'Generate Landing Page' to create the HTML/CSS code.
4. Download the generated HTML file using the download button.
5. View a basic preview of the landing page below the code.
6. Ensure you have an OpenAI API key set as an environment variable (`OPENAI_API_KEY`) in .env file.
""")


