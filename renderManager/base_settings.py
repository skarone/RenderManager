"""Base Settings Module.

This works as an interface for each plugin settings.
"""
from attrDict import AttrDict


class BaseSetting(AttrDict):

    REQUIRED_SETTINGS = {
        'cameras': list,
        'frame': list,
        'is_range': bool,
        'resolution': tuple,
    }

    def __init__(self, settings):
        self.validate(settings)
        super(BaseSetting).__init__(settings)

    def validate(self, settings):
        for setting in self.REQUIRED_SETTINGS.items():
            if not setting in settings:
                raise KeyError('Missing setting in provided settings: {}'.format(setting))
            if not isinstance(settings[setting], self.REQUIRED_SETTINGS[setting]):
                raise KeyError('Setting {} is not the required type {}'.format(setting, self.REQUIRED_SETTINGS[setting]))
    