## Models

Welcome to the yolo10 Models directory! Here you will find a wide variety of pre-configured model configuration files (`*.yaml`s) that can be used to create custom YOLO models. The models in this directory have been expertly crafted and fine-tuned by the yolo10 team to provide the best performance for a wide range of object detection and image segmentation tasks.

These model configurations cover a wide range of scenarios, from simple object detection to more complex tasks like instance segmentation and object tracking. They are also designed to run efficiently on a variety of hardware platforms, from CPUs to GPUs. Whether you are a seasoned machine learning practitioner or just getting started with YOLO, this directory provides a great starting point for your custom model development needs.

To get started, simply browse through the models in this directory and find one that best suits your needs. Once you've selected a model, you can use the provided `*.yaml` file to train and deploy your custom YOLO model with ease. See full details at the yolo10 [Docs](https://docs.yolo10.com/models), and if you need help or have any questions, feel free to reach out to the yolo10 team for support. So, don't wait, start creating your custom YOLO model now!

### Usage

Model `*.yaml` files may be used directly in the Command Line Interface (CLI) with a `yolo` command:

```bash
yolo task=detect mode=train model=yolov8n.yaml data=coco128.yaml epochs=100
```

They may also be used directly in a Python environment, and accepts the same [arguments](https://docs.yolo10.com/usage/cfg/) as in the CLI example above:

```python
from yolo10 import YOLO

model = YOLO("model.yaml")  # build a YOLOv8n model from scratch
# YOLO("model.pt")  use pre-trained model if available
model.info()  # display model information
model.train(data="coco128.yaml", epochs=100)  # train the model
```

## Pre-trained Model Architectures

yolo10 supports many model architectures. Visit https://docs.yolo10.com/models to view detailed information and usage. Any of these models can be used by loading their configs or pretrained checkpoints if available.

## Contribute New Models

Have you trained a new YOLO variant or achieved state-of-the-art performance with specific tuning? We'd love to showcase your work in our Models section! Contributions from the community in the form of new models, architectures, or optimizations are highly valued and can significantly enrich our repository.

By contributing to this section, you're helping us offer a wider array of model choices and configurations to the community. It's a fantastic way to share your knowledge and expertise while making the yolo10 YOLO ecosystem even more versatile.

To get started, please consult our [Contributing Guide](https://docs.yolo10.com/help/contributing) for step-by-step instructions on how to submit a Pull Request (PR) 🛠️. Your contributions are eagerly awaited!

Let's join hands to extend the range and capabilities of the yolo10 YOLO models 🙏!
