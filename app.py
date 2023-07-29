from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from classifier.utils.common import decodeImage
from classifier.pipeline.predict import PredictionPipeline
from classifier.pipeline.download_model import DownloadModelPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self) -> None:
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)
    

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    return "Training currently not supported"
    # Uncomment following lines if deploying to a capable system
    # (at least 8GB RAM and 10GB gpuRAM)
    # os.system("dvc repro")
    # return "Training done successfully!"

@app.route("/getTrainedModel", methods=['GET', 'POST'])
@cross_origin()
def getTrainedModel():
    get_model_pipeline = DownloadModelPipeline()
    status = get_model_pipeline.main()
    return f"Trained model downloaded! {status}"


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    # Downloads model and birds.csv if needed before prediction
    download_model_pipeline = DownloadModelPipeline()
    if not download_model_pipeline.readyToPredict():
        download_model_pipeline.main()

    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)


if __name__ == '__main__':
    clApp = ClientApp()
    # app.run(host='0.0.0.0', port=8080)  # For localhost or AWS deployment
    app.run(host='0.0.0.0', port=80)