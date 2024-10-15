import re
def extract_urls(email_body):
    # Biểu thức chính quy để trích xuất URL
    url_pattern = r'(https?://[^\s]+)'
    # Tìm tất cả các URL trong nội dung email
    urls = re.findall(url_pattern, email_body)

    return urls
   # vi du
email_body = """
    Hi there, please check the following links:
    - https://www.example.conm
    http://3033671.mf559305.web.hosting-test.net/wtrfsrer0242
"""
# Xuat URLs
extracted_urls = extract_urls(email_body)
print(extracted_urls)