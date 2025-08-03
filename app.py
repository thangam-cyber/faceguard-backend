from flask import Flask, request, jsonify
from flask_cors import CORS
import face_recognition

app = Flask(__name__)
CORS(app)

@app.route("/compare", methods=["POST"])
def compare_faces():
    try:
        uploaded_image = request.files['image']
        image = face_recognition.load_image_file(uploaded_image)
        uploaded_encodings = face_recognition.face_encodings(image)

        if not uploaded_encodings:
            return jsonify({"match": False, "similarity_percent": 0, "alert": "No face detected."})

        uploaded_encoding = uploaded_encodings[0]

        known_image = face_recognition.load_image_file("ref_images/person1.jpg")
        known_encoding = face_recognition.face_encodings(known_image)[0]

        result = face_recognition.compare_faces([known_encoding], uploaded_encoding)[0]
        distance = face_recognition.face_distance([known_encoding], uploaded_encoding)[0]
        similarity = round((1 - distance) * 100, 2)

        if result:
            alert = "Misuse detected! Face matched."
        else:
            alert = "Safe! No match found."

        return jsonify({
            "match": result,
            "similarity_percent": similarity,
            "alert": alert
        })

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/')
def home():
    return "FaceGuard Backend is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
