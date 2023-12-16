from pathlib import Path
from romanalyzer_extractor.utils import execute
from romanalyzer_extractor.extractor.base import Extractor


class AndrOtaPayloadExtractor(Extractor):
    def __init__(self, target):
        super().__init__(target)
        self.tool = Path('romanalyzer_extractor/tools/extract_android_ota_payload/extract_android_ota_payload.py').absolute()

    def extract(self):
        self.log.debug("Android OTA Payload extract target: {}".format(self.target))
        self.log.debug("\tstart extract payload.bin.")

        # Extraction command parts.
        extract_script = self.tool,
        payload = self.target.absolute(),
        extracted_dir = self.extracted

        # Build extraction command.
        convert_cmd = f"python3 {extract_script} {payload} {extracted_dir}"

        # Extract OTA image.
        execute(convert_cmd)

        if self.extracted.exists():
            self.log.debug(f"\textracted ota payload.bin to: {self.extracted}")
            return self.extracted

        else:
            self.log.warning(f"\tfailed to extract {self.extracted} using unzip")
            return None
