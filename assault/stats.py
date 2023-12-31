from typing import List, Dict
from statistics import mean

class Results:
    """
    Results handles calculating statistics based on a list of
    requests that were made.
    Here's an example of what the information will look like:
    Successful requests 3000
    Slowest 0.010s
    Fastest 0.001s
    assault/stats.py (partial)
    Average 0.003s
    Total time 2.400s
    Requests Per Minute 90000
    Requests Per Second 125
    """
    def __init__(self, total_time: float, requests: List[Dict]):
        self.total_time = total_time
        self.requests = sorted(requests, key=lambda r:r["request_time"]) # Since we're working with dictionaries and we want to sort by the key, we need to use a lambda.
    #  The equivalent named function for this lambda would be this
    # def request_time(request_dict):
    #     return request_dict['request_time']

    def slowest(self) -> float:
        # Doctest for the slowest method
        """
        Returns the slowest request's completion time
        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.slowest()
        6.1
        """
        # Need to get the last item to get the slowest response time [-1]
        return self.requests[-1] ["request_time"]


    def fastest(self) -> float:
        """
        Returns the slowest request's completion time
        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.fastest()
        1.04
        """
        # Need to get the first item to get the fastest response time [0]
        return self.requests[0] ["request_time"]
    def average_time(self) -> float:
        """
        Returns the slowest request's completion time
        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.average_time()
        3.513333333333333
        """
        return mean([r["request_time"] for r in self.requests]) # Extract information from one list and return a new list with the information. In this case we want only the request_time volue from each dictionary.
    def total_time(self) -> float:
            pass
    def successful_requests(self) -> int:
        """
        Returns the slowest request's completion time
        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.successful_requests()
        2
        """
        return len([r for r in self.requests if r["status_code"] in range(200, 299)]) # Return 'r' for each 'r' in the 'self.requests' list if the r's 'status_code' is within the range 200 - 299

    def requests_per_minute(self) -> int:
        """
        Returns the number of requests made per minute
        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.requests_per_minute()
        17
        """
        # 3 / 10.6 = x / 60
        # 60 * 3 / 10.6 = x
        return round(60 * len(self.requests) / self.total_time)

    def requests_per_second(self) -> int:
        """
        Returns the number of requests made per second
        >>> results = Results(3.5, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 2.9
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 0.4
        ... }])
        >>> results.requests_per_second()
        1
        """
        # 4 / 3.5 = x / 1
        return round(len(self.requests) / self.total_time)
