FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit-pypi==2022.9.5
RUN pip install git+https://github.com/bp-kelley/descriptastorus.git@86eedc60546abe6f59cdbcb12025a61157ba178d
RUN pip install chemprop==1.3.0
RUN pip install tensorboardX==2.0

WORKDIR /repo
COPY . /repo
