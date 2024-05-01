import vertexai
from vertexai.language_models import TextGenerationModel
from bs4 import BeautifulSoup as bs
import io
import pypandoc
import panflute


def summ (text):
    project_id = "optimum-task-411411"
    location = "us-west1"
    
    vertexai.init(project=project_id, location=location)
    
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.95,
        "top_k": 40,
    }

    model = TextGenerationModel.from_pretrained("text-bison@002")
    
    #j = "Bonsoir, a bientot"
    
    response = model.predict (text, **parameters)
    
    print (f"Response is: {response.text}")
    
    return response


data = pypandoc.convert_file ("sample.md", "html")
soup = bs (data, "html.parser")

head = soup.find_all ("h2")
text = soup.find_all ("p")

op = open ("op.md", "w")

for i, j in zip (head, text):
    op.write (f"## {i.string}\n")
    
    res = summ (j.string)
    op.write (f"{res.text}\n\n")
    
op.close ()
