# ASER-Dataset

## Citing
If you are using any of the resources, please cite the following article:
D. Agarwal, J. Gupchup and N. Baghel, "A Dataset for Measuring Reading Levels In India At Scale," ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Barcelona, Spain, 2020, pp. 9210-9214, doi: 10.1109/ICASSP40776.2020.9053380.
(https://ieeexplore.ieee.org/abstract/document/9053380)
												

## About Pratham
Pratham was founded in 1995, to provide pre-school education to children in Mumbai slums. Over the last 20 years Pratham has grown to be India’s largest NGO working to provide quality education to underprivileged youth and 
children in over 21 states and union territories across the country, with a range of interventions. Pratham is a widely recognized organization, having received notable awards such as the WISE Prize for Innovation, 
Skoll Award for Social Entrepreneurship, the Henry R Kravis Prize in Leadership and the CNN-IBN Indian of the Year for Public Service. More info at: http://pratham.org/


## About ASER
The Annual Status of Education Report (ASER), a nationwide survey of reading and math achievement of children from rural India, has been conducted annually since 2005. 
The ASER test inference is about a child’s level of foundational reading skills (letter identification, word decoding, proficiency in reading paragraph and story) and basic math ability 
(number recognition, subtraction, and division). The tests are orally and individually administered and require about 10 minutes of administration time. 
The tests are designed to understand what students can do and the skills they have mastered. More info at: https://www.asercentre.org/

## About ASER Dataset
In order to facilitate deep learning research in automating reading assessments in India we present ASER dataset of children in the age group 6-14 years. 
The dataset was generated using a custom mobile app and includes labeled audio clips of children reading out different levels of text in Hindi, Marathi and English. The labels represent expert opinions on whether the child is qualified at the specified reading level. This dataset facilitates research in speech and language processing, STT for Indian languages, prosody, combination of rhythm, stress, phonemes intonation, pace and reading styles of children.
The goal of this work is to make this dataset public to spur innovation and generate novel solutions for automation of assessing reading levels. 

The dataset consists of 5301 samples. Each sample consist of audio files and it's corresponding json file.
Below we explain the Question Sample set used and the JSON file structure generated while collecting audio samples of ASER test (conducted manually) through Android app.	  

### Question Sample Set Description
For each language (Hindi and Marathi), there are 4 question sample sets. Each question sample set consists of 2 sections - the Reading and English tools. Each sample has a question_id in the format <b> language_SampleNo_level_count </b> explained in detail below:<br>
Language = "HI" or "MR" (for Hindi, Marathi respectively)<br>
SampleNo can be S1, S2, S3, S4<br>
Count is the serial number count of the sample<br>
The symbols used for level are described below. 

<table>
  <tr>
  <th>Section</th>
  <th>Symbol</th>
  <th>Meaning</th>
  </tr>
  <tr>
    <td rowspan=4>Native Reading Levels	</td>
    <td>ST</td>
    <td>Story</td>
   </tr>
    <tr>
    <td>P</td>
    <td>Paragraph</td>
   </tr>
   <tr>
    <td>WD</td>
    <td>Word</td>
   </tr>
    <tr>
    <td>L</td>
    <td>Letter</td>
   </tr>
   <tr>
    <td rowspan=4>English Levels	</td>
    <td>CL</td>
    <td>Capital Letter</td>
   </tr>
    <tr>
    <td>SL</td>
    <td>Small Letter</td>
   </tr>
   <tr>
    <td>W</td>
    <td>Word</td>
   </tr>
    <tr>
    <td>S</td>
    <td>Sentence</td>
   </tr>
</table>

### JSON File Description
The JSON file is generated simultaneously while conducting the test. In the JSON Object, we keep proficiency of student as marked by the interviewer taking the test according to how the child performs in the test.

Proficiency can be marked for 
* Native language
* English language.

A child can be classified in any of the 5 Reading levels, and 5 English Level. English Language test is optional.
5 Reading levels are:
- Beginner
- Letter level
- Word level
- Paragraph level
- Story level  

5 English Levels are:
- Capital Letter
- Small Letter
- Word
- Sentence
			
In the JSONObject, there is a field called "sequenceList" which is a JSONArray containing all the questions that are attempted by students sequentially. The fields in the sequenceList is explained in the table below.

<table>
	<tr>
		<th>Field</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>isCorrect</td>
		<td>Represents whether the text/question was read out correctly (True) or not (False)</td>
	</tr>
	<tr>
		<td>noOfMistakes</td>
		<td>Represents the number of mistakes done while reading out sentence, paragraph or story</td>
	</tr>
	<tr>
		<td>recordingName</td>
		<td>Name of the recorded audioclip</td>
	</tr>
</table>

*Note:  "noOfMistakes" field of sequenceList is asked to CRL to enter only for Story, paragraph and sentence. Otherwise it is set to total number of mistakes done in that particular section (Word/Letter).

Example :	
				
    {
    "ageGroup": "7-10 years",             // selected Agegroup of student
    "date": "Mon May 27 10:37:35 GMT+05:30 2019",  // system date
    "deviceID": "92ca9361fbd010ba",		// Id of device on which test is conducted
    "englishProficiency": "word",		// Proficiency of english language marked
    "nativeProficiency": "Paragraph",		// Proficiency of native language(Hindi/Marathi) marked
    "sequenceList": [         // sequencelist of attempted questions 
    {
      "isCorrect": true,	// true or false to represent whether it was correct or incorrect
      "noOfMistakes": "5",	// mistakes count
      "que_id": "MR_S2_P_0",	// Id of question -format(language_SampleNo_level_count)
      "que_text": "एकदा मी पडले. सगळे मला हसले. एकदा सोनल पडली. मी तिला हसले." ,     //question text
	  "recordingName":"MR_S2_P_0.mp3"		// recording file Name(set as que_id)
	  },
	  {
		"isCorrect": true,
		"noOfMistakes": "3",	 // Total number of mistakes done in the small letter section
		"que_id": "MR_S2_SL_0",
		"que_text": "z",
		"recordingName": "MR_S2_SL_0.mp3"
	},
	{
		"isCorrect": false,
		"noOfMistakes": "3",
		"que_id": "MR_S2_SL_4",
		"que_text": "g",
		"recordingName": "MR_S2_SL_4.mp3"
	},
	{
		"isCorrect": false,
		"noOfMistakes": "3",
		"que_id": "MR_S2_SL_7",
		"que_text": "k",
		"recordingName": "MR_S2_SL_7.mp3"
	},
	{
		"isCorrect": true,
		"noOfMistakes": "3",
		"que_id": "MR_S2_SL_2",
		"que_text": "o",
		"recordingName": "MR_S2_SL_2.mp3"
	},
	{
		"isCorrect": false,
		"noOfMistakes": "3",
		"que_id": "MR_S2_SL_1",
		"que_text": "j",
		"recordingName": "MR_S2_SL_1.mp3"
	}
       ],
    "studClass": "5",          // class of student
    }

