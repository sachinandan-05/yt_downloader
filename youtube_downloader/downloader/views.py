from django.shortcuts import render

# Create your views here.
import os
import yt_dlp
from django.http import FileResponse, HttpResponse
from django.shortcuts import render

DOWNLOAD_FOLDER = "downloads/"  
def download_video(request):
    url = request.GET.get("url")
    if not url:
        return HttpResponse("No URL provided", status=400)

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
        
        return FileResponse(open(filename, 'rb'), as_attachment=True)
    
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)
    
def home(request):
    return render(request, "index.html")

