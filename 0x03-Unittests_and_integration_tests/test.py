def our_side_effect_function(url):
    # If URL is asking for org info (like "https://api.github.com/orgs/google")
    if "":  # What condition should go here?
        return # What should we return?
    
    # If URL is asking for repos (like "https://api.github.com/orgs/google/repos") 
    elif "condition_2":  # What condition should go here?
        return # What should we return?

# Remember: requests.get() returns a response object that has a .json() method
# So we need to mock both the response object AND its json() method

class MockResponse:
    def __init__(self, json_data):
        self._json_data = json_data
    
    def json(self):
        return self._json_data  
