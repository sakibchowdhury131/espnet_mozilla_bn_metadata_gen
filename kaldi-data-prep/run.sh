python3 train-test-val-split.py
python3 generate_utt2spk.py
perl utt2spk_to_spk2utt.pl data/train/utt2spk > data/train/spk2utt
perl utt2spk_to_spk2utt.pl data/val/utt2spk > data/val/spk2utt
perl utt2spk_to_spk2utt.pl data/test/utt2spk > data/test/spk2utt
python3 gen-text.py
python3 gen-scp.py
scp -r data nlp@172.16.4.132:/media/nlp/data/tts/content/espnet/egs/ljspeech/tts1