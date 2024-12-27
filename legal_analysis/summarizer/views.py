from django.shortcuts import render, redirect
from .models import Document
from transformers import pipeline

def upload_document(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        doc = Document(title=uploaded_file.name, uploaded_file=uploaded_file)
        doc.save()

        summarizer = pipeline('summarization')
        with open(doc.uploaded_file.path, 'r') as file:
            text = file.read()
            doc.summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
            doc.save()

        return redirect('summary', pk=doc.pk)
    return render(request, 'summarizer/upload.html')

def summary_view(request, pk):
    doc = Document.objects.get(pk=pk)
    return render(request, 'summarizer/summary.html', {'doc': doc})
