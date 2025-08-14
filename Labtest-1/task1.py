import re

def extract_urls(text):
    # Regex pattern to match http, https, and www URLs
    url_pattern = r'(https?://[^\s]+|www\.[^\s]+)'
    urls = re.findall(url_pattern, text)
    return urls

if __name__ == "__main__":
    sample_text = """
    Here are some links: https://www.example.com, http://test.org/page?query=1,
    and also www.sample-site.net. Not a link: ftp://not-a-web-link.com
    """
    found_urls = extract_urls(sample_text)
    print("Extracted URLs:")
    for url in found_urls:
        print(url)
