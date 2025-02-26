# UnderstandPython

[ZTM:PythonDev](https://github.com/aneagoie/ztm-python-course-exercises)

---

[Expert Python Tutorial #1 - Overview of Python & How it Works](https://youtu.be/mclfteWlT2Q?si=y1G2sLThk26xOCEn)

## Decorator

- Decorator is a function that modifies another function
- There's a bunch of built in decorators in python and we can create our own as well
- let's start with a custom decorator

## PYTHON API TO Control access to an LLM or an Model.

- use Ollama to run LLM locally.once you download it , open cmd and run `ollama`. To pull a model we do `ollama pull mistral`. to use that model we do `ollama run mistral` opens up a chat and to exit it - we do `/bye`. will be using llama3.2 for now.
- now we will use ollama from python code. 
- `pip install -r requirements.txt`
- `uvicorn main:app`  -- main is name of the file and app is our fastapi application , -- reload runs in dev mode