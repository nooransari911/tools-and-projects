from genai_gemini_app import *
from flask import Blueprint

test_blueprint = Blueprint('test', __name__)


@test_blueprint.route("/json")
def test_json():
    test_results = []

    try:
        with open("test-steps.json", "r") as f:
            test_cases = json.load(f).get("tests", [])

        base_url = request.host_url  # Use the current request's host URL

        if not test_cases:
            return jsonify({"summary": "No test cases found", "detailed_output": test_results})

        for test_case in test_cases:
            method = test_case.get("method")
            url = base_url + test_case.get("url", "")
            data = test_case.get("data", {})

            if not method or not url:
                test_results.append(f"Invalid test case: {test_case}")
                continue

            try:
                if method == "GET":
                    response = requests.get(url)
                elif method == "POST":
                    response = requests.post(url, data=data)
                else:
                    test_results.append(f"Unsupported method: {method} for URL: {url}")
                    continue

                # Check response status code and validate content if necessary
                if response.status_code == 200:
                    test_results.append(f"{method} {url}: Success")
                    # Add more specific assertions if needed
                    # For example:
                    # if "expected_text" in response.text:
                    #     test_results.append("Response contains expected text.")
                    # else:
                    #     test_results.append("Response does not contain expected text.")
                else:
                    test_results.append(f"{method} {url}: Failed (Status code: {response.status_code})")
                    test_results.append(response.text)  # Print the error response for debugging

            except requests.RequestException as e:
                test_results.append(f"{method} {url}: Exception occurred - {str(e)}")

        return jsonify({"summary": "Tests completed", "detailed_output": test_results})

    except FileNotFoundError:
        return jsonify({"error": "Test cases file not found"})
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON from test cases file"})
    except Exception as e:
        return jsonify({"error": str(e)})


@test_blueprint.route("/")
def test():
    return render_template("test_results.html")