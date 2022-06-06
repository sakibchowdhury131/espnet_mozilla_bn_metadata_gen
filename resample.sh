for i in `ls *.wav`;
do
outdir='../resampled/'
let a++;
echo "Processing file $i"
sox $i -r 22050 -b 16 -c 1 $outdir$i

done