from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Knowledge base with rules
knowledge_base = {
    "Migraine": [
        "throbbing pain",
        "sensitivity to light",
        "nausea",
        "pain worsens with activity"
    ],
    "Tension Headache": [
        "dull pain",
        "forehead or back of head",
        "stress or anxiety",
        "no sensitivity to light"
    ],
    "Cluster Headache": [
        "severe pain",
        "around one eye",
        "occurs in patterns or clusters",
        "restlessness"
    ],
    "Sinus Headache": [
        "pain around cheeks or forehead",
        "fever",
        "stuffy nose",
        "sinus infection symptoms"
    ]
}

# Backward chaining function
def diagnose_headache(symptoms):
    symptoms = [s.strip() for s in symptoms]  # Clean extra spaces

    # Loop through each headache type
    for headache_type, rules in knowledge_base.items():
        match_count = 0

        # Check if any rule matches the symptoms
        for rule in rules:
            if any(rule.lower() in symptom for symptom in symptoms):  # Match part of the symptom
                match_count += 1

        # If all the rules for a headache type match, return the diagnosis
        if match_count >= len(rules):  # Ensure most rules are matched
            return headache_type

    return "No matching headache type found. Please consult a doctor."


# Home route to render the HTML page
@app.route("/")
def home():
    return render_template("index.html")  # This renders the HTML page

# Chatbot endpoint to process symptoms and return diagnosis
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    symptoms = user_input.lower().split(", ")  # Expect symptoms as a comma-separated string
    diagnosis = diagnose_headache(symptoms)
    return jsonify({"response": f"Based on the symptoms, it seems like you have: {diagnosis}."})

if __name__ == "__main__":
    app.run(debug=True)
