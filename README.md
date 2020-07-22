# transformers-jobs

The transformers directory contains the slightly modified filed of transformers from huggingface.

```scrape.py``` used for scraping linkedin.
```preprocess.py``` convert the json to train,val,test files that can be used with transformer code.

Run ```pip install requirements.txt``` 

Run ```git clone github.com/huggingface/transformers```


Update the relevant files in transformers repository.

To finetune:

```python run_language_modeling.py --output_dir=/path/to/output --model_type=gpt2 --model_name_or_path=gpt2 --do_train --train_data_file=/path/to/train.txt --do_eval --eval_data_file=/path/to/val.txt --do_eval --per_device_train_batch_size=1 --per_device_eval_batch_size=1 --line_by_line --evaluate_during_training --learning_rate 5e-5 --num_train_epochs=5```

To generate text:

```python run_generation.py --model_type gpt2 --model_name_or_path /path/to/output --length 300 --prompt "<BOS>" --stop_token "<EOS>" --k 0 --num_return_sequences 100```


 
