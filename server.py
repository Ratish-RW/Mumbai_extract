from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Route to accept JSON list and return it back
@app.route('/echo', methods=['POST'])
def echo_json():
    try:
        # Get the JSON data from the request
        data = request.get_json(force=True)
        return jsonify({
            "message": "Received JSON list successfully",
            "data": data
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=False)
