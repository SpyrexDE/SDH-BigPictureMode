import subprocess

class Plugin:
    name = "BigPictureMode"

    author = "Spyrex"

    hot_reload = True

    main_view_html = "main_view.html"

    tile_view_html = "tile_view.html"

    BPM = False

    async def open_BPM(self):
        self.BPM = True
        subprocess.Popen("steam steam://open/bigpicture", shell=True)

    async def close_BPM(self):
        self.BPM = False
        subprocess.Popen("steam -shutdown", shell=True)
    
    async def get_BPM(self):
        return self.BPM
