FROM ubuntu:22.04

RUN apt-get update -yq \
&& apt-get install -yq autoconf automake build-essential cmake gdb-multiarch git libtool libusb-1.0-0 libusb-1.0-0-dev make pkg-config texinfo wget \
&& apt-get clean -y

RUN useradd --create-home user
WORKDIR /home/user

RUN mkdir toolchain
WORKDIR /home/user/toolchain

RUN mkdir renode \
&& wget https://github.com/renode/renode/releases/download/v1.15.1/renode-1.15.1.linux-portable.tar.gz \
&& tar xf renode-1.15.1.linux-portable.tar.gz -C renode --strip-components=1 \
&& rm -rf renode-1.15.1.linux-portable.tar.gz

RUN mkdir arm-gnu-toolchain \
&& wget https://developer.arm.com/-/media/Files/downloads/gnu/13.3.rel1/binrel/arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi.tar.xz \
&& tar xf arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi.tar.xz -C arm-gnu-toolchain --strip-components=1 \
&& rm -rf arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi.tar.xz

RUN git clone https://github.com/openocd-org/openocd.git \
&& cd openocd \
&& git checkout v0.12.0 \
&& ./bootstrap \
&& ./configure \
&& make \
&& make install

ENV PATH="${PATH}:/home/user/toolchain/renode:/home/user/toolchain/arm-gnu-toolchain/bin"

RUN mkdir /home/user/workspace
WORKDIR /home/user/workspace

USER user