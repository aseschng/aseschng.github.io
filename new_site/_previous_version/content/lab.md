---
title: Research
nav: Research
order: 2
---

The speech and language research group in SCSE (now CCDS of NTU) was founded in 2007 by Chng Eng Siong and [Prof Li Haizhou](http://www.colips.org/~eleliha/) (now in CUHK-Shenzhen, China). The group is situated within [HESL Lab - N4-B2b-05](https://maps.ntu.edu.sg/#/ntu/). We also founded the [AISG Speech Lab](https://aisingapore.org/aiproducts/speech-lab/), funded by NRF since 2018. Research in the group focuses on the areas described below; see also [People](people.html) and [Funding](funding.html).

<!-- Each research area: a ## heading, an optional image with {: .side } (floats right),
     a paragraph, then a "Recent work:" list of links. -->

## Speech Recognition and Large Language Models {: #asr-llm }

![Speech indexing with the MAGOR system](images/magor_picture.jpg){: .side }

We build robust large-vocabulary speech recognition for code-switched speech (English/Mandarin, Malay, Indonesian-English), and increasingly do so with large language models. Current work includes speech LLMs with the AISG SeaLion and StepFun teams, transfer learning from large pre-trained models to under-resourced languages, using LLMs to correct ASR output by generative error correction, and joint end-to-end ASR with speech enhancement, wav2vec2 and speaker extraction front ends. A key question is adaptation: how to improve a model for a target environment (speaker, noise, type of dialogue).

Recent work:
{: .pubs-label }

- [Speech SeaLion](https://sea-lion.ai/)
- [Step Audio 2 Technical Report](https://arxiv.org/abs/2507.16632)
- [HyPoradise: generative error correction for ASR with LLMs](https://arxiv.org/pdf/2309.15701.pdf)
- [Code-switch end-to-end ASR](https://dblp.org/pers/p/Pham:Van_Tung.html)

## Speech Enhancement, Speaker and Audio Classification {: #classification }

We study who spoke, when, and what kind of sound it is: speaker identification and diarization (including VAD, overlapping speech and speaker extraction), noisy audio event and scene classification, audio captioning, and deepfake detection and generation. On the signal side we work on speech enhancement: speaker extraction, denoising, dereverberation, feature enhancement and overlapping-speech separation.

Recent work:
{: .pubs-label }

- [Audio scene and event analysis (DCASE)](http://dcase.community/challenge2019/index)
- [Automatic audio captioning (DCASE 2020)](http://dcase.community/challenge2020/task-automatic-audio-captioning)
- [Speaker extraction: SpEx multi-scale time-domain network](https://www.researchgate.net/publication/340643534_SpEx_Multi-Scale_Time_Domain_Speaker_Extraction_Network)
- [Speaker diarization (Microsoft approach)](https://arxiv.org/abs/2010.11458)
- [Deepfake detection](https://paperswithcode.com/task/deepfake-detection)

## Towards Speech Understanding {: #understanding }

![ASR for air-traffic control speech with named-entity highlighting](images/ATC_Demo.jpg){: .side }

Beyond transcription, we look at the language-processing steps that make speech useful: topic detection, named-entity recognition and text normalisation. One example is our ASR for air-traffic-control speech with named entities highlighted in the transcript. Related background: [sequence-to-sequence models](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/46687.pdf), as widely studied in [machine translation](https://arxiv.org/abs/1609.08144).

Demo:
{: .pubs-label }

- [ATC speech recognition with NER (YouTube)](https://www.youtube.com/watch?v=CFsaeK6vP7k)

## Applied AI and Industry: Abax.AI {: #abax }

We formed the startup [Abax.AI](https://www.abax.ai/) from the AISG 100E project in 2022 ([how it was formed](https://cde.nus.edu.sg/ece/project-4/)). Abax.AI offers transcription of code-mixed Singapore English, Mandarin and Malay as an SDK with on-premise support. It is deployed at SCDF (project began 2018, live since 2023) and NKF (live since 2025, for case recording and analytics), and was trialled for medical triaging in 2024.

In the news:
{: .pubs-label }

- [SCDF turns to AI to help emergency call dispatchers (Straits Times, 2018)](https://www.straitstimes.com/singapore/scdf-turns-to-artificial-intelligence-to-help-emergency-call-dispatchers)
- [Demo to Minister Shanmugam (Straits Times, 2019)](https://www.straitstimes.com/singapore/automated-system-transcribing-995-calls-may-also-recognise-singlish-shanmugam)
- [AI masters Singlish for healthcare (Straits Times, 2024)](https://www.straitstimes.com/singapore/ai-masters-singlish-in-key-breakthrough-to-serve-healthcare-and-patients-needs)
- [NKF uses speech technology (LinkedIn, 2026)](https://www.linkedin.com/posts/nkfsg_thisisnkf-sginnovation-sgdialysis-activity-7392168883241033728-qHc3/)

## Demos {: #demos }

![Chatbot framework demo, 2020](images/russell_chatbotPic2020.jpg){: .side }

- Code-switch speech recognition in action: [recognizing English/Mandarin code-switch speech with our LVCSR system](https://www.youtube.com/watch?v=qfLTJkvYZYc) (Jun 2018) and [comparing our system against Google and Siri](https://www.youtube.com/watch?v=wuQQ3fLu5yE) (Sep 2018).
- Source separation: separating Hillary Clinton's and Trump's voices from a YouTube recording, from Chenglin's [demo slides](https://www.dropbox.com/s/jdzrwz1ojobad35/2018_Chenglin_DemoTrumpvsHillary.pptx?dl=0) (Oct 2018).
- Speech indexing with our MAGOR system (code-switch English/Mandarin and Malay).
- 2020 FYP demo: deploying speech recognition on a high-availability Kubernetes cluster ([YouTube](https://www.youtube.com/watch?v=le79VEOjeuQ)).
- 2020 FYP demo: chatbot framework using Dialogflow and Q&A modules ([YouTube](https://www.youtube.com/watch?v=upFpCp4LDgo), [live demo](https://chatbot.speechlab.sg/)).

## Code {: #code }

- PhD student Hou Nana (2018–2021): single-channel speech enhancement, [GitHub](https://github.com/nanahou/Awesome-Speech-Enhancement)
- PhD student Xu Chenglin (2015–2020): single-channel speech separation/extraction, [GitHub](https://github.com/xuchenglin28/)
- Intern Ge Meng (Tianjin, 2020–2021): speech separation tutorial, [GitHub](https://github.com/gemengtju/Tutorial_Separation)
- Intern Shangeth (BITS, Aug 2020 – Jun 2021): accent, age and height classification, [PDF](https://www.dropbox.com/s/z834va4hvfngzo8/Shangeth%E2%80%99s%20Work%20at%20Speech%20Lab%2C%20NTU%20Singapore.pdf?dl=0)
- MSAI student Samuel Samsudin (2020–2021): emotion detection, [GitHub](https://github.com/samsudinng/speech_emo_recognition.git), [Kaggle IEMOCAP](https://www.kaggle.com/samuelsamsudinng/iemocap-emotion-speech-database)
- EEE PhD student Liu Hexin (2021): spoken language identification, [GitHub](https://github.com/Lhx94As/Awesome-Spoken-Language-Identification)
- Intern Shashank Shirol (Jan–Jun 2020): GANs to create noisy speech, [GitHub](https://github.com/shashankshirol/GeneratingNoisySpeechData)
