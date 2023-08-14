import numpy as np
import pandas as pd
import pickle
from content import *

picklefile=open('res','wb')
pickle.dump(ContentBasedRecommender,picklefile)
print("DONE")
