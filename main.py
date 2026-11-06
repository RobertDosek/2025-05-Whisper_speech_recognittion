import whisper

model = whisper.load_model("turbo")
result = model.transcribe("test.mp4", fp16=False, language='Czech')
print(result["text"])