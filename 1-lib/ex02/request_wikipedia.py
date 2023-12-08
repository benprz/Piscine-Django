import requests, json, dewiki, sys

def request_wikipedia(title):
    api = "https://en.wikipedia.org/w/api.php"
    search = "?action=opensearch&search={title}"
    parse = "?action=parse&page={page}&format=json"

    # Search the page
    response = requests.get(api + search.format(title=title))
    # for e in response.json():
    #     print(e, end="\n\n")

    if response.status_code == 200:
        response_json = response.json()
        if (len(response_json[1]) == 0):
            print("Error: No page found")
            sys.exit(1)
        page = response_json[1][0]
    else:
        print("Error: HTTP status code {code}".format(code=response.status_code))
        sys.exit(1)

    # Get the page content
    response = requests.get(api + parse.format(page=page))
    # for e in response.json():
    #     print(e, end="\n\n")

    if response.status_code == 200:
        json = response.json()
        if "parse" not in json:
            print("Error: No page found")
            sys.exit(1)
        content = json["parse"]["text"]["*"]
        print(dewiki.from_string(content))
        pass
        
    else:
        print("Error: HTTP status code {code}".format(code=response.status_code))
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python request_wikipedia.py <title>")
        sys.exit(1)
    request_wikipedia(sys.argv[1])
