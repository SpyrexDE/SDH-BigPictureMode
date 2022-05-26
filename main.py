import subprocess

class Plugin:
    BPM = False

    async def close_BPM(self):
        self.BPM = False
        subprocess.Popen("pkill -sigint -x steam", shell=True)
    
    async def set_BPM(self):
        self.BPM = True

    async def get_BPM(self):
        return self.BPM
