def make_analytics_request():
    
    """
     , 
    if the change is positive by more than 20% return 
    'Buy', if the change is lower by more than 20% return 'Sell', else return 'Hold'."""
    
    requirements = [
        "Only return one word answer from list ('Buy', 'Hold', 'Sell')"
        f"Based on past 10 days accumulative price changes of crypto currency $FET",
        """Make a result following thus 3 rules: 
            1. If the change is positive by more than 20% return 'Buy',
            2. If the change is lower by more than 20% return 'Sell',
            3. If the change is not more than 20% return 'Hold'
            4. In case of any error, return 'Hold""",
    ]   
    context = ". ".join(requirements)
    response_schema = {
        "type": "object",
        "properties": {
            "result": {
                "type": "string",
                "description": "The result returned by ASI:ONE as plain text.",
            },
        },
        "required": ["result"],
    }
    return context, response_schema