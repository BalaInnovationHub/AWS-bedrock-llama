import boto3
import json
import os

prompt_data = """you are an python expert and write a program to generate fibonacci series"""



session = boto3.session.Session(
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_KEY'),
    aws_session_token=os.environ.get('SESSION_TOKEN'))

bedrock = session.client(service_name="bedrock-runtime")

payload = {
    "prompt":"[INST]"+ prompt_data +"[/INST]",
    "max_gen_len":512,
    "temperature":0.1,
    "top_p":0.9
}
body = json.dumps(payload)
model_id="meta.llama2-70b-chat-v1"
response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType ="application/json"
)

response_body = json.loads(response.get("body").read())
response_text = response_body['generation']
print(response_text)