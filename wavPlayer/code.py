import board
#import audioio
import audiocore
import audiobusio
import digitalio

f = open("cow.wav", "rb")
wav = audiocore.WaveFile(f)

a = audiobusio.I2SOut(bit_clock=board.GP10, word_select=board.GP11, data=board.GP9)

print("playing")
a.play(wav)
while a.playing:
  pass
print("stopped")