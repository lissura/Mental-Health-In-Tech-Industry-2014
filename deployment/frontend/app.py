import streamlit as st
import requests


st.markdown(
         """ 
         <style>
          h2{text-align : center;
          font-size:100px;}
          h3{text-align:center;
          font-size:40px;}
          h4{font-size:35px}
          h5{text-align:justify;
          front-size:20px}
          </style>

          <h2> 📝 Please Fill The Question 📝 </h2> 
          """,unsafe_allow_html=True)

st.markdown(''' <h3> Employee Profile <h3>''', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,1,1])
with col1:
    st.markdown('''<h5> What is your gender?</h5>''',unsafe_allow_html=True)
    gender = st.radio('',['Female','Male','Others'])
with col2:
    st.markdown('''<h5> Which contient are you in?</h5>''',unsafe_allow_html=True)
    continent = st.radio('',['America','Asia','Balkans','Africa','Oceania','Others'])
with col3:
    st.markdown('''<h5> Do you have a family history of mental illness?</h5>''',unsafe_allow_html=True)
    family_history = st.radio('',['No','Yes'])

st.markdown(''' <h3><br> </br>Employer Support <h3>''', unsafe_allow_html=True)
st.markdown('''<h5> Do you think that discussing a mental health issue with your employer would have negative consequences?</h5>''',unsafe_allow_html=True)
mental_health_consequence = st.radio('', ['No','Maybe','Yes'])

st.markdown('''<h5>Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?</h5>''',unsafe_allow_html=True)
anonymity = st.radio('',["Don't know",'No','Yes'])

st.markdown('''<h5>How easy is it for you to take medical leave for a mental health condition?</h5>''',unsafe_allow_html=True)
leave = st.radio('',["Don't know","Somewhat easy",'Very easy','Somewhat difficult','Very difficult'])

st.markdown('''<h5>Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?</h5>''',unsafe_allow_html=True)
obs_consequence = st.radio(" ",['No', 'Yes'])

st.markdown('''<h5>Does your employer provide mental health benefits?</h5>''',unsafe_allow_html=True)
benefits = st.radio(' ',["Don't know",'No','Yes'])

st.markdown('''<h5>Do you know the options for mental health care your employer provides?</h5>''',unsafe_allow_html=True)
care_options = st.radio('',['Not sure','No','Yes'])

st.markdown('''<h5>If you have a mental health condition, do you feel that it interferes with your work?</h5>''',unsafe_allow_html=True)
work_interfere = st.radio('',['Never','Rarely','Sometimes','Often'])

data = {'gender':gender,
        'continent':continent,
        'mental_health_consequence': mental_health_consequence,
        'anonymity':anonymity,
        'leave':leave,
        'obs_consequence':obs_consequence,
        'benefits':benefits,
        'care_options':care_options,
        'family_history':family_history,
        'work_interfere':work_interfere}

URL = "https://cindra-love-yourself.herokuapp.com/predict"

treatment_prediction = st.button('Predict')
if treatment_prediction :
    r = requests.post(URL, json=data)
    res = r.json()

    if res['code'] == 200:
        rezz = (res['result']['description'])
        if rezz == 'No Need Treatment':
            st.markdown(''' <h2> No Need Treatment </h2>''', unsafe_allow_html=True)
            col4,col5,col6 = st.columns([1,1,1])
            with col5 : 
                st.image('love.png')
        else:
            st.markdown(''' <h2> Need Treatment </h2>''', unsafe_allow_html=True)
            col7,col8,col9 = st.columns([1,1,1])
            with col8:
                st.image('speakup.png')
    else:
        st.write("Something Went Wrong....")
        st.write(f"Details : {res['result']['error_msg']}")

