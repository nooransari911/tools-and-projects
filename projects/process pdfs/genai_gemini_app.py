from flask import Flask, request, render_template, jsonify
from genai_gemini import *
from functools import wraps

app = Flask(__name__)


def time_route(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        duration = time.time() - start_time
        print(f"Route {f.__name__} took {duration:.4f} seconds")
        return result
    return wrapper


def time_route2(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = f(*args, **kwargs)
            duration = time.time() - start_time
            print(f"Route {f.__name__} took {duration:.4f} seconds")

            # Handle the return types properly
            if isinstance(result, Response):
                return result
            elif isinstance(result, (str, bytes)):
                return result
            elif isinstance(result, tuple):
                # Unpack the tuple if it contains a Response object and a status code
                if isinstance(result[0], Response):
                    return result[0]
                else:
                    return Response(response=result[0], status=result[1] if len(result) > 1 else None)
            elif isinstance(result, dict):
                # For JSON responses, convert the dictionary to a JSON response
                return jsonify(result)
            else:
                raise TypeError("Unsupported return type")
        except Exception as e:
            print(f"Error in route {f.__name__}: {e}")
            raise

    return wrapper



@app.route('/', methods=['GET', 'POST'])
@time_route
def home():
    if request.method == 'POST':
        directory = request.form.get('dir')

        if os.path.exists(directory):
            #print("Directory exists!!")
            responses = gemini_chain_all_files(directory)
            json_data = {
                'heading': "Selected directory:",
                'directory': directory,
                'responses': responses
            }
            #print(responses)
            return render_template ('gemini_responses.html',
                                    directory=directory, responses=responses)
        else:
            #print("No such directory")
            return render_template('gemini_app.html', heading="No such directory")


    return render_template('gemini_app.html', file_name=None)




if __name__ == '__main__':
    app.run(debug=True)
