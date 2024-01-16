from pynput.mouse import Button, Controller
from vosk import Model, KaldiRecognizer
import pyaudio


class Mouse:
	SHIELD_LOCATION = (1871, 208)
	MAGNET_LOCATION = (1868, 368)
	DIAMONDS_2X_LOCATION = (1870, 528)

	mouse = Controller()

	def activate_shield(self):
		self.mouse.position = self.SHIELD_LOCATION
		self.mouse.click(Button.left, 1)

	def activate_magnet(self):
		self.mouse.position = self.MAGNET_LOCATION
		self.mouse.click(Button.left, 1)

	def activate_2x_diamonds(self):
		self.mouse.position = self.DIAMONDS_2X_LOCATION
		self.mouse.click(Button.left, 1)


mouse = Mouse()


def speech_processing(mouse):
	model = Model(r'models/vosk-model-small-ru-0.22')
	rec = KaldiRecognizer(model, 44100)
	p = pyaudio.PyAudio()
	stream = p.open(
		format=pyaudio.paInt16,
		channels=1,
		rate=44100,
		input=True,
		frames_per_buffer=44100,
	)
	stream.start_stream()

	while True:
		data = stream.read(500)

		if rec.AcceptWaveform(data):
			text = eval(rec.Result())['text']
			if 'щит' in text:
				mouse.activate_shield()
			if 'магнит' in text:
				mouse.activate_magnet()
			if 'икс' in text:
				mouse.activate_2x_diamonds()
		else:
			print(rec.PartialResult())


speech_processing(mouse)