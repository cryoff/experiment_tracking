# from dataclasses import dataclass
#
# import mlflow
# from langchain_community.callbacks import MlflowCallbackHandler
#
# from utils.tracker.experiment_tracker import ExperimentTracker
#
#
# class MlFlowTracker(ExperimentTracker):
#     service_name = "mlflow"
#     _instance = None
#
#     def _get_instance(self, config: dict = None) -> MlflowCallbackHandler | None:
#         return MlflowCallbackHandler(tracking_uri=self._endpoint)
#
#     @dataclass
#     class LangChainExperimentData:
#         input_text: str
#         age: str
#         gender: str
#         response: str
#         execution_time: float
#
#     @classmethod
#     def track_experiment(cls, experiment_data: LangChainExperimentData):
#         if cls._instance:
#             with mlflow.start_run():
#                 # we can't use mlflow langchain integration: SequentialChain is not supported
#                 # i tried to hack it but no luck
#                 # logged_model = mlflow.langchain.log_model(self.llm_chain.chain, "self_llm_chain")
#                 mlflow.log_param("input_text", experiment_data.input_text)
#                 mlflow.log_param("age", experiment_data.age)
#                 mlflow.log_param("gender", experiment_data.gender)
#                 mlflow.log_param("response_content", experiment_data.response)
#                 mlflow.log_metric("execution_time", experiment_data.execution_time)
