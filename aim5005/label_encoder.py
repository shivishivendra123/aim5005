import numpy as np
from typing import List, Tuple
### YOU MANY NOT ADD ANY MORE IMPORTS (you may add more typing imports)

class LabelEncoder:
    def __init__(self):
        self.classes_ = None
        
    def _check_is_array(self, x:np.ndarray) -> np.ndarray:
        """
        Try to convert x to a np.ndarray if it'a not a np.ndarray and return. If it can't be cast raise an error
        """
        if not isinstance(x, np.ndarray):
            x = np.array(x)
            
        assert isinstance(x, np.ndarray), "Expected the input to be a list"
        return x
        
    
    def fit(self, x:np.ndarray) -> None:
       x = self._check_is_array(x) 
       unique_classes = sorted(set(x))
       self.classes_ = np.array(unique_classes)

    def transform(self,x:np.ndarray)->np.ndarray:
        x = self._check_is_array(x)
        obj = []
        obj = {val:ind for ind,val in enumerate(self.classes_)}
        ret = [obj[i] for i in x]

        return ret
    
    def fit_transform(self,x:np.ndarray)->np.ndarray:
        x = self._check_is_array(x)
        self.fit(x)
        return self.transform(x)
    
        