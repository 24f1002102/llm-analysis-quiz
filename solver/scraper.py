from bs4 import BeautifulSoup
import json
import base64
import re

def extract_question(html):
    soup = BeautifulSoup(html, "html.parser")

    # Extract human-readable text
    text = soup.get_text(" ", strip=True)

    # Find question like: Q834. Download file...
    question_match = re.search(r"Q\d+.*", text)
    question = question_match.group(0) if question_match else text

    submit_url = None

    # Try to find JSON inside <pre> tags
    pre_tags = soup.find_all("pre")
    for pre in pre_tags:
        decoded_str = pre.text.strip()
        try:
            # Attempt base64 decoding
            decoded_bytes = base64.b64decode(decoded_str)
            decoded_str = decoded_bytes.decode("utf-8")
        except Exception:
            pass

        try:
            js = json.loads(decoded_str)
            submit_url = js.get("url") or js.get("submit_url")
            if submit_url:
                break
        except Exception:
            continue

    if not submit_url:
        raise Exception("Could not find submit URL in the quiz page")

    return question, submit_url
