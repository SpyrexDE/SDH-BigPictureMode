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
                </head>
                <body>
                    <center><p style="top: 50%; margin-top: 50%;">Starting Big Picture Mode...</p></center>
                </body>
        </html>
    <!--!html-->
    """

    tile_view_html = """
    <!--html-->
            <div class="quickaccesscontrols_PanelSectionRow_26R5w">
                <div onclick="open_BPM()" class="basicdialog_Field_ugL9c basicdialog_WithChildrenBelow_1RjOd basicdialog_InlineWrapShiftsChildrenBelow_3a6QZ basicdialog_ExtraPaddingOnChildrenBelow_2-owv basicdialog_StandardPadding_1HrfN basicdialog_HighlightOnFocus_1xh2W Panel Focusable" style="--indent-level:0;">
                    <div class="basicdialog_FieldChildren_279n8">
                        <button type="button" tabindex="0" class="DialogButton _DialogLayout Secondary basicdialog_Button_1Ievp Focusable">🖼️ Big Picture Mode</button>
                    </div>    
                </div>
            </div>
            <script>
                function open_BPM() {
                    call_plugin_method("open_BPM", {})
                }
            </script>
    <!--!html-->
    """

    def open_BPM(self, **kwargs):
        subprocess.Popen("steam steam://open/bigpicture")
