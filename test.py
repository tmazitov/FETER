import asyncio
import time
from uagents import Agent, Context, Protocol
from model import AnalyticsRequest, AnalyticsResponse

tester = Agent(name="Tester.AI", seed="1234")

agent_address = input("Enter the address of the analytics agent: ")
analytics_protocol = Protocol(name="analytics_protocol", version="1.0")

@tester.on_interval(5)
async def check_fet(ctx: Context):
    ctx.logger.info("Checking for new analytics requests...")
    asyncio.create_task(ctx.send(agent_address, AnalyticsRequest()))

@analytics_protocol.on_message(AnalyticsResponse)
async def receive_analytics(ctx: Context, sender: str, message: AnalyticsResponse):
    if message.error:
        ctx.logger.info(f"Error from analytics agent: {message.error}")
        return

    message = message.message
    ctx.logger.info(f"Received response from analytics agent: {message}")

        
tester.include(analytics_protocol)

tester.run()