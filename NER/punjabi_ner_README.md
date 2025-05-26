# DL-DiscoMT - Named Entity Recognition (NER) - Punjabi

 This project provides a Named Entity Recognition (NER) model specifically designed for Punjabi text analysis. It accurately identifies and classifies named entities such as persons, organizations, locations, dates, and other important entities within Punjabi language content. This project is ideal for developers, researchers, and organizations requiring Punjabi text processing capabilities for information extraction, content analysis, document processing, and natural language understanding applications.
   
## Download - Model

Download the model from the provided drive link: 

   [Drive link](Drive link)

Alternatively, you can use the following command:

```bash
pip install gdown

gdown --folder <drive link>

```
* The download path, we will consider as **"basePath"** in this readme

## Deployment - Docker  

* To create a Docker image, use the following command. Replace <Image Name> with your desired image name, and <replace/the/path/Dockerfile> with the actual path to the Dockerfile you downloaded from the drive.


```bash
## windows

   docker build -t <Image Name> <basepath/Punjabi-NER-AUKBC-ULCA-Deploy/>
```
Or on Ubuntu:
```bash
## ubuntu

   sudo docker build -t <Image Name> <basepath/Punjabi-NER-AUKBC-ULCA-Deploy/>
```

* After creating the Docker image, use this command to run the model. Make sure to replace <Image Name> with the actual image name you created.

```bash
## windows

   docker run -ti --gpus all -p 8000:8000 -p 8001:8001 -p 8002:8002 <Image Name>
```
Or on Ubuntu:
```bash
## ubuntu

   sudo docker run -ti --gpus all -p 8000:8000 -p 8001:8001 -p 8002:8002 <Image Name>
```
**Breakdown of the Command:**

- docker run: This command starts a new container from an existing Docker image.

- ti:

  - t: Allocates a pseudo-TTY, which allows you to interact with the container.
  - i: Keeps the standard input open so you can interact with the container, useful for running commands interactively.
- --gpus all: This option enables the use of all available GPUs on the host machine inside the container. It ensures the container can access the GPU resources, which is crucial for running machine learning models or any computation that requires GPU acceleration.

- -p 8000:8000 -p 8001:8001 -p 8002:8002: These options map the container’s internal ports to the host machine’s ports. In this case:

  - 8000:8000: Maps the container's internal port 8000 to port 8000 on the host machine.
  - 8001:8001: Maps port 8001 in the container to port 8001 on the host.  - 8002:8002: Maps port 8002 in the container to port 8002 on the host.

    This ensures that any services running inside the container on these ports (e.g., Triton Inference Server) can be accessed externally on the same ports from the host machine.

- <Image Name>: This is a placeholder for the actual name of the Docker image that was built earlier. You will replace <Image Name> with the name of your Docker image containing the model and the server.



## Access the Model Using Python 

* Install the required dependencies:

```bash
  pip install tritonclient[all] numpy
```

* Run the Python file NER_tritonAPI_request.py. Before running, replace url="<url of triton server>" in the code with the actual URL of your Triton server (e.g., 192.168.85.24:8000)




## Screenshots
input :"ਜਦੋਂ ਗੁਰੂ ਸਾਹਿਬ ਨੇ ਇਕ ਤੀਰ ਚਲਾਇਆ ਤਾਂ ਹਾਥੀ ਉਸ ਤੀਰ ਨੂੰ ਚੁਕ ਕੇ ਲਿਆਇਆ ।"
![App Screenshot](https://github.com/aashiqlove/code/blob/main/NER/picture/pubpicture-1.jpg?raw=true)


input :"ਰਤਨ ਰਾਏ ਚੱਕ ਨਾਨਕੀ ਵਿਚ ਏਨਾ ਖੁਸ਼ ਸੀ ਕਿ ਉਸਦਾ ਵਾਪਿਸ ਤ੍ਰਿਪੁਰਾ ਜਾਣ ਨੂੰ ਦਿਲ ਨਹੀਂ ਕਰਦਾ ਸੀ ।"
![App Screenshot ](https://github.com/aashiqlove/code/blob/main/NER/picture/pubpicture-2.jpg?raw=true)


input :"ਅਖ਼ੀਰ ਪੰਜ ਮਹੀਨੇ ਬੀਤ ਜਾਣ ਮਗਰੋਂ ਗੁਰੂ ਸਾਹਿਬ ਨੇ ਉਸਨੂੰ ਆਖਿਆ ਕਿ ਉਹ ਵਾਪਿਸ ਤ੍ਰਿਪੁਰਾ ਜਾ ਕੇ ਆਪਣੀ ਰਿਆਸਤ ਦੀ ਵਾਗ-ਡੋਰ ਸੰਭਾਲੇ ।"
![App Screenshot](https://github.com/aashiqlove/code/blob/main/NER/picture/pubpicture-3.jpg?raw=true)



## License
CC BY 4.0 
