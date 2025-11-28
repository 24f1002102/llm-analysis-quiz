import requests
import json

# ---------------- CONFIG ----------------
API_URL = "http://127.0.0.1:5000/quiz"
EMAIL = "24f1002102@ds.study.iitm.ac.in"
SECRET = "MySecret123"
QUIZ_URL = "https://tds-llm-analysis.s-anand.net/demo"

# ---------------- POST PAYLOAD ----------------
payload = {
    "email": EMAIL,
    "secret": SECRET,
    "url": QUIZ_URL
}

# ---------------- SEND REQUEST ----------------
res = requests.post(API_URL, json=payload)
print("Status code:", res.status_code)

try:
    data = res.json()
except:
    print("Response is not JSON")
    print(res.text)
    exit()

# ---------------- PRINT STEP-WISE DETAILS ----------------
if "steps" in data:
    for i, step in enumerate(data["steps"], start=1):
        print(f"\n--- Step {i} ---")
        print("Quiz URL:", step.get("quiz_url"))
        print("Submitted Answer:", step.get("answer_submitted"))
        print("Submit URL:", step.get("submit_url"))
        submit_resp = step.get("submit_response", {})
        if submit_resp.get("correct") is not None:
            print("Correct?:", submit_resp.get("correct"))
            print("Next URL:", submit_resp.get("url"))
            print("Reason:", submit_resp.get("reason"))
        else:
            print("Submit Response:", submit_resp)
        if step.get("plot_b64"):
            print("Plot generated (base64 length):", len(step["plot_b64"]))
else:
    print(json.dumps(data, indent=2))
