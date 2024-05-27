from typing import Any, Dict, Optional

from langchain_core.agents import AgentAction, AgentFinish
from langchain_core.callbacks.base import BaseCallbackHandler
from loguru import logger

from utils.tracker.experiment_tracker import ExperimentTracker


class LoguruInfoCallbackHandler(BaseCallbackHandler, ExperimentTracker):
    service_name = "loguru_callback_handler"

    @classmethod
    def get(cls, config: dict = None):
        return cls()

    def on_chain_start(
            self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> None:
        """Print out that we are entering a chain."""
        class_name = serialized.get("name", serialized.get("id", ["<unknown>"])[-1])
        logger.debug(f"\033[1m> Entering new {class_name} chain...\033[0m")

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        """Print out that we finished a chain."""
        logger.debug("\033[1m> Finished chain.\033[0m")

    def on_agent_action(
            self, action: AgentAction, color: Optional[str] = None, **kwargs: Any
    ) -> Any:
        """Run on agent action."""
        logger.debug(action.log)

    def on_tool_end(
            self,
            output: str,
            color: Optional[str] = None,
            observation_prefix: Optional[str] = None,
            llm_prefix: Optional[str] = None,
            **kwargs: Any,
    ) -> None:
        """If not the final action, print out observation."""
        if observation_prefix is not None:
            logger.debug(f"{observation_prefix}")
        logger.debug(output)
        if llm_prefix is not None:
            logger.debug(f"{llm_prefix}")

    def on_text(
            self,
            text: str,
            color: Optional[str] = None,
            end: str = "",
            **kwargs: Any,
    ) -> None:
        """Run when agent ends."""
        logger.debug(text)

    def on_agent_finish(
            self, finish: AgentFinish, color: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Run on agent end."""
        logger.debug(finish.log)
