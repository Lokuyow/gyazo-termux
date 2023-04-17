# Gyazo-Termux
Android端末の画像フォルダから共有ボタンを押してTermuxを選択すると、画像がGyazoにアップロードされ、拡張子付きのURLをクリップボードにコピーすることができます。
### 手順
1. [F-Droid](https://f-droid.org/)からF-Droidアプリをインストールします。
1. F-Droidアプリを起動し、検索バーからTermuxとTermux:APIアプリを見つけてインストールします。
1. Termuxを開き、ストレージへのアクセス許可を得るために以下のコマンドを実行します
    ```
    termux-setup-storage
    ```
1. Termuxを起動し、次のコマンドを実行して、必要なパッケージをインストールします。
    ```  
    pkg update  
    pkg upgrade  
    pkg install python  
    pkg install termux-api  
    pkg install python-pip  
    pip install requests  
    ```  
    インストール途中の確認は `y` or `n` を適宜選択してください。
1. 次のコマンドを実行して、 `$HOME/bin` ディレクトリを作成し、`gyazo-upload.py` スクリプトを作成します。
    ```
    mkdir -p $HOME/bin
    nano $HOME/bin/gyazo-upload.py
    ```
1. githubの `gyazo-upload.py` のコードをコピーして貼り付けます。
1. Gyazo APIキーを取得し置き換えて保存します。  
    Gyazoアカウントでログインし、https://gyazo.com/api にアクセスしてAPIキーを取得し、 `YOUR_API_KEY` を自分のAPIキーに置き換えます（''の記号は必要）。  
    保存します（`Ctrl + X` を押してからYを押し、Enterを押して保存します）。
1. 次のコマンドを実行して、 `$HOME/bin` ディレクトリに `termux-file-editor` スクリプトを作成します。
    ```
    nano $HOME/bin/termux-file-editor
    ```
1. githubの `termux-file-editor` のコードをコピーして貼り付け、保存します。
1. 次のコマンドを実行して、 `gyazo-upload.py` と `termux-file-editor` に実行権限を与えます。
    ```
    chmod +x $HOME/bin/gyazo-upload.py
    chmod +x $HOME/bin/termux-file-editor
    ```
1. これで、Androidの画像フォルダから共有ボタンを押してTermuxを選択するとポップアップ画面が出るので `EDIT`を押すと、画像がGyazoにアップロードされ、拡張子付きURLがクリップボードにコピーされます。
#### 以下の表示がでた場合
`Termux requires "Display over other apps" permission to start terminal sessions from background on Android >= 10.Grants it from Settings -> Apps -> Termux -> Advanced`
> このエラーメッセージは、Android 10以降のバージョンでTermuxがバックグラウンドからターミナルセッションを開始するために必要な、"他のアプリの上に表示"の許可が付与されていないことを示しています。
> 
> 許可を付与するには、次の手順に従ってください。
> 
> 1. Androidの設定を開きます。
> 1. "アプリ"または"アプリと通知"を選択します。
> 1. "Termux"を検索し、タップします。
> 1. "高度な設定"を選択します。
> 1. "他のアプリの上に表示"を有効にします。  
> 
> この許可を有効にすることで、Termuxはバックグラウンドで実行される場合でもターミナルセッションを開始できます。