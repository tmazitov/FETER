from analytics_agent.asi1 import asi1_send_request
from analytics_agent.model import AnalyticsRequest, AnalyticsResponse
from analytics_agent.request import make_analytics_request
from main_agent.models import EthicsRequest
from uagents import Agent, Context, Protocol, Model
from uagents.setup import fund_agent_if_low
from env import SEED

# Initialize the database and agent
agent = Agent(name="Celebrity.AI", seed=SEED)
fund_agent_if_low(agent.wallet.address())

# Define the protocol
analytics_protocol = Protocol(name="analytics_protocol", version="1.0")

@analytics_protocol.on_message(model=AnalyticsRequest, replies=AnalyticsResponse)
async def analytics_handler(ctx: Context, sender: str, req: AnalyticsRequest):
    ctx.logger.info(f"Received request for analytics")
    
    message = None
    context, response_schema = make_analytics_request()
    try:
        message = asi1_send_request(context=context, prompt="", response_schema=response_schema)
    except Exception as e:
        ctx.logger.error(f"Error during analytics processing: {e}")
        await ctx.send(sender, AnalyticsResponse(error="500 Internal server error."))
        return

    await ctx.send(sender, AnalyticsResponse(message=message))

agent.include(analytics_protocol)

agent.run()