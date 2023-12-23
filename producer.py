import requests
import json 

def get_json(url, data):
    r = requests.get(url)
    
    #In case the JSON decoding fails, r.json() raises an exception
    try:
       
        print(r.raise_for_status())
        with open(data, 'w+') as f:
            json.dump(r.json(), f )
        return r.status_code
    except Exception as e:
        return r.status_code


def parse_json(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)   
        children = data['data']['children']
        #print(children)
        count = 0
        for child in children:
            print(f"[{count}] {child['data']['title']}")
            count += 1

def main():
    url = "https://api.reddit.com/r/dancarlin/"
    file = "new_file.json"
    code_request = get_json(url, file)
    if code_request == 200:
        parse_json(file)
    else:
        print("there was a problem")

if __name__ == "__main__":
    main()
