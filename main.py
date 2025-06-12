import streamlit as st
from logger import init_logger
from dotenv import load_dotenv

load_dotenv()


logger = init_logger()
logger.info("Starting app")


st.set_page_config(
    layout="wide",
    page_title="🤖 Landing Page generator",
)

st.markdown('# Landing page generator')
st.text("Write down in the text box the details of your landing page. If you don\'t have any special requirements, click on 'Generate' button and wait for a few seconds. Then you can download the HTML of your landing page.")


if "user_query" not in st.session_state:
    st.session_state.title_value = "Landing Page Gen"
    st.title(st.session_state.title_value)

st.button("Generate", type="primary")

st.badge("Success", icon=":material/check:", color="green")
st.success('Landing page HTML successfully created!', icon="✅")
st.download_button(
    label="Download HTML",
    data=html_file,
    file_name="landing_page.html",
    mime="text/csv",
    icon=":material/download:",
)

st.badge("Fail", icon=":material/cancel:", color="red")