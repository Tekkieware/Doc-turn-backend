from django.shortcuts import render
import os
from django.http import HttpResponse
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema



 
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
    # Assuming your DOCX file is sent as part of the request
    pass