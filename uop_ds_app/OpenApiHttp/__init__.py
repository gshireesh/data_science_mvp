import logging
import os

import azure.functions as func
import openai


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    API_KEY = os.environ.get(
        "OPENAPI_KEY", None
    )
    if API_KEY is None:
        raise Exception("api key needs to be present")
    openai.api_key = API_KEY
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(f"request data is not present. A request json with at"
                                 f" least `message` attribute should be sent", status_code=400)
    prompt = req_body.get("prompt")
    if not prompt:
        return func.HttpResponse(f"Prompt needs to be passed.", status_code=400)

    messages = [{"role": "user", "content": prompt}]
    output = openai.ChatCompletion.create(
        model=req_body.get("model", "gpt-3.5-turbo"),
        messages=messages,
        temperature=req_body.get("temperature", 0)
    )
    return func.HttpResponse(
        output.choices[0].message["content"],
        status_code=200
    )
