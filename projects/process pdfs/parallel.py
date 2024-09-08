from genai_gemini_parallel import *


RESULT_DICT = Manager().dict()
METADATA_DICT = Manager().dict()
PPROCESS = []







@timestamped_print
@parallel_blueprint.route('/', methods=['GET', 'POST'])
def phome_async():
    if request.method == 'POST':
        directory = request.form.get('dir')


        if os.path.exists(directory):
            #print("Directory exists!!")
            process = multiprocessing.Process(target=pgemini_chain_all_files, args=(directory, PROMPT_LIST, RESULT_DICT, METADATA_DICT))
            process.start()
            PPROCESS.append(process)
            print (f"for pgemini_chain_all_files: {process.pid}")
            return render_template('plive status.html', directory=directory)
        else:
            #print("No such directory")
            return render_template('gemini_app.html', heading="No such directory")


    return render_template('gemini_app.html', file_name=None)


@timestamped_print
@parallel_blueprint.route('/results', methods=['GET', "POST"])
def presults():
    if request.method == 'POST':
        directory = request.form.get('dir')
        print("presults; PPROCESS: ", PPROCESS)

        if PPROCESS:
            active_processes = [p for p in PPROCESS if psutil.pid_exists(p.pid)]
            print("presults; PPROCESS: ", PPROCESS)
            print("presults; active process: ", active_processes)
            if not active_processes:
                # Processes have completed
                all_responses_string, iint, oint, total_time = putil(RESULT_DICT, METADATA_DICT)
                return render_template('pgemini_responses.html',
                                       directory=directory, responses=all_responses_string, iint=iint, oint=oint, total_time=total_time)
            else:
                # Processes are still running
                return render_template('plive status.html', directory=directory)
        else:
            # No processes have been started
            return render_template('plive status.html', directory=directory)  # Return live status for idle state


    else:
        return render_template('gemini_app.html', file_name=None)



def pprocess_status():
    done_sent = False  # Flag to track if "done" has been sent

    while True:
        if not PPROCESS:
            status_string = "data: status: idle\n\n"
        else:
            active_processes = [p for p in PPROCESS if psutil.pid_exists(p.pid)]
            if not active_processes and not done_sent:
                status_string = "data: status: done\n\n"
                done_sent = True  # Set the flag to True
                #PPROCESS.clear()  # Clear the list only once
            elif not active_processes:
                # Keep yielding "done" until the connection is closed by the client
                status_string = "data: status: done\n\n"
            else:
                status_string = "data: status: processing\n\n"

        yield status_string
        time.sleep(1)




@parallel_blueprint.route("/events")
def pevents():
    return Response(pprocess_status(), content_type='text/event-stream')