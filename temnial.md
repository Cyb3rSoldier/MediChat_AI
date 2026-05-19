pip install flask flask-cors

python -m pip install flask flask-cors

python -u "d:\Medichat v1\app_version1.py"

python -m venv venv

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

.\venv\Scripts\Activate.ps1

pip install flask flask-cors

python app_version1.py

Alternative

pip install streamlit

# app_streamlit.py
import streamlit as st
from medichat_core import SymptomExtractorBFS, DiseaseMatcher

st.set_page_config(page_title="MediChat UI Prototyper", page_icon="🩺", layout="centered")

st.title("🩺 MediChat Core Diagnostic Prototype")
st.caption("Testing Framework powered by Streamlit and your Backend Engine")

# Instantiate classes
@st.cache_resource
def load_engine():
    return SymptomExtractorBFS(), DiseaseMatcher()

extractor, matcher = load_engine()

# Main input text area
user_input = st.text_area("Describe all patient symptoms in detail:", 
                          placeholder="Example: I am experiencing a severe headache, sudden high fever, and shivering chills.")

if st.button("Analyze Symptoms", type="primary"):
    if user_input.strip():
        with st.spinner("Running Best-First Search & NLP Tokenization..."):
            # Run core classes logic
            extracted = extractor.extract(user_input)
            match_results = matcher.find_matches(extracted)
            
        st.subheader("1. Extracted Key Symptoms")
        if extracted:
            st.write(", ".join([f"`{s}`" for s in extracted]))
        else:
            st.warning("No standard dictionary symptoms recognized.")
            
        st.subheader("2. Diagnosis Results")
        st.info(f"Match Classification Type: **{match_results['type'].upper()}**")
        
        if match_results["results"]:
            for res in match_results["results"]:
                with st.expander(f"Condition: {res['disease']['name']} ({int(res['score'] * 100)}% Match)"):
                    st.write(f"**Description:** {res['disease']['description']}")
                    
                    st.write("**Matched Symptoms:**")
                    st.write(", ".join(res['matched']))
                    
                    st.write("**Recommended Specialists:**")
                    for doc in res['disease']['doctors']:
                        st.write(f"- {doc['specialty']} (*{doc['reason']}*)")
                        
                    st.write("**Actionable Care Steps:**")
                    for behavior in res['disease']['behaviors']:
                        st.write(f"- {behavior}")
        else:
            st.error("No cross-referenced conditions match these symptom combinations.")
            
        st.caption("⚠️ **Disclaimer:** This information is for prototyping validation only. Consult a licensed physician.")
    else:
        st.warning("Please type something before submitting.")

streamlit run app_streamlit.py

whoel below copy temr

PS D:\Medichat v1> python -m venv venv
PS D:\Medichat v1> .\venv\Scripts\Activate.ps1
.\venv\Scripts\Activate.ps1 : File D:\Medichat v1\venv\Scripts\Activate.ps1 
cannot be loaded because running scripts is disabled on this system. For more 
information, see about_Execution_Policies at 
https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .\venv\Scripts\Activate.ps1
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
PS D:\Medichat v1> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
PS D:\Medichat v1> .\venv\Scripts\Activate.ps1
(venv) PS D:\Medichat v1> pip install flask flask-cors
WARNING: Cache entry deserialization failed, entry ignored
Collecting flask
  Using cached flask-3.1.3-py3-none-any.whl.metadata (3.2 kB)
Collecting flask-cors
  Downloading flask_cors-6.0.2-py3-none-any.whl.metadata (5.3 kB)
WARNING: Cache entry deserialization failed, entry ignored
Collecting blinker>=1.9.0 (from flask)
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting click>=8.1.3 (from flask)
  Downloading click-8.4.0-py3-none-any.whl.metadata (2.6 kB)
WARNING: Cache entry deserialization failed, entry ignored
Collecting itsdangerous>=2.2.0 (from flask)
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2>=3.1.2 (from flask)
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting markupsafe>=2.1.1 (from flask)
  Using cached markupsafe-3.0.3-cp314-cp314-win_amd64.whl.metadata (2.8 kB)
WARNING: Cache entry deserialization failed, entry ignored
Collecting werkzeug>=3.1.0 (from flask)
  Using cached werkzeug-3.1.8-py3-none-any.whl.metadata (4.0 kB)
