"""Base Plugin Class.

Works as an interface for subclasses.
You can add pre/post hooks to the process, the order of adding them will be the order of execution.

"""

class BasePlugin(object):
    def __init__(self, settings=None):
        self.settings = settings
        self._pre_hooks = []
        self._post_hooks = []

    def execute(self):
        """"""
        self.run_pre_hooks()
        self.run()
        self.run_post_hooks()