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