Collecting colorama (from click>=8.1.3->flask)
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Using cached flask-3.1.3-py3-none-any.whl (103 kB)
Downloading flask_cors-6.0.2-py3-none-any.whl (13 kB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading click-8.4.0-py3-none-any.whl (116 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached markupsafe-3.0.3-cp314-cp314-win_amd64.whl (15 kB)
Using cached werkzeug-3.1.8-py3-none-any.whl (226 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Installing collected packages: markupsafe, itsdangerous, colorama, blinker, werkzeug, jinja2, click, flask, flask-cors
Successfully installed blinker-1.9.0 click-8.4.0 colorama-0.4.6 flask-3.1.3 flask-cors-6.0.2 itsdangerous-2.2.0 jinja2-3.1.6 markupsafe-3.0.3 werkzeug-3.1.8

[notice] A new release of pip is available: 25.3 -> 26.1.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(venv) PS D:\Medichat v1> python app_version1.py
Traceback (most recent call last):
  File "D:\Medichat v1\app_version1.py", line 2, in <module>
    from flask import Flask, render_init_string, render_template_string, request, redirect, url_for
ImportError: cannot import name 'render_init_string' from 'flask' (D:\Medichat v1\venv\Lib\site-packages\flask\__init__.py). Did you mean: 'render_template_string'?
(venv) PS D:\Medichat v1> python app_version1.py
 * Serving Flask app 'app_version1'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
(venv) PS D:\Medichat v1> python app_version1.py
 * Serving Flask app 'app_version1'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
127.0.0.1 - - [17/May/2026 22:41:59] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 22:41:59] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [17/May/2026 22:43:05] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 22:43:05] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 22:43:49] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 22:43:57] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 22:43:57] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 22:44:22] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 22:44:22] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [17/May/2026 22:44:51] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 22:44:51] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 22:45:07] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 22:45:07] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 22:48:19] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 22:48:20] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 22:48:25] "GET / HTTP/1.1" 200 -
 * Detected change in 'D:\\Medichat v1\\app_version1.py', reloading
 * Restarting with stat
(venv) PS D:\Medichat v1> ^C
(venv) PS D:\Medichat v1> python app_version1.py
 * Serving Flask app 'app_version1'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
127.0.0.1 - - [17/May/2026 22:57:58] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 22:58:02] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 22:58:06] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 22:58:06] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 22:59:03] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 22:59:03] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 22:59:15] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 22:59:15] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:02:24] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:02:24] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:02:37] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:02:37] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:03:01] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:03:01] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:03:15] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:03:15] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:04:27] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:04:27] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:04:42] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:04:42] "GET / HTTP/1.1" 200 -
 * Detected change in 'D:\\Medichat v1\\medichat_core.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
127.0.0.1 - - [17/May/2026 23:10:00] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:10:00] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:10:10] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:10:10] "GET / HTTP/1.1" 200 -
(venv) PS D:\Medichat v1> python app_version1.py
 * Serving Flask app 'app_version1'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
127.0.0.1 - - [17/May/2026 23:10:23] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:10:38] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:10:38] "GET / HTTP/1.1" 200 -
(venv) PS D:\Medichat v1> python app_version1.py
 * Serving Flask app 'app_version1'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
127.0.0.1 - - [17/May/2026 23:10:58] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:11:00] "GET /session/delete/ca99e491-5dde-4e38-92ef-d6983196fc73 HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:11:00] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:11:08] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:11:08] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:11:18] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:11:18] "GET / HTTP/1.1" 200 -
(venv) PS D:\Medichat v1> python app_version1.py
 * Serving Flask app 'app_version1'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
127.0.0.1 - - [17/May/2026 23:14:35] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:14:42] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:14:42] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:14:50] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:14:50] "GET / HTTP/1.1" 200 -
(venv) PS D:\Medichat v1> python app_version1.py
 * Serving Flask app 'app_version1'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
127.0.0.1 - - [17/May/2026 23:19:18] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:19:27] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:19:27] "GET / HTTP/1.1" 200 -
 * Detected change in 'D:\\Medichat v1\\medichat_core.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
(venv) PS D:\Medichat v1> python app_version1.py
 * Serving Flask app 'app_version1'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
127.0.0.1 - - [17/May/2026 23:21:47] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:22:02] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:22:02] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:22:19] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:22:19] "GET / HTTP/1.1" 200 -
 * Detected change in 'D:\\Medichat v1\\app_version1.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
(venv) PS D:\Medichat v1> python app_version1.py
 * Serving Flask app 'app_version1'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
127.0.0.1 - - [17/May/2026 23:31:51] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:31:55] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:31:55] "GET / HTTP/1.1" 200 -
 * Detected change in 'D:\\Medichat v1\\test_diagnostic.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
 * Detected change in 'D:\\Medichat v1\\test_diagnostic.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
(venv) PS D:\Medichat v1> python app_version1.py      
 * Serving Flask app 'app_version1'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
127.0.0.1 - - [17/May/2026 23:37:01] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:37:05] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:37:05] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:37:16] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:37:16] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:37:23] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:37:23] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:38:42] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:38:53] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:39:04] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:39:04] "GET / HTTP/1.1" 200 -
 * Detected change in 'D:\\Medichat v1\\medichat_core.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
(venv) PS D:\Medichat v1> python app_version1.py
 * Serving Flask app 'app_version1'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
127.0.0.1 - - [17/May/2026 23:50:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:50:40] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:50:40] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:51:38] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:51:38] "GET / HTTP/1.1" 200 -
 * Detected change in 'D:\\Medichat v1\\medichat_core.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
 * Detected change in 'D:\\Medichat v1\\app_version1.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
(venv) PS D:\Medichat v1> python app_version1.py
 * Serving Flask app 'app_version1'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-780-217
127.0.0.1 - - [17/May/2026 23:55:22] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:55:25] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:55:25] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2026 23:55:32] "POST /chat/send HTTP/1.1" 302 -
127.0.0.1 - - [17/May/2026 23:55:32] "GET / HTTP/1.1" 200 -
(venv) PS D:\Medichat v1> 