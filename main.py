from PyQt6.QtWidgets import QApplication, QFileDialog, QMessageBox, QMainWindow
# from PyQt6 import uic
import sys, threading, tts, os, gui
import sounddevice as sd
import soundfile as sf

def sbar_log(t='Готово к работе'):
    ui.statusBar.setText(t)

def dmodel():
    pcent = 0
    for percent in tts.download_model():
        if not pcent == percent:
            sbar_log(f'Загрузка модели Silero ... ({percent}%)')
        pcent = percent
    sbar_log()
def onRunTTS():
    text = ui.textInput.toPlainText()
    global result
    sbar_log('Озвучка ...')
    result = tts.speak(text, device='gpu' if ui.useGPU.isChecked() else 'cpu')
    sbar_log()
    ui.saveButton.setEnabled(True)
    ui.playButton.setEnabled(True)

def onPlayResult():
    sbar_log('Проигрывание ...')
    sd.play(result)
    sd.wait()
    sbar_log()

def onSaveResult():
    dialog = QFileDialog(ui)
    dialog.setFileMode(QFileDialog.FileMode.AnyFile)
    dialog.setNameFilter('Аудио (*.wav)')
    if not dialog.exec():
        return
    global filenames
    filenames = dialog.selectedFiles()
    name = filenames[0]
    rdialog = QMessageBox()
    if not name.endswith('.wav'):
        rdialog.setText('Расширение файла должно быть .wav.')
        rdialog.setIcon(QMessageBox.Icon.Warning)
    else:
        sf.write(name, result, 48000)
        rdialog.setText('Результат успешно сохранён!')
        rdialog.setIcon(QMessageBox.Icon.Information)
    rdialog.exec()

def onTextEdit():
    ui.runButton.setEnabled(bool(ui.textInput.toPlainText()))
    ui.playButton.setEnabled(False)
    ui.playButton.setEnabled(False)

app = QApplication([])
MainWindow = QMainWindow()
# ui = uic.loadUi('gui.ui')
ui = gui.Ui_MainWindow()
ui.setupUi(MainWindow)
if not os.path.exists('silero.pt'):
    sbar_log('Загрузка модели Silero ... (0%)')
    threading.Thread(target=dmodel).start()
MainWindow.setWindowTitle('VoiceOver by Sovenok-Hacker')
ui.textInput.textChanged.connect(onTextEdit)
ui.useGPU.setEnabled(tts.gpu_available)
ui.runButton.clicked.connect(lambda: threading.Thread(target=onRunTTS).start())
ui.playButton.clicked.connect(lambda: threading.Thread(target=onPlayResult).start())
ui.saveButton.clicked.connect(onSaveResult)
MainWindow.show()
sys.exit(app.exec())
