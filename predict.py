from yolo10 import YOLOv10
import yaml
from pathlib import Path


def main():
    # Load configuration from YAML file
    config_path = Path(__file__).parent / "config" / "config.yaml"
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # Load the trained model for prediction
    model = YOLOv10(config["predict_model"])

    # Run prediction on custom test images
    results = model.predict(
        source=config["predict_data"],
        save=config["predict_save"]
    )

    # print results
    print(results)


if __name__ == "__main__":
    main()
