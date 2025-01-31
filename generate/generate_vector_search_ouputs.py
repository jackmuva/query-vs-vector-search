import requests
import pandas as pd
import re

url = "http://localhost:3000"

data = {
    "email": "jack.mu@useparagon.com"
}

response = requests.post(url + "/api/auth/signJwt", json=data)
jwt = response.json()['jwt']

goldens_df = pd.read_csv("../results/golden.csv")
goldens_dict = goldens_df.to_dict()
for i in goldens_dict[list(goldens_dict.keys())[0]].keys():
    prompt = goldens_dict['input'][i]
    actual_response = ""
    actual_context = ""
    messages = [{"content": prompt,
                "role": "user",
                 }]
    body = {"messages": messages, "tools": {}}
    response = requests.post(url + "/api/chat", json=body, headers={"Authorization": "Bearer " + jwt}, stream=True)
    if response.status_code==200:
        with response:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    try:
                        if chunk.decode('utf-8')[:2] == "0:":
                            actual_response += str(chunk.decode('utf-8')[2:]).replace('"', '').replace("\n", " ")
                        else:
                            raw = chunk.decode('utf-8')

                            pattern = r'(?<="content":")[^"]*'
                            match = re.search(pattern, raw)
                            if match:
                                extracted_text = match.group(0)
                                actual_context += extracted_text.replace('"', '').replace("\n", " ")
                    except:
                        continue
    goldens_dict['actual_output'][i] = actual_response
    goldens_dict['retrieval_context'][i] = actual_context 
output_df = pd.DataFrame.from_dict(goldens_dict)
output_df.to_csv("../results/parato-outputs.csv")
