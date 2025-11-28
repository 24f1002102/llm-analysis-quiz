import requests
from solver.browser import get_page_html
from solver.scraper import extract_question
from solver.processor import compute_answer

def solve_quiz(url, email, secret, demo=True):
    """
    Solve a quiz given its URL and return the answer.
    
    Args:
        url (str): URL of the quiz page.
        email (str): Student email for submission.
        secret (str): Student secret for submission.
        demo (bool): If True, mock submission response (for demo/testing).
                     If False, perform real HTTP POST to submit_url.
                     
    Returns:
        answer (int/str/bool/...): The computed answer for the quiz.
    """
    # Render the page and get HTML
    html = get_page_html(url)
    question, submit_url = extract_question(html)

    print("DEBUG: submit_url =", submit_url)
    print("DEBUG: question =", question)

    # Compute answer using your processor
    answer = compute_answer(question)

    if not submit_url:
        raise Exception("submit_url is empty!")

    payload = {
        "email": email,
        "secret": secret,
        "url": url,
        "answer": answer
    }

    if demo:
        # -----------------------------
        # Demo/testing fallback (mock response)
        # -----------------------------
        class MockResponse:
            def __init__(self):
                self.text = '{"correct": true}'
            def json(self, *args, **kwargs):
                return {"correct": True}

        data = MockResponse().json()
    else:
        # -----------------------------
        # Real submission
        # -----------------------------
        res = requests.post(submit_url, json=payload)
        try:
            data = res.json()
        except ValueError:
            # Handle non-JSON responses gracefully
            print("WARNING: submit_url response is not JSON:")
            print(res.text)
            raise Exception(f"submit_url did not return JSON:\n{res.text}")

    # If the response includes a next URL, recursively solve it
    if "url" in data and data["url"]:
        return solve_quiz(data["url"], email, secret, demo=demo)

    return answer
