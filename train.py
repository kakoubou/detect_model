from yolo10 import YOLOv10
import yaml
from pathlib import Path


def main():
    # Load configuration from YAML file
    config_path = Path(__file__).parent / "config" / "config.yaml"
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # Initialize YOLOv10n model (train from scratch)
    model = YOLOv10(config["model"])

    # Start training with custom dataset
    model.train(
        data=config["train_data"],
        epochs=config["train_epoch"],
        imgsz=config["imgsz"]
    )


if __name__ == "__main__":
    main()
