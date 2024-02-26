from django.shortcuts import render
import os
from django.http import HttpResponse
from rest_framework.decorators import api_view
from docx import Document
from drf_spectacular.utils import extend_schema
from xhtml2pdf import pisa



 
@extend_schema(
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "docx_file": {"type": "string", "format": "binary"}},
            },
        },
)
@api_view(['POST'])
def convert_docx_to_pdf(request):
    docx_file = request.FILES.get('docx_file')

    if docx_file is None:
        return HttpResponse("No file provided", status=400)

    try:
        # Read the DOCX file and extract text
        doc = Document(docx_file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"

        # Convert text to HTML
        html_content = f"<html><body>{text}</body></html>"

        # Generate PDF from HTML using xhtml2pdf
        pdf_file = os.path.join('output', 'converted_document.pdf')
        with open(pdf_file, 'w+b') as output_file:
            pisa.CreatePDF(html_content, dest=output_file)

        # Return the path to the output PDF file
        return HttpResponse(pdf_file, content_type='text/plain')

    except Exception as e:
        return HttpResponse("Error converting DOCX to PDF: " + str(e), status=500)