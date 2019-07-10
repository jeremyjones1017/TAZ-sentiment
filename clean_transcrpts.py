from textblob import TextBlob
import io
import numpy as np
from matplotlib import pyplot as plt
import csv
import pandas as pd
import glob

def main():
	'''
	filenames = ['C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_1_HtbG_1.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_1-5_HtbG_1-5.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_2_HtbG_2.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_3_HtbG_3.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_4_HtbG_4.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_5_HtbG_5.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_6_HtbG_6.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_7_Moon_1.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_8_Moon_2.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_9_Moon_3.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_10_MotRL_1.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_11_MotRL_2.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_12_MotRL_3.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_13_MotRL_4.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_14_MotRL_5.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_15_MotRL_6.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_16_MotRL_7.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_17_LI_1.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_18_PttM_1.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_19_PttM_2.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_20_PttM_3.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_21_PttM_4.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_22_PttM_5.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_23_PttM_6.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_24_PttM_7.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_25_PttM_8.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_26_PttM_9.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_27_PttM_10.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_28_LI_2.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_29_CK_1.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_30_CK_2.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_31_CK_3.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_32_CK_4.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_33_CK_5.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_34_CK_6.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_35_CK_7.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_36_CK_8.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_37_CK_9.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_39_CK_11.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_40_LI_3.txt'
		]
	'''
	filenames = [
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_29_CK_1.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_30_CK_2.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_31_CK_3.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_32_CK_4.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_33_CK_5.txt',
		'C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/Balance_34_CK_6.txt',
		]
	#'''
	#for filename in glob.iglob('C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/raw_transcripts/*txt'):
	
	epi_pol = []
	epi_sub = []
	
	for i,filename in enumerate(filenames):
		print('================================================================')
		print(filename)
		just_filename = filename.split('/')[-1]
		campaign_name = just_filename.split('_')[0]
		campaign_epnum = just_filename.split('_')[1]
		arc_name = just_filename.split('_')[2]
		arc_epnum = just_filename.split('_')[3]
		arc_epnum = arc_epnum.split('.')[0]
		if i == 0:
			df = read_transcript(filename)
			df['CAMPAIGN'] = campaign_name
			df['CAMPAIGN_EPISODE'] = campaign_epnum
			df['ARC'] = arc_name
			df['ARC_EPISODE'] = arc_epnum
		else:
			this_df = read_transcript(filename)
			this_df['CAMPAIGN'] = campaign_name
			this_df['CAMPAIGN_EPISODE'] = campaign_epnum
			this_df['ARC'] = arc_name
			this_df['ARC_EPISODE'] = arc_epnum
			df = df.append(this_df, ignore_index = True)
			
			
		#epi_pol.append(np.mean(this_df.POLARITY))
		#epi_sub.append(np.mean(this_df.SUBJECTIVITY))
	
	pol_rm = running_mean(df.POLARITY,500)
	plt.plot(df.POLARITY,'bo')
	plt.plot(pol_rm,'r-')
	plt.show()
	#plt.plot(epi_pol,'bo')
	#plt.show()
	#plt.plot(epi_sub,'ro')
	#plt.show()
	
def read_transcript(transcript_file):
	known_speakers = []
	line_speaker = []
	clean_lines = []
	
	sentence_speaker = []
	sentence_content = []
	sentence_polarity = []
	sentence_subjectivity = []
	
	with io.open(transcript_file,'r') as my_file:
		lines = my_file.readlines()
	
	with open('C:/Users/Jeremy/Dropbox/Programing/TAZ-analysis/speaker_list.csv','r') as input_file:
		input_file_reader = csv.reader(input_file)
		for speaker in input_file_reader:
			known_speakers.append(speaker[0]+': ')
	
	print('This helps find unknown speakers')
	for line in lines:
		find_unknown_speakers(line,known_speakers)
	
	for line in lines:
		this_speaker,this_clean_line = do_clean(line,known_speakers)
		if this_clean_line != '-':
			line_speaker.append(this_speaker)
			clean_lines.append(this_clean_line)
			
	
	for i,line in enumerate(clean_lines):
		sentences = line.sentences
		for sentence in sentences:
			sentence_speaker.append(line_speaker[i])
			sentence_content.append(sentence)
			sentence_polarity.append(sentence.sentiment.polarity)
			sentence_subjectivity.append(sentence.sentiment.subjectivity)
	
	sentence_number = list(range(len(sentence_speaker)))
	data = {'SPEAKER':sentence_speaker,'SENTENCE':sentence_content,'POLARITY':sentence_polarity,'SUBJECTIVITY':sentence_subjectivity,'NUMBER':sentence_number}
	df = pd.DataFrame(data)
	
	'''
	#print(df.SPEAKER.unique())
	
	taako_df = df[df.SPEAKER == 'Taako: ']
	merle_df = df[df.SPEAKER == 'Merle: ']
	magnus_df = df[df.SPEAKER == 'Magnus: ']
	
	pol_arr = np.array(sentence_polarity)
	pol_rm = running_mean(pol_arr,100)
	
	sub_arr = np.array(sentence_subjectivity)
	sub_rm = running_mean(sub_arr,100)
	
	mean_pol = np.mean(sentence_polarity)
	#print('Mean polarity',mean_pol)
	#print('Taako, Merle, and Magnus Polarity: ',np.mean(taako_df.POLARITY)/mean_pol,np.mean(merle_df.POLARITY)/mean_pol,np.mean(magnus_df.POLARITY)/mean_pol)
	#print('Mean subjectivity',np.mean(sentence_subjectivity))
	
	#plt.plot(df.NUMBER,df.POLARITY,'ko')
	#plt.plot(taako_df.NUMBER,taako_df.POLARITY,'ro')
	#plt.plot(merle_df.NUMBER,merle_df.POLARITY,'go')
	#plt.plot(magnus_df.NUMBER,magnus_df.POLARITY,'bo')
	#plt.show()
	'''
	return df
	
def running_mean(x,N):
	return np.convolve(x, np.ones((N,))/N)[(N-1):]

def find_unknown_speakers(line,known_speakers):
	import re
	'''
	Tests to see if a known speaker is in a line. Prints out if not. 
	So we can see if there's a new unknown speaker
	'''
	speaker_is_known = False
	text = TextBlob(line)
	text = text.replace('\n','')
	nws_text = text.replace(' ','')
	for test_speaker in known_speakers:
		if text.startswith(test_speaker):
			speaker_is_known = True
	if speaker_is_known == False and nws_text != '':
		text = str(text)
		print_text = re.sub("\[.*?\]","[]",text)
		print_text = re.sub("\{.*?\}","{}",print_text)
		if print_text != '[]' and print_text != '{}':
			print(print_text)#,'|||',text
	

def do_clean(line,known_speakers): 
	speaker_is_known = False
	text = TextBlob(line)
	text = text.replace('\n','')
	#nws_text = text.replace(' ','')
	for test_speaker in known_speakers:
		if text.startswith(test_speaker):
			speaker_is_known = True
			speaker = test_speaker
			clean_line = remove_prefix(text,speaker)
			return speaker,clean_line
	#if speaker_is_known == False and nws_text != '':
	#	print(text)
	return '-','-'

def remove_prefix(text, prefix):
	if text.startswith(prefix):
		return text[len(prefix):]
	else:
		return text
if __name__=="__main__":
	main()