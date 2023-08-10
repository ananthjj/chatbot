from langchain import PromptTemplate, LLMChain, OpenAI # Import the classes
from langchain.agents import create_json_agent, AgentExecutor
from langchain.agents.agent_toolkits import JsonToolkit
from langchain.requests import TextRequestsWrapper
from langchain.tools.json.tool import JsonSpec
from socceraction.data.wyscout import PublicWyscoutLoader # Import the data loader
from langchain.vectorstores import VectorStore;
from langchain.tools import JsonListKeysTool, JsonGetValueTool;
import json
import pandas as pd
from langchain.agents import create_pandas_dataframe_agent  




# Create the data loader
api = PublicWyscoutLoader(root="data/wyscout")

"""api = WyscoutLoader(getter="local", root="data/wyscout", feeds={
  "competitions": "competitions.json",
  "seasons": "seasons_{competition_id}.json",
  "games": "matches_{season_id}.json",
  "events": "matches/events_{game_id}.json",
})"""

"""
# Create the prompt template
prompt = PromptTemplate(
    input_variables=["statistic", "player_name", "season"],
    template="What is the {statistic} of {player_name} in the {season} season?",
)

# Create the language model
llm = OpenAI(openai_api_key="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")

chain = LLMChain(llm=llm, prompt=prompt) # Create the chain"""

# Connect to the data store and load the data
competitions = pd.read_json("data/wyscout/competitions.json")

#with open("data/wyscout/seasons.json") as s_file:
#    seasons = json.load(s_file)

#with open("data/wyscout/games.json") as g_file:
#    games = json.load(g_file)

players = pd.read_json("data/wyscout/players.json")

teams = pd.read_json("data/wyscout/teams.json")


    
"""  
competitions_data = api.competitions()  # Load competitions data
games_data = api.games()  # Load games data
teams_data = api.teams()  # Load teams data
"""
"""players_data = api.players()  # Load players data
events_data = api.events()  # Load events data"""

#print(games_data)
"""
competition_spec = JsonSpec(dict_=api, max_value_length=4000)

competition_toolkit = JsonToolkit(spec=competition_spec)

#print(competition_toolkit)

json_agent_executor = create_json_agent(
    llm=OpenAI(openai_api_key="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", 
               temperature=0.9), toolkit=competition_toolkit, verbose=True
               )

# json_agent_executor.run("What competition is played in England?")
"""

agent = create_pandas_dataframe_agent(OpenAI(
    openai_api_key="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", temperature=0),
      [competitions, players, teams], verbose=True)

agent.run("What competition is played in England?")