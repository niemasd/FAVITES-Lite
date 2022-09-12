# Minimal Docker image for FAVITES-Lite using Ubuntu base
FROM ubuntu:20.04
MAINTAINER Niema Moshiri <niemamoshiri@gmail.com>

# Set up environment and install dependencies
RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y g++ make python3 python3-pip wget && \

    # install Python 3 packages
    pip3 install --no-cache-dir treesap treeswift && \

    # install NiemaGraphGen
    wget -qO- "https://github.com/niemasd/NiemaGraphGen/archive/refs/tags/1.0.6.tar.gz" | tar -zx && \
    cd NiemaGraphGen-* && \
    make && \
    mv ngg_* /usr/local/bin/ && \
    cd .. && \
    rm -rf NiemaGraphGen-* && \

    # install GEMF_FAVITES
    wget -qO- "https://github.com/niemasd/GEMF/archive/refs/tags/1.0.2.tar.gz" | tar -zx && \
    cd GEMF-* && \
    make && \
    mv GEMF GEMF_FAVITES.py /usr/local/bin/ && \
    cd .. && \
    rm -rf GEMF-* && \

    # install CoaTran
    wget -qO- "https://github.com/niemasd/CoaTran/archive/refs/tags/0.0.4.tar.gz" | tar -zx && \
    cd CoaTran-* && \
    make && \
    mv coatran_* /usr/local/bin/ && \
    cd .. && \
    rm -rf CoaTran-* && \

    # install Seq-Gen
    wget -qO- "https://github.com/rambaut/Seq-Gen/archive/refs/tags/1.3.4.tar.gz" | tar -zx && \
    cd Seq-Gen-*/source && \
    make && \
    mv seq-gen /usr/local/bin/ && \
    cd ../.. && \
    rm -rf Seq-Gen-* && \

    # set up FAVITES-Lite
    wget -qO- "https://github.com/niemasd/FAVITES-Lite/tarball/master" | tar -zx && \
    mv *FAVITES-Lite* /usr/local/bin/FAVITES-Lite && \
    ln -s /usr/local/bin/FAVITES-Lite/favites_lite.py /usr/local/bin/favites_lite.py && \

    # Clean up
    rm -rf /root/.cache /tmp/*
