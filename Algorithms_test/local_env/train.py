from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
path = r"D:\Lecturs\Machine Vision\Machine_vision_code\train_yolov8_custom_dataset\local_env\config.yaml"
# Use the model
results = model(path, show=True, line_thickness=2)


results = model.train(data=path, epochs=1)  # train the model
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
path = r"D:\Lecturs\Machine Vision\Machine_vision_code\train_yolov8_custom_dataset\local_env\config.yaml"
# Use the model
results = model(path, show=True, line_thickness=2)


results = model.train(data=path, epochs=1)  # train the model
