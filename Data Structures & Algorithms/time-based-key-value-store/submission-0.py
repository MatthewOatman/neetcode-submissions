class TimeMap:

    '''
    Notes:
    - All timestamps are strictly increasing with set
    - lowercase
    - 


    I am confused why you can't have the values simply be a list where the later elements in the list are those that were set at a later timestamp

    however I think this messes up when the user adds a bunch of keys incrementing the timestamp and then searches for a timestamp say 


    set matt hello 1
    set james hi 2
    set matt hey 3
    get matt 2
    I need to know that I need to return hello with 1 however don't know how to search in that time. 

    so I can set with 

    '''

    def __init__(self):
        self.data = {} # Key : value = [(val, timestamp), ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If already key-value pair associated - append
        if key in self.data:
            self.data[key].append((value, timestamp))
        else:
            self.data[key] = [(value, timestamp)]
        
    def get(self, key: str, timestamp: int) -> str:
        # if there are no values return "" - if key does not exist or if no values in the key 
        if key not in self.data:
            return ""

        arr = self.data[key]
        l = 0
        r = len(arr) - 1

        res = ""

        while l <= r:
            m = (l + r) // 2
            if arr[m][1] == timestamp:
                return arr[m][0]
            elif arr[m][1] > timestamp:
                r = m - 1
            elif arr[m][1] < timestamp:
                res = arr[m][0]
                l = m + 1

        # This is the case if the timestamp is too early for values added
        return res






        
