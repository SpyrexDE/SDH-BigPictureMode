import subprocess

class Plugin:
    BPM = False

    async def open_BPM(self):
        self.BPM = True
        subprocess.Popen("steam steam://open/bigpicture", shell=True)

    async def close_BPM(self):
        self.BPM = False
        subprocess.Popen("steam -shutdown", shell=True)
    
    async def get_BPM(self):
        return self.BPM
