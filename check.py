import requests

def check_subreddit_exists(subreddit):
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers = {'User-agent': 'your bot 0.1'})
    return response.status_code != 404

def write_existing_subreddits_to_file(subreddits):
    with open('existing_subreddits.txt', 'w') as f:
        for i, subreddit in enumerate(subreddits, start=1):
            exists = check_subreddit_exists(subreddit)
            if exists:
                f.write(f'{subreddit}\n')
            print(f'{i}. {"exists" if exists else "does not exist"}')

def read_subreddits_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

# Read list of subreddits from file
subreddits = read_subreddits_from_file('subreddits.txt')

write_existing_subreddits_to_file(subreddits)