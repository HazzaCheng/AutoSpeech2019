[![license](https://img.shields.io/badge/license-GPL%203.0-green.svg)](https://github.com/HazzaCheng/AutoSpeech/blob/master/LICENSE)

# AutoSpeech2019

## Introduction

The 1st place solution for [AutoSpeech 2019](https://www.4paradigm.com/competition/autospeech2019). Asian Conference on Machine Learning (ACML) 2019 was held in WINC AICHI, Nagoya, Japan from November 17 to 19, 2019. AutoSpeech is one of the competitions in main conference provided by 4Paradigm, ChaLearn and Google. 

## Usage

Run

```
python run_local_test.py -dataset_dir=./sample_data/DEMO -code_dir=./code_submission
```

You can change the argument `dataset_dir` to other datasets, and change the argument `code_dir` to the directory containing this code (`model.py`).

## Basic Solution

Our algorithm preprocess data and select models automatically, model lib contains some different models. Because this competition is focused on both AUC and speed, also, the time is limited. So we use the simple model and extract simple features in the earlier loops to get the scores as fast as possible, and we use the complex models and extract complex features in the later loops to get the higher scores. For all datasets, we use a sequence of models and features.

## Dataset

You can get the dataset format form [here](https://www.4paradigm.com/competition/autospeech2019).

## Contributor

- Feng Cheng, NJU, [hazzacheng@gmail.com](mailto:hazzacheng@gmail.com)
- Zhuoer Xu, NJU, [xuzhuoer.rex@gmail.com](mailto:xuzhuoer.rex@gmail.com)
- Wenjie Wang, NJU, [wjwangpt@gmail.com](mailto:wjwangpt@gmail.com)
- Mengchuan Qiu, NJU, [mengchuan.qiu@smail.nju.edu.cn](mailto:mengchuan.qiu@smail.nju.edu.cn)
