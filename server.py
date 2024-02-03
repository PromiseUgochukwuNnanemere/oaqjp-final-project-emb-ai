"""
Module to run a Flask server for emotion detection.
"""
from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Emotion detection route.

    Returns:
        JSON response with emotion analysis results or an error message.
    """
    try:
        if request.method == 'POST':
            data = request.get_json()

            if 'statement' in data:
                statement = data['statement']
                result = emotion_detector(statement)

                dominant_emotion = result.get('dominant_emotion', '')
                if dominant_emotion is None:
                    return jsonify({'output': "Invalid text! Please try again!"})

                response = {
                    'anger': result.get('anger', None),
                    'disgust': result.get('disgust', None),
                    'fear': result.get('fear', None),
                    'joy': result.get('joy', None),
                    'sadness': result.get('sadness', None),
                    'dominant_emotion': dominant_emotion
                }

                output = (
                    f"For the given statement, the system response is {response}. "
                    f"The dominant emotion is {dominant_emotion}."
                )

                return jsonify({'output': output})
            else:
                return jsonify({'error': "'statement' parameter missing in the request."})
        else:
            return jsonify({'error': "Method Not Allowed. Use POST request with 'statement' parameter."})
    except Exception as e:
        return jsonify({'error': f"Unexpected error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
