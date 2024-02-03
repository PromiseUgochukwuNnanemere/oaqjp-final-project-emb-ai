import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():  # Check if the input is blank
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # URL for the Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Headers for the request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Input JSON format with the text to be analyzed
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Make a POST request to the Emotion Predict function
        response = requests.post(url, headers=headers, json=input_json)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response JSON
            result_json = response.json()

            # Check if 'emotionPredictions' field is present in the result
            if 'emotionPredictions' in result_json:
                # Extract the first prediction
                first_prediction = result_json['emotionPredictions'][0]

                # Extract emotion scores from the prediction
                emotion_scores = first_prediction['emotion']

                # Find the dominant emotion with the highest score
                dominant_emotion = max(emotion_scores, key=emotion_scores.get)

                # Return the output format
                return {
                    'anger': emotion_scores.get('anger', None),
                    'disgust': emotion_scores.get('disgust', None),
                    'fear': emotion_scores.get('fear', None),
                    'joy': emotion_scores.get('joy', None),
                    'sadness': emotion_scores.get('sadness', None),
                    'dominant_emotion': dominant_emotion
                }
            else:
                # If 'emotionPredictions' field is not present, return the entire response JSON
                return result_json
        elif response.status_code == 400:
            # Handle blank entries (status code 400)
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code}, {response.text}")
            return None

    except Exception as e:
        # Print an error message if an exception occurs
        print(f"Error: {str(e)}")
        return None
