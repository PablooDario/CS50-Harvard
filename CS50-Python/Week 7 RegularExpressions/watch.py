import re

#Given an html iframe tag, extract the youtube url if it exists

# Valid urls
# http://youtube.com/embed/...
# https://youtube.com/embed/...
# https://www.youtube.com/embed/...

# Example: <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'src="(https?://(?:www\.)?youtube.com/embed/)(\w+)"'
    if url := re.search(pattern, s):
        return "https://youtu.be/" +url.group(2)
    return None


if __name__ == "__main__":
    main()