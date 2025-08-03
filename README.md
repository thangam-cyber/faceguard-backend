# FaceGuard Backend (Render-Compatible Version)

This backend uses `face_recognition` instead of DeepFace to allow smooth, conflict-free hosting on Render.com.

## Features
- Accepts uploaded image
- Compares it to a stored reference image
- Returns face match result with similarity percentage

## Setup
1. Place a photo to protect in `ref_images/person1.jpg`
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```

## Endpoint
- **POST /compare** — with form field `image`
- Returns: `match`, `similarity_percent`, and `alert` message

## Hosting
- Recommended: [Render.com](https://render.com) Free Plan

## License
MIT
