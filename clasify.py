#!/usr/bin/env python

import os
from os.path import abspath, dirname, join

from bayesian import classify

def _get_train_set():
    TRAIN_PATH = join(dirname(abspath(__file__)), 'training-set')
    train = []
    for root, directories, files in os.walk(TRAIN_PATH):
        for filename in files:
            filepath = join(root, filename)
            with open(filepath) as f:
                train.append((filename.split('.')[0], f.readlines()))
    return dict(train)


def get_language(s):
    train = _get_train_set()
    return classify(s, train)
