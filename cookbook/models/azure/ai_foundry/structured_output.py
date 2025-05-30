from typing import List

from agno.agent import Agent, RunResponse  # noqa
from agno.models.azure import AzureAIFoundry
from pydantic import BaseModel, Field
from rich.pretty import pprint  # noqa


class MovieScript(BaseModel):
    setting: str = Field(
        ..., description="Provide a nice setting for a blockbuster movie."
    )
    ending: str = Field(
        ...,
        description="Ending of the movie. If not available, provide a happy ending.",
    )
    genre: str = Field(
        ...,
        description="Genre of the movie. If not available, select action, thriller or romantic comedy.",
    )
    name: str = Field(..., description="Give a name to this movie")
    characters: List[str] = Field(..., description="Name of characters for this movie.")
    storyline: str = Field(
        ..., description="3 sentence storyline for the movie. Make it exciting!"
    )


agent = Agent(
    model=AzureAIFoundry(id="gpt-4o"),
    description="You help people write movie scripts.",
    response_model=MovieScript,
    # debug_mode=True,
)

# Get the response in a variable
# run: RunResponse = agent.run("New York")
# pprint(run.content)

agent.print_response("New York")
