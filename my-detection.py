import jetson.inference
import jetson.utils

net = jetson.inference.detectNet(argv=['--model=/my-detection/ssd-mobilenet.onnx', '--labels=/my-detection/Data/labels.txt', '--input-blob=input_0', '--output-cvg=scores', '--output-bbox=boxes'])
camera = jetson.utils.videoSource("/dev/video0")
display = jetson.utils.videoOutput()

while True:
	img = camera.Capture()
	detections = net.Detect(img)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))



