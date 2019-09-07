ffmpeg -framerate 25 -start_number 1950 -i pbmnet_year_%d.png -vcodec mpeg4 NetworkEvo.avi
ffmpeg -i NetworkEvo.avi Network_Evolution.mp4
