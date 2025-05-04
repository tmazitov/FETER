from uagents import Model

class AnalyticsRequest(Model):
    pass
    
class AnalyticsResponse(Model):
    message: str = None
    error: str = None