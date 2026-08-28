from agents import ModelSettings
from common.agent_utils import llm_agent
from common.model import openai_gpt_mini, gemini_flash_lite, openai_gpt_oss, GEMINI_BASE_URL, GROQ_BASE_URL
from common.emails import send_email_tool, email_guardrail

instructions = """
You are a sales agent working for ComplAI,
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI.
You write emails.
"""

instructions1 = instructions + "Your email style is professional, serious, with gravitas and credibility."
instructions2 = instructions + "Your email style is witty, engaging, and humorous."
instructions3 = instructions + "Your email style is concise, to the point, in the style of a busy senior executive."

sales_agent1 = llm_agent(agent_name="Professional Sales Agent", model=openai_gpt_mini, instructions=instructions1)
sales_agent2 = llm_agent(agent_name="Humorous Sales Agent", model=openai_gpt_mini, instructions=instructions2)
sales_agent3 = llm_agent(agent_name="Executive Sales Agent", model=openai_gpt_mini, instructions=instructions3)

decision_picker = """
You pick the best cold sales email from the given options.
Imagine you are a customer and pick the one you are most likely to respond to.
Do not give an explanation; reply with the selected email only.
"""

sales_picker = llm_agent(agent_name="Sales Picker", model=openai_gpt_mini, instructions=decision_picker)

decision_sender = """
You pick the best cold sales email from the given options.
Imagine you are a customer and pick the one you are most likely to respond to.
Then use your tool to send the email.
"""

require_tool = ModelSettings(tool_choice="required")

sales_sender = llm_agent(agent_name="Sales Sender", model=openai_gpt_mini, instructions=decision_sender, tools_list=[send_email_tool], model_settings=require_tool)

gemini_sales_agent = llm_agent(agent_name="Gemini Sales Agent", model=gemini_flash_lite, instructions=instructions, api_key="GEMINI_API_KEY", base_url=GEMINI_BASE_URL)
oss_sales_agent = llm_agent(agent_name="GPT-OSS Sales Agent", model=openai_gpt_oss, instructions=instructions, api_key="GROQ_API_KEY", base_url=GROQ_BASE_URL)

description = "Use this tool to write a sales email. In the input, just instruct it to write a sales email."

gemini_tool = gemini_sales_agent.as_tool(tool_name="gemini_tool", tool_description=description)
oss_tool = oss_sales_agent.as_tool(tool_name="oss_tool", tool_description=description)

tools = [gemini_tool, oss_tool, send_email_tool]

multi_manager_instructions = """
You are a Sales Manager at ComplAI. Your goal is to find the single best cold sales email using the provided sales agent tools.
"""

multi_sales_manager = llm_agent(agent_name="Multiple LLM Sales Manager", model=openai_gpt_mini, instructions=multi_manager_instructions, tools_list=tools)