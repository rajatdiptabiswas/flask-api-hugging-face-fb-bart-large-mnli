# Flask API Hugging Face [facebook/bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli)
:hugs: Flask API for Hugging Face's `facebook/bart-large-mnli` model

## Setup

Create a Python virtual environment `py3env`
```
python3 -m venv py3env
```

Activate the virtual environment `py3env`
```
source py3env/bin/activate
```

Install the Python packages from `requirements.txt`
```
pip3 install -r requirements.txt
```

Install PyTorch
```
pip3 install torch==1.9.0+cpu torchvision==0.10.0+cpu torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
```

Run the Flask application `app.py`
```
flask run --host=0.0.0.0
```

## Usage

### Request
Send JSON POST requests to `http://<address>:5000`
```json
{
  "sentence": "Last week I upgraded my iOS version and ever since then my phone has been overheating whenever I use your app.",
  "labels": ["mobile", "website", "billing", "account access"],
  "multi_label": 1
}
```

### Response
```json
{
  "labels": [
    "mobile",
    "account access",
    "billing",
    "website"
  ],
  "scores": [
    0.990887463092804,
    0.4456685483455658,
    0.37061989307403564,
    0.0016618024092167616
  ],
  "sequence": "Last week I upgraded my iOS version and ever since then my phone has been overheating whenever I use your app."
}
```


## Authors

* **Rajat Dipta Biswas** - *Initial work*

See also the list of [contributors](https://github.com/rajatdiptabiswas/flask-api-hugging-face-fb-bart-large-mnli/graphs/contributors) who participated in this project.

## Acknowledgments

* [Hugging Face](https://huggingface.co/)
* [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
