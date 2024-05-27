    def set_trackers(self, experiment_trackers: list[ExperimentTracker] = None):
        if experiment_trackers:
            self.chain_callbacks = experiment_trackers
            logger.info(f"chain_callbacks: {self.chain_callbacks}")

            effective_callbacks = []
            for cb in self.chain_callbacks:
                effective_callbacks.append(cb.get())

            logger.info(f"Effective callback handlers: {effective_callbacks}")
            self.chain_callback_effective_config = {"callbacks": effective_callbacks}

        return self
