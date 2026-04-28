import re
import sys

def main():
    HTML = input("Html: ")
    
    print(prase(HTML))



def prase(s):
    match = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_]+)"', s)

    if match:
        video_id = match.group(1)
        return  f"https://youtu.be/{video_id}"
    
    return None


if __name__ == "__main__":
    main()
