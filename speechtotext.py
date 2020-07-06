import speech_recognition as sr
import os


files_list = {}
anger_transcripts = ""
disgust_transcripts = ""
fear_transcripts = ""
surprise_transcripts = ""
happy_transcripts = ""
sad_transcripts = ""
# initialize the recognizer
r=sr.Recognizer()

path = r"/home/raj/Desktop/SpeechEmotionRecognition/Sound files/"

folder_list = os.listdir(path)

i=0
for folder in folder_list:
	files_list[folder] = os.listdir(path + folder + "/")
	i+=1

for folder_name, folder_items in files_list.items():
	for file_name in folder_items:
		print(file_name)
		try:
			with  sr.AudioFile(path + folder_name + '/' + file_name) as source:
				audio_data = r.record(source)
				try:
					text = r.recognize_google(audio_data) + "\n"
					if "happy" in file_name.lower():
						happy_transcripts += text
					elif "sad" in file_name.lower():
						sad_transcripts += text
					elif "surprise" in file_name.lower():
						surprise_transcripts += text
					elif "angry" in file_name.lower() or "anger" in file_name.lower():
						anger_transcripts += text
					elif "fear" in file_name.lower():
						fear_transcripts += text
					elif "disgust" in file_name.lower():
						disgust_transcripts += text	
				except Exception:
					text = ""
					print("Error in transcribing: " + folder_name + '/' +file_name)
		except Exception:
			print("Error in opening: " + folder_name + '/' +file_name)
			continue


with open("newtrainingtext.txt", "w") as transcript_file:
	transcript_file.write("Sad text:\n"+sad_transcripts+"\n\n")
	transcript_file.write("Happy text:\n"+happy_transcripts+"\n\n")
	transcript_file.write("Surprised text:\n"+surprise_transcripts+"\n\n")
	transcript_file.write("Fear text:\n"+fear_transcripts+"\n\n")
	transcript_file.write("Disgust text:\n"+disgust_transcripts+"\n\n")
	transcript_file.write("Anger text:\n"+anger_transcripts+"\n\n")
