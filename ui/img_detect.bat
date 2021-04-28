F:
cd F:\ComputerParctice\yolov4\darknet-master\build\darknet\x64
darknet.exe detector test  data\voc_hat.data  cfg\yolov4-test.cfg backup\yolov4-custom_final-old-520.weights F:/ComputerParctice/yolov4/ui/000005.jpg
copy F:\ComputerParctice\yolov4\darknet-master\build\darknet\x64\predictions.jpg F:\ComputerParctice\yolov4\ui
exit