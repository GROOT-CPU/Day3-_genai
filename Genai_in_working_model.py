import numpy as np
import google.generativeai as genai 
from dotenv import load_dotenv
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
load_dotenv()

import os
key=os.getenv("GOOGLE_API_KEYS")
genai.configure(api_key=key)
model=genai.GenerativeModel("gemini-1.5-flash")
print(model)
res=model.generate_content(" what is the captial of japan")
print(res.text)

