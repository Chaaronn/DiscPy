import requests
import requests.packages
from typing import List, Dict
from exceptions import DiscuitAPIException
from json import JSONDecodeError
from models import Result

class RestAdapter:
    def __init__(self, hostname: str, api_key: str = '', ssl_verify: bool = True):
        self.url = "https://{}/".format(hostname)

        # save to private member variables
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            requests.packages.urllib3.disable_warnings()

    def _do(self, http_method: str, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        full_url = self.url + endpoint
        # will be required for auth down the line
        headers = {}
        try:
            response = requests.request(method=http_method, url=full_url, verify=self._ssl_verify, 
                                        headers=headers, params=ep_params, json=data)
        except requests.exceptions.RequestException as e:
            raise DiscuitAPIException("Request Failed") from e

        try:
            data = response.json()
        except (ValueError, JSONDecodeError) as e:
            raise DiscuitAPIException("Bad JSON response") from e

        if 299 >= response.status_code >= 200: # okay 
            # return a result object
            return Result(response.status_code, message=response.reason, data=data)
        raise DiscuitAPIException(f"{response.status_code} :  {response.reason}")


    def get(self, endpoint: str, ep_params: Dict = None) -> Result:
        return self._do(http_method='GET', endpoint=endpoint, ep_params=ep_params)
    
    def post(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        return self._do(http_method='POST', endpoint=endpoint, ep_params=ep_params, data=data)
    
    def delete(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        return self._do(http_method='DELETE', endpoint=endpoint, ep_params=ep_params, data=data)

discuitapi = RestAdapter(hostname= "discuit.net/api")
test_params = {'communityId' : '17692e122def73f25bd757e0'}
result = discuitapi.get("posts", ep_params=test_params)
print(result.data)