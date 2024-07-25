import streamlit as st
import pickle
import pandas as pd
import sklearn

pkl_filename = "pickle_model.pkl"
st.header("AI-Driven Mental Health Risk Assmt. Webapp")
st.write("Please answer the questions to the best of your ability.")
col1, col2 = st.columns(2)

with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

# with col1:
    with st.form('Form1'):
#        add timestamp____________________________

        
        age = st.slider(label='1.What is your age?', min_value=18, max_value=100, key=0)

        gender_options = ['Male', 'Female', 'Transgender/Non Binary']
        gender = st.radio("2.Gender ", gender_options, index=0)
        gender_index = gender_options.index(gender)
        
        country_options = [
            'Australia', 'Austria', 'Belgium', 'Bosnia and Herzegovina', 'Brazil', 'Bulgaria', 
            'Canada', 'China', 'Colombia', 'Costa Rica', 'Croatia', 'Czech Republic', 'Denmark', 
            'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 
            'Israel', 'Italy', 'Japan', 'Latvia', 'Mexico', 'Moldova', 'Netherlands', 'New Zealand', 
            'Nigeria', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Romania', 'Russia', 
            'Singapore', 'Slovenia', 'South Africa', 'Spain', 'Sweden', 'Switzerland', 'Thailand', 
            'United Kingdom', 'United States', 'Uruguay', 'Zimbabwe'
        ]
        country = st.radio('What country do you live in?', country_options, index=country_options.index('United States'))
        country_index = country_options.index(country)

        employment_options = ['No', 'Yes']
        employment = st.radio('Are you self employed?', employment_options, index=employment_options.index('No'))
        employment_index = employment_options.index(employment)

        family_history_options = ['No', 'Yes']
        family_history = st.radio('Do you have a family history of mental illness?', family_history_options, index=family_history_options.index('No'))
        family_history_index = family_history_options.index(family_history)

        employees_options = ['1-5', '100-500', '26-100', '500-1000', '6-25', 'More than 1000']
        employees = st.radio('How many employees does your company or organization have?', employees_options, index=employees_options.index('1-5'))
        employees_index = employees_options.index(employees)

        remote_options = ['No', 'Yes']
        remote = st.radio('Do you work remotely (outside of an office) at least half of the time?', remote_options, index=remote_options.index('No'))
        remote_index = remote_options.index(remote)

        tech_company_options = ['No', 'Yes']
        tech_company = st.radio('Is your employer primarily a tech company/organization?', tech_company_options, index=tech_company_options.index('No'))
        tech_company_index = tech_company_options.index(tech_company)

        wellness_program_options = ['Do not know', 'No', 'Yes']
        wellness_program = st.radio('Has your employer ever discussed mental health as part of an employee wellness program?', wellness_program_options, index=wellness_program_options.index('Do not know'))
        wellness_program_index = wellness_program_options.index(wellness_program)

        resources_mh_issues_options = ['Do not know', 'No', 'Yes']
        resources_mh_issues = st.radio('Does your employer provide resources to learn more about mental health issues and how to seek help?', resources_mh_issues_options, index=resources_mh_issues_options.index('Do not know'))
        resources_mh_issues_index = resources_mh_issues_options.index(resources_mh_issues)

        neg_conseq_mh_options = ['Maybe', 'No', 'Yes']
        neg_conseq_mh = st.radio('Do you think that discussing a mental health issue with your employer would have negative consequences?', neg_conseq_mh_options, index=neg_conseq_mh_options.index('No'))
        neg_conseq_mh_index = neg_conseq_mh_options.index(neg_conseq_mh)

        neg_conseq_ph_options = ['Maybe', 'No', 'Yes']
        neg_conseq_ph = st.radio('Do you think that discussing a physical health issue with your employer would have negative consequences?', neg_conseq_ph_options, index=neg_conseq_ph_options.index('No'))
        neg_conseq_ph_index = neg_conseq_ph_options.index(neg_conseq_ph)

        discuss_coworkers_options = ['No', 'Some of them', 'Yes']
        discuss_coworkers = st.radio('Would you be willing to discuss a mental health issue with your coworkers?', discuss_coworkers_options, index=discuss_coworkers_options.index('No'))
        discuss_coworkers_index = discuss_coworkers_options.index(discuss_coworkers)

        discuss_supervisors_options = ['No', 'Some of Them', 'Yes']
        discuss_supervisors = st.radio('Would you be willing to discuss a mental health issue with your direct supervisor(s)?', discuss_supervisors_options, index=discuss_supervisors_options.index('No'))
        discuss_supervisors_index = discuss_supervisors_options.index(discuss_supervisors)

        discuss_potential_mh_options = ['Maybe', 'No', 'Yes']
        discuss_potential_mh = st.radio('Would you bring up a mental health issue with a potential employer in an interview?', discuss_potential_mh_options, index=discuss_potential_mh_options.index('Maybe'))
        discuss_potential_mh_index = discuss_potential_mh_options.index(discuss_potential_mh)

        discuss_potential_ph_options = ['Maybe', 'No', 'Yes']
        discuss_potential_ph = st.radio('Would you bring up a physical health issue with a potential employer in an interview?', discuss_potential_ph_options, index=discuss_potential_ph_options.index('Maybe'))
        discuss_potential_ph_index = discuss_potential_ph_options.index(discuss_potential_ph)

        takes_mh_seriously_options = ['Do not know', 'No', 'Yes']
        takes_mh_seriously = st.radio('Do you feel that your employer takes mental health as seriously as physical health?', takes_mh_seriously_options, index=takes_mh_seriously_options.index('Do not know'))
        takes_mh_seriously_index = takes_mh_seriously_options.index(takes_mh_seriously)

        observed_neg_conseq_options = ['No', 'Yes']
        observed_neg_conseq = st.radio('Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?', observed_neg_conseq_options, index=observed_neg_conseq_options.index('No'))
        observed_neg_conseq_index = observed_neg_conseq_options.index(observed_neg_conseq)

        family_history_options = ['No', 'Yes']
        family_history = st.radio('3.Do you have a family history of mental illness?', family_history_options, index=0)
        family_history_index = family_history_options.index(family_history)

        benefits_options = ['Do not know', 'No', 'Yes']
        benefits = st.radio('4.Does your employer provide mental health benefits?', benefits_options, index=0)
        benefits_index = benefits_options.index(benefits)

        care_options = ['No', 'Not sure', 'Yes']
        care = st.radio('5.Do you know the options for mental health care your employer provides?', care_options, index=0)
        care_options_index = care_options.index(care)

        anonymity_options = ['Do not know', 'No', 'Yes']
        anonymity = st.radio('6.Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?', anonymity_options, index=0)
        anonymity_index = anonymity_options.index(anonymity)

        leave_options = ['Do not know', 'Somewhat Difficult','Somewhat Easy', 'Very difficult', 'Very easy']
        leave = st.radio('7.How easy is it for you to take medical leave for a mental health condition?', leave_options, index=0)
        leave_index = leave_options.index(leave)

        work_interfere_options = ["Don't know", 'Never', 'Often', 'Rarely', 'Sometimes']
        work_interfere = st.radio('8.If you have a mental health condition, do you feel that it interferes with your work?', work_interfere_options, index=0)
        work_interfere_index = work_interfere_options.index(work_interfere)

        comment = st.text_input("Comments/Concerns")
        
        submitted = st.form_submit_button('Submit')

        if submitted:
            X_temp = {
                'Age': [age],
                "Gender": [gender],
                "Country": [country],
                "Employment": [employment],
                "work_interfere": [work_interfere],
                "family_history": [family_history],
                "employees": [employees],
                "remote": [remote],
                "Tech_company": [tech_company],
                "Benefits": [benefits],
                "care_options": [care],
                "wellness_program": [wellness_program],
                "Mental_Health_Resources": [resources_mh_issues],
                "anonymity": [anonymity],
                "leave": [leave],
                "Negative_Mental_Health_Consequence": [neg_conseq_mh],
                "Negative_Physical_Health_Consequence": [neg_conseq_ph],
                "Discuss_Coworkers":[discuss_coworkers],
                "Dicuss_Supervisors":[discuss_supervisors],
                "Discuss_potential_mental":[discuss_potential_mh],
                "Discuss_potential_physical":[discuss_potential_ph],
                "Take_Mental_Serious":[takes_mh_seriously],
                "Observe_Neg_Consequence":[observed_neg_conseq], 
                "Comments":[comment]
            }
            X_test = {
                'Age': [(age - 18)/(72 - 18)],
                "Gender": [gender_index],
                "family_history": [family_history_index],
                "benefits": [benefits_index],
                "care_options": [care_options_index],
                "anonymity": [anonymity_index],
                "leave": [leave_index],
                "work_interfere": [work_interfere_index]
            }

            X_temp = pd.DataFrame(X_temp)
            X_temp.to_excel('MentalHealthData.xlsx', index=False)
            X_test = pd.DataFrame(X_test)
            Ypredict = pickle_model.predict_proba(X_test)

            st.divider()
            st.subheader("Mental Health Risk Assessment")
            st.write("The data collected from the above survey form:")
            st.write(X_temp)
            st.write("The probability that one should be treated of mental health:")
            st.write(round(Ypredict[0][1], 2))