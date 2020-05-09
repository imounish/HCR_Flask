import os
import cv2
from core.Model import Model, DecoderType
from core.SamplePreprocessor import preprocess
from core.DataLoader import Batch

class FilePaths: 
    fnCharList = os.path.abspath("../hcr_flask/model/charList.txt") 
    fnAccuracy = os.path.abspath("../hcr_flask/model/accuracy.txt") 
    # fnInfer = os.path.abspath("../static/data/test.png") 

def infer(imgPath):
    decoderType = DecoderType.BestPath
    model = Model(open(FilePaths.fnCharList).read(), decoderType, mustRestore = True, dump = False)
    img = preprocess(cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE), Model.imgSize)
    batch = Batch(None, [img])
    (recognized, probability) = model.inferBatch(batch, True)
    return (recognized[0], probability[0])

