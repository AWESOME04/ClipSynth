from openai import OpenAI
from typing import List
from pydantic import BaseModel, Field
import instructor 

class Character(BaseModel):
    name: str

class Response(BaseModel):
    characters : List[Character]
    scene: str
    script: List[str]





# client = instructor.from_openai(
#     OpenAI(
#         base_url = "",
#         api_key="ollama"
#     )
#      mode=instructor.Mode.JSON,
# )

client = instructor.from_openai(
    client=OpenAI(api_key="*********************************************"),
    mode = instructor.Mode.TOOLS,
)

resp = client.chat.completions.create(
    model = "gpt-4-turbo",
    messages= [
        {"role": "system",
         "content": "You are an expert in writing a video script from\
           a story a user tells. From the story, choose generic names for the characters.\
          Create a description for the scenes for the story, this scene would be used to set up a video.\
            After that, write a script for the scene including what each user is supposed to say during the scene.\
          I want a very long script"},

        {"role": "user" ,
         "content" :"generate a story for two people who are the only people left and the world is about to end"}
    ],
    response_model= Response,
)



print(resp.model_dump_json(indent=3))

