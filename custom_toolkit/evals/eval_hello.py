import arcade_custom_toolkit
from arcade_custom_toolkit.tools.hello import hello

from arcade.sdk import ToolCatalog
from arcade.sdk.eval import (
    EvalRubric,
    EvalSuite,
    SimilarityCritic,
    tool_eval,
)

# Evaluation rubric
rubric = EvalRubric(
    fail_threshold=0.85,
    warn_threshold=0.95,
)


catalog = ToolCatalog()
catalog.add_module(arcade_custom_toolkit)


@tool_eval()
def custom_toolkit_eval_suite():
    suite = EvalSuite(
        name="custom_toolkit Tools Evaluation",
        system_message="You are an AI assistant with access to custom_toolkit tools. Use them to help the user with their tasks.",
        catalog=catalog,
        rubric=rubric,
    )

    suite.add_case(
        name="Saying hello",
        user_message="Say hello to the developer!!!!",
        expected_tool_calls=[
            (
                hello,
                {
                    "name": "developer"
                }
            )
        ],
        rubric=rubric,
        critics=[
            SimilarityCritic(critic_field="name", weight=0.5),
        ],
    )

    return suite