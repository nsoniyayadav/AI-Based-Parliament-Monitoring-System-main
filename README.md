<<<<<<< HEAD
# Live Sansad (Django)

Live Sansad is a Django-based web application that powers a **digital parliament platform** for:
- **Citizens**: watch live sessions, comment, vote, give feedback, and view engagement history
- **MPs / Admins**: manage videos and MP face detections, view session data, and run analytics

> This repo uses server-side rendered HTML templates (Django) and Django models for persistence. Some features integrate AI/LLM and media processing.

---

## Project Structure

- `manage.py` - Django entry point
- `myproject/` - Django project package
- `myapp/` - Main application
  - `views.py` - All request handlers (login, dashboards, uploads, session pages, etc.)
  - `models.py` - Database schema
  - `templates/` - HTML templates
  - `urls.py` - Routes for the app
- `media/` - Uploaded files served via Django in development
- `mp_face_detection/` and other top-level folders may contain seeded/asset files (depending on your setup)

---

## Requirements

You need a working Python + pip environment.

Typical dependencies used by the code include:
- Django 5.x
- `python-dotenv` (uses `load_dotenv()` in `views.py`)
- `requests`
- `yt-dlp`
- `youtube-transcript-api`
- `groq` (LLM integration)
- `openpyxl` (Excel `.xlsx` upload for MP face detections)
- plus Django media handling requirements (Pillow for `ImageField`

> Note: There is currently no `requirements.txt` in this project folder (at least from what was visible). Create one if you want fully reproducible installs.

---

## Environment Variables

The code reads `GROQ_API_KEY` for the USP generation feature.

Set it before running the server, for example:

- Windows (PowerShell):
  - `$env:GROQ_API_KEY="your_key_here"`

- Or create a `.env` file (repo root) with:
  - `GROQ_API_KEY=your_key_here`

---

## Setup & Run (Development)

From the `myproject/` directory:

1. Create and activate a virtual environment (example):
   - `python -m venv venv`
   - `venv\Scripts\activate`

2. Install dependencies (adjust list as needed):
   - `pip install django python-dotenv requests yt-dlp youtube-transcript-api groq openpyxl pillow`

3. Apply migrations:
   - `python manage.py makemigrations`
   - `python manage.py migrate`

4. Start the server:
   - `python manage.py runserver`

5. Open in browser:
   - `http://127.0.0.1:8000/`

---

## Admin / Login Flows

This project uses **custom role-based login** (not Django’s auth system).

Routes:
- `POST /login/` handled by `login_view`
- `GET /logout/` handled by `logout_view`

Session keys used:
- `citizen_id`
- `mp_id`
- `admin_id`

---

## Key Routes

Defined in `myapp/urls.py`:

### Home
- `GET /` → `home`

### Auth
- `GET /login/` (form)
- `POST /login/` (processes role: citizen/mp/admin)
- `GET /logout/`
- `GET /register/`

### Dashboards
- `GET /citizen/dashboard/` → `citizen_dashboard`
- `GET /mp/dashboard/` → `mp_dashboard`
- `GET /admin-dashboard/` → `admin_dashboard`

### Citizen session pages
- `GET /live-session/` → `live_session`
- `GET /session-player/` → `session_player`
- `GET /session-history/` → `session_history`
- `GET /session-details/<pk>/` → `session_details`
- `GET /my-activity/` → `my_activity`

### MP Face Detection Management (Admin)
- `GET  /mp-face-detections/list/` → `mp_face_detection_list` (JSON)
- `POST /mp-face-detections/single-upload/` → `mp_face_single_upload`
- `POST /mp-face-detections/excel-upload/` → `mp_face_excel_upload`
- `POST /mp-face-detections/zip-upload/` → `mp_face_zip_upload`
- `POST /mp-face-detections/single-edit/` → `mp_face_single_edit`
- `POST /mp-face-detections/delete/` → `mp_face_delete`

#### Excel Upload Notes
The Excel endpoint expects:
- File: `.xlsx`
- First sheet
- Column A: MP name
- Column B: embedded image (Excel picture)

It returns a JSON response containing:
- `created`, `failed`, and `errors`

### USP Video Generation / Live Flow
- `GET /go-live/<pk>/` → `go_live` (marks a USP video as live)
- `GET /stop-live/` → `stop_live` (marks none live)
- `GET /generate-usp/<pk>/` → `generate_usp_video` (Groq LLM-based USP extraction)

---

## Media / Uploads

The project serves `MEDIA_URL` and `MEDIA_ROOT` in development:
- `MEDIA_URL = 'media/'`
- `MEDIA_ROOT = BASE_DIR / 'media'`

Uploaded `ImageField` / `FileField` outputs will be available under `/media/...` when `DEBUG=True`.

---

## Troubleshooting

- **Groq key errors**: set `GROQ_API_KEY`.
- **Image uploads failing**: ensure Pillow is installed (`pip install pillow`).
- **Excel upload failing**: ensure you upload a `.xlsx` with images embedded into the cells (Column B).
- **No database tables**: run `python manage.py migrate`.

---

## Notes / Known Issues (From Code)

- Some template filenames include spaces (e.g. `Mp face detections.html`, `youtube videos.html`, `USP_videos.html`). This is unusual; keep template paths exact.
- There are a few duplicated/overlapping routes in `myapp/urls.py` (e.g. `session-history/` appears multiple times). Django resolves by first match.

---

## License

# Parliament Session Intelligence and Citizen Engagement Platform

## Overview

The Parliament Session Intelligence and Citizen Engagement Platform is an AI-powered web application designed to improve transparency, accessibility, and citizen participation in parliamentary proceedings. The system automatically collects Parliament session videos from YouTube, extracts transcripts, generates AI-powered summaries and highlights, and provides an interactive platform for citizens, Members of Parliament (MPs), and administrators.

The platform utilizes Artificial Intelligence (AI), Natural Language Processing (NLP), and the Llama 3.3 70B Versatile Large Language Model through the Groq API to transform lengthy parliamentary discussions into concise, searchable, and understandable information.

---

## Key Features

### Video Collection and Processing

* YouTube Parliament Session Video Collection
* Automatic Video Download using yt-dlp
* Transcript Extraction using YouTube Transcript API
* Transcript Cleaning and Processing

### AI-Powered Analysis

* AI-Based Session Summarization
* Topic-wise Highlight Generation
* Important Discussion Identification
* Parliamentary Information Extraction

### Citizen Engagement

* Watch Parliament Session Videos
* View AI Summaries and Highlights
* Vote on Important Issues
* Add Comments
* Submit Feedback
* Register Complaints

### MP Dashboard

* Access Parliament Session Information
* Review Citizen Feedback
* Monitor Public Complaints
* View Participation Statistics

### Admin Dashboard

* Manage Videos and Sessions
* Monitor Platform Activities
* Analyze User Engagement
* Track Votes, Comments, Feedback, and Complaints

---

## Technology Stack

| Component             | Technology              |
| --------------------- | ----------------------- |
| Backend               | Django                  |
| Programming Language  | Python                  |
| Database              | SQLite                  |
| AI Platform           | Groq API                |
| AI Model              | Llama 3.3 70B Versatile |
| Video Download        | yt-dlp                  |
| Transcript Extraction | YouTube Transcript API  |
| Frontend              | HTML, CSS, JavaScript   |
| Version Control       | Git & GitHub            |

---

## System Workflow

1. Admin selects a Parliament Session video from YouTube.
2. The system downloads the video using yt-dlp.
3. Transcript is extracted using YouTube Transcript API.
4. Transcript is cleaned and processed.
5. Llama 3.3 70B analyzes the transcript.
6. AI generates summaries and highlights.
7. Processed information is stored in the database.
8. Sessions are published on the platform.
9. Citizens and MPs access videos, summaries, and highlights.
10. Citizens participate through voting, comments, feedback, and complaints.
11. Admin monitors platform analytics and engagement.

---

## Project Objectives

* Improve accessibility of parliamentary information.
* Increase transparency in parliamentary proceedings.
* Generate AI-powered summaries and highlights.
* Encourage citizen participation in governance.
* Bridge the gap between Parliament and citizens.
* Support informed decision-making through AI-generated insights.

---

## Team Members

* Vinod Prajapati (Team Leader)
* Team Member 2
* Team Member 3
* Team Member 4

---

## Future Enhancements

* MP Face Recognition
* Speaker Identification
* Real-Time Session Processing
* Sentiment Analysis
* Multi-Language Translation
* Mobile Application Development

---

## License

This project is developed for educational and research purposes.

=======
# AI-Based-Parliament-Monitoring-System
Parliament Session Intelligence and Citizen Engagement Platform is an AI-powered system that collects Parliament session videos from YouTube, extracts transcripts, generates summaries and highlights using Llama 3.3 70B via Groq, and enables citizen participation through voting, comments, feedback, complaints, and analytics dashboards.
>>>>>>> 127d0862cd60a8482bad7f909a37430d8855e2b9
