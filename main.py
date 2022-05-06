import subprocess

class Plugin:
    BPM = False

    async def close_BPM(self):
        self.BPM = False
        subprocess.Popen("steam -shutdown", shell=True)
    
    async def get_BPM(self):
        return self.BPM
