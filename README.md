
# FaceGuard Backend

This is the backend for the FaceGuard project — an AI-powered tool to detect and prevent photo misuse online.

## Features
- Compares two face images using DeepFace (AI)
- Returns match percentage and misuse alert
- Flask-based REST API with CORS enabled

## Requirements
- Python 3.7+

## Installation

```bash
pip install -r requirements.txt
python app.py
```

## API Endpoint

**POST** `/compare`

**Form Data:**
- `img1`: Base/reference image
- `img2`: Uploaded image to compare

**Response:**
```json
{
  "match": true,
  "similarity_percent": 92.67,
  "alert": "Photo matched securely."
}
```

## Deployment
You can deploy this using [Render](https://render.com/) by connecting it to a GitHub repository.

## License
MIT
