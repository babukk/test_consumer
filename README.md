## Test consumer

### Features
Fetches the jobs/messages from simple redis-queue (redis://localhost:6379/1) and parses the content from text data. Then prints out all links (<a href="..."> to stdout.

### How to

First install everything in a virtualenv:
```bash
cd test_consumer
virtualenv venv
. ./venv/bin/activate
pip install -I -r requirements.txt
```

Run it:
```bash
cd test_consumer
. ./venv/bin/activate
python run.py
```

