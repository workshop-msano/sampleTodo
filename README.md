# 概要
コンテナ内部にgitをインストールしVSCodeでリモート接続します。開発、バージョン管理を容易に行えるため実際の開発にDockerコンテナを取り入れやすくなったと思います。
本アプリ作成を通して得た学びをQiitaに[投稿](https://qiita.com/miku0129/items/e9d7276a1c3bda56d1df)しました。


# デモ

## 使用するツール
私の環境ではUbuntuにDockerをインストールしています。
VSCodeでGithubにSSH接続できることが前提です。

__※検証に協力いただいた方からDockerをVSCodeで使用するにあたり[Rootlessモード](https://docs.docker.com/engine/security/rootless/)が必要だったと報告を頂きました。__ これについて追加情報があればアップデートします


| ツール | バージョン | 備考 | 
|:-----------|:------------|:------------|
| Docker     | 20.10.21    |             |
| docker-compose | 1.29.2  |             |
| Dev Containers | 0.266.1 | VSCode 拡張機能     |


## フォルダ構成 

```
root/
  ├ .devcontainer/
  │  └ devcontainer.json
  ├ templates/
  │  └ index.html
  ├ .dockerignore
  ├ Dockerfile　
  ├ docker-compose.yml
  ├ .gitignore
  ├ app.py
  └ requirements.txt
```

## テンプレートのクローンから開発環境を整えるまでの流れ

※[各ツール](https://github.com/workshop-msano/sampleTodo/edit/main/README.md#%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E3%83%84%E3%83%BC%E3%83%AB)のインストールは完了しています
1. 本リポジトリから[SampleTodo](https://github.com/workshop-msano/sampleTodo) をクローンします。

    ```
    git clone git@github.com:workshop-msano/sampleTodo.git
    ```

2. ファイルをVSCodeで開きます。VSCodeの左下にある Remote Container起動ボタンを押下します。
<br>
    <img src="https://i.ibb.co/wKywrNk/2022-12-10-104132.png" alt="2022-12-10-104132" border="0">
<br>

3. VSCodeのポップアップ画面から `Open Folder in Container`を選択します。
<br>
    <img src="https://i.ibb.co/1MLJ6kV/2022-12-10-104902.png" alt="2022-12-10-104902" border="0" width=600><br><br>
<br>

4. ポップアップ画面の`Open`を押下します。
<br>
    <img src="https://i.ibb.co/f0Z6XQf/2022-12-10-105428.png" alt="2022-12-10-105428" border="0">
<br>

5. しばらく待つと VSCodeが表示されます。左下の Remote Developmentボタンの隣に `Dev Container`と表示されていれば成功です！
<br>　
  <img src="https://i.ibb.co/GWQ4zcq/2022-12-10-105935.png" alt="2022-12-10-105935" border="0">
<br>
    
6. `http://localhost:8000`からウェブアプリにアクセス可能です。
<br>
    <img src="https://i.ibb.co/zFG6TTS/2022-12-10-214935.jpg" alt="2022-12-10-214935" border="0" width=400>
<br>

7. すでにコンテナにはgitをインストールしているので、コンテナからGithubにアクセスできるように設定します。 ターミナルを開き、以下のコマンドを実行します。<br>
    ※VSCodeでGithubにSSH接続できることが前提です。
   
    ```
    git config --global user.email '<your setting>'
    git config --global user.name '<Your setting>'
    
    mkdir -p ~/.ssh/
    curl -s -o ~/.ssh/id_ed25519 "https://github.com/$(git config --global --get user.name).keys"
    ```

8. 次にターミナルで `ssh -v git@github.com`と入力しましょう。<br>
   ログの中に Githubアクセス成功の表示があれば完了です！Githubにリポジトリを作成し、Dockerコンテナ内からソースコードのバージョン管理をおこなうことが出来ます。

<br>
<br>

## ボーナス
Dockerコンテナのデータベースにシェルスクリプトを使ってアクセスしてみましょう。
以下のコマンドをコンテナの外で実行します。

```
docker exec -it sampletodo_db /bin/sh
```
```
psql --username postgres
```

#### お疲れさまでした！🎉🎉🎉
