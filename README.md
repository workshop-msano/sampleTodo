# Overview
Install git inside a container and establish remote connection using VSCode. Incorporating Docker containers into actual development has become easier for development and version control purposes. I have shared the knowledge gained from creating this application in a [Qiita post](https://qiita.com/miku0129/items/e9d7276a1c3bda56d1df).

# Demo

## Tools Used
In my environment, I have installed Docker on Ubuntu. It is assumed that you can connect to GitHub via SSH using VSCode.

__※ I received a report from someone who helped with the verification process that [Rootless Mode](https://docs.docker.com/engine/security/rootless/) is required to use Docker with VSCode. __ I will update with additional information if available.

| Tool | Version | Remarks |
|:-----------|:------------|:------------|
| Docker     | 20.10.21    |             |
| docker-compose | 1.29.2  |             |
| Dev Containers | 0.266.1 | VSCode extension     |

## Folder Structure

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

## Flow from Cloning the Template to Setting Up the Development Environment

※ The installation of each [tool](https://github.com/workshop-msano/sampleTodo/edit/main/README.md#%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E3%83%84%E3%83%BC%E3%83%AB) has been completed.

1. Clone the [SampleTodo](https://github.com/workshop-msano/sampleTodo) repository from this repository.

    ```
    git clone git@github.com:workshop-msano/sampleTodo.git
    ```

2. Open the files in VSCode. Press the Remote Container start button at the bottom left of VSCode.
<br>
    <img src="https://i.ibb.co/wKywrNk/2022-12-10-104132.png" alt="2022-12-10-104132" border="0">
<br>

3. Select `Open Folder in Container` from the popup window in VSCode.
<br>
    <img src="https://i.ibb.co/1MLJ6kV/2022-12-10-104902.png" alt="2022-12-10-104902" border="0" width=600><br><br>
<br>

4. Click `Open` in the popup window.
<br>
    <img src="https://i.ibb.co/f0Z6XQf/2022-12-10-105428.png" alt="2022-12-10-105428" border="0">
<br>

5. After a while, VSCode will be displayed. If `Dev Container` is displayed next to the Remote Development button at the bottom left, it means it was successful!
<br>　
  <img src="https://i.ibb.co/GWQ4zcq/2022-12-10-105935.png" alt="2022-12-10-105935" border="0">
<br>
    
6. You can access the web app from `http://localhost:8000`.
<br>
    <img src="https://i.ibb.co/zFG6TTS/2022-12-10-214935.jpg" alt="

2022-12-10-214935" border="0" width=400>
<br>

7. Since git is already installed in the container, configure it to access GitHub from the container. Open the terminal and run the following commands. <br>
   It is assumed that you can connect to GitHub via SSH using VSCode.

    ```
    git config --global user.email '<your setting>'
    git config --global user.name '<Your setting>'
    
    mkdir -p ~/.ssh/
    curl -s -o ~/.ssh/id_ed25519 "https://github.com/$(git config --global --get user.name).keys"
    ```

8. Next, enter `ssh -v git@github.com` in the terminal. <br>
   If there is a successful access to GitHub displayed in the log, it is complete! You can create a repository on GitHub and manage the source code version from within the Docker container.

<br>
<br>

## Bonus
Let's use a shell script to access the database in the Docker container. Execute the following commands outside the container.

```
docker exec -it sampletodo_db /bin/sh
```
```
psql --username postgres
```

#### Well done! 🎉🎉🎉