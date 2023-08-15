import requests
import requests.packages
from typing import List, Dict

class RestAdapter:
    def __init__(self, hostname: str, api_key: str = '', ssl_verify: bool = True):
        self.url = "https://{}/".format(hostname)

        # save to private member variables
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            requests.packages.urllib3.disable_warnings()

    def get(self, endpoint: str, ep_params: Dict = None) -> List[Dict]:
        full_url = self.url + endpoint
        headers = {}
        response = requests.get(full_url, verify=self._ssl_verify, 
                                headers=headers, params=ep_params)
        data = response.json()

        if response.status_code >= 200 and response.status_code <= 299: # okay 
            return data
        raise Exception(data['message'])    # todo, raise custom expection
    
    # needs auth to work so adding for future
    
    

discuitapi = RestAdapter(hostname= "discuit.net/api")
test_params = {'communityId' : '17692e122def73f25bd757e0'}
post_list = discuitapi.get("posts", ep_params=test_params)
print(post_list)