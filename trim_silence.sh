for fle in `ls *.wav`;
do
outdir='../trimmed_silence/'
echo "Processing file $fle"
ffmpeg -i $fle -af "silenceremove=start_periods=1:start_duration=1:start_threshold=-90dB:detection=peak,aformat=dblp,areverse,silenceremove=start_periods=1:start_duration=1:start_threshold=-90dB:detection=peak,aformat=dblp,areverse" $outdir$fle
done