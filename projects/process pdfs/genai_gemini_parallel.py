from utils import *
from genai_gemini import extract_numbers, upload_directory_to_genai, delete_all_genai_files

import os
from functools import partial
import concurrent.futures


parallel_blueprint = Blueprint('parallel', __name__)
manager = Manager()
task_results = manager.dict()
PROCESS: list[multiprocessing.Process] = []


genai.configure(api_key=os.environ["API_KEY_FREE"])

model = genai.GenerativeModel("gemini-1.5-flash")




def pupload_file_to_genai(directory_path, filename):
    """Uploads a single file to GenAI."""
    file_path = os.path.join(directory_path, filename)
    try:
        genai_file = genai.upload_file(
            path=file_path,
            display_name=filename  # Set display name to the file name
        )
        print(f"Uploaded: {filename} (ID: {genai_file.name})")
    except Exception as e:
        print(f"Error uploading {filename}: {e}")

def pupload_directory_to_genai(directory_path):
    """Uploads all files in a directory to GenAI in parallel."""
    if not os.path.isdir(directory_path):
        print(f"The directory {directory_path} does not exist.")
        return

    filenames = os.listdir(directory_path)
    filenames = [f for f in filenames if os.path.isfile(os.path.join(directory_path, f))]
    filenames.sort(key=lambda x: extract_numbers(x), reverse=True)  # Case-insensitive sorting

    if not filenames:
        print("No files to upload.")
        return

    print("Sorted filenames:", filenames)

    # Use a pool of workers to upload files in parallel
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.starmap(pupload_file_to_genai, [(directory_path, filename) for filename in filenames])



def pgemini_chain (prompt_list, file=None):
    gemini_input = [file] if file else []
    #gemini_input = LOREM_IPSUM_STRING
    gemini_response = None


    if not prompt_list:
        raise Exception("Empty List")
        return


    for pri in prompt_list:
        # Append the current prompt to the input
        gemini_input.append(pri)

        # Add previous response (if available) to the current prompt
        if gemini_response:
            gemini_input.append(gemini_response.text)

        # Send the input (PDF or previous response + current prompt) to Gemini
        gemini_response = model.generate_content(gemini_input)
        #time.sleep(80)
        RESPONSES.append (gemini_response.text)
        gemini_input = []

    with open (output_file, "w") as md_output_file:
        md_output_file.write (f"{datetime.datetime.now ()};\n\n{gemini_response.text}")
    with open(all_iterations_file, "w") as md_file:
        md_file.write (f"{datetime.datetime.now ()};\n\n{RESPONSES}")

    # Return Gemini output text
    return gemini_response.text




@timestamped_print
def psingle_file (file, directory, prompt_list, result_dict, metadata_dict):
    print(f"Processing file {file.display_name}")
    time_start = time.time_ns()
    iint = model.count_tokens(file).total_tokens
    gemini_response = pgemini_chain(prompt_list, file)
    oint = model.count_tokens(gemini_response).total_tokens
    time_end = time.time_ns()
    elapsed_time = (time_end - time_start) / (10 ** 9)

    result_dict [file.display_name] = {
        "status": "completed",
        "directory": directory,
        "file name": file.display_name,
        "response": gemini_response
    }

    metadata_dict [file.display_name] = {
        "status": "completed",
        "directory": directory,
        "file name": file.display_name,
        "input tokens": iint,
        "output tokens": oint,
        "time_taken": elapsed_time
    }



    print(f"Done processing file {file.display_name}")




def pgemini_chain_all_files (directory, prompt_list, result_dict, metadata_dict):
    upload_directory_to_genai(directory)


    for file in genai.list_files():
        process = multiprocessing.Process (target=psingle_file, args=(file, directory, prompt_list, result_dict, metadata_dict)).start()



@timestamped_print
def putil (result_dict, metadata_dict):
    # 1. Create a new string with all values from result_dict[]["response"]
    all_responses_string = ""
    for file_data in result_dict.values():
        all_responses_string += file_data["response"]

    # 2. Calculate the sum of all iint and oint in metadata_dict
    total_iint = 0
    total_oint = 0
    total_time = 0
    for file_data in metadata_dict.values():
        total_iint += file_data["input tokens"]
        total_oint += file_data["output tokens"]
        total_time += file_data["time_taken"]

    # Print the results (or do whatever you need with them)
    #print("All responses string:", all_responses_string)
    print("Total input tokens:", total_iint)
    print("Total output tokens:", total_oint)
    print("Total output tokens:", total_time)
    print ("All keys in result_dict:", result_dict.keys())

    return all_responses_string, total_iint, total_oint, total_time
