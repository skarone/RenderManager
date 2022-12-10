"""Base Settings Module.

This works as an interface for each plugin settings.
"""
from attrDict import AttrDict


class BaseSettings(AttrDict):
    """Abstract Base Settings."""

    _REQUIRED_SETTINGS = {
        'cameras': list,  # List of cameras to render.
        'frames': list,  # List of frames to render (Ex: [1001, 1200, 1305])
        'is_range': bool,  # If True will use first and last frames only and render as a range.
        'resolution': tuple,  # Width and Height of the images to render.
        'in_farm': bool,  # If True is rendering on the farm.
        'use_local': bool  # If True is rendering from the submit pc.
    }
    REQUIRED_SETINGS = None  # Settings that SubClasses can populate.

    def __init__(self, settings):
        self.validate(settings)
        super(BaseSettings).__init__(settings)

    # pylint: disable=consider-using-f-string
    def validate(self, settings):
        """Validate provided settings."""
        self._REQUIRED_SETTINGS.update(self.REQUIRED_SETINGS or {})
        for setting in self._REQUIRED_SETTINGS.items():
            if not setting in settings:
                raise KeyError('Missing setting in provided settings: {}'.format(setting))
            if not isinstance(settings[setting], self._REQUIRED_SETTINGS[setting]):
                raise KeyError('Setting {} is not the required type {}'.format(
                    setting, self._REQUIRED_SETTINGS[setting]
                ))
    # pylint: disable=consider-using-f-string
