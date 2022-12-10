"""Base Plugin Class.

Works as an interface for subclasses.
"""
from abc import ABC
import traceback


class BasePlugin(ABC):
    """Abstract Base Plugin Class.

    Props to override:
        NAME (str): Name of the plugin.
        CAN_FARM (bool): Can the plugin run on the farm.

    Methods that can be overriden:
        pre_local/farm_run
        local/farm_run
        post_local/farm_run
    """
    NAME = None
    CAN_FARM = None

    def __init__(self, settings):
        """Initialize Plugin.

        Args:
            settings (BaseSettings): Settings of the plugin.
        """
        self.settings = settings
        # This directory will be deleted after process ran/failed.
        self.temp_dir = None

    # pylint: disable=bare-except
    def execute(self):
        """Main call to run the plugin."""
        self.temp_dir = ''  # TODO: Add mktempdir call.
        try:
            self._pre_run()
            self._run()
            self.post_run()
        except:
            traceback.print_exc()
        finally:
            self._clean()
    # pylint: enable=bare-except

    def _pre_run(self):
        """Run pre processes."""
        if self.settings.in_farm:
            self.pre_farm_run()
        else:
            self.pre_local_run()

    def pre_farm_run(self):
        """Run pre processes needed on the farm."""
        pass

    def pre_local_run(self):
        """Run pre processes needed on local."""
        pass

    def _run(self):
        """the main process to run."""
        if self.settings.in_farm:
            self.farm_run()
        else:
            self.local_run()

    def farm_run(self):
        """Run main process needed on farm."""
        pass

    def local_run(self):
        """Run main process needed on local."""
        pass      

    def submit(self):
        """Use it to send to the farm."""
        pass

    def post_run(self):
        """Run post processes."""
        if self.settings.in_farm:
            self.post_farm_run()
        else:
            self.post_local_run()

    def post_farm_run(self):
        """Run pre processes needed on local."""
        pass

    def post_local_run(self):
        """Run pre processes needed on local."""
        pass

    def _clean(self):
        """Delete temp directory."""
        # TODO: add delete tmp dir folder.
        pass
