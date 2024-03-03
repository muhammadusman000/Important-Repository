import requests

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
api_key = "AIzaSyCmRXbYhBYz_xz5Gunn9RSFGavRG0p6fQA"
request_list=["What is CNAPP Cloud Native, giving details of each layer","Elaborate More","Elaborate it in more depth"]
responses=[""]
count = 0
for r in request_list:
  print("RESQUEST NO ",count+1)
  headers = {
      "Content-Type": "application/json"
  }

  data = {
      "contents": [
          {
              "parts": [
                  {
                      "text": r+responses[count]
                  }
              ]
          }
      ]
  }
  params = {
      "key": api_key
  }

  response = requests.post(url, headers=headers, json=data, params=params)
  if response.status_code == 200:
      # Extract and print the text part from the response
      text_part = response.json().get('candidates', [])[0].get('content', {}).get('parts', [])[0].get('text', '')
      responses.append(text_part)
    #  print(text_part)
  else:
      print(f"Error: {response.status_code}")
  count=count+1

text=""
print("Result of the responses")
for i in range(0,len(responses)):
  if i>0:
    print(f"RESPONSE NO{i}\n",responses[i])
    text=text+" "+responses[i]


print("KNOWLEDGE GRAPH")

import spacy
# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Process the text
doc = nlp(text)

# Extract entities and relationships
knowledge_graph = []

for ent in doc.ents:
    knowledge_graph.append((ent.text, ent.label_))

for token in doc:
    if token.dep_ == "prep" and token.head.pos_ == "NOUN":
        knowledge_graph.append((token.text, token.head.text))

# Print the knowledge graph
for item in knowledge_graph:
    print(item)
