import requests
import json 

url = "https://api.reddit.com/r/dancarlin/"
def get_json(url):
    r = requests.get(url)
    print(r.json())
    print(r.status_code)
    print("THE END")


def parse_json(json_file):
    with open(json_file) as f:
        data = json.load(f)   
        children = data['data']['children']
        #print(children)
        count = 0
        for child in children:
            print(f"[{count}] {child['data']['title']}")
            count += 1

def main():
    parse_json('api.reddit.com.json')

if __name__ == "__main__":
    main()
