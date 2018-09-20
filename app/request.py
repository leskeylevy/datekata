import urllib.request, json
from .models import Github_username

# getting the api key
api_key = None

# getting base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['GITHUB_API_BASE_URL']
    base_url = 'https://api.github.com/search/users?q={}'
    # print(base_url)


def get_github_user(username):
    dump_url = 'https://api.github.com/search/users?q={}'
    '''
    function that gts the json response to our url request
    '''
    search_github_url = dump_url.format(username)
    with urllib.request.urlopen(search_github_url) as url:
        search_github_data = url.read()
        search_github_response = json.loads(search_github_data)

        search_github_results = None
        print(search_github_url)
        if search_github_response['items']:
            search_github_list = search_github_response['items']
            search_github_results = process_results(search_github_list)
    return search_github_results


def process_results(user_list):
    '''
    processing  the search results
    '''
    user_results = []
    for user in user_list:
        username = user.get('login')

        if username:
            user_object = Github_username(username)
            user_results.append(user_object)

    return user_results
