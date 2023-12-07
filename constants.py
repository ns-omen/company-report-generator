import streamlit as st

ENV = 'prd'
API_BASE_URL = 'https://pmqutigs5m.execute-api.us-west-2.amazonaws.com'
GENERATE_COMPANY_REPORT_ENDPOINT = f'{API_BASE_URL}/{ENV}/generate-company-report'
GET_PROGRESS_ENDPOINT = f'{API_BASE_URL}/{ENV}/get-progress?transactionID='
API_KEY = st.secrets['api_key']
