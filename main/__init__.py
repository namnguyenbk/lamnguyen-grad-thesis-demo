from flask import Flask, request, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/text-to-speech', methods=['POST'])
def text_to_speech_():
    payload = request.json

    if not payload or not payload.get('text'):
        return jsonify({'error': 'Text is required'}), 400

    # TODO: Call text_to_speech function
    def _mock_speech_to_text(text: str):
        with open('TellMeGoodbye-BIGBANG.mp3', 'rb') as audio_file:
            audio = audio_file.read()

        return audio

    return Response(_mock_speech_to_text('Nam Nguyen'), mimetype='audio/mp3')


@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_():
    audio = request.files.get('audio')

    # TODO: Call speech_to_text function
    def _mock_speech_to_text(audio):
        """
        :param audio: Bytes
        :return: string
        """
        return 'Nam Nguyen'

    return jsonify({'speech_to_text': _mock_speech_to_text(audio.read())})
