# Tensorflow 2.5 on Apple M1

Steps to recreate this environment:

1. `conda create --name tf25 --file ./conda-explicit.txt`
2. `conda activate tf25`
3. `pip install --no-deps -r requirements.txt`
4. `python confirm.py`

This is the output I get:
```
Init Plugin
Init Graph Optimizer
Init Kernel
Running TensorFlow 2.5.0 with 1 GPUs recognized
```
