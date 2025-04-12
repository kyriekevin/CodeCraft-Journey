"""
Platform: DeepML
Problem: 53 - Implement Self-Attention Mechanism
Difficulty: Medium
URL: https://www.deep-ml.com/problems/53

Date: 2025-04-12
Time: 12:29

Author: Kyire
"""

import numpy as np


def compute_qkv(X, W_q, W_k, W_v):
    Q = np.dot(X, W_q)
    K = np.dot(X, W_k)
    V = np.dot(X, W_v)
    return Q, K, V


def self_attention(Q, K, V):
    d_k = K.shape[1]
    scores = np.matmul(Q, K.T) / np.sqrt(d_k)
    weights = np.exp(scores) / np.sum(np.exp(scores), axis=-1, keepdims=True)
    attention_output = np.matmul(weights, V)
    return attention_output
