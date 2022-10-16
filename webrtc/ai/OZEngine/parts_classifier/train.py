# Import the libraries
from random import uniform
from pathlib import Path
from PIL import Image
import numpy as np
import os, sys
import pickle

from OZEngine.FeatureExtractor import FeatureExtractor

fe = FeatureExtractor('./FullDressUniform')
fe.train()