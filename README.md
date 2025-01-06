# bird-finderz

This project is an end-to-end image classification project which has the proper pipelines in place to get training data from a source url, train and evaluate a convolutional neural network, and deploy that model with a simple frontend for inference. 

This particular model is trained to classify 525 bird species based on a dataset sourced from Kaggle: https://www.kaggle.com/datasets/gpiosenka/100-bird-species


<hr>

### Steps to run locally:

1. Clone this repository
```bash
git clone https://github.com/rohith42/bird-finderz.git
```

2. Create a conda environment
```bash
conda create -n bird python=3.11 -y
conda activate bird
```

3. Install the required packages
```bash
cd bird-finderz
pip install -r requirements.txt
```

4. Run the application and visit the specified url
```bash
python app.py
```

5. Visit the `/getTrainedModel` endpoint first to download the trained model and necessary `birds.csv` file to your computer

6. Return to the home route and upload an image of a bird to find out what species it is! 

<hr>

### Training a model

Run `python main.py` to execute the entire pipeline from data ingestion to model training and evaluation. Make sure you have a capable system with a decent GPU for training or modify `params.yaml` to match your system.

The code is currently set up to fine-tune the VGG-16 model with ImageNet weights. You can change the model architecture in `src/classifier/components/prepare_base_model.py` in the `PrepareBaseModel.get_base_model()` method.

<hr>

### Adding a new pipeline
1. Update `config.yaml`
2. Update `secrets.yaml` [Optional]
3. Update `params.yaml`
4. Update the entity in `src/classifier/entity/config_entity.py`
5. Update the configuration manager in `src/classifier/config/configuration.py`
6. Update the components in `src/classifier/components`
7. Update the pipeline in `src/classifier/pipeline`
8. Update `main.py`
9. Update `dvc.yaml`

### Pipeline management with DVC
DVC prevents running pipelines unnecessarily. Relevant DVC commands:
```bash
dvc init   # Initialize DVC repo
dvc repro  # Run all the necessary pipelines
dvc dag    # Visualize dependencies between pipelines
```

<hr>


### Azure CI/CD deployment with Github Actions

1. Create a resource group for this project in your Azure portal
2. Create an Azure container registry for the Docker image
   * Save the username and password!
3. Download and install Docker Desktop on your computer (make sure it's running)
4. Build the Docker image of the source code
    ```bash
    docker build -t [CONTAINER_REGISTRY_NAME].azurecr.io/[REPOSITORY_NAME]:latest .
    ```
5. Push the Docker image to the container registry
    ```bash
    docker login [CONTAINER_REGISTRY_NAME].azurecr.io  # Use the username and password from step 2
    docker push [CONTAINER_REGISTRY_NAME].azurecr.io/[REPOSITORY_NAME]:latest
    ```
6. Create and deploy a new Web App Service in Azure, using the Docker image that should be in the Container Registry
7. After it's deployed, go to the Deployment Center for the Web App and follow the instructions for CI/CD deployment with Github Actions
