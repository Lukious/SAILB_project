1. 우분투 16.04 설치
2. 우분투 내에 인터넷으로 아나콘다 홈페이지 들어가  리눅스용으로 파일 다운로드
3. 터미널로 가서 bash Anaconda3-2020.02-Linux-x86_64.sh 입력
4. source ~/.bashrc 입력
5. conda 설치 완료!!
6. 터미널에서 git clone git@github.com:akaraspt/deepsleepnet.git <-- 이거 쳐서 original deepsleepnet 다운
7. original deepsleepnet 만을 위한 환경을 conda로 구축해주어야됨
8. 터미널에서 conda create --n originaldsn <--- 환경 하나 만들어주자 
9. 터미널에서 conda activate originaldsn
10. originaldsn 환경에 필요한 모듈들 설치해 주어야 한다
conda install python=2.7
pip install mne==0.15.2
pip install pandas==0.18.1
pip install matplotlib==1.5.3
--> 이거 4개 정도 깔면 됨 pip 쓸려면 pip도 conda install pip 로 설치해주셈
11. 위에 4개 깔았으면 original deepsleepnet 디렉토리에 data파일로 가주셈 (cd로) 그다음에
	chmod +x download_physionet.sh
	./download_physionet.sh
	요거 터미널에 쳐서 edf파일 다운받으셈
12. 그다음 터미널에 python prepare_physionet.py --data_dir data --output_dir data/eeg_fpz_cz --select_ch 'EEG Fpz-Cz' 요거 쳐서 npz파일로 변환 하셈
13. 변환을 마쳤다면 이제 original deepsleepnet은 이제 안씀 데이터만 필요했던거임
14. 이제 우리가 돌려야할 deepsleepnet을 위해 새로운 환경을 만들어야 함
15. cd 로 타고 들어가 우리가 돌려야 하는 deepsleepnet 디렉토리 안으로 들어가셈
16. 그다음 conda create -n dns --file requirements.txt 로 환경을 만들어주셈
17. 그다음 conda activate dns 로 환경에 들어가고 deepsleepnet 디렉토리에 아까 만들어둔 npz 폴더를 넣고
18. python data_preparation.py
19. python trainer.py
20. 추후 나오는 에러에대해서는 update 예정...