<p align="center"><a href="https://github.com/cybersecurity-dev/awesome-docker">
  <img width="35%" src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/Docker_logo2.svg" />
</a></p>

# [Docker](https://github.com/cybersecurity-dev/awesome-docker) Toolkit [<img src="https://img.shields.io/badge/dockerhub-Docker_Toolkit-blue.svg?logo=Docker">](https://hub.docker.com/u/cyberthreatdefense)
[![FreeBSD](https://img.shields.io/badge/FreeBSD-AB2B28?style=for-the-badge&logo=freebsd&logoColor=white)]()
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)]()
[![Windows](https://custom-icon-badges.demolab.com/badge/Windows-0078D6?style=for-the-badge&logo=windows11&logoColor=white)]()
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)]()
[![Reddit](https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white)]()
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=fff)](https://www.docker.com/)

<p align="center">
    <a href="https://github.com/cybersecurity-dev/"><img height="25" src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/github.svg" alt="GitHub"></a>
    &nbsp;
    <a href="https://www.youtube.com/@CyberThreatDefence"><img height="25" src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/youtube.svg" alt="YouTube"></a>
    &nbsp;
    <a href="https://cyberthreatdefence.com/my_awesome_lists"><img height="20" src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/blog.svg" alt="My Awesome Lists"></a>
    <img src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/bar.gif">
</p>

Reusable Docker Toolkit Scripting for Development Environment

## Most used command
### Get the output (logs) of the last run container
Identify the last run container (_both running and stopped_)
```concole
docker ps -a
docker ps -a --format "{{.ID}}\t{{.Names}}\t{{.Status}}" -n 1
docker ps -lq
```
View the container's logs
```concole
docker logs <container_id_or_name>
```

```console
LAST_CONTAINER_ID=$(docker ps -lq) && docker logs $LAST_CONTAINER_ID
```

## :clipboard: Autokeras

### :fast_forward: Quick Start

Building the image:

```console
docker build . --file Dockerfile --tag cyberthreatdefense/autokeras
[...]
<<<wait for a while>>>
[...]
```
or Pull the Image:

```console
docker pull cyberthreatdefense/autokeras
```

Starting it up with the current working directory mounted as `/mnt/share` in the container:

```bash
docker run -it -h --name autokeras -v `pwd`:/mnt/share cyberthreatdefense/autokeras
```
```powershell
docker run -it -h --name autokeras -v ${PWD}:/mnt/share cyberthreatdefense/autokeras
```

Start the container
```console
docker start -i autokeras
```
<img src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/bar.gif">

[🔼 Back to top](#docker-toolkit)

## :clipboard: Detect-It-Easy

### :fast_forward: Quick Start

[![dockeri.co](https://dockerico.blankenship.io/image/cyberthreatdefense/diec)](https://hub.docker.com/r/cyberthreatdefense/diec)

Building the image:

```console
docker build . --file Dockerfile --tag cyberthreatdefense/diec
[...]
<<<wait for a while>>>
[...]
```

or Pull the Image:

```console
docker pull cyberthreatdefense/diec
```

Starting it up with the current working directory mounted as `/mnt/share` in the container:

```bash
docker run -it -h --name diec -v `pwd`:/mnt/share cyberthreatdefense/diec
```
```powershell
docker run -it -h --name diec -v ${PWD}:/mnt/share cyberthreatdefense/diec
```

Start the container
```console
docker start -i diec
```

<img src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/bar.gif">

[🔼 Back to top](#docker-toolkit)

## :clipboard: Manalyze

### :fast_forward: Quick Start

#### Alpine
Building the image:

```console
docker build . --file Dockerfile.alpine --tag cyberthreatdefense/manalyze-alpine
[...]
<<<wait for a while>>>
[...]
```

or Pull the Image:

```console
docker pull cyberthreatdefense/manalyze-alpine
```
Starting it up with the current working directory mounted as `/mnt/share` in the container:

```bash
docker run -it -h --name manalyze-alpine -v `pwd`:/mnt/share cyberthreatdefense/manalyze-alpine
```

```powershell
docker run -it -h --name manalyze-alpine -v ${PWD}:/mnt/share cyberthreatdefense/manalyze-alpine
```

Start the container
```console
docker start -i manalyze-alpine
```

#### Ubuntu

```console
docker build . --file Dockerfile.ubuntu --tag cyberthreatdefense/manalyze-ubuntu
[...]
<<<wait for a while>>>
[...]
```
Starting it up with the current working directory mounted as `/mnt/share` in the container:

```bash
docker run -it -h --name manalyze-ubuntu -v `pwd`:/mnt/share cyberthreatdefense/manalyze-ubuntu
```

```powershell
docker run -it -h --name manalyze-ubuntu -v ${PWD}:/mnt/share cyberthreatdefense/manalyze-ubuntu
```

Start the container

```console
docker start -i manalyze-ubuntu
```

<img src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/bar.gif">

[🔼 Back to top](#docker-toolkit)


## :clipboard: PCAP Extractor

### :fast_forward: Quick Start

Building the image:

```console
docker build . --file Dockerfile --tag cyberthreatdefense/pcap-extractor
[...]
<<<wait for a while>>>
[...]
```
or Pull the Image:

```console
docker pull cyberthreatdefense/pcap-extractor
```

Starting it up with the current working directory mounted as `/mnt/share` in the container:

```bash
docker run -it -h --name pcap-extractor -v `pwd`:/mnt/share cyberthreatdefense/pcap-extractor
```
```powershell
docker run -it -h --name pcap-extractor -v ${PWD}:/mnt/share cyberthreatdefense/pcap-extractor
```

Start the container

```console
docker start -i pcap-extractor
```

<img src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/bar.gif">

[🔼 Back to top](#docker-toolkit)


## :clipboard: ML Malware Detection Competition/MalConv-Keras Malware Analysis Environment

### :fast_forward: Quick Start

Building the image:

```console
# docker build . --file Dockerfile --tag cyberthreatdefense/malconv-keras-malware-benchmark
[...]
<<<wait for a while>>>
[...]
```

Starting it up with the current working directory mounted as `/mnt/share` in the container:

```console
# docker run -it -h malconv-keras-malware-benchmark -v `pwd`:/mnt/share cyberthreatdefense/malconv-keras-malware-benchmark
```
```powershell
# docker run -it -h malconv-keras-malware-benchmark -v ${PWD}:/mnt/share cyberthreatdefense/malconv-keras-malware-benchmark
```

<img src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/bar.gif">

[🔼 Back to top](#docker-toolkit)

## :clipboard: ML Malware Detection Competition/EMBER Malware Analysis Environment

### :fast_forward: Quick Start

Building the image:

```console
# docker build . --file Dockerfile --tag cyberthreatdefense/ember-malware-benchmark
[...]
<<<wait for a while>>>
[...]
```

Starting it up with the current working directory mounted as `/mnt/share` in the container:

```console
# docker run -it -h ember-malware-benchmark -v `pwd`:/mnt/share cyberthreatdefense/ember-malware-benchmark
```
```powershell
# docker run -it -h ember-malware-benchmark -v ${PWD}:/mnt/share cyberthreatdefense/ember-malware-benchmark
```

<img src="https://github.com/cybersecurity-dev/cybersecurity-dev/blob/main/assets/bar.gif">

##

### My Awesome Lists
You can access the my awesome lists [here](https://cyberthreatdefence.com/my_awesome_lists)

### Contributing

[Contributions of any kind welcome, just follow the guidelines](contributing.md)!

### Contributors

[Thanks goes to these contributors](https://github.com/cybersecurity-dev/Docker-Toolkit/graphs/contributors)!

[🔼 Back to top](#docker-toolkit)


