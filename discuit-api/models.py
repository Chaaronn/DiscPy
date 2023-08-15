from typing import Dict, List

class Result:
    def __init__(self, status_code: int, message: str = '', data: List[Dict] = None):
        self.status_code = status_code
        self.message = str(message)
        self.data = data if data else []

        
        