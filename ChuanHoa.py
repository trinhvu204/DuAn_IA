from urllib.parse import urlparse


def normalize_domains(urls):
    normalized_domains = set()  # Sử dụng một bộ để tránh trùng lặp

    for url in urls:
        parsed_url = urlparse(url)
        # Trích xuất netloc (phần vị trí mạng của URL)
        domain = parsed_url.netloc
        # Xóa 'www.' và bất kỳ tên miền phụ nào khác
        domain_parts = domain.split('.')
        if len(domain_parts) > 2:  # Nếu có nhiều hơn hai phần
            domain = '.'.join(domain_parts[-2:])  # Giữ lại hai phần cuối (ví dụ: paypal.com)
        # Chuyển sang chữ thường để đảm bảo tính nhất quán
        normalized_domains.add(domain.lower())
    return list(normalized_domains)
# Example URLs
urls = [
    "https://www.paypal.com",
    "http://paypal.com",
    "https://subdomain.paypal.com/path",
    "https://PAYPAL.COM",
    "https://example.com",
    "http://www.example.com",
]

# Normalize domains
normalized = normalize_domains(urls)
print(normalized)
