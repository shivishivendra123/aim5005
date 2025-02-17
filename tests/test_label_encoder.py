from aim5005.label_encoder import LabelEncoder
import numpy as np
import unittest
from unittest.case import TestCase

class TestFeatures(TestCase):
    def test_initialize_label_encoder(self):
        label_encoder = LabelEncoder()
        assert isinstance(label_encoder, LabelEncoder), "label_encoder is not a LabelEncoder object"
        
    def test_label_encoder_fit(self):
        label_encoder = LabelEncoder()
        data = ['animal','cats','cats','dogs']
        expected = np.array(['animal','cats','dogs'])
        label_encoder.fit(data)
        assert (label_encoder.classes_== expected).all(), "lLabel Encoder fit does not return expected values"
        
    def test_label_encoder_transform(self):
        data = ['animal','cats','cats','dogs']
        expected = np.array([0,1,1,2])
        label_encoder = LabelEncoder()
        label_encoder.fit(data)
        result = label_encoder.transform(data)
        assert (result == expected).all(), "Label Encoder transform does not return expected values Got: {}".format(result.reshape(1,-1))

    def test_label_encoder_fit_transform(self):
        data = ['animal','cats','cats','dogs']
        expected = np.array([0,1,1,2])
        label_encoder = LabelEncoder()
        result = label_encoder.fit_transform(data)
        assert (result == expected).all(), "Label Encoder fit_transform does not return expected values. Got: {}".format(result.reshape(1,-1))
        
if __name__ == '__main__':
    unittest.main()