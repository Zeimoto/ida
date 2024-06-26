# **Image Description Assistant**
---

If you want to use this repo, start by clonning it inside the directory you wish to work in:

`git clone https://github.com/Zeimoto/ida.git`

Now you must setup your python virtual environment to store your libraries without compromising other projects you might have.
To create you virtual environment simply run the following command inside the project directory:

`python -m virtualenv venv`

To activate the virtual environment run the following:<br>
(Linux\MacOS):

`source venv/bin/activate`

(windows):

`venv\Scripts\activate`

Now that your virtual environment has been created and activated you need to install all the library dependencies:

`pip install -r requirements.txt`

One other thing missing is the HuggingFace Access Token. For that you'll need to create your own HuggingFace account if you haven't already, and create an Access Key. <br>
For that you can follow [these instructions](https://huggingface.co/docs/hub/security-tokens). <br><br>
After that, you must create one last file inside the project directory:

`touch resources.py`

Inside the file simply add your HF access key, like so:

`HF_ACCESS_TOKEN="<your_access_key>"`

After that you should be good to go!

To run your program simply type the following command in your terminal:

`python app.py`
