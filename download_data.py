from roboflow import Roboflow
rf = Roboflow(api_key="Lb9qZRB3WF1jjFoZMJrZ")
project = rf.workspace("sohams-workspace-im5qd").project("fried-garlic-guard")
version = project.version(2)
dataset = version.download("yolov8")