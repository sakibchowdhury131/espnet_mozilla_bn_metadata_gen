# define paths
TRAIN=./train.tsv
DEV=./dev.tsv
TEST=./test.tsv
OTHER=./other.tsv
INVALIDATED=./invalidated.tsv
VALIDATED=./validated.tsv


AUDIO_DESTINATION=./audio_destination
rm -rf $AUDIO_DESTINATION
mkdir $AUDIO_DESTINATION

#generate new metadata
METADATA_OUT=./mozilla_metadata.txt
echo '' > $METADATA_OUT

list_of_audios=(`ls audio-files`)
for i in "${list_of_audios[@]}"
do
    :
    #echo $i
    # check the file in TRAIN directory
    UTTID=(`basename $i .flac`)
    SPKID=(`cat $OTHER | grep $UTTID | cut -f1`)

    if [ -z "$SPKID" ]
    then 
        SPKID=(`cat $TRAIN | grep $UTTID | cut -f1`)
        if [ -z "$SPKID" ]
        then
            #check another directory
            SPKID=(`cat $TEST | grep $UTTID | cut -f1`)
            if [ -z "$SPKID" ]
            then
                SPKID=(`cat $DEV | grep $UTTID | cut -f1`)
                if [ -z "$SPKID" ]
                then
                    SPKID=(`cat $INVALIDATED | grep $UTTID | cut -f1`)
                    if [ -z "$SPKID" ]
                    then
                        SPKID=(`cat $VALIDATED | grep $UTTID | cut -f1`)
                        if [ -z "$SPKID" ]
                        then
                            echo "$UTTID has no log"
                        else
                            cp audio-files/$i $AUDIO_DESTINATION    # copy the audio file
                            TEXT=(`cat $VALIDATED | grep $UTTID | cut -f3`)
                            DURATION=(`ffprobe -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio-files/$i 2>/dev/null`)
                            echo $UTTID$'\t'$SPKID$'\t'${TEXT[*]}$'\t'$DURATION >> $METADATA_OUT
                        fi
                    else
                        cp audio-files/$i $AUDIO_DESTINATION    # copy the audio file
                        TEXT=(`cat $INVALIDATED | grep $UTTID | cut -f3`)
                        DURATION=(`ffprobe -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio-files/$i 2>/dev/null`)
                        echo $UTTID$'\t'$SPKID$'\t'${TEXT[*]}$'\t'$DURATION >> $METADATA_OUT
                    fi
                else
                    cp audio-files/$i $AUDIO_DESTINATION    # copy the audio file
                    TEXT=(`cat $DEV | grep $UTTID | cut -f3`)
                    DURATION=(`ffprobe -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio-files/$i 2>/dev/null`)
                    echo $UTTID$'\t'$SPKID$'\t'${TEXT[*]}$'\t'$DURATION >> $METADATA_OUT
                fi
            else
                cp audio-files/$i $AUDIO_DESTINATION    # copy the audio file
                TEXT=(`cat $TEST | grep $UTTID | cut -f3`)
                DURATION=(`ffprobe -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio-files/$i 2>/dev/null`)
                echo $UTTID$'\t'$SPKID$'\t'${TEXT[*]}$'\t'$DURATION >> $METADATA_OUT
            fi
        else
            cp audio-files/$i $AUDIO_DESTINATION    # copy the audio file
            TEXT=(`cat $TRAIN | grep $UTTID | cut -f3`)
            DURATION=(`ffprobe -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio-files/$i 2>/dev/null`)
            echo $UTTID$'\t'$SPKID$'\t'${TEXT[*]}$'\t'$DURATION >> $METADATA_OUT
        fi
    else
        cp audio-files/$i $AUDIO_DESTINATION    # copy the audio file
        TEXT=(`cat $OTHER | grep $UTTID | cut -f3`)
        DURATION=(`ffprobe -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio-files/$i 2>/dev/null`)
        echo $UTTID$'\t'$SPKID$'\t'${TEXT[*]}$'\t'$DURATION >> $METADATA_OUT
    fi
done