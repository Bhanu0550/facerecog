import json, requests, subprocess, shlex

def execute_request():
    bashCommand = '''curl --request POST --url https://lambda-face-recognition.p.rapidapi.com/recognize 
    --header 'content-type: multipart/form-data' 
    --header 'x-rapidapi-host: lambda-face-recognition.p.rapidapi.com' 
    --header 'x-rapidapi-key: your_rapid_api_key' 
    --form albumkey=album_key
    --form album=ADMINS --form files=@photo.jpg'''

    args = shlex.split(bashCommand)
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    output, error = process.communicate()
    json_obj = json.loads(output)
    return json_obj

def check_confidence(json_obj):
    if json_obj['status'] == 'success':
        if len(json_obj['photos'][0]['tags']) == 0:
            return False
        confidence = json_obj['photos'][0]['tags'][0]['uids'][0]['confidence']
        flag = False
        if confidence > 0.5:
            flag = True
        return flag
