import subprocess

class Plugin:
    name = "BigPictureMode"

    author = "Spyrex"

    title_view_html = """
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

    main_view_html = ""

    hot_reload = True

    async def __main(self):
        pass

    async def open_BPM(self, **kwargs):
        subprocess.Popen("steam steam://open/bigpicture"), stdout=subprocess.PIPE, shell=True)