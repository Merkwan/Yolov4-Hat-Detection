F:
cd F:\ComputerParctice\yolov4\darknet-master\build\darknet\x64
darknet.exe detector demo  data\voc_hat.data  cfg\yolov4-test.cfg backup\yolov4-custom_final-old-520.weights F:/ComputerParctice/yolov4/ui/test5.mp4 -thresh 0.2 -ext_output -out_filename  F:\ComputerParctice\yolov4\ui\resultVideo.mp4
exit