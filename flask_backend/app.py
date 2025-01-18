from flask import Flask, jsonify
from google.cloud import firestore

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

if __name__ == "__main__":
    app.run(debug=True)
