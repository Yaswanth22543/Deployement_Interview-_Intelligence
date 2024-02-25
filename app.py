import pandas as pd
import numpy as np
import streamlit as st
import pickle

# page config
st.set_page_config(
    page_title="Multi-class Classification App", 
    page_icon="🎫", 
    layout='wide'
)


model = pickle.load(open('reg1.pkl', 'rb')) 

# title 
st.markdown("<h1 style='text-align: center;'>Multi-class Classification App</h1>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'>this is a multi-class classification app that uses a simple machine learning model to predict the class of a given input</h1>", unsafe_allow_html=True)

col1,col2,col3,col4 = st.columns(4)

with col1:
    slrc = st.number_input("S.L.R.C", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    slri = st.number_input("S.L.R.I", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    att  = st.number_input("A.T.T", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    lmi  = st.number_input("L.M.I", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    lmc  = st.number_input("L.M.C", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    sr   = st.number_input("S.R", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

with col2:
    ljtc = st.number_input("L.J.T.C", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    ljti = st.number_input("L.J.T.I", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    nic  = st.number_input("N.I.C", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    nii  = st.number_input("N.I.I", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    spi  = st.number_input("S.P.I", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    spc  = st.number_input("S.P.C", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

with col3:
    lac  = st.number_input("L.A.C", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    lai  = st.number_input("L.A.I", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    qa   = st.number_input("Q.A", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    comp_ratio = st.number_input("COMPLIANCE Ratio", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    intr_dur  = st.number_input("Interview duration", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

    prof_disp = ('Account Manager', 'Data Scientist', 'Developer', 'HR',  'Marketing', 'Product Manager', 'Program Manager', 'QA Automation', 'QA Manual', 'Sales')
    prof_options = list(range(len(prof_disp)))
    prof = st.selectbox("Profile", prof_options, format_func = lambda x: prof_disp[x])

with col4:
    pei_disp = ('Negative', 'Neutral', 'Positive')
    pei_options = list(range(len(pei_disp)))
    pei = st.selectbox("P.E.I", pei_options, format_func = lambda x: pei_disp[x])

    pec_disp = ('Negative', 'Neutral', 'Positive')
    pec_options = list(range(len(pec_disp)))
    pec = st.selectbox("P.E.C", pec_options, format_func = lambda x: pec_disp[x])

    intr_disp = ('No','Yes')
    intr_options = list(range(len(intr_disp)))
    intr_intro = st.selectbox("Interviewer Intro",intr_options, format_func = lambda x: intr_disp[x])

    cand_disp = ('No','Yes')
    cand_options = list(range(len(cand_disp)))
    cand_intro = st.selectbox("Candidate intro", cand_options, format_func = lambda x: cand_disp[x])

    opp_disp = ('No', 'Yes')
    opp_options = list(range(len(opp_disp)))
    opp_to_as = st.selectbox("Opp to ask", opp_options, format_func = lambda x: opp_disp[x])


if st.button('Predict'):
    result = model.predict([[slrc,slri,att,lmi,lmc,sr,ljtc,ljti,nic,nii,spi,spc,lac,lai,qa,comp_ratio,intr_dur,prof,pei,pec,intr_intro,cand_intro,opp_to_as]])
    if result == 0:
        st.write('Consider')
    elif result == 1:
        st.write('May Consider')
    else:
        st.write('Not Consider')