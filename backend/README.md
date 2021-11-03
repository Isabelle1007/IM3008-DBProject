# README.md
## Set Up Virtual Environment
### Open VM
* vm 是我們取名的虛擬環境名稱，可替換成任意名稱
#### Windows
```shell=
cd backend
python3 -m venv vm
vm\Scripts\activate.bat
```

#### Mac
```shell=
cd backend
python3 -m venv vm
source tutorial-env/bin/activate
```

### Download Required Packages
**在虛擬環境執行以下指令，以安裝所需套件**
```shell=
python -m pip install --upgrade pip
pip install -r requirements.txt
pip list # check
```

### Set the Environment Info.
* 開啟 .env 檔案
* `DATABASE_URL=postgres://postgres:<passord>@127.0.0.1:5432/DBP` 更改此行將 <password> 改為自己 postgres 的密碼。
  
## Start Django Server
**在虛擬環境執行以下指令，以開啟環境伺服器**
```shell=
cd online_course
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
