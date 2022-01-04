# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:30:27 2022

@author: hp
"""

FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python flask_api.py
© 2022 GitHub, Inc.
Terms
Privac