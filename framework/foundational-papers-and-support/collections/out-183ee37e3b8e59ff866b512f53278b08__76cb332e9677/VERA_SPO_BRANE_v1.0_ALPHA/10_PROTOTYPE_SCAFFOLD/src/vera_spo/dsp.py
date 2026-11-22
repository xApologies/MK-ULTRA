class DSPBackend:
    """Interface placeholder. No production audio transformation is implemented in 1.0 Alpha."""
    def apply(self, pcm_frame, decision):
        raise NotImplementedError("DSP realization belongs to a later executable/audio prototype")
