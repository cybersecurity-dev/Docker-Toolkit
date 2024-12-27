# docker-toolkit
Reusable Docker Scripting Toolkit for Development Environment Setup

## :clipboard: Autokeras

### :fast_forward: Quick Start

Building the image:

```console
# docker build . -t cyberthreatdefense/autokeras
[...]
<<<wait for a while>>>
[...]
```

Starting it up with the current working directory mounted as `/mnt/share` in the container:

```console
# docker run -it -h autokeras -v `pwd`:/mnt/share cyberthreatdefense/autokeras
```

## :clipboard: Detect-It-Easy

### :fast_forward: Quick Start

Building the image:

```console
# docker build . -t cyberthreatdefense/diec
[...]
<<<wait for a while>>>
[...]
```

Starting it up with the current working directory mounted as `/mnt/share` in the container:

```console
# docker run -it -h diec -v `pwd`:/mnt/share cyberthreatdefense/diec
```

## :clipboard: PCAP Extractor

### :fast_forward: Quick Start

Building the image:

```console
# docker build . -t cyberthreatdefense/pcap-extractor
[...]
<<<wait for a while>>>
[...]
```

Starting it up with the current working directory mounted as `/mnt/share` in the container:

```console
# docker run -it -h pcap-extractor -v `pwd`:/mnt/share cyberthreatdefense/pcap-extractor
```