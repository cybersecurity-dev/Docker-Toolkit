# docker-toolkit
Reusable Docker Toolkit Scripting for Development Environment

## :clipboard: Autokeras

### :fast_forward: Quick Start

Building the image:

```console
# docker build . --file Dockerfile --tag cyberthreatdefense/autokeras
[...]
<<<wait for a while>>>
[...]
```

Starting it up with the current working directory mounted as `/mnt/share` in the container:

```console
# docker run -it -h autokeras -v `pwd`:/mnt/share cyberthreatdefense/autokeras
```
```powershell
# docker run -it -h autokeras -v ${PWD}:/mnt/share cyberthreatdefense/autokeras
```

## :clipboard: Detect-It-Easy

### :fast_forward: Quick Start

Building the image:

```console
# docker build . --file Dockerfile --tag cyberthreatdefense/diec
[...]
<<<wait for a while>>>
[...]
```

Starting it up with the current working directory mounted as `/mnt/share` in the container:

```console
# docker run -it -h diec -v `pwd`:/mnt/share cyberthreatdefense/diec
```
```powershell
# docker run -it -h diec -v ${PWD}:/mnt/share cyberthreatdefense/diec
```

## :clipboard: PCAP Extractor

### :fast_forward: Quick Start

Building the image:

```console
# docker build . --file Dockerfile --tag cyberthreatdefense/pcap-extractor
[...]
<<<wait for a while>>>
[...]
```

Starting it up with the current working directory mounted as `/mnt/share` in the container:

```console
# docker run -it -h pcap-extractor -v `pwd`:/mnt/share cyberthreatdefense/pcap-extractor
```
```powershell
# docker run -it -h pcap-extractor -v ${PWD}:/mnt/share cyberthreatdefense/pcap-extractor
```

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