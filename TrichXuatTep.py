import os
import mimetypes
import PyPDF2
from docx import Document
# Chức năng trích xuất nội dung từ tệp PDF
def extract_pdf_content(file_path):
    content = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            content += page.extract_text() + "\n"
    return content
# Chức năng trích xuất nội dung từ tệp .Doc

def extract_docx_content(file_path):
    content = ""
    doc = Document(file_path)
    for para in doc.paragraphs:
        content += para.text + "\n"
    return content
# Chức năng trích xuất siêu dữ liệu và nội dung đính kèm

def extract_attachment_info(attachments):
    attachment_info = []

    for attachment in attachments:
        file_path = attachment['path']
        file_type, _ = mimetypes.guess_type(file_path)  # Get MIME type based on file extension
        file_size = os.path.getsize(file_path)  # Get file size in bytes

        # Khởi tạo nội dung trống
        content = ""
        # Trích xuất nội dung dựa trên loại tệp
        if file_type == 'application/pdf':
            content = extract_pdf_content(file_path)
        elif file_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            content = extract_docx_content(file_path)
        attachment_info.append({
            'name': attachment['name'],
            'type': file_type,
            'size': file_size,
            'content': content  # Lưu trữ nội dung được trích xuất

        })
    return attachment_info
# Ví dụ về danh sách tệp đính kèm có đường dẫn tệp
attachments = [
    {'name': 'Invoice.pdf', 'path': 'C:/Users/bobmi/Documents/Invoice.pdf'},
    {'name': 'Report.docx', 'path': 'C:/Users/bobmi/Documents/Report.docx'}
]
extracted_info = extract_attachment_info(attachments)
print(extracted_info)
