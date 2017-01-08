## Test consumer

### Features
Fetches the jobs from simple redis-queue and parses the content from text data. Then prints out all href-links to stdout.

### How to

First install everything in a virtualenv:

```bash
virtualenv venv
. ./venv/bin/activate
pip install -I -r requirements.txt
```
Run the rq-worker (in separate terminal winwod):
```bash
cd test-producer
. ./venv/bin/activate
python run.py
```


