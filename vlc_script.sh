#Convert a sram to different format
cvlc "rtsp://vesa:lollero@dt6288.myfoscam.org:88/videoMain" --sout "#transcode{vcodec=mp2v,vb=800,scale=1,acodec=mpga,ab=128,channels=2,samplerate=44100}:duplicate{dst=rtp{sdp=rtsp://:8554/output.mpeg},dst=display}" --sout-keep

# Way to save a steam to a file. Have to give start time and run time
cvlc -vvv rtsp://vesa:lollero@192.168.0.102:88/videoMain --start-time=00 --run-time=10 --sout file/ts:test2.ts vlc:://quit

