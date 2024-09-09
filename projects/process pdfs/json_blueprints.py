from genai_gemini_parallel import *

json_blueprint = Blueprint('json', __name__)


@json_blueprint.route ("/process")
def json_all_processes ():
    active_processes_L0 = [p for p in PROCESS_L0 if psutil.pid_exists(p)]
    active_processes_L1 = [p for p in PROCESS_L1 if psutil.pid_exists(p)]
    active_processes_dict = {
        "L0 target": "pgemini_chain_all_files()",
        "L1 target": "psingle_file()",
        "active_level_L0": active_processes_L0,
        "active_level_L1": active_processes_L1,
        "level_L0": PROCESS_L0,
        "level_L1": PROCESS_L1
    }
    return jsonify(active_processes_dict)


