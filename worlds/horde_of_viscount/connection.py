from typing import Optional

from worlds.Files import APPlayerContainer


class HoVConnectionFile(APPlayerContainer):
    game: Optional[str] = "Horde of Viscount"
    patch_file_ending = ".aphov"

    def get_manifest(self):
        manifest = super().get_manifest()
        manifest.update({
            # Intentionally show the password can be filled in by the user if they open the file.
            "password": "",
            # Intentionally show that the server can be set to an http call. Usually only with localhost.
            "secure": True,
        })
        return manifest
