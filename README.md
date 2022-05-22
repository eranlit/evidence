# Anecdotes - Backend Exercise - by Eran Litvak
Implements a simple service that asynchronously receives "events" with "evidence" objects in the format of JSON and knows how to convert them into a structured table based on
configuration.

## How to install
- Activate the virtual environment
- Install the requirements from requirements.txt
- Run the application with: ```uvicorn main:app```
- Go to:

http://127.0.0.1:8000 - app
http://127.0.0.1:8000/docs - documentation
http://127.0.0.1:8000/redoc - alternative documentation

## App Folders
- main.py: Implements FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- routes: Implements the 'evidence/upload' route for uploading a JSON file containing evidence
- payloads: Sample evidence JSON files (just for testing)
- parsers: Implements the evidence parser for switching between different evidence types
- models: Implements pydantic model for each evidence type (generated automatically by using https://jsontopydantic.com/)

## Test Evidence Parser
- Go to: http://127.0.0.1:8000/docs
- Expand the POST method 'evidence/upload'
- Click 'Try it out' button
- Click on 'Choose File' button and select one of the files from payloads folder
- Click on 'Execute'
- Examine the results in the 'Response body' section

### Step 3 (Bonus, Just theoretical)
Assuming that we receive a lot of evidence, and every evidence includes tons of rows (for
instance, evidence data with 100K entries) - are you extracting the evidence payload
efficiently?

I would have used a NO-SQL database like 'MongoDB' to store each evidence type in its own collection. Then call my custom select for each evidence type.
For a scenario where an immediate response is not required, you can go back to the user with a message like "your upload is being processed” and continue to perform the data processing in a background task. When the data processing is done you can send a message to the user saying you can access your data now with a link to the results.




