🎬 Django YouTube Downloader

A simple YouTube downloader built using Django and yt-dlp that allows users to download videos in different formats.

🚀 Features

🎥 Download YouTube videos in different resolutions (720p, 1080p, 4K)

🎵 Extract and download audio (MP3 format)

📂 Store downloaded files temporarily

🖥️ Simple web interface for easy use

🛠️ Tech Stack

Backend: Django, yt-dlp

Frontend: HTML, CSS (Django Templates)

Database: (Optional) PostgreSQL / SQLite for user history

Hosting: VPS (if deployed online)

📦 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/yourusername/youtube-downloader.git
cd youtube-downloader

2️⃣ Create a Virtual Environment

uv venv .venv  # Create virtual environment
source .venv/bin/activate  # Activate (Linux/Mac)
.venv\Scripts\activate  # Activate (Windows)

3️⃣ Install Dependencies

uv pip install -r requirements.txt

4️⃣ Run Migrations

python manage.py migrate

5️⃣ Start the Django Server

python manage.py runserver

Now visit http://127.0.0.1:8000/ in your browser.

🎯 How to Use

Open the web interface.

Enter the YouTube video URL.

Click the Download button.

The video/audio file will be processed and downloaded.

🔥 Future Enhancements

✅ Add support for batch downloads

✅ Show download progress

✅ Implement user authentication for history tracking

✅ Deploy to a cloud server

⚠️ Disclaimer

This project is for educational purposes only. Downloading copyrighted videos from YouTube without permission violates YouTube’s Terms of Service. Use responsibly.

📝 License

MIT License. Feel free to modify and use it.

🙌 Contributing

Pull requests are welcome! If you find a bug or want to improve something, feel free to submit an issue.

Made with ❤️ by sachinandan 
mail: sachinandan.priv05@gmail.com

