#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
from math import log
from zkit.tofromfile import tofile, fromfile

def idf_dumps(count, df):
    result = {}
    count = float(count)
    for k, v in df.iteritems():
        rank = count/v
        if rank > 1000000: # idf训练中, 低于1/100w的的词直接去掉..
            continue
        result[k] = log(rank)

    return result

def tf_idf(idf, word_list):
    tf = defaultdict(int)
    for i in word_list:
        tf[i] += 1
    result = []
    for k, v in tf.iteritems():
        if k in self._idf:
            result.append((k, v*idf[k]))
    return result
