FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
apt-get install --yes --no-install-recommends wget git python3 python3-pip python-is-python3 && \
rm -rf /var/lib/apt/lists/*
RUN pip install numpy pyfaidx tqdm
COPY ./mutation_simulator /opt/Mutation-Simulator/mutation_simulator
ENV PYTHONPATH=$PYTHONPATH:/opt/Mutation-Simulator
RUN printf '#!/bin/bash \
\npython -m mutation_simulator "$@"\n' > /usr/local/bin/mutation_simulator && chmod ogu+x /usr/local/bin/mutation_simulator
