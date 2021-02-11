import json
from jsonschema import validate, ValidationError
from pathlib import Path
import re
from console import close, color


class settingsID:
    audio_only = 'audioOnly'
    video_quality = 'defaultVideoQuality'
    download_directory = 'downloadDirectory'
    new_folder_playlist = 'newFolderForPlaylist'
    open_file = 'openFileAfterDownload'

    def error():
        color.red("problem with settings.json")
        close()


class Settings:
    def __init__(self) -> None:
        data_settings = json.load(open(Path.joinpath(
            Path(__file__).parent.absolute(), "settings/settings.json"), "r"))
        schema_settings = json.load(open(Path.joinpath(
            Path(__file__).parent.absolute(), "settings/settings.schema.json"), "r"))
        try:
            validate(instance=data_settings, schema=schema_settings)
        except ValidationError:
            color.red("problem with settings.json")
            close()
        self.settings = data_settings
        self.settings_properties = schema_settings['properties']

    def get_settings(self, id: str):
        in_settings_json = self.settings[id]
        examples = self.settings_properties[id]['examples']
        if(in_settings_json in examples):
            return in_settings_json
        regex = self.settings_properties[id]['pattern']
        if len(re.findall(regex, in_settings_json)) > 0:
            return in_settings_json
        raise settingsID.error
