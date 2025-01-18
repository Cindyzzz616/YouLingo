from flask import Flask, jsonify, request
from google.cloud import firestore
import re

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore client
db = firestore.Client.from_service_account_json("serviceAccountKey.json")

@app.route("/videos", methods=["GET"])
def get_videos():
    try:
        # Reference to the "videos" collection
        videos_ref = db.collection("videos")
        docs = videos_ref.stream()

        # Collect all video documents
        videos = []
        for doc in docs:
            video = doc.to_dict()
            video["id"] = doc.id  # Include document ID
            videos.append(video)

        return jsonify({"success": True, "data": videos}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/check_video", methods=["POST"])
def check_video():
    try:
        data = request.get_json()
        youtube_link = data.get("youtube_link")
        
        # Extract video ID from YouTube link
        video_id_match = re.search(r"v=([^&]+)", youtube_link)
        if not video_id_match:
            return jsonify({"success": False, "error": "Invalid YouTube link"}), 400
        
        video_id = video_id_match.group(1)
        print(f"Extracted video_id: {video_id}", flush=True)  # Print the video_id for debugging
        
        # Check if video ID exists in Firestore
        videos_ref = db.collection("videos")
        query = videos_ref.where("youtube_id", "==", video_id).stream()
        video_exists = any(query)
        
        if video_exists:
            return jsonify({"success": True, "exists": True}), 200
        else:
            return jsonify({"success": True, "exists": False}), 200
    except Exception as e:
        return jsonify({"success": False, "error": f"{str(e)} (video_id: {video_id})"}), 500

if __name__ == "__main__":
    app.run(debug=True)
