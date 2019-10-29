# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
  AutoNLP datasets.
"""

import os
import numpy as np
import pickle

class AutoSpeechDataset(object):
    def __init__(self, dataset_dir):
        """
            train_dataset, test_dataset: list of strings
            train_label: np.array
        """
        self.dataset_name_ = dataset_dir
        self.dataset_dir_ = dataset_dir
        self.metadata_ = self.read_metadata(os.path.join(dataset_dir, "meta.json"))

    def read_dataset(self):
        self.train_dataset = self._read_dataset(os.path.join(self.dataset_dir_, "train.pkl"))
        self.train_label = self.read_label(os.path.join(self.dataset_dir_, "train.solution"))
        self.test_dataset = self._read_dataset(os.path.join(self.dataset_dir_, "test.pkl"))

    def get_train(self):
        return self.train_dataset, self.train_label

    def get_test(self):
        return self.test_dataset

    def get_metadata(self):
        return self.metadata_

    def read_metadata(self, metadata_path):
        import json
        return json.load(open(metadata_path))

    def _read_dataset(self, dataset_path):
        with open(dataset_path, 'rb') as fin:
            return pickle.load(fin)

    def read_label(self, label_path):
        return np.loadtxt(label_path)

    def get_class_num(self):
        """ return the number of class """
        return self.metadata_["class_num"]

    def get_train_num(self):
        """ return the number of train instance """
        return self.metadata_["train_num"]

    def get_test_num(self):
        """ return the number of test instance """
        return self.metadata_["test_num"]

    def get_language(self):
        """ ZH or EN """
        return self.metadata_["language"]
