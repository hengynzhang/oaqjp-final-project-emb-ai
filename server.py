from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def emo_detector():
    text_to_detect = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_detect)

    anger = result.get('anger', 0)
    disgust = result.get('disgust', 0)
    fear = result.get('fear', 0)
    joy = result.get('joy', 0)
    sadness = result.get('sadness', 0)
    dominant_emotion = result.get('dominant_emotion', 'Unknown')

    if dominant_emotion == None:
        return jsonify({"message": "Invalid text! Please try again!. "})

    return (f"<p>For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. The dominant emotion is <b>{dominant_emotion}</b>.</p>")

if __name__ == '__main__':
    app.run(debug=True)