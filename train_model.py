from ultralytics import YOLO

if _name_ == '_main_':
    # Load the YOLOv8 Nano model (extremely fast and accurate)
    model = YOLO("yolov8n.pt") 

    # Start the training process!
    results = model.train(
        data="fried-garlic-guard-2/data.yaml", 
        epochs=100,       
        imgsz=640,       
        batch=32,        # Increased to 32 to utilize the 6GB VRAM!
        device=0,        # Targets the RTX 4050
        name="Garlic_Brain_v1"
    )