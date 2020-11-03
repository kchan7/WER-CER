# WER-CER

1. wer.py
   行毎に単語を比較するので句点(。)は調整して、読点(、)は不要なので削除して下さい。
   original_file.txt は正解とする文書、target_file.txt は STT で書き起こした文書です。

```bash
pip install numpy
brew install mecab
pip install mecab-python3

python wer.py [original_file.txt]  [target_file.txt]
```

2. cer.py
   行毎に単語を比較するので句点(。)は調整して、読点(、)は不要なので削除して下さい。
   original_file.txt は正解とする文書、target_file.txt は STT で書き起こした文書です。

```bash
python cer.py [original_file.txt]  [target_file.txt]
```
