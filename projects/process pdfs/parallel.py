from genai_gemini_parallel import *


RESULT_DICT = Manager().dict()
METADATA_DICT = Manager().dict()
PPROCESS = []








@parallel_blueprint.route('/', methods=['GET', 'POST'])
def phome_async():
    if request.method == 'POST':
        directory = request.form.get('dir')


        if os.path.exists(directory):
            #print("Directory exists!!")
            process = multiprocessing.Process(target=pgemini_chain_all_files, args=(directory, PROMPT_LIST, RESULT_DICT, METADATA_DICT))
            process.start()
            PPROCESS.append(process)
            return render_template('plive status.html', directory=directory)
        else:
            #print("No such directory")
            return render_template('gemini_app.html', heading="No such directory")


    return render_template('gemini_app.html', file_name=None)



@parallel_blueprint.route('/results', methods=['GET', "POST"])
def presults():
    if request.method == 'POST':
        directory = request.form.get('dir')

        if PPROCESS and not PPROCESS [-1].is_alive():
            # Return the result (either success or failure) as a JSON response
            all_responses_string, iint, oint, total_time = putil (RESULT_DICT, METADATA_DICT)
            return render_template ('pgemini_responses.html',
                                   directory=directory, responses=all_responses_string, iint=iint, oint=oint, total_time=total_time)

        else:
            return render_template('plive status.html', directory=directory)

    else:
        return render_template('gemini_app.html', file_name=None)



def pprocess_status():
    while True:  # Keep checking the status indefinitely
        if not PPROCESS:  # Handle the case where the list is empty
            status_string = "data: status: idle\n\n"
        else:
            status_value = PPROCESS[-1].is_alive()
            if status_value == False:
                status_string = "data: status: done\n\n"
                #PPROCESS.pop()  # Remove the finished process from the list
            else:
                status_string = "data: status: processing\n\n"
        yield status_string
        time.sleep(1)




@parallel_blueprint.route("/events")
def pevents():
    return Response(pprocess_status(), content_type='text/event-stream')