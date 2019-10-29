#!/bin/bash

log_folder="./log_output"
if [ ! -x $log_folder ]; then
	mkdir $log_folder
fi
for arg in $*
do
	dataset_dir="/home/chengfeng/autospeech/data/data0$arg"
	cur_time="`date +%Y-%m-%d-%H-%M-%S`"
	log_file="$log_folder/O$arg-$cur_time.log"
	python_command="python run_local_test.py --dataset_dir=$dataset_dir -code_dir=./code_submission 2>&1"
	log_command="tee -i $log_file"
	echo "Current time: $cur_time"
	echo "Run command: $python_command"
	echo "Log info into file: $log_file"
	eval "$python_command | $log_command"
    cp scoring_output/*.png $log_folder/O$arg-$cur_time.png
done

