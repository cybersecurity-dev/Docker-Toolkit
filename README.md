# Docker Toolkit
[<img src="https://img.shields.io/badge/dockerhub-Docker_Toolkit-blue.svg?logo=Docker">](https://hub.docker.com/u/cyberthreatdefense)

Reusable Docker Toolkit Scripting for Development Environment

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
