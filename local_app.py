import streamlit as st
import subprocess
import os

st.title('GPT Engineer Web Interface')
prompt = st.text_area('Enter your prompt:')
if st.button('Run GPT Engineer'):
    if prompt:
        os.makedirs('project', exist_ok=True)
        with open('project/prompt', 'w') as f:
            f.write(prompt)
        st.info('Running gpt-engineer...')
        # Use the locally installed gpt-engineer package
        result = subprocess.run(['python3', '-m', 'gpt_engineer.applications.cli.main', 'project', '--lite'], capture_output=True, text=True)
        st.text_area('Output:', result.stdout + result.stderr, height=400)
    else:
        st.error('Please enter a prompt.')
