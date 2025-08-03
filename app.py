from flask import Flask, request, jsonify
from flask_cors import CORS
from deepface import DeepFace
import os

app = Flask(__name__)
CORS(app)

@app.route("/compare", methods=["POST"])
def compare_faces():
    try:
        img1 = request.files['img1']
        img2 = request.files['img2']
        img1_path = "img1.jpg"
        img2_path = "img2.jpg"
        img1.save(img1_path)
        img2.save(img2_path)

        result = DeepFace.verify(img1_path, img2_path, enforce_detection=False)

        similarity = 100 - result['distance'] * 100
        is_match = result['verified']

        # If match is suspicious
        if is_match and similarity < 90:
            alert = "Potential misuse detected! Face matched with low confidence."
        elif is_match:
            alert = "Photo matched securely."
        else:
            alert = "No match found. Safe."

        return jsonify({
            "match": is_match,
            "similarity_percent": round(similarity, 2),
            "alert": alert
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
