# -*- coding: utf-8 -*-
"""
Created on 6/23/2024
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    """
    Class which describes Bank Notes measurements
    """
    variance: float
    skewness: float
    curtosis: float
    entropy: float