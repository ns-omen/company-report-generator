import streamlit as st
from api_handler import create_new_report, get_existing_report

st.set_page_config(page_title = 'AI Company Reports')

hide_streamlit_style = "<style> footer { visibility: hidden; } </style>"
st.markdown(hide_streamlit_style, unsafe_allow_html = True) 

st.subheader('Company Report Generator', divider = 'rainbow')
st.write('Harness the power of generative AI to create insightful company reports')

# form to create a new report
create_report_form = st.form(key = 'create_report')
input_url = create_report_form.text_input(label = 'Company Webpage URL', placeholder = '', value = '', disabled = False, help = 'This can be any webpage that provides basic information about the company (e.g. https://fluxus.io).')
create_report_submitted = create_report_form.form_submit_button(label = 'Create a New Report', disabled = False)
if create_report_submitted: 
    with st.spinner('creating report...'): create_new_report(create_report_form, input_url)

# form to query an existing report
get_report_form = st.form(key = 'get_report')
report_id = get_report_form.text_input(label = 'Report ID', placeholder = '', value = '', disabled = False, help = "All reports have a unique identifier assigned to them. This was provided to you in the response when creating a new report.")
get_report_submitted = get_report_form.form_submit_button(label = 'Get an Existing Report', disabled = False)
if get_report_submitted:
    with st.spinner('retrieving report...'): get_existing_report(get_report_form, report_id)            
