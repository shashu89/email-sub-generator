#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from dotenv import load_dotenv
#from IPython.display import Markdown, display
from openai import OpenAI


# In[2]:


# Load environment variables in a file called .env

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

# Check the key

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")


# In[ ]:


openai = OpenAI()
     
system_prompt = """
You are a helpful assistant that analyzes the contents of a email,
and provides a subject line for the same.
"""

user_prompt_prefix = """
Here are the contents of a email.
Provide a subject line for the email.
"""


# In[5]:


def generateSubject(email_content: str) -> str:
    response = openai.chat.completions.create(model="gpt-5-nano", messages=
        [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt_prefix + email_content}
        ]
    )
    return response.choices[0].message.content


# In[7]:

'''
email_content = """
    Dear Team,

    I hope this message finds you well. I wanted to remind everyone about the upcoming project deadline next Friday. Please ensure that all your tasks are completed and submitted by then.

    Additionally, we will be having a team meeting on Wednesday at 10 AM to discuss our progress and address any challenges we may be facing. Your attendance is important.

    Thank you for your hard work and dedication.

    Best regards,
    Manager
"""


# In[8]:


email_content = """
    Hi,

    Is this API publicly available?

    I was trying run on port 9000 as per the example shown in website:
    https://kgis.ksrsac.in:9000/genericwebservices/ws/districtcode?districtname=Bengaluru(Urban)

    But this shows connection timeout.
    Please confirm.

    Thanks,
    Shashank
"""
'''
