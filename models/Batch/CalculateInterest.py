from Interfaces.IBatch import IBatch
from models.Result import Result
from models.Batch import BatchCreateHelper as bh
from app import db

class CalculateInterest(IBatch):

    def __init__(self):
        self=self

    def Create(self,form):
        bhelper = bh.batchHelper
        batch = bhelper.createBatchObject(request.form)

        
        #return Result(True,"Batch Created")

    
    def Execute(self):
        return Result(True,"Batch Run SuccessFully")