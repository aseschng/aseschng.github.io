---
title: Speech and Language Laboratory
id: SpeechLab
---

last updated: 13 Feb 2026

## Speech and Language laboratory {: #speechLab_intro }

The speech and language research group in SCSE (now CCDS of NTU) was founded in 2007 by Chng Eng Siong and [Prof Li Haizhou](http://www.colips.org/~eleliha/) (now in CUHK-Shenzen, China). The group is now situated within [HESL Lab - N4-B2b-05](https://maps.ntu.edu.sg/#/ntu/) in SCSE. We also founded the [AISG Speech Lab](https://aisingapore.org/aiproducts/speech-lab/) funded by NRF since 2018~current.

### AISG Speech Lab Startup: Abax.AI {: #subsection-1 }

We formed the startup [Abax.AI](https://www.abax.ai/) from 100E project of AISG in 2022. Details of how this startup was formed can be found [here](https://cde.nus.edu.sg/ece/project-4/). Abax.AI offers speech transcription of code-mixing Singapore English+Manadrin+Malay solution as SDK and on-premise support. This solution is now deployed in the following agencies/companies

<!-- list: a -->

1. SCDF - project began 2018~ deployed live 2023-> current). Some news: [StraitsTimes-2018](https://www.straitstimes.com/singapore/scdf-turns-to-artificial-intelligence-to-help-emergency-call-dispatchers) and [Demo to Minister Shanmugam-2019](https://www.straitstimes.com/singapore/automated-system-transcribing-995-calls-may-also-recognise-singlish-shanmugam)
1. NKF - project began 2025 ~ live to current). NKF uses speech technology for case recording and analytics. [news in Linkedin-2026](https://www.linkedin.com/posts/nkfsg_thisisnkf-sginnovation-sgdialysis-activity-7392168883241033728-qHc3/), we are Abax.AI (the company providing the speech recognition technology)
1. Medical triaging (2024) POC. [StraitsTimes](https://www.straitstimes.com/singapore/ai-masters-singlish-in-key-breakthrough-to-serve-healthcare-and-patients-needs)

### Research Focus {: #subsection-2 }

Our research interest is primarily speech and language processing, classifications using ML:

1. `ASR and LLM`
    1. Speech LLM research with AISG SeaLion team [Speech SeaLion](https://sea-lion.ai/)and StepFun team [Step Audio 2](https://arxiv.org/abs/2507.16632)
    1. Tranfer Learning: from large trained LLM model for under-resourced languages (Indonesian-English, Malay-English)
    1. Using LLM to improve ASR by generative error correction: see [Hyporadise](https://arxiv.org/pdf/2309.15701.pdf)
    1. Robust Large vocabulary continuous speech recognition: joint end-to-end ASR with speech enhancement module, wave2vec2, speaker extraction
    1. Speech enhancement: speaker extraction, denoising, feature enhancement, overlapping speech extraction
1. `Classification`
    1. Noisy Audio event and scene classifications, Audio captioning [DCase](http://dcase.community/challenge2020/task-automatic-audio-captioning)
    1. Speaker identification and speaker diarization: diarization, VAD, and speaker extraction issues, see [Microsoft diarization approach](https://arxiv.org/abs/2010.11458)
    1. Deep Fake Detection (and generation)[Link](https://paperswithcode.com/task/deepfake-detection)
1. `Towards Speech Understanding` - some aspects of NLP such as topic detection, name entity recognition, text normalization. See a demo of our ASR for ATC speech with NER highlighting. [ATC with NER](https://www.youtube.com/watch?v=CFsaeK6vP7k)

Examples of relevant papers to the research area include: [sequence to sequence model](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/46687.pdf) which has been widely studied in [machine translation](https://arxiv.org/abs/1609.08144). The problems we are keen on include

- Code switch end to end and Adaptation -> how to improve the model in certain target environment (speaker, noise, type of dialogues), etc. [Code-switch End-to-end](https://dblp.org/pers/p/Pham:Van_Tung.html)
- Classification-> what type of sound is this? [Audio Scene and Event Analysis](http://dcase.community/challenge2019/index)
- Speaker id: who spoke it: [speaker id](http://danielpovey.com/files/2019_interspeech_xvector_refinement.pdf) under [overlapping condition](https://arxiv.org/pdf/1902.02546.pdf) and [when (Diarization).](https://ai.googleblog.com/2018/11/accurate-online-speaker-diarization.html)
- Speech Enhancement - [speaker extraction](https://www.researchgate.net/publication/340643534_SpEx_Multi-Scale_Time_Domain_Speaker_Extraction_Network) and [derevberation](https://link.springer.com/article/10.1186/s13634-015-0300-4).

### Demos {: #subsection-3 }

Some of our previous works:

1. Youtube recordings: Our code-switch speech recognition in action:
    1. [Recognizing English/Mandarin code-switch speech using our LVCSR system](https://www.youtube.com/watch?v=qfLTJkvYZYc) (2018 June).
    1. [Comparing our system against Google, Siri](https://www.youtube.com/watch?v=wuQQ3fLu5yE) (2018 Sep).
1. Source separation - Separating Hillary Clinton and Trump voice from Youtube recording, from Chenglin's [Demo slide](https://www.dropbox.com/s/jdzrwz1ojobad35/2018_Chenglin_DemoTrumpvsHillary.pptx?dl=0) (Oct 2018)
1. Speech indexing using our MAGOR system (Code-switch English/Mandarin and Malay system) ![](images/magor_picture.jpg)
1. See a demo of our ASR for ATC speech with NER highlighting. [ATC with NER](https://www.youtube.com/watch?v=CFsaeK6vP7k) ![](images/ATC_Demo.jpg)

### Our recent demos using our speech engine {: #subsection-4 }

2020 FYPs demo:

1. Deploying Speech Recognition System using high availability and scalability kubernetes cluster [Youtube](https://www.youtube.com/watch?v=le79VEOjeuQ)
1. Chatbot framework using Dialog flow and various Q and A modules (2020 Demo) [Youtube](https://www.youtube.com/watch?v=upFpCp4LDgo) and a live demo[Demo](https://chatbot.speechlab.sg/) ![](images/russell_chatbotPic2020.jpg)

### Some of our recent works in git {: #subsection-5 }

1. PhD Student Hou Nana's work in NTU (2018~2021), single channel speech enhancement, [github](https://github.com/nanahou/Awesome-Speech-Enhancement)
1. PhD Student Xu Chenglin's work in NTU (2015~2020), single channel speech separation/extration,[github](https://github.com/xuchenglin28/)
1. Intern GeMeng's work (intern from Tianjin 2020~2021), tutorial speech separation, [github](https://github.com/gemengtju/Tutorial_Separation)
1. Intern Shangeths work (intern from BITS) (2020 Aug- 2021 June), Accent, Age, Height classification[Pdf link](https://www.dropbox.com/s/z834va4hvfngzo8/Shangeth%E2%80%99s%20Work%20at%20Speech%20Lab%2C%20NTU%20Singapore.pdf?dl=0)
1. MSAI student Samuel Samsudin (2020~2021), emotion detection, [github depository](https://github.com/samsudinng/speech_emo_recognition.git), [kaggle iEmoCap](https://www.kaggle.com/samuelsamsudinng/iemocap-emotion-speech-database)
1. Language Identification by EEE's PhD student Liu Hexin (2021) [github link](https://github.com/Lhx94As/Awesome-Spoken-Language-Identification)
1. Intern Shashank Shirol's work (2020 Jan-June), using GAN to create noisy speech, [github depository](https://github.com/shashankshirol/GeneratingNoisySpeechData)

## Collaborators {: #my_collaborator }

1. [Prof Chen Xie](https://www.cs.sjtu.edu.cn/en/jiaoshiml/chenxie.html), Shanghai JiaoTong University (since 2024~) - supervision of PhD student Ma Ziyang, and research.
1. [Prof Li Haizhou](https://sds.cuhk.edu.cn/en/teacher/498), CUHK and AISG Speech Lab (since 2008~) - AISG Speech Lab
1. [Prof Zhong Xionghu](https://scholar.google.com.sg/citations?user=V-ISRXwAAAAJ), Hunan University, China. Microphone Array DOA and diarization. (2019~)
1. [Dr Ma Bin](https://www.linkedin.com/in/bin-ma-b278a44b/), Alibaba. Robust End-to-End Code switch ASR (2018~)
1. [Prof Huang Hao](https://scholar.google.com/citations?user=gCxEFxIAAAAJ), Xinjiang University. PhD students exchange - Code switch ASR and classification (2018~) - multiple student exchanges
1. [Prof Xie Lei](http://www.nwpu-aslp.org/lxie/), Northwestern Polytechnic, Xian, China. PhD students exchange - ASR (2015~) - multiple CSC student exchanges

### Past Collaborators {: #Past_collaborator }

1. [Prof Wang Longbiao](http://cic.tju.edu.cn/faculty/wanglongbiao/experiences.html), Tianjin University, China. PhD students exchange - Emotion recognition (2016~2025) - exchange of CSC students
1. [A/Prof Sun Linhui](https://www.researchgate.net/profile/Linhui-Sun-3), (Speech Enhancement (2022~2025)) - as visiting Prof in CCDS
1. [A/Prof Li Ming](https://faculty.dukekunshan.edu.cn/faculty_profiles/ming-li), Duke-Kunshan (Deep Fake, (2023~2025)) - MEng Student to CCDS
1. [A/Prof Wu Zhizheng](https://drwuz.com/), CUHK (TTS, (2023~2025)) - on TTS
1. [A/Prof Lee KongAik](https://www.linkedin.com/in/kong-aik-lee-3b49a868), HK Poly Uni (Speaker Anonymisation, SV, DeepFake (2023~Nov2026)) - supervision of Tuan, Nikita
1. [Prof XI Wei](https://gr.xjtu.edu.cn/web/xiwei), Xian JiaoTong University, China. CSC PhD students exchange - self-supervised learning
1. [Dr Raphael Banchs](https://www.linkedin.com/in/rafaelbanchs/), ChatBot.
1. [Prof Lee Chin Hui](https://chl.ece.gatech.edu/), Robust ASR (~2008-2015)
1. [Prof Tanja Schultz (~2008-2013)](https://www.uni-bremen.de/en/csl/team/staff/prof-dr-ing-tanja-schultz/), Code-switch ASR


## Staff {: #my_Staff }

1. [Dr Rao Wei](https://www.linkedin.com/in/wei-rao-49382080/),senior research fellow (LLM) (joned April 2025~)
1. [Dr Liu Hexin](https://www.linkedin.com/in/hexin-liu-2a7a91212/?originalSubdomain=sg),research fellow (LLM) (joned Oct 2023~)
1. [Ly Vu Thi](https://www.linkedin.com/in/lyvt1/),Full-stack and chatBot
1. [Tanmay Surana](https://www.linkedin.com/in/tanmay-surana-118a79192/), `NLP and Depression classification` (Jan 2024~)
1. [Lim Zhi Hao](https://sg.linkedin.com/in/lim-zhi-hao-025546115) Speaker verification and DNN
1. [Kyaw Zin Tun (AISG-NTU)](https://www.linkedin.com/in/kyaw-zin-tun-170b52122), full-stack development
1. [Peng Yizhou (AISG-NUS)](https://www.linkedin.com/in/yizhou-peng-18425b202/?originalSubdomain=cn), speech research, in NUS AISG lab (Jan 2023~)
1. [Nur Shahidah Binte Jamaludin](https://www.linkedin.com/in/nurshahidahj/), corpus development and linguistic support, (Sep 2021~)
1. [Liu Changsong](https://www.linkedin.com/in/changsong-liu/),Project Officer (joned Aug 2024~)

### Past Staff {: #Past_Staff }

1. [Azmat Adnan](https://www.linkedin.com/in/adnan-azmat-496000153/?originalSubdomain=sg),Research Associate (joned April 2025~May 2026)
1. [Dr Luong Hieu Thi](https://www.hieuthi.com/),research fellow (Deepfake) (joined Jan 2024~Dec 2025)
1. [Ho Thi Nga](https://sg.linkedin.com/in/ngaho), sentence unit detection and full-stack, backend. (May 2013~Jul 2024)
1. [Nabilah Ismail](https://www.linkedin.com/in/nabilah-ismail-6b3aa0164), Corpus Development (joined Oct 2020~Oct2023
1. [Dr Ge Meng](https://gemengtju.github.io/),research fellow NUS AISG (Speech recognition) (Oct 2019~Apr 2020, then 2023~2024 for Prof Morning project)
1. [Dr Rajendra Prasad Sirigina](https://www.linkedin.com/in/RajendraPrasadSirigina9b691859/), Research Fellow, Time series, 2019 Feb-> 2021 June
1. [Ma Duo (AISG-NUS)](https://www.linkedin.com/in/maduo-843771197/), LVCSR and classification, 2019-2021
1. [Dr Pham Van Tung](https://www.linkedin.com/in/tungpv85/), Research Fellow, Speech recognition, end-to-end, keyword spotting, Jan 2012-2021 May
1. [Dr Xu Haihua](https://www.linkedin.com/in/haihua-xu-42757419), Principal Research Fellow, Robust LVCSR, keyword spotting, Feb 2012-2021 March
1. [Mai Trung Duc](https://www.linkedin.com/in/duc-mai-trung-1410/), full-stack and mobile app development, Mar 2019-Dec2021
1. [Xu Chenglin](https://www.linkedin.com/in/xuchenglin28), PhD (2020), Single Channel Multi-talker Speech Separation with Deep Learning
1. [Zeng Zhiping](https://www.linkedin.com/in/zengzhiping/), LVCSR, March 2018- April 2020
1. [Ho Danyuan](https://www.linkedin.com/in/danyuan-ho-4a7312173/), corpus development and linguistic, May 2018-March 2020
1. [Tian XiaoHai](https://www.linkedin.com/in/xhtian/), TTS and voice morphing, part-time PhD and Staff, 2013-2018. Now in NUS.
1. [Rao Wei](https://www.linkedin.com/in/wei-rao-49382080), Speaker verification, 2015-2018, Now in NUS.
1. [XiaoXiong](https://www.linkedin.com/in/xiong-xiao-0a6a9b29/), PhD Student 2004-2008, Staff 2008-2017, Now in Microsoft, Redmond - since Apr 2017
1. [Benjamin Bigot](https://www.linkedin.com/in/benjamin-bigot-ab175291/), 2014-2016 - LVCSR for RR
1. [Huang Guangpu](https://orcid.org/0000-0001-5880-7956), 2012-2015 - Articulatory Phonetics Features
1. [Lyu Daucheng](https://www.linkedin.com/in/dau-cheng-lyu-48794916/), 2009-2013 - Code switch LVCSR
1. [Zhao Shengkui](https://www.linkedin.com/in/shengkui-zhao-%EF%BC%88%E8%B5%B5%E8%83%9C%E5%A5%8E%EF%BC%89-74983b22/),2009-2010 - Microphone array and beamforming.



## Current PhD and Graduate Students {: #my_Students }

1. [Liu Changsong](https://www.linkedin.com/in/changsong-liu/), ROBUST AND EXPRESSIVE SPEECH GENERATION IN LOW-RESOURCE AND STREAMING SCENARIOS (PhD reg Aug 2026, Supervisor: Chng Eng Siong)
1. [Wu Mengjun](https://linkedin.com/in/alex-mengjun-wu-9844122b6), Towards Efficient and Robust Audio Understanding (PhD reg Aug 2026, Supervisor: Chng Eng Siong)
1. [Wu Donghang](https://scholar.google.com/citations?user=-ubODQ4AAAAJ), Full-Duplex Diaglog LLM (reg: Jan 2026)
1. [Ma Ziyang](https://ziyang.tech/), Advancing LLM research (PhD reg Aug 2022, Supervisor: Chng Eng Siong, Shanghai Jiao Tong: Chen Xie)
1. [Peng Yizhou](https://linkedin.com/in/yizhou-peng-18425b202?originalSubdomain=sg), Versatile Large Speech Language Modeling for Duplex Dialogue Systems (PhD reg Jan 2025, Supervisor: Chng Eng Siong)
1. [Chao Yi-Wen](https://www.linkedin.com/in/yi-wen-chao-407277295/), Paralinguistics-enhanced LLM for Spoken Dialogue System (PhD reg Aug 2024, Supervisor: Chng Eng Siong, AStar: Lu Yanfeng)
1. [Yeo Yue Heng](https://www.linkedin.com/in/yeoyueheng), LLM for speech recognition (PhD reg Jan 2024, Supervisor: Chng Eng Siong, AStar Co-Sup:Tran Huy Dat), AStar Scholar
1. [Li Haoyang](https://www.linkedin.com/in/davisl44622), Neural Text to Speech (PhD reg Aug 2023)
1. [Tuan Truong Duc](https://www.linkedin.com/in/ductuantruong/), Robust Speaker verification and Deep Fake Detection under noisy and short duration scenario (reg Jan 2023, PhD)

### Current Co-Sup: PhD Students {: #my_co_sup_Students }

1. [Ashutosh Anshul](https://www.linkedin.com/in/ashutosh-anshul-b12508148), Multi-modal Deep Fake classification and detection (reg Jan 2024, Supervisor: Deepu Rajan, Co-Sup:Chng Eng Siong)
1. [Shreyas Gopas](https://www.linkedin.com/in/the-shreyas-gopal/), Speech Recognition using LLM for under-resourced languages (reg Jan 2024, Supervisor: Quek Hiok Chai, Co-Sup:Chng Eng Siong). [QE(2026 June)](https://www.dropbox.com/scl/fi/wkhj3i34i8rnzjpfkenbk/2026_Shreyas_QE.pdf?rlkey=oj3wtm5nfv4l1v76kyrzzkc8m&st=3naltyx0&dl=0) [Slides](https://www.dropbox.com/scl/fi/4rgcchhekpx4sb182du0l/2026_Shreyas_QE_Presentation.pptx?rlkey=suf8cewjulipiv41m2c7fchcn&st=u1zatw6h&dl=0)

### Current MEng and Masters Program Students {: #my_MSAI_Students }

1. [Zhang Qianen](https://www.linkedin.com/in/%E8%B0%A6%E6%81%A9-%E5%BC%A0-029ab4431/), Noise Robust SSL for Speech processing Applications (MEng reg Aug 2026, Supervisor: Chng Eng Siong)
1. [Liu Haisu](https://linkedin.com/in/haisu-liu-33b1aa359/), Emotion-Enhanced LLM for Spoken Dialogue Systems (MEng reg Aug 2026, Supervisor: Chng Eng Siong)
1. [Wang Yuxi](https://wailywang.github.io/), Voice Conversion Audio Security: Classification of Audio for Deepfake and Audio Watermarking Presence (MEng reg Aug 2025, Supervisor: Chng Eng Siong)
1. [Hu Guoqiang](https://coding-sharks.github.io/), LLM for Audio editing tasks (MEng reg Aug 2025, Supervisor: Chng Eng Siong)

### Collaborating graduate Student (China) {: #my_collaborator_Students_China }

Every year, we will host graduate students from China. We have hosted students from China Scholarship Council (program), Peking University, Xinjiang University, Hunan University, Tianjin University and Northwestern University. The visits have been very rewarding, and many publications have come out of these visits. We hope to see more such outstanding students, so do apply!

1. [Yang Yuhang](https://arxiv.org/abs/2311.17382) (2023 June~, PhD student (Hunan University), China), LLM ASR
1. [Zhang Xiangyu](https://www.linkedin.com/in/xiangyu-zhang-a0735b194/) (2023 June~, PhD student (UNSW, Australia), Depression classification




### Past PhD Students {: #Past_PhD_Students data-count=past-phd }

![](images/recentPhDGrad.jpg)

1. [Fabian Ritter Gutierrez](https://www.linkedin.com/in/fabian-ritter-gutierrez-9ab4317a/), EFFICIENT SELF SUPERVISED REPRESENTATIONS FOR SPEECH AND MUSIC (PhD, reg Aug 2022, submitted Thesis Aug 2026, AStar scholar) (co-supervised with AStar: Nancy Chen. QE (2024): [Github of Thesis and Video](https://github.com/FabianRitter/NTU_QE_PRESENTATION/tree/main) [Thesis submitted (Aug 2026)](https://www.dropbox.com/scl/fi/hm1wlmvz4k3daqscyr94r/2026_Fabian_submitAug2026.pdf?rlkey=yrf2wlzikd4097mxmvisyzinf&dl=0)
1. [Nikita Kuzmin](https://www.linkedin.com/in/paniquex/), TOWARDS STREAMING SPEAKER ANONYMIZATION: FROM OFFLINE SYSTEMS TO REAL-TIME FULL-DUPLEX SPEECH DIALOGUE MODELS (PhD, reg Aug 2022, submitted Thesis Aug 2026, AStar scholar) [Thesis submitted (Aug 2026)](https://www.dropbox.com/scl/fi/7n666p4c25dkald4ihsmg/2026Aug_NikitaThesis_Submission.pdf?rlkey=9bjxm0a8x5w4xz1su3s1wffif&dl=0) (co-supervised with AStar: Lee Kong Aik. [QE: 2025](https://github.com/paniquex/PHD_QE_NTU)
1. [Kwok Chin Yuen](https://www.linkedin.com/in/aaron-kwok-b1163b1b4/), Efficient Adaptation of Speech Foundation Models for Low-Resource Tasks (reg Aug 2021, MEng, converted to PhD program, Aug 2022) [PhD Thesis (submitted Sep 2025) [Aaron's gitHub for writing his thesis](https://github.com/cyaaronk/thesis_writing_tutorial)](https://www.dropbox.com/scl/fi/32z7zo6c69n4f48pdle9u/aaron_thesis_Sep_18_2025.pdf?rlkey=xbth2wwpczgq4ehgu7kox6zxh)
1. [Hu Yuchen 胡宇晨](https://yuchen005.github.io/), Advances in End-to-End Robust Automatic Speech Recognition (reg Aug 2021, MEng, converted to PhD program, Aug 2022, Thesis submitted: June 2025). [PhD Thesis (final version: Sep 2025)](https://www.dropbox.com/scl/fi/2sk9mmlg2tmsi4cm69eu2/2025_HuYuchen_submit.pdf?rlkey=7z5tth2087k3sgrpe5kowj2mc)
1. [Yip Jia Qi](https://www.linkedin.com/in/yip-jia-qi/), From Time-domain to Generative Speech Separation (reg Aug 2021, Alibaba scholar PhD) [(Thesis (final): June 2025)](https://www.dropbox.com/scl/fi/40c7mlxcfz8qblo081xs0/2025_YipJiaQi_final.pdf?rlkey=458iqptqohyano3rpomfm1f6p)
1. [Zou HeQing](https://sites.google.com/view/hqzou/), Multimodal Machine Learning (reg Jan 2021, submitted June 2025, PhD) (Sup:Deepu Rajan, Co-Sup: Chng Eng Siong)
1. [Chen Chen](https://www.linkedin.com/in/chen-chen-4bb7231b8/), Advancing Speech-to-Text Adaptation for Large Speech Models (PhD reg Jan 2021) (defended: June2025) [Google Scholar](https://scholar.google.com.hk/citations?user=uUmSp1QAAAAJ?hl=zh-CN), [(Thesis final: June 2025)](https://www.dropbox.com/scl/fi/tqhwjvfn9bamqal4a12g3/2025_ChenChen_Thesis_Submission.pdf?rlkey=koupcieg3a3qbtsvtuwwzhp09)
1. [Ng Dian Wen](https://www.linkedin.com/in/dianwen-ng-34691a129/), Optimizing Speech Representation Learning for Enhanced Noise Robustness in Downstream Applications (PhD reg Jan 2021, graduated 2025 May, Alibaba scholar PhD) [(Thesis :May 2025)](https://www.dropbox.com/scl/fi/5aped99ygawmsqxy7yr0l/2025_dianwen_final.pdf?rlkey=k6vr2hrzjh974d1tt49th8hld?st=wgmg7bdu?dl=0)
1. [Rae Koh Jia Xin](https://www.linkedin.com/in/rae-jia-xin-koh-9b10b3105/), Singapore English (reg Aug 2019, PhD) (graduated 2025) (Sup: Tan Ying Ying (HSS), Co-Sup: Chng Eng Siong)
1. [Andrew Koh Jin Jie](https://www.linkedin.com/in/andrew-koh-5464a5118/), Sequence to Sequence Machine Learning (reg Aug 2019, PhD, graduated 2023)
1. [Zhao Yingzhu](https://www.linkedin.com/in/yingzhuzhaophd/), End-to-End speech recognition (reg Jan 2019, PhD, graduated May 2023). [Oral Defence rehearsal](https://youtu.be/6vCzAem8Hbo) [PhD Slides](https://www.dropbox.com/s/x9hcwk383htwlvl/Yingzhu_oral_SlidesApr2023.pptx?dl=0) [PhD report](https://www.dropbox.com/s/1yf2ajg86777bzq/2023_April_thesis_ZhaoYingzhu.pdf?dl=0) [PhD latex folder](https://www.dropbox.com/s/26as7mwlafg0akg/ZhaoYingZhu_PhDThesis_Apr2023Latex.zip?dl=0)
1. [Hou Nana](https://www.linkedin.com/in/nana-hou-592a80127/), Robust LVCSR for air traffic control speech (reg Jan 2017, PhD, submitted Jan 2022)
1. [Xu Chenglin](https://www.linkedin.com/in/xuchenglin28), [PhD Slides](https://www.dropbox.com/s/as78r4txv0z27kc/ChenglinPhDDefenceSlidesAug2020.pptx?dl=0) [PhD Thesis (2020) Single Channel Multi-talker Speech Separation with Deep Learning](https://www.dropbox.com/s/zn6ad5j3lose4r6/ChenglinPhDThesis18July2020.pdf?dl=0)
1. [Paul Chan](https://www.linkedin.com/in/paul-yaozhu-chan-9408777a/), Synthesis of the human singing voice (2020)
1. [Khassan Yerbolat](https://www.linkedin.com/in/khassanov/), [PhD Slides](https://www.dropbox.com/s/1z4d6y2fd5crdwk/2020_Khassan_Slides.pptx?dl=0), [Online Presentation](https://www.youtube.com/watch?v=1Dm16krGgv0)(April 2020) and final [PhD thesis.](https://www.dropbox.com/s/nc6hijq2l6q18ip/Khassan_FinalAmended_Thesis_May2020.pdf?dl=0), (2020) Language Model Domain Adaptation for Automatic Speech Recognition Systems.
1. [Pham Van Tung](https://www.linkedin.com/in/tungpv85/), [PhD Thesis](https://www.dropbox.com/s/76wrdu426xr4x3z/2019_PhamVanTung_Thesis_amended.pdf?dl=0)(2019) Robust Spoken Term Detection using partial search and re-scoring hypothesized detections techniques. Now in NTU.
1. [Tian Xiaohai](https://www.linkedin.com/in/xhtian/), [PhD Thesis](https://www.dropbox.com/s/pli1uh2i9dr3n0r/2019_Xiaohai_Tian_revised.pdf?dl=0)(2019) Voice Conversion with Parallel/Non-Parallel Data and Synthetic Speech Detection. Now in NUS.
1. [Chong Tze Yuang](https://www.linkedin.com/in/tze-yuang-chong-4b9b2a61/), [PhD Thesis](https://www.dropbox.com/s/9ur3bon1whthsk8/2018_June_ChongTzeYuangPhDThesis.pdf?dl=0), [Slides](https://www.dropbox.com/s/m8y59n6nv0kqjdu/2018_June_ChongTzeYuang_Presentation.pptx?dl=0), [Thesis organization](https://www.dropbox.com/s/kjfap8a4e1zfnkr/2018_June_ChongTzeYuangPhDThesis_organization.docx?dl=0), (2018) Exploiting Long Context Using Joint Distance and Occurrence Informationfor Language Modeling.
1. [Nguyen Duc Hoang Ha](https://www.linkedin.com/in/ha-nguyen-4101517a/), [PhD Thesis](https://www.dropbox.com/s/a0gvjb73rqrmb1f/2017_NguyenDucHoangHa_PhDThesis.pdf?dl=0)(2017) [Slides](https://www.dropbox.com/s/pmsluvihe41lk3d/2017_NguyenDucHoangHa_PresentSlide.pdf?dl=0) Feature based robust techniques for speech recognition.
1. [Nguyen Trung Hieu](https://www.linkedin.com/in/trung-hieu-nguyen-a99569b8/), [PhD Thesis](https://www.dropbox.com/s/siggnj3dvmu3xq0/2014_NguyenTrungHieu_PhDThesis.pdf?dl=0)(2015). Speaker Diarization in Meeting room domain. Now at Alibaba.
1. [Do Van Hai](https://www.linkedin.com/in/van-hai-do-7a252850/), [PhD Thesis](https://www.dropbox.com/s/0v9npacoacghqwf/2015_DoVanHai_PhDThesis.pdf?dl=0)(2015). Acoustic modelling of speech under limited training data condition. Now in Vietnam Telecoms.
1. [Wu Zhizheng](https://www.linkedin.com/in/zhizhengwu/), [PhD Thesis](https://www.dropbox.com/s/m6u9ccmuvkbo0av/2015_WuZZ_PhDThesis.pdf?dl=0)(2015). Spectral Mapping for Voice Conversion.
1. [Jonathan Dennis](https://www.linkedin.com/in/jonathan-dennis-9ab85186/), [PhD Thesis](https://www.dropbox.com/s/zpxrbvlhto7199y/2014_JohnDennis_PhDThesis2014.pdf?dl=0)(2014). [Slides](https://www.dropbox.com/s/72md2vuw2jebjmy/2014_JonDennis_PhD_oral_defence_slides.pptx?dl=0), Sound Event Recognition in Unstructured Environments using Spectrogram Image Processing.
1. [Wang Lei](https://www.linkedin.com/in/lei-wang-44190967/), (2013). Audio Pattern Discovery and retrieval.
1. [Tong Rong](https://www.linkedin.com/in/rong-tong-3028924a/), [PhD Thesis](https://www.dropbox.com/s/gcqmbqaq9vd52si/2012_TongRong_PhDThesis.pdf?dl=0)(2012). Towards high performance phonotactic features for spoken language recognition. Now at Alibaba.
1. [Omid Dehzanghi](https://www.linkedin.com/in/omiddehzangi/), (2012). Discriminative Learning for speech recognition, U of Michigan
1. [Xiao Xiong](https://www.linkedin.com/in/xiong-xiao-0a6a9b29/), [PhD Thesis (2009)](https://www.dropbox.com/s/ywqbhkz0vfnh06s/2009_XiaoXiong_PhDThesis.pdf?dl=0). PhD Thesis: Robust speech features and acoustic models for speech recognition. [QE (2006)](https://www.dropbox.com/s/7muljjnvlqn5f7r/2006_XiaoXiong_PhD_QE.pdf?dl=0),Speech Enhancement with Applications in speech recognition, now in Microsoft, US since Apr 2017
1. [Wang Jinjun](https://www.linkedin.com/in/wangjinjun/), PhD (2008), Content based sports video analysis and composition. Now in Xian Jiaotong.

### Past MEng {: #Past_MEng_Students data-count=past-meng }

1. [Wu Yihao](https://www.linkedin.com/in/%E4%BE%9D%E8%B1%AA-%E5%90%B4-0b5523325/), Robust diarization for large scale meeting scenario,[Thesis](https://www.dropbox.com/scl/fi/ps0dbxwvn602mofo2fqms/2026_MEng_Wu-Yihao.pdf?rlkey=xm79jbkbup8i14upp3njkwt3r&dl=0) (MEng reg Aug 2024, Graduated: July 2026, Supervisor: Chng Eng Siong)
1. [Liu Songting](https://www.linkedin.com/in/songting-liu-b0098b220/), Streaming High Fidelity Voice Conversion Through ASR-Guided Discrete Representations. [Masters Thesis (2026)](https://www.dropbox.com/scl/fi/dxz3j0om1ujqoygi9j4on/2026_MEng_LiuSongTing.pdf?rlkey=0a1y00itn56pcs8fdmtluulia&dl=0) (MEng reg Aug 2024, graduated Apr 2026, Supervisor: Chng Eng Siong)
1. [Tanmay Surana](https://www.linkedin.com/in/tanmay-surana-118a79192/), `Deep Learning-based Text Augmentation for Named Entity Recognition` (reg Aug 2021, MEng, completed Oct 2023)
1. [Prachaseree Chaiyasait](https://www.linkedin.com/in/chaiyasait/), Adaptation of Language Models via Text Augmentation (reg Aug 2021, MEng, submitted Jul 2023, completed Oct 2023)
1. [Kyaw Zin Tun](https://www.linkedin.com/in/kyaw-zin-tun-170b52122), Name entity recognition for chatbot applcications(MEng, started Aug 2020, submitted thesis Aug 2022)
1. [Xue Fuzhao](https://www.linkedin.com/in/fuzhao-xue-6410561a6/), Information extraction from text (MEng 2020)
1. [Lim Zhi Hao](https://sg.linkedin.com/in/lim-zhi-hao-025546115), (MEng 2020), Anti-Spoofing Techniques for Robust Speaker Verification[Thesis (2020)](https://www.dropbox.com/s/tjhprq3dvj79hjm/2020_LimZhiHao_Robust_Speaker_Verification.pdf?dl=0)
1. [Ho Thi Nga](https://www.linkedin.com/in/ngaho/), (MEng 2019), Sentence unit detection for automatic speech transcripts using lexical information
1. [Leow Sujun](https://www.linkedin.com/in/su-jun-leow-52755085/), (MEng 2018), Image Processing Technique for Speech Signal Processing
1. [Nguyen Quy Hy](https://www.linkedin.com/in/hy-nguyen-quy-61292739/), (MEng 2017), Voice conversion using DNN
1. [Steven Du](https://www.linkedin.com/in/steven-du-1662511b/), (MEng 2015), Robust Front End for Speaker Verification
1. [Terrence Ng Wen Zheng](https://www.linkedin.com/in/terence-ng-70411320/), [Thesis](https://www.dropbox.com/s/2staf3jboruaozr/2014_MENG_TerrenceNgWenZheng.pdf?dl=0),(MEng 2014), Sound Event recognition in home environment
1. [Chen Wenda](https://www.linkedin.com/in/wenda-chen-6261732a/), (MEng 2014),Computer Assisted Language Learning
1. [Ben Pham Chau Khoa](https://www.linkedin.com/in/pckben/), [Thesis](https://www.dropbox.com/s/tfvf6sx3wpb9eeb/2012_MEng_BenPhamChauKhoa.pdf?dl=0),(MEng 2012), Robust VAD
1. Eugene Koh, (MEng 2009), Speaker Diarizaton

### Past MSAI Students and Others (CSC) collaboration students {: #Past_MSAI_Students }

1. [Thirunavukarasu Suresh Sathya Krishnan](https://www.linkedin.com/in/skandml/?originalSubdomain=sg), Advancing Dialogue Systems: Synthetic Dialogue Generation and Code-Switching in LLMs (MSAI reg Aug 2024, Supervisor: Chng Eng Siong)
1. [Azmat Adnan](https://www.linkedin.com/in/adnan-azmat-496000153/?originalSubdomain=sg),(MSAI Thesis, 2024) Robust Diarization
1. [Ni Yunyi](https://www.linkedin.com/in/yunyi-ni-3a6885325/?original_referer=https%3A%2F%2Fwww%2Egoogle%2Ecom%2F?originalSubdomain=sg), VoiceForge: A Text-Driven Character Voice Generation System for Narrative Content Creation (MSAI reg Aug 2024, Supervisor: Chng Eng Siong)
1. `Chen Weiguang` (2022 June~,2023 PhD student (Hunan University), Diarization using multi-channel approaches
1. [Yao Jixun](https://scholar.google.co.uk/citations?user=KjcXd6cAAAAJ) (2023 Oct~ Oct 2024, AISG NUS visitor), PhD student (Northwestern Poly, China), Speech Enhancement and TTS
1. [Le Yuquan](https://scholar.google.com/citations?user=GEVwy4sAAAAJ) (2023 Oct~ Oct 2024, CSC visitor), PhD student (Hunan University, China), LLM for Legal
1. `Luo Juan` (2023 Oct~ Oct 2024, CSC visitor), PhD student (Hunan University, China), Audio event detection and classification
1. [Zhang Zizheng](https://arxiv.org/abs/2305.10761) (2023 June~ Jun 2024, AISG remote), Masters student (Peking University, China), Speech Separation, [github](https://github.com/TzuchengChang/NASS)
1. [Zheng Haorui](https://openreview.net/profile?id=~Haorui_Zheng1) (2024 June~ , AISG remote), Masters student (Peking University, China), Speaker Diarization with Speech Separation
1. [Bo Han](https://github.com/fluide1022) (2023 Oct ~Oct 2024, CSC visitor), PhD student Zhejiang Uni, China), Deep Fake TTS audio generation
1. [Chen Yanru](https://www.linkedin.com/in/yanru-chen-2b38b8221/) (2024 Jan~), Masters Data Science, Classification of Depression Syndrome by Deep Learning
1. [Qin Xiaokai](https://www.linkedin.com/in/xiaokaiqin/) (2023 Aug~), MSAI student, Deepfake audio generation using voice conversion
1. [Azmat Adnan](https://in.linkedin.com/in/adnan-azmat-496000153) (Reg 2023 Aug, completed Aug 2024), MSAI student, DNN Approaches for noisy speech diarization
1. `Zhuo Ning` (Reg 2023 Aug, completed Aug 2024), Masters Cybersecurity student, Deep Fake Corpus developmenet and detection
1. `Jiang Yufei` (2022 Aug~ 2023 Aug), MSAI (NTU), Adopting Neural Translation Model in Data Generation for Inverse Text Normalization
1. `Liu Jiaxing` (2021 Oct ~2023 Oct, CSC visitor, PhD student Tianjin University, China), Multi-modal emotion recognition
1. `Cheng Qi` (2021 Oct ~2022 Oct, CSC visitor, PhD student Harbin Engineering Uni, China), Graph Neural Network for Lattice rescoring
1. [Samuel Samsudin Ng](https://www.linkedin.com/in/samuel-samsudin-ng/), (MSAI 2020-S1), Speech emotion recognition with AlexNet and Fully convolutional network, [Sam's MSAI Thesis](https://www.dropbox.com/s/3ullgc88cfihj2e/2020_MSAI_Report_SamuelSamsudinNg.pdf?dl=0), [github depository](https://github.com/samsudinng/speech_emo_recognition.git), [kaggle iEmoCap](https://www.kaggle.com/samuelsamsudinng/iemocap-emotion-speech-database)
1. [Cheung Chin Ka](https://www.linkedin.com/in/andy-cheung-a0847572/), (MSAI 2020-S1), Acoustic Scene Classication with cutting edge hyperparameter tuning tool, [Andy's MSAI Thesis](https://www.dropbox.com/s/0bpudw98ra4f80k/2020_msai-cheung-chin-ka-master-project-report.pdf?dl=0)
1. [Liu Bozhong](https://www.linkedin.com/in/bozhong-sampson-liu/), (MSAI 2020-S2), Wakeup keyword detection for far-field microphone array using end to end framework

### Past MSAI Students and Other collaboration students {: #PastStudents }

1. `Zhao Yang` (2021 Oct ~2023 Oct, CSC visitor, PhD student Xian JiaoTong Uni, China), Semi/Self supervised representation for speech recognition
1. `Peng Yizhou` (2020 June ~2022 June, Masters student Xinjiang, China), ASR development (Kaldi and End2End)
1. `Yang Yuhang` (2021 June~2023 June, Masters student Xinjiang, China), WeNet ASR, End2End ASR
1. `Guo Yachao` (2021 June~2023 June, Masters student Xinjiang, China), End2End Hotword LM Adaptation

## Internship in Speech Lab@SCSE, NTU {: #Past_Interns }

We have a tradition of hosting senior undergraduate students (final year) and graduate students (Masters and PhD) in our lab.

Typically we only host students who can work with us for 6 months or more in 2 sessions. Session 1: Jan-June, Session 2: Jul->Dec each year. Since covid (it had been remote). Currently we only host students who are doing this as part of their course sanctioned by their school and its graded *so its not a personal arrangement*.

To apply, you should be writing to us at least 1/2 year before the start of the attachment. Kindly send me an email with a detailed cv. As we receive huge number of applicants, only shortlisted students will receive a response.

We have two tracks, one for research and the other for development. For research, we expect students to have work with pyTorch, tensorflow, etc. For development, we expect experiene with google summer of code, full stack experience. During this internship, you will be actively working with our speech-team researchers on tasks such as implementing and realising state-of-the-art ML/DL techniques and deploying them for various tasks listed below:

**Our current Research projects are:**

1. LMM for summarization and Inverse Text Normalization.
1. Classification from Audio: Speaker profiling (age, height, weight, accent, emotion) classification, Audio Event classification (DCASE), Speaker diarization and overlapping speech detection
1. Speech Enhancement and Audio processing: Enhancing noisy speech to clean DNN approaches, Deep Fake Speech: Modifying audio eavefiles to target environment/speaker/ noise using GAN

**Our current Development projects are:**

1. Terraform and cloud deployment of speech engine with scaling, auto-update, security and dashboard.
1. MAGOR - search and indexing speech, video and audio
1. Async speech recording and recognition Interface - recording and async update of speech recognised with update on name entity
1. Transcriptor - GUI for correction of erroneous recognised text

Upon completion of the project, we expect a formal project report + code repository, and if possible submit the work for publication.

Pls find attached a writeup by Shashank (2021 intern) onboarding help file, have a look. [Onboarding writeup by Shashank](https://www.dropbox.com/s/fq34mfqtmuvy42a/SpeechLab_Onboarding_Shshank_2021.pdf?dl=0)

**Current and Past Interns:**

The list is incomplete, we began to the tradition of taking pictures with the students from India about 2017, there were many others. The pictures here include CSC students, undergraduate students, and details included inside.

1. [2026 group of students](https://docs.google.com/document/d/1NKbp4-oh3UbGMoqDJqghpMLgU0Fjjebl3rWH0-g5H9E/edit?usp=sharing)
1. [2025 group of students](https://www.dropbox.com/scl/fi/et19yyf5ij5za37vw7syi/Visiting-Student_Intern-2025_CSC.docx?rlkey=oer1ny14pdkz4bh9v1196plkn?e=1?dl=0)
1. [2024 and 2025 June~Dec(fully remote)](https://www.dropbox.com/scl/fi/isftidn65ha7fhaqrisqm/2024_2025_Interns.pdf?rlkey=uoeg0eh6doyb2sno53rmxapce?e=1?st=mv05imeq?dl=0)
1. [2023 June~Dec(fully remote)](https://www.dropbox.com/scl/fi/h8q31r9gw2ck3d9l3a87l/2023_June_Dec_Interns.pdf?rlkey=vlyi0kkfg9mf7mo41c514l6u9)
1. [Some pictures of our group meetings with Interns from 2023(fully remote)](https://www.dropbox.com/scl/fi/ix2zecra23egczjk83x43/Interns-Jan-June2023.pdf?rlkey=v1fddv3g0n5etibyqsbskndtc)
1. [Some pictures of our group meetings with Interns from 2022(fully remote)](https://www.dropbox.com/scl/fi/re9mcme80i63cnmefoqnl/Interns-2022.pdf?rlkey=tidhkiguwqmgjj6sm6wnaquxt)
1. [Some pictures of our group meetings with Interns from 2021(fully remote)](https://www.dropbox.com/s/qpbyp5yb8mxujcg/pic_2021.docx?dl=0)
1. [Interns from 2020 (July-Dec) (fully remote)](https://www.dropbox.com/s/6jncuc9srnekg3o/MICL_Interns_AugDec2020.pdf?dl=0)
1. [Interns from 2020 (Jan-May) (our last group before we could not have students in Singapore)](https://www.dropbox.com/s/qj1c3lytdy8b7mz/MICL_Interns_feb2020.pdf?dl=0)
1. [Interns from 2019 (Nov, Grp1)](https://www.dropbox.com/s/eu0ewshlvcpu9xp/MICL_Interns_Nov%202019_Grp1.pdf?dl=0)
1. [Interns from 2019 (Nov, Grp2)](https://www.dropbox.com/s/cbeqnrd5vu7nl9s/MICL_Interns_Nov%202019_Grp2.pdf?dl=0)
1. [Interns from 2019 (Jul)](https://www.dropbox.com/s/e7t42elpkkepxla/MICL_Interns_July2019.pdf?dl=0)
1. [Interns from 2019 (Apr)](https://www.dropbox.com/s/hhvxdkrsy36umxp/MICL_interns_Apr2019.pdf?dl=0)
1. [Interns from 2018 (Oct)](https://www.dropbox.com/s/5kvr37n34m5dgso/InternsGroupPhotoOct2018a.pdf?dl=0)
1. [Interns from 2018 (Jul)](https://www.dropbox.com/s/p96jev90lw1n5iq/InternsGroupPhotoJuly2018.pdf?dl=0)
1. [Interns from 2018 (May)](https://www.dropbox.com/s/yur445nl12lwvlk/InternsGroupPhotoMay2018.pdf?dl=0)
1. [Interns from 2018 (Jan)](https://www.dropbox.com/s/u16qn9f4lu7hqai/InternsGroupPhotoJan2018.pdf?dl=0)
1. [Interns from 2017 (Jul)](https://www.dropbox.com/s/hup912rma6p9loc/MMLInternsNTU2017.pdf?dl=0)
1. [Gangeshwar Krishnamurthy,2017 (Jan-Apr)](http://www.linkedin.com/in/gangeshwark)
1. [Gao Shengheng,2016 (Mar-Jun)](https://www.linkedin.com/in/shengheng-gao-2779043a/)
