""""""
from ..base_plugin import BasePlugin
from ..base_settings import BaseSettings


class MayaPlaybastSettings(BaseSettings):
    
    REQUIRED_SETINGS = {
        'audio_path': str,
        'scene_path': str,
    }


class MayaPlayblastPlugin(BasePlugin):

    NAME = 'MayaPlayblast'
    CAN_FARM = True

    def pre_farm_run(self):
        from maya import cmds
        cmds.file(self.settings.scene_path, open=True, force=True)


