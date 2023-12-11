import streamlit as st

ENV = st.secrets['env']
API_BASE_URL = st.secrets['api_base_url']
API_KEY = st.secrets['api_key']
GENERATE_COMPANY_REPORT_ENDPOINT = f'{API_BASE_URL}/{ENV}/generate-company-report'
GET_PROGRESS_ENDPOINT = f'{API_BASE_URL}/{ENV}/get-progress?transactionID='
