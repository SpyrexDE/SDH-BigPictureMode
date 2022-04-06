import subprocess

class Plugin:
    name = "BigPictureMode"

    author = "Spyrex"

    hot_reload = True

    main_view_html = """
    <!--html-->
        <html>
                <head>
                    <link rel="stylesheet" href="/steam_resource/css/2.css">
                    <link rel="stylesheet" href="/steam_resource/css/39.css">
                    <link rel="stylesheet" href="/steam_resource/css/library.css">
                    <script src="/static/library.js"></script>
                </head>
                <body>
                    <center><p id="label" style="top: 50%; margin-top: 50%;">Loading</p></center>
                    <script>
                        (async function() {
                            if(await call_plugin_method("get_BPM")) {
                                document.getElementById("label").innerHTML = "Leaving Big Picture Mode...";
                                call_plugin_method("close_BPM")
                            } else {
                                document.getElementById("label").innerHTML = "Starting Big Picture Mode...";
                                call_plugin_method("open_BPM")
                            }
                        })();

                        window.setTimeout(load_plugins, 5000);
                        
                        function load_plugins() {
                            location.href = "http://127.0.0.1:1337/plugins/iframe";
                        }
                    </script>
                </body>
        </html>
    <!--!html-->
    """

    tile_view_html = """
    <!--html-->
            <div class="quickaccesscontrols_PanelSectionRow_26R5w">
                <div class="basicdialog_Field_ugL9c basicdialog_WithChildrenBelow_1RjOd basicdialog_InlineWrapShiftsChildrenBelow_3a6QZ basicdialog_ExtraPaddingOnChildrenBelow_2-owv basicdialog_StandardPadding_1HrfN basicdialog_HighlightOnFocus_1xh2W Panel Focusable" style="--indent-level:0;">
                    <div class="basicdialog_FieldChildren_279n8">
                        <button id ="tile_btn" type="button" tabindex="0" class="DialogButton _DialogLayout Secondary basicdialog_Button_1Ievp Focusable">🖼️ Big Picture Mode</button>
                    </div>    
                </div>
            </div>
            <script>
                (async function() {
                    if(await call_plugin_method("get_BPM")) {
                        document.getElementById("tile_btn").innerHTML = "🖼️ Leave Big Picture Mode";
                    } else {
                        document.getElementById("tile_btn").innerHTML = "🖼️ Big Picture Mode";
                    }
                })();
            </script>
    <!--!html-->
    """

    BPM = False

    async def open_BPM(self):
        self.BPM = True
        subprocess.Popen("steam steam://open/bigpicture", shell=True)

    async def close_BPM(self):
        self.BPM = False
        subprocess.Popen("reboot", shell=True)#"steam -shutdown", shell=True) steam -shutdown is faster but does not re-inject the plugin loader UI
    
    async def get_BPM(self):
        return self.BPM
