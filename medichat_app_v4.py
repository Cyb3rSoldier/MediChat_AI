from flask import Flask, render_template_string, request, redirect, url_for
from medichat_core import SymptomExtractorBFS, DiseaseMatcher, SessionStoreManager

app = Flask(__name__)

extractor = SymptomExtractorBFS()
session_manager = SessionStoreManager()
current_session_id = session_manager.create_session()

UI_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>MediBlast AI Chat</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background: linear-gradient(135deg, #104860d3, #2e6284);
      height: 100vh;
      display: flex;
      margin: 0;
      font-family: Arial, sans-serif;
    }
    .sidebar {
      width: 300px;
      background: #1e293b;
      color: white;
      display: flex;
      flex-direction: column;
      padding: 15px;
      border-right: 1px solid #334155;
    }
    .sidebar h2 { font-size: 20px; margin-top: 0; padding-bottom: 10px; border-bottom: 1px solid #334155; font-weight: bold; }
    .session-btn { background: #0d6efd; color: white; border: none; padding: 10px; border-radius: 8px; cursor: pointer; margin-bottom: 15px; width: 100%; font-weight: bold; }
    .session-list { flex: 1; overflow-y: auto; list-style: none; padding: 0; margin: 0; }
    .session-item { padding: 10px; border-radius: 8px; margin-bottom: 8px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #334155; }
    .session-item.active { background: #0d6efd; }
    .session-item a { color: white; text-decoration: none; flex: 1; font-size: 14px; text-overflow: ellipsis; overflow: hidden; white-space: nowrap; }
    .del-btn { color: #f87171; text-decoration: none; font-size: 12px; margin-left: 5px; padding: 2px 8px; background: #475569; border-radius: 5px; font-weight: bold; }
    .del-btn:hover { background: #ef4444; color: white; }
    .chat-container {
      flex: 1;
      height: 100vh;
      background: #022141;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }
    .chat-header { background: #0d6efd; color: white; padding: 20px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); }
    .chat-header h2 { margin: 0; font-weight: bold; font-size: 24px; }
    .chat-box { flex: 1; padding: 20px; overflow-y: auto; background: #022141; display: flex; flex-direction: column; }
    .message { margin-bottom: 15px; padding: 12px 15px; border-radius: 15px; max-width: 80%; word-wrap: break-word; line-height: 1.5; }
    .user-message { background: #89b4f4; color: white; margin-left: auto; border-bottom-right-radius: 0; }
    .bot-message { background: #e9ecef; color: #333; margin-right: auto; border-bottom-left-radius: 0; white-space: pre-wrap; font-family: monospace; font-size: 13px; }
    .chat-input { padding: 15px; border-top: 1px solid #ddd; background: white; }
    .powered { text-align: center; font-size: 14px; color: gray; padding-top: 5px; padding-bottom: 5px; background: white; }
    .send-btn, input.form-control { border-radius: 10px; }
  </style>
</head>
<body>

  <div class="sidebar">
    <h2>MediBlast Sessions</h2>
    <form action="/session/new" method="POST">
      <button class="session-btn" type="submit">+ New Session</button>
    </form>
    <ul class="session-list">
      {% for s in sessions %}
      <li class="session-item {% if s.id == active_id %}active{% endif %}">
        <a href="/session/select/{{ s.id }}">{{ s.title }}</a>
        <a class="del-btn" href="/session/delete/{{ s.id }}">Del</a>
      </li>
      {% endfor %}
    </ul>
  </div>

  <div class="chat-container">
    <div class="chat-header">
      <h2>Submissions Diagnostic Center</h2>
      <p class="mb-0 text-white-50">Active Tracker: {{ active_session.title if active_session else "None" }}</p>
    </div>

    <div class="chat-box" id="chatBox">
      {% if not active_session or not active_session.messages %}
        <div class="message bot-message">Hello! 👋<br>I am your AI Medical Assistant. Describe your symptoms in plain language (e.g., "I have a running nose and fever").</div>
      {% endif %}
      
      {% if active_session %}
        {% for m in active_session.messages %}
          <div class="message {% if m.sender == 'user' %}user-message{% else %}bot-message{% endif %}">
            {% if m.sender == 'user' %}<strong>USER:</strong> {% endif %}{{ m.text }}
          </div>
        {% endfor %}
      {% endif %}
    </div>

    <div class="chat-input">
      <form action="/chat/send" method="POST" class="input-group">
        <input type="hidden" name="session_id" value="{{ active_id }}">
        <input type="text" name="message" class="form-control" placeholder="Type symptoms here..." required autocomplete="off">
        <button class="btn btn-primary send-btn" type="submit">Send</button>
      </form>
    </div>
    
    <div class="powered">Powered By MediBlast</div>
  </div>

  <script>
    window.onload = function() {
      var cb = document.getElementById('chatBox');
      cb.scrollTop = cb.scrollHeight;
    };
  </script>
</body>
</html>
"""

@app.route('/')
def index():
    global current_session_id
    sessions = session_manager.get_all_sessions()
    active_session = session_manager.sessions.get(current_session_id)
    return render_template_string(UI_TEMPLATE, sessions=sessions, active_id=current_session_id, active_session=active_session)

@app.route('/session/new', methods=['POST'])
def new_session():
    global current_session_id
    current_session_id = session_manager.create_session()
    return redirect(url_for('index'))

@app.route('/session/select/<string:sid>')
def select_session(sid):
    global current_session_id
    if sid in session_manager.sessions:
        current_session_id = sid
    return redirect(url_for('index'))

@app.route('/session/delete/<string:sid>')
def delete_session(sid):
    global current_session_id
    session_manager.delete_session(sid)
    all_sess = session_manager.get_all_sessions()
    if all_sess:
        current_session_id = all_sess[0]["id"]
    else:
        current_session_id = session_manager.create_session()
    return redirect(url_for('index'))

@app.route('/chat/send', methods=['POST'])
def send_chat():
    sid = request.form.get('session_id')
    user_msg = request.form.get('message', '').strip()
    
    if sid and user_msg:
        session_manager.add_message(sid, "user", user_msg)
        extracted = extractor.extract(user_msg)
        matches = DiseaseMatcher.find_matches(extracted)
        
        output_buffer = []
        symptoms_str = ', '.join(extracted) if extracted else 'None'
        output_buffer.append(f"Extracted Key Symptoms: {symptoms_str}\n")
        
        if not matches:
            output_buffer.append("No matching conditions identified in the local directory map.")
        else:
            for index, match in enumerate(matches, start=1):
                disease = match["disease"]
                confidence_pct = int(match["confidence"] * 100)
                match_rate_pct = int(match["match_rate"] * 100)
                
                output_buffer.append(f"{index}. Condition: {disease['name']} (Confidence: {confidence_pct}%) (match rate : {match_rate_pct}%)")
                output_buffer.append(f"{disease['description']}")
                
                all_disease_symptoms = ", ".join(disease["symptoms"])
                output_buffer.append(f"symtoms: {all_disease_symptoms}.")
                
                output_buffer.append("Recommended types of Specialists:")
                for doc in disease["doctors"]:
                    output_buffer.append(f" - {doc['specialty']}: {doc['reason']}")
                    
                output_buffer.append("Actionable Directives:")
                for behavior in disease["behaviors"]:
                    output_buffer.append(f" - {behavior}")
                
                if index < len(matches):
                    output_buffer.append("-" * 40)
        
        bot_response_text = "\n".join(output_buffer)
        session_manager.add_message(sid, "bot", bot_response_text)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)