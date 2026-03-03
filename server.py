'''servidor que ejecuta la funcion emotion_detector. Tiene Localhost:5000'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detect():
    '''la funcion dispondra una salida dependiendo del texto a analizar'''
    #extrae el texto
    text_to_analyze = request.args.get("textToAnalyze")
    #usa la funcion y guarda en una variable
    response = emotion_detector(text_to_analyze)
    #si el texto esta en blanco, sera considerado invalido
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given input, the system response is 'anger': {response['anger']}, "
        f" 'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}.")

@app.route("/")
def render_index_page():
    '''renderiza la pagina web'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)
