DURATION=(`ffprobe -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "audio-files/common_voice_bn_30991288.flac" 2>/dev/null`)
echo $DURATION